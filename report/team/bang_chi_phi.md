# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 · ĐẠT |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 · ĐẠT |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 · ĐẠT (= 1/p, k triệt tiêu) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool (5.600 lần gọi) | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại (890 phút) | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại (1.132 phút) | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated (gồm xem lại, làm lại) |
| Số việc thành công | 978 | `ket_qua` | đo từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | tổng ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (token + tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? **16,3 lần** (4.472 đ so với 274,7 đ) [simulated]: tử số tính mọi lần chạy kể cả lần lỗi và giờ nhân viên, mẫu số chỉ đếm 978 việc thành công.
- So với nhân viên tự làm: chi phí cả hệ thống (cộng 222 ca không thành công × 12.000 đ) = 5.865 đ/yêu cầu = **0,49×** của 12.000 đ [simulated].
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%** [simulated], tiếp theo là xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5% tổng, token + tool chỉ 7,5%.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

- Loại nào không đáng để trợ lý xử lý? **quoc_te**: 1,88× của 12.000 đ [simulated], thành công 27,3%. Chạy lại không giúp: tỉ lệ ok lần 1 là 30,0%, lần 2 chỉ 11,4%, lần 3 chỉ 2,2%, vì lỗi lặp lại trên cùng yêu cầu nên chạy lại chỉ tốn thêm tiền.
- doi_tac sát ngưỡng (0,85× [simulated], thành công 54,4%) và có điều khoản riêng, nên cũng loại khỏi phạm vi pilot; phạm vi đề xuất là noi_dia + hang_nang.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 (= 45.000 × 900 / 1.200) | 1.185 đ | 3.414 + 1.185 = 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 3.414 + 2.370 = 5.784 đ [simulated] | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi kết luận ở 45.000 yêu cầu/tháng (0,38× [simulated]), nhưng cố định tăng gấp đôi lên 2.370 đ/việc khi khối lượng còn một nửa (0,48× [simulated]). Chi phí phạm vi chưa cộng cố định: 3.072.513 ÷ 900 = 3.414 đ [simulated].

## B1 · Đổi từng yếu tố

Mọi chi phí trong bảng là simulated (gồm tiền xem lại, làm lại từ cột `_simulated`). Tự kiểm tra: mỗi kịch bản giảm một nửa làm chi phí giảm đúng nửa mức tăng của kịch bản gấp đôi (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Gốc (A2) | Tham số mặc định | 4.472 đ | |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (+51,8%) · 2. **tỉ lệ xem lại** (+40,7%) · 3. **lương nhân viên** (+23,1% khi tăng 25%). Giá token chỉ +5,6%, nên pilot phải theo dõi tỉ lệ làm lại và xem lại, không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Mọi số tiền trong bảng là simulated.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? **2 lần**: 6.901.220 đ cả hệ thống [simulated], rẻ hơn 3 lần 136.365 đ. Không trùng với giới hạn có chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ): giới hạn 1 lần đẩy thêm 85 yêu cầu sang nhân viên (319 so với 234) nên cả hệ thống đắt hơn 548.561 đ.

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: (948 yêu cầu có lần chạy ok × 5 phút × 2.000 đ = 9.480.000 đ + 48 ca làm lại × 9 phút × 2.000 đ = 864.000 đ + token/tool 224.513 đ) ÷ 900 = **11.743 đ = 0,98×** [simulated].
- Nếu dùng phút làm lại theo cột `phut_lam_lai_simulated` (trung bình 15,3 phút/ca, trung vị 14,5; simulated): 11.173.313 ÷ 900 = **12.415 đ = 1,03×** [simulated], đắt hơn nhân viên tự làm. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút).
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% thì trợ lý gần như không tiết kiệm (tiền xem lại chiếm 90% của 10,57 triệu đ [simulated]). Pilot phải đo được tỉ lệ xem lại có thể giảm an toàn xuống mức nào và mỗi lần xem lại có dưới 5 phút không, bằng phút đo thật thay cho cột simulated.
