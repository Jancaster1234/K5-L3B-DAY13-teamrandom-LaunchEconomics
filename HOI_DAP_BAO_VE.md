# Hỏi đáp bảo vệ Gate 2a · nhóm teamrandom

Tài liệu chuẩn bị cho lượt duyệt chéo lúc 17:00. Mọi số lấy từ output `python lab13.py` (chạy trong `src/`) và các file trong `report/team/`. Khi trả lời: không quá ba dòng, luôn kèm con số; số tính từ cột `_simulated` phải nói rõ là simulated.

Người trả lời chính: **TV2** trình bày hồ sơ (1 phút); **TV1** trả lời phần 1 và 2 (chi phí, pilot); **TV3, TV4** trả lời phần 4 (bảng lỗi).

## 0. Nắm bối cảnh trong 1 phút

- **Bài toán:** LogiX-VN chạy thử trợ lý hoàn phí 2 tuần ở 6 depot. Nhóm có mẫu 1.200 yêu cầu (1.624 lần chạy của trợ lý) và phải trả lời: có đáng chạy pilot không, đo gì, hỏng thì sao, pilot thiết kế thế nào. Hội đồng Gate 2a chỉ duyệt **kế hoạch pilot**.
- **Chi phí mỗi việc thành công** (A2, `bang_chi_phi.md`) = (tiền token + tiền tool + tiền xem lại + tiền làm lại) ÷ số yêu cầu thành công. Đây là con số chính của nhiệm vụ A: **4.472 đ** [simulated].
- **Hoá đơn token chia số yêu cầu** = (tiền token + tiền tool) ÷ 1.200 = **274,7 đ**. Đây là con số "nhìn hoá đơn nhà cung cấp", dễ gây hiểu nhầm là rẻ.
- **12.000 đ** = chi phí khi nhân viên tự làm một yêu cầu (6 phút × 2.000 đ/phút). Mọi so sánh "0,49×", "0,98×" là chia cho 12.000 đ.
- **Xem lại / làm lại:** nhân viên đọc lại gợi ý của trợ lý trước khi gửi (xem lại), hoặc phải tự làm lại vì trợ lý trả lời sai (làm lại). Số phút của hai việc này lấy từ hai cột `_simulated`, nên mọi số dựa trên chúng ghi **[simulated]**.
- **Phạm vi pilot:** chỉ hai loại yêu cầu `noi_dia` (nội địa) và `hang_nang` (hàng nặng); loại `quoc_te` và `doi_tac`.
- **Chia theo cụm:** pilot chia ngẫu nhiên theo **nhân viên** (mỗi nhân viên là một cụm), không theo từng yêu cầu. Yêu cầu của cùng một người giống nhau hơn, nên mẫu "hiệu dụng" nhỏ hơn số yêu cầu thật. **ICC 0,02** đo mức giống nhau đó; **DE** (hệ số thiết kế) là số lần mẫu bị "thổi phồng".
- **MDE** = mức chênh nhỏ nhất pilot đủ mẫu để phát hiện; **power** = xác suất phát hiện được nếu tác động có thật.

## 1. Chi phí (nhiệm vụ A, B · file `bang_chi_phi.md`)

**Công thức chi phí mỗi việc thành công ở A2 là (token + tool + xem lại + làm lại) ÷ số việc thành công. Vì sao tử số cộng tiền của mọi lần chạy, kể cả lần lỗi, còn mẫu số chỉ đếm yêu cầu thành công?**
Lần chạy lỗi vẫn tốn token, tool và giờ nhân viên, nên phải tính vào chi phí. Mẫu số là thứ công ty thật sự nhận được: 978 yêu cầu có `ket_qua = thanh_cong`. Nếu chia cho cả 1.200 yêu cầu thì chi phí thấp giả tạo, vì tính cả những yêu cầu trợ lý làm hỏng.

**Chi phí mỗi việc thành công là 4.472 đ, trong khi hoá đơn token + tool chia số yêu cầu chỉ 274,7 đ. Vì sao chênh tới 16,3 lần?**
Vì phần lớn chi phí là giờ nhân viên, không phải token: tiền làm lại chiếm 51,8%, xem lại 40,7% tổng chi phí [simulated]. Token + tool chỉ chiếm 7,5%. Nhìn hoá đơn nhà cung cấp sẽ đánh giá thấp chi phí thật rất nhiều.

**Hồ sơ mục 3 ghi trợ lý tốn 0,49× so với nhân viên tự làm (12.000 đ). Sao không lấy 4.472 ÷ 12.000 = 0,37×?**
Con số 4.472 đ chỉ chia cho việc trợ lý làm xong, chưa tính 222 yêu cầu không thành công mà nhân viên phải làm thay. Tính cả phần đó: (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ/yêu cầu = **0,49×** [simulated].

**Bảng A3 tách chi phí theo loại yêu cầu. Vì sao pilot loại `quoc_te` và `doi_tac`?**
`quoc_te` tốn 1,88× so với 12.000 đ, chỉ thành công 27,3% [simulated]. Cho chạy lại tới 3 lần cũng không giúp: tỉ lệ lần chạy đúng ở lần 1, 2, 3 là 30,0% → 11,4% → 2,2%, vì lỗi lặp lại trên cùng yêu cầu. `doi_tac` sát ngưỡng (0,85×) và có điều khoản riêng.

**Mục B4: nếu tuần đầu pilot bắt buộc nhân viên xem lại 100% gợi ý của trợ lý thì chi phí mỗi việc thành công là bao nhiêu?** (câu gợi ý của đề)
Trong phạm vi `noi_dia` + `hang_nang`: 11.743 đ = **0,98×** so với 12.000 đ [simulated]. Nếu mỗi ca làm lại mất 15,3 phút (trung bình trong cột simulated) thì 12.415 đ = **1,03×**, tức đắt hơn nhân viên tự làm. Chỉ hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (hoặc ≤ 4,8 phút), nên hồ sơ đặt điều kiện giảm tỉ lệ xem lại theo bậc.

**Bảng độ nhạy B1 đổi từng yếu tố một. Yếu tố nào làm chi phí mỗi việc thành công thay đổi nhiều nhất, và pilot phải theo dõi gì?**
Số ca làm lại (+51,8% khi gấp đôi), tỉ lệ xem lại (+40,7%), lương nhân viên (+23,1% khi tăng 25%) [simulated]. Giá token gấp đôi chỉ làm tăng 5,6%. Vì vậy pilot theo dõi tỉ lệ làm lại và tỉ lệ xem lại, không cần lo giá token.

**Mục B3 giới hạn số lần trợ lý được chạy lại cho một yêu cầu (1, 2 hoặc 3 lần). Giới hạn nào tốt nhất?**
Giới hạn 2 lần rẻ nhất cho công ty: 6.901.220 đ chi phí cả hệ thống [simulated], tính cả tiền nhân viên làm thay các yêu cầu thất bại. Giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ), nhưng đẩy thêm 85 yêu cầu sang nhân viên, nên tổng đắt hơn 548.561 đ.

**Mục A4: trợ lý còn tốn chi phí cố định 40 triệu đ/tháng. Khoản này có làm đổi kết luận không?**
Ở khối lượng đầy đủ 45.000 yêu cầu/tháng thì không: cộng thêm 1.185 đ/việc, tổng 4.599 đ = 0,38× [simulated]. Nếu khối lượng chỉ còn một nửa thì cộng 2.370 đ/việc, tổng 5.784 đ = 0,48×. Đây là một dòng rủi ro trong mục E2 của `chi_so.md`.

## 2. Pilot (nhiệm vụ D · file `pilot_plan.yaml`)

**Pilot chia theo nhân viên (cụm). Cỡ mẫu hiệu dụng khi chia theo cụm tính thế nào?**
Hệ số thiết kế DE = 1 + (m − 1) × ICC, với m là số yêu cầu mỗi nhân viên. Cỡ mẫu hiệu dụng = c × m ÷ DE, với c là số nhân viên mỗi nhóm; con số này luôn nhỏ hơn c ÷ ICC. Với 20 nhân viên mỗi nhóm, mẫu hiệu dụng luôn dưới 20 ÷ 0,02 = 1.000, không đạt 1.251 cần cho mức chênh 5 điểm, dù mỗi người xử lý bao nhiêu yêu cầu.

**Cách chia nhóm trong pilot có ít nhất 20 cụm mỗi nhóm không?** (câu gợi ý của đề)
Có: chia theo nhân viên, 20 người dùng trợ lý và 20 người đối chứng, bốc thăm bằng code với seed ghi trước, phân tầng theo depot. Chia theo depot chỉ có 6 cụm mỗi nhóm và tối đa 300 mẫu hiệu dụng, nên bị loại.

**Nếu chia ngẫu nhiên theo từng yêu cầu thì đủ 1.251 mẫu cho mức chênh 5 điểm. Sao nhóm không chọn cách đó?**
Khi đó cùng một nhân viên lúc dùng, lúc không dùng trợ lý, nên kinh nghiệm học từ trợ lý tràn sang các yêu cầu đối chứng. Kết quả không tách được tác động thật của trợ lý.

**Giám đốc vận hành muốn thấy chỉ số chính tăng 5 điểm, nhưng 40 nhân viên không đủ mẫu cho mức đó. Nhóm xử lý thế nào?**
Nhóm thiết kế pilot cho mức chênh (MDE) 6 điểm: cần 859 mẫu hiệu dụng mỗi nhóm, tức mỗi nhân viên ≥ 299 yêu cầu (DE 6,96), tổng 5.980 yêu cầu thực tế mỗi nhóm. Bất lợi: nếu tác động thật chỉ 5 điểm thì power chỉ còn **0,64** (36% khả năng bỏ sót). Giám đốc vận hành ký chấp nhận trước ngày bắt đầu; kết quả không có ý nghĩa thống kê thì không được kết luận "không có tác động".

**Trong đợt chạy thử, tỉ lệ yêu cầu bị khách mở lại trong 7 ngày là 4,25%. Ngưỡng an toàn trong luật dừng của nhóm có làm pilot dừng ngay tuần đầu không?** (câu gợi ý của đề)
Không. Trong phạm vi pilot, tỉ lệ hiện tại là 3,97%. Luật dừng so với nhóm đối chứng (nhóm trợ lý cao hơn ≥ 2 điểm) kèm trần tuyệt đối 6%. Nếu đặt ngưỡng tuyệt đối 3% thì pilot sẽ dừng ngay tuần đầu.

**Câu hội đồng 4mems đã hỏi: luật dừng 3 đặt ngưỡng 8.000 đ/việc thành công trên cả phạm vi, nhưng riêng `hang_nang` đã là 8.221 đ. Nếu `hang_nang` xấu đi thì số gộp vẫn dưới 8.000 đ, vậy luật này phát hiện được gì?**
Nhóm nhận đây là chỗ cần sửa: `noi_dia` chiếm 824/982 yêu cầu và chỉ 2.696 đ, nên kéo số gộp xuống 3.414 đ [simulated] và che `hang_nang`. Đã sửa `pilot_plan.yaml`: tính chi phí tách theo `loai` (lấy `loai` từ event `request_created`) và thêm ngưỡng riêng `hang_nang` > 12.000 đ, tức đắt hơn nhân viên tự làm, trong 2 tuần liên tiếp thì PM trợ lý hoàn phí thu hẹp về `noi_dia`.

**Khi một luật dừng bị kích hoạt, ai có quyền tắt trợ lý, mất bao lâu, và khách được phục vụ bằng gì?**
Giám đốc vận hành bấm cờ tắt trợ lý, hiệu lực trong 30 phút; khách được phục vụ bằng luồng nhân viên tự làm như hiện nay. Riêng hoàn tiền trùng: chỉ cần 1 ca đã đối soát sổ cái xác nhận là tắt ngay.

**Vì sao ngày ra quyết định của pilot là 2027-01-15?**
Bước rollout 50% (20 + 20 nhân viên) bắt đầu 2026-12-21. Mỗi người đủ 299 yêu cầu vào khoảng 2027-01-04; chỉ số chính cần chờ thêm 7 ngày để biết yêu cầu có bị mở lại không, nên khoảng 2027-01-11 mới đủ dữ liệu. Thiếu mẫu thì gia hạn từng tuần, tối đa đến 2027-01-29.

## 3. Chỉ số (nhiệm vụ E · file `chi_so.md`)

**Chỉ số chính là % yêu cầu đóng trong 24 giờ và không bị mở lại trong 7 ngày. Sao hồ sơ chỉ ghi "chỉ số trong đợt chạy thử là 82,83%", mà không nói trợ lý đã nâng chỉ số từ mức 0,70 khi chưa có trợ lý?**
Đợt chạy thử không có nhóm đối chứng chạy cùng thời gian, nên không biết 82,83% là nhờ trợ lý hay do yếu tố khác. Pilot có nhóm đối chứng chính là để trả lời câu đó.

**Các chỉ số và luật dừng trong hồ sơ có tính được từ dữ liệu sẽ ghi lại không?**
Có. Mục "Kiểm tra chéo" trong `chi_so.md` ghi rõ mỗi chỉ số và mỗi luật dừng dùng event nào: chi phí từ `agent_run_completed`, hoàn trùng từ `refund_ledger_write`, mức sử dụng từ `suggestion_shown`. Event nào cũng có `trace_id` để nối về lần chạy của trợ lý.

**Trong hồ sơ, những con số nào là giả lập (simulated)?**
Phút xem lại (890 phút) và phút làm lại (1.132 phút) lấy từ hai cột `_simulated`, cùng mọi số dựa trên chúng: chi phí mỗi việc thành công, so sánh với 12.000 đ, bảng độ nhạy, rủi ro kinh tế. Hồ sơ đặt điều kiện thay bằng phút đo thật sau tuần đầu pilot.

## 4. Bảng lỗi (nhiệm vụ C · file `bang_loi.md`)

**Hai người gắn nhãn 20 ca lỗi độc lập vào năm loại của Google PAIR. Hai bộ nhãn trùng nhau bao nhiêu?**
17/20 ca = 85%, đạt yêu cầu ≥ 80%. Ba ca lệch (3, 13, 19) đã được thống nhất, mỗi ca có một câu quy tắc phân biệt trong `bang_loi.md`.

**Ca 13 (khách hỏi hoàn phí bảo hiểm của công ty đối tác, trợ lý trả lời chung chung về phí vận chuyển): vì sao gắn "Giới hạn hệ thống" mà không phải "Hệ thống"?**
Nguyên nhân gốc là yêu cầu nằm ngoài phạm vi trợ lý được thiết kế để xử lý. Việc trợ lý trả lời chung chung chỉ là cách xử lý giới hạn kém, được sửa ở cột khắc phục. Quy tắc: ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém.

**Ca 6 (khách chọn nhầm mục "giao trễ" cho hàng vỡ) và ca 9 (khách nhập mã đơn của sàn thay vì mã vận đơn): vì sao gắn "Do người dùng"?**
Gốc lỗi là khách chọn sai mục hoặc nhập sai mã. Việc trợ lý không gợi ý cho khách là chỗ cần cải thiện, ghi ở cột khắc phục, không làm đổi loại lỗi.

**Ca 8 (trợ lý trích "Điều 7.2" không có trong chính sách) và ca 15 (trợ lý tính hoàn 100% thay vì 50%, nhân viên bắt được): vì sao là "Hệ thống" mà không phải "Ngầm"?**
Vì sai đã lộ ra: trích dẫn sai nhìn thấy được, nhân viên phát hiện trước khi gửi. "Ngầm" chỉ dùng khi không ai nhận ra cho tới lúc kiểm tra mẫu, như ca 5, 12, 17.

**Ca 12 (tool của depot D05 trả thiếu trường, trợ lý gọi lại nhiều lần nên vẫn ra kết quả đúng): kết quả đúng sao lại là lỗi, và vì sao là "Ngầm"?**
Tiền token của D05 gấp 3 lần các depot khác suốt 3 tuần mà không ai thấy. Sai có thể là sai về chi phí, không chỉ về câu trả lời; không ai phát hiện nên là Ngầm.

## 5. Đề xuất (file `ho_so_launch_v0.md`)

**Hồ sơ đề xuất "Go có điều kiện". Vì sao không chọn Go hay No-go?**
Trong phạm vi `noi_dia` + `hang_nang`, chi phí mỗi việc thành công là 3.414 đ [simulated], đủ để đáng chạy pilot. Nhưng có hai con số bất lợi: xem lại 100% thì tốn 0,98–1,03× so với nhân viên tự làm, và power chỉ 0,64 nếu tác động thật là 5 điểm. Vì vậy mỗi điều kiện có người phụ trách và ngày kiểm tra: sửa khoá chống hoàn trùng, Giám đốc vận hành ký chấp nhận mức chênh 6 điểm, bật đủ event, giảm xem lại theo bậc.

---

## Khi nhóm mình làm hội đồng (ghi vào `phieu_cham.md`)

Nhóm mình chấm hồ sơ của nhóm n + 1 theo ba tiêu chí, mỗi tiêu chí 0, 5 hoặc 10 điểm. Chấm theo bằng chứng, không chấm theo cách trình bày.

- **C6 · Đề xuất có khớp bằng chứng không:** đề xuất có mâu thuẫn với số của chính nhóm đó không? Có nêu con số bất lợi (ví dụ chi phí khi xem lại 100%, power ở mức chênh 5 điểm) kèm cách xử lý không?
- **C7 · Số giả lập và phạm vi:** mọi số tính từ cột `_simulated` có ghi nhãn không? Phạm vi pilot có được thu hẹp, có lý do bằng số (bảng A3) không?
- **C8 · Pilot có ra được quyết định không:** có nhóm đối chứng chạy cùng thời gian và ít nhất 20 cụm mỗi nhóm không? Luật dừng có ngưỡng, thời hạn, người có quyền dừng không? Ngưỡng an toàn có làm pilot dừng ngay tuần đầu không?

Ba câu hỏi gợi ý để hỏi nhóm bạn:
1. "Nếu tuần đầu nhân viên phải xem lại 100% gợi ý thì chi phí mỗi việc thành công của nhóm bạn là bao nhiêu?"
2. "Cách chia nhóm trong pilot của nhóm bạn có ít nhất 20 cụm mỗi nhóm không?"
3. "Tỉ lệ mở lại trong đợt chạy thử là 4,25%. Ngưỡng an toàn của nhóm bạn có làm pilot dừng ngay tuần đầu không?"
