# Hỏi đáp bảo vệ Gate 2a · nhóm teamrandom

Tài liệu chuẩn bị cho lượt duyệt chéo lúc 17:00. Mọi số lấy từ output `python lab13.py` và các file trong `report/team/`. Mỗi câu trả lời không quá ba dòng, luôn kèm con số; số tính từ cột `_simulated` phải nói rõ là simulated.

Người trả lời chính: **TV2** trình bày hồ sơ (1 phút); **TV1** trả lời câu về chi phí và cỡ mẫu; **TV3, TV4** trả lời câu về bảng lỗi.

## 1. Chi phí (nhiệm vụ A, B)

**Vì sao tử số tính mọi lần chạy, còn mẫu số chỉ đếm việc thành công?**
Lần chạy lỗi vẫn tốn token, tool và giờ nhân viên, nên phải tính vào chi phí. Mẫu số là thứ công ty thật sự nhận được: 978 yêu cầu `thanh_cong`. Chia cho 1.200 sẽ làm chi phí thấp giả tạo.

**Vì sao chi phí mỗi việc thành công gấp 16,3 lần hoá đơn token?**
4.472 đ so với 274,7 đ [simulated]. Giờ nhân viên chiếm 92,5% tổng chi phí: làm lại 51,8%, xem lại 40,7%. Token + tool chỉ 7,5%.

**Vậy trợ lý rẻ hơn nhân viên bao nhiêu? Sao không ghi 0,37×?**
4.472 ÷ 12.000 = 0,37× chưa tính 222 yêu cầu không thành công mà nhân viên phải làm thay. Tính cả phần đó: (4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ = **0,49×** [simulated].

**Vì sao loại quoc_te và doi_tac khỏi phạm vi pilot?**
quoc_te 1,88× của 12.000 đ, thành công 27,3% [simulated]. Chạy lại không giúp: tỉ lệ ok lần 1, 2, 3 là 30,0% → 11,4% → 2,2%. doi_tac sát ngưỡng 0,85× và có điều khoản riêng.

**Nếu tuần đầu phải xem lại 100% thì chi phí là bao nhiêu?** (câu gợi ý của đề)
Trong phạm vi noi_dia + hang_nang: 11.743 đ = **0,98×** [simulated]; nếu làm lại 15,3 phút/ca như cột simulated thì 12.415 đ = **1,03×**, đắt hơn nhân viên. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (hoặc ≤ 4,8 phút). Vì vậy hồ sơ đặt điều kiện giảm xem lại theo bậc.

**Yếu tố nào làm chi phí thay đổi nhiều nhất? Pilot phải theo dõi gì?**
Số ca làm lại (+51,8% khi gấp đôi), tỉ lệ xem lại (+40,7%), lương (+23,1% khi tăng 25%) [simulated]. Giá token gấp đôi chỉ +5,6%. Pilot theo dõi tỉ lệ làm lại và xem lại, không theo dõi giá token.

**Giới hạn số lần chạy nào tốt nhất?**
2 lần rẻ nhất cho công ty: 6.901.220 đ cả hệ thống [simulated]. 1 lần có chi phí mỗi việc thành công thấp nhất (4.111 đ) nhưng đẩy thêm 85 yêu cầu sang nhân viên, nên cả hệ thống đắt hơn 548.561 đ.

**Chi phí cố định 40 triệu đ/tháng có đổi kết luận không?**
Không, ở 45.000 yêu cầu/tháng: +1.185 đ/việc, tổng 4.599 đ = 0,38× [simulated]. Khối lượng còn một nửa thì +2.370 đ/việc, tổng 5.784 đ = 0,48×. Đây là dòng rủi ro trong E2.

## 2. Pilot (nhiệm vụ D)

**Cỡ mẫu hiệu dụng khi chia theo cụm tính thế nào?**
Hệ số thiết kế DE = 1 + (m − 1) × ICC; n hiệu dụng = c × m ÷ DE, luôn nhỏ hơn c ÷ ICC. Với 20 nhân viên mỗi nhóm, n hiệu dụng luôn dưới 20 ÷ 0,02 = 1.000 < 1.251 cần cho mức 5 điểm, dù mỗi người xử lý bao nhiêu yêu cầu.

**Cách chia của nhóm có ít nhất 20 cụm mỗi nhóm không?** (câu gợi ý của đề)
Có: chia theo nhân viên, 20 người mỗi nhóm, bốc thăm bằng code với seed ghi trước, phân tầng theo depot. Chia theo depot chỉ có 6 cụm và tối đa 300 hiệu dụng nên bị loại.

**Sao không chia theo từng yêu cầu, vốn đủ 1.251 mẫu?**
Cùng một nhân viên vừa dùng vừa không dùng trợ lý, nên kinh nghiệm từ trợ lý tràn sang nhóm đối chứng. Kết quả sẽ không tách được tác động.

**Không đủ mẫu cho 5 điểm thì sao?**
Nhóm chấp nhận mức chênh 6 điểm: 859 hiệu dụng mỗi nhóm, mỗi người ≥ 299 yêu cầu (DE 6,96), tức 5.980 yêu cầu thực tế mỗi nhóm. Bất lợi: nếu tác động thật chỉ 5 điểm thì power còn **0,64**. Giám đốc vận hành ký chấp nhận trước ngày bắt đầu; kết quả không có ý nghĩa thì không được kết luận "không có tác động".

**Tỉ lệ mở lại hiện tại 4,25%, ngưỡng an toàn có làm pilot dừng ngay tuần đầu không?** (câu gợi ý của đề)
Không. Trong phạm vi, tỉ lệ hiện tại là 3,97%. Luật dừng so với nhóm đối chứng (cao hơn ≥ 2 điểm) kèm trần tuyệt đối 6%. Nếu đặt ngưỡng tuyệt đối 3% thì pilot dừng ngay tuần đầu.

**Ai có quyền dừng, mất bao lâu, khách được phục vụ bằng gì?**
Giám đốc vận hành bấm cờ tắt, hiệu lực trong 30 phút; khách được phục vụ bằng luồng nhân viên tự làm như hiện nay. Riêng hoàn trùng: chỉ 1 ca đã đối soát sổ cái xác nhận là tắt ngay.

**Vì sao ngày quyết định là 2027-01-15?**
Bước 0.50 bắt đầu 2026-12-21. Mỗi người đủ 299 yêu cầu vào khoảng 2027-01-04, cộng 7 ngày để đo mở lại thì đủ dữ liệu khoảng 2027-01-11. Thiếu mẫu thì gia hạn từng tuần, tối đa đến 2027-01-29.

## 3. Chỉ số (nhiệm vụ E)

**Sao hồ sơ ghi "chỉ số trong đợt chạy thử là 82,83%" mà không nói trợ lý đã nâng từ 0,70?**
Đợt chạy thử không có nhóm đối chứng chạy cùng thời gian, nên chưa tách được tác động của trợ lý. Pilot có đối chứng chính là để trả lời câu đó.

**Chỉ số nào cũng tính được từ event chứ?**
Có. Mỗi chỉ số và mỗi luật dừng đều có event ghi trong mục "Kiểm tra chéo" của `chi_so.md`, ví dụ chi phí từ `agent_run_completed`, hoàn trùng từ `refund_ledger_write`, mức sử dụng từ `suggestion_shown`. Event nào cũng có `trace_id`.

**Số nào là simulated?**
Phút xem lại (890 phút) và phút làm lại (1.132 phút), cùng mọi số dựa trên chúng: chi phí mỗi việc thành công, so sánh với 12.000 đ, bảng độ nhạy, rủi ro kinh tế. Hồ sơ yêu cầu thay bằng phút đo thật sau tuần 1.

## 4. Bảng lỗi (nhiệm vụ C)

**Hai người gắn nhãn đồng thuận bao nhiêu?**
17/20 = 85% ≥ 80%. Ba ca lệch (3, 13, 19) đã thống nhất, mỗi ca có một câu quy tắc phân biệt.

**Ca 13 vì sao là Giới hạn hệ thống, không phải Hệ thống?**
Nguyên nhân gốc là yêu cầu hoàn phí bảo hiểm của công ty đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung chỉ là cách xử lý giới hạn kém, cần sửa ở cột khắc phục. Quy tắc: ngoài phạm vi thì là giới hạn.

**Ca 6, 9 vì sao là Do người dùng?**
Gốc lỗi là khách chọn sai mục (ca 6) hoặc nhập sai mã (ca 9). Trợ lý không gợi ý là việc cần cải thiện, nằm ở cột khắc phục, không đổi loại.

**Ca 8, 15 vì sao là Hệ thống mà không phải Ngầm?**
Sai đã lộ ra: trích dẫn điều khoản không tồn tại nhìn thấy được (ca 8), nhân viên bắt được trước khi gửi (ca 15). Ngầm chỉ dùng khi không ai nhận ra cho tới lúc kiểm tra mẫu, như ca 5, 12, 17.

**Ca 12 kết quả vẫn đúng, sao lại là lỗi?**
Chi phí token của depot D05 gấp 3 lần suốt 3 tuần mà không ai thấy. Sai có thể là sai về chi phí, không chỉ về câu trả lời; không ai phát hiện nên là Ngầm.

## 5. Đề xuất

**Vì sao Go có điều kiện, không phải Go hay No-go?**
Trong phạm vi noi_dia + hang_nang, chi phí 3.414 đ/việc thành công [simulated], nên đáng chạy pilot. Nhưng có hai con số bất lợi: xem lại 100% thì 0,98–1,03×, và power 0,64 ở mức 5 điểm. Vì vậy mỗi điều kiện đều có người phụ trách và ngày kiểm tra: sửa khoá chống trùng, ký chấp nhận mức chênh 6 điểm, bật event, giảm xem lại theo bậc.

---

## Khi nhóm mình làm hội đồng (ghi vào `phieu_cham.md`)

Chấm theo bằng chứng, không chấm theo cách trình bày. Kiểm tra nhanh hồ sơ nhóm bạn:

- **C6 · Đề xuất khớp bằng chứng:** đề xuất có mâu thuẫn với số của chính nhóm đó không? Có nêu con số bất lợi (xem lại 100%, power ở mức 5 điểm) và cách xử lý không?
- **C7 · Số giả lập và phạm vi:** mọi số từ cột `_simulated` có nhãn không? Phạm vi có thu hẹp, có lý do bằng số (A3) không?
- **C8 · Pilot ra được quyết định:** có đối chứng chạy cùng thời gian, ít nhất 20 cụm mỗi nhóm không? Luật dừng có ngưỡng, thời hạn, người có quyền dừng không? Ngưỡng an toàn có làm pilot dừng ngay tuần đầu không?

Ba câu hỏi gợi ý để hỏi nhóm bạn:
1. "Chi phí mỗi việc thành công là bao nhiêu nếu tuần đầu phải xem lại 100%?"
2. "Cách chia của nhóm có ít nhất 20 cụm mỗi nhóm không?"
3. "Với tỉ lệ mở lại 4,25% hiện tại, ngưỡng an toàn của nhóm có làm pilot dừng ngay tuần đầu không?"
