# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Chỉ số chính trong đợt chạy thử là 82,83% (994/1.200 yêu cầu). Đợt chạy thử thiếu nhóm đối chứng nên chưa thể ước lượng tác động của trợ lý. Nguồn số liệu là phần E1 của `python lab13.py` chạy trong `src/`.

| Loại | Chỉ số | Công thức | Kết quả đợt chạy thử |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu thỏa cả hai điều kiện / tổng yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số yêu cầu được xem lại có quyết định cuối là `sua` hoặc `bo` / số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu mở lại trong 7 ngày / tổng yêu cầu | 4,25% (51/1.200) |
| Dùng (đề xuất) | Tỉ lệ yêu cầu được mở bằng trợ lý | Số yêu cầu trong phạm vi của nhóm trợ lý có ít nhất 1 lượt mở bằng trợ lý / tổng yêu cầu trong phạm vi được giao cho nhóm trợ lý trong tuần | Đo trong pilot, dùng ngưỡng 50% của kế hoạch pilot |
| An toàn (đề xuất) | Tỉ lệ hoàn sai số tiền qua kiểm tra mẫu hằng tuần | Số yêu cầu có số tiền hoàn thực tế lệch số tiền đúng / tổng yêu cầu đã kiểm tra trong tuần | Đo trong pilot để phát hiện lỗi ngầm |

## Danh sách event đề xuất

Mỗi event có `trace_id` để đối soát đường đi và `request_id` để nối các lần chạy của cùng một yêu cầu. Mỗi tỷ lệ đếm yêu cầu duy nhất. Chờ đủ 7 ngày theo dõi theo kế hoạch pilot trước khi tính chỉ số kết quả.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_created` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian tạo, loại, `staff_id`, nhóm được phân, bước mở rộng | Khi tiếp nhận và đã ghi nhận phân nhóm |
| `assistant_request_opened` | Ứng dụng nhân viên | `trace_id`, `request_id`, `staff_id`, thời gian mở | Khi nhân viên mở yêu cầu bằng trợ lý |
| `agent_run_completed` | Trợ lý | `trace_id`, `request_id`, lần chạy, số token vào/ra, số lượt gọi công cụ, trạng thái | Sau mỗi lần chạy, kể cả lần lỗi |
| `staff_review_decision` | Ứng dụng nhân viên | `trace_id`, `request_id`, quyết định `giu`/`sua`/`bo`, thời gian và số phút xem lại đo thực tế | Khi hoàn tất xem lại |
| `request_closed` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian đóng | Khi đóng yêu cầu |
| `request_reopened` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian mở lại | Khi mở lại |
| `staff_rework_completed` | Ứng dụng nhân viên | `trace_id`, `request_id`, số phút làm lại đo thực tế | Khi hoàn tất làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `request_id`, mã nghĩa vụ hoàn phí, khóa chống trùng, mã giao dịch, số tiền, kết quả ghi sổ | Sau mỗi lần ghi sổ |
| `request_outcome_recorded` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian, kết quả cuối của trợ lý | Khi chốt kết quả xử lý |
| `quality_sample_checked` | Kế toán | `trace_id`, `request_id`, số tiền hoàn thực tế, số tiền đúng, thời gian kiểm tra | Khi kiểm tra yêu cầu được lấy mẫu hằng tuần |

**Kiểm tra chéo:**

- Chỉ số chính: `request_created`, `request_closed`, `request_reopened`; dùng thời gian tạo và đóng, kiểm tra không mở lại trong 7 ngày sau đóng.
- Bỏ qua gợi ý: `staff_review_decision`; lấy quyết định cuối của mỗi yêu cầu được xem lại, đếm `sua` hoặc `bo`.
- Mở lại trong 7 ngày: `request_created`, `request_closed`, `request_reopened`; đếm yêu cầu mở lại trong 7 ngày sau đóng trên tổng yêu cầu đủ thời gian theo dõi.
- Mở bằng trợ lý: `request_created` xác định yêu cầu được giao trong tuần cho nhóm trợ lý và đúng phạm vi. Nối với `assistant_request_opened` để đếm mỗi yêu cầu đã mở một lần.
- Hoàn sai số tiền: `quality_sample_checked`; so số tiền thực tế với số tiền đúng rồi đếm số yêu cầu lệch trong mẫu tuần.
- Hoàn tiền trùng: `refund_ledger_write`; đối soát khi 1 nghĩa vụ hoàn phí có từ 2 mã giao dịch ghi sổ thành công.
- Chi phí mỗi việc thành công: cộng token và lượt gọi công cụ từ `agent_run_completed`, phút thực tế từ `staff_review_decision` và `staff_rework_completed`. Chia cho số yêu cầu thành công từ `request_outcome_recorded`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, B1) | +51,8%: chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ [simulated] | Tỉ lệ `lam_lai` theo tuần trong phạm vi > 7%, tính từ event `staff_rework_completed` (đợt chạy thử: 4,9% = 48/982) | Thu hẹp về `noi_dia`, rà 20 trace làm lại trong 3 ngày trước khi sang bước rollout tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài (B4) | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca như cột simulated [simulated] | % yêu cầu được xem lại > 50% cuối bước rollout 0,25 hoặc phút xem lại đo thật > 5 phút/lần, tính từ event `staff_review_decision` (đợt chạy thử: 13,0% được xem lại trong phạm vi) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% (đợt chạy thử: 21,1% = 27/128 trong phạm vi) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến (A4) | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa, tức 5.784 đ = 0,48× [simulated] | Số việc thành công theo tuần < 50% kế hoạch (kế hoạch 33.750 việc/tháng ở quy mô đầy đủ) | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
