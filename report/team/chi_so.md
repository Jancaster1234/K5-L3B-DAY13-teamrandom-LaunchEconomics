# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Chỉ số trong đợt chạy thử được tính trên 1.200 yêu cầu; không có nhóm đối chứng để suy ra tác động.

| Loại | Chỉ số | Công thức | Kết quả đợt chạy thử |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu thỏa cả hai điều kiện / tổng yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số yêu cầu có quyết định `sua` hoặc `bo` / số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu mở lại trong 7 ngày / tổng yêu cầu | 4,25% (51/1.200) |
| Dùng | Tỉ lệ chấp nhận gợi ý | Số yêu cầu được xem lại có quyết định chấp nhận / số yêu cầu được xem lại | Chưa tính |
| An toàn | Tỉ lệ lỗi phát hiện qua kiểm tra mẫu | Số yêu cầu kiểm tra mẫu có lỗi / số yêu cầu được kiểm tra mẫu mỗi tuần | Chưa tính |

## Danh sách event đề xuất

Mỗi event mang `trace_id` và `request_id`; cần triển khai và kiểm tra dữ liệu trước khi đo. Đếm yêu cầu duy nhất, đối chiếu mốc 24 giờ và theo dõi đủ 7 ngày; yêu cầu chưa đủ thời gian theo dõi không đưa vào mẫu kết quả đã trưởng thành.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_created` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian tạo, loại | Khi nhận yêu cầu |
| `suggestion_generated` | Trợ lý | `trace_id`, `request_id`, mã gợi ý | Khi tạo gợi ý |
| `staff_review_decision` | Ứng dụng nhân viên | `trace_id`, `request_id`, quyết định, thời gian và thời lượng xem lại | Khi hoàn tất xem lại |
| `request_closed` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian đóng | Khi đóng yêu cầu |
| `request_reopened` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian mở lại | Khi mở lại |
| `staff_rework_completed` | Ứng dụng nhân viên | `trace_id`, `request_id`, thời lượng làm lại | Khi hoàn tất làm lại |
| `quality_sample_checked` | Công cụ kiểm tra chất lượng | `trace_id`, `request_id`, kết quả lỗi, thời gian kiểm tra | Khi kiểm tra mẫu |

**Kiểm tra chéo:**

- Chỉ số chính: `request_created`, `request_closed`, `request_reopened`; dùng thời gian tạo và đóng, kiểm tra không mở lại trong 7 ngày sau đóng.
- Bỏ qua gợi ý và chấp nhận gợi ý: `staff_review_decision`; tử số theo quyết định, mẫu số là yêu cầu có quyết định xem lại.
- Mở lại trong 7 ngày: `request_created`, `request_closed`, `request_reopened`; đếm yêu cầu mở lại trong 7 ngày sau đóng trên tổng yêu cầu đủ thời gian theo dõi.
- Lỗi kiểm tra mẫu: `quality_sample_checked`; đếm yêu cầu có lỗi trên yêu cầu được kiểm tra.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, B1) | +51,8%: chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ [simulated] | Tỉ lệ `lam_lai` theo tuần trong phạm vi > 7%, tính từ event `staff_rework_completed` (đợt chạy thử: 4,9% = 48/982) | Thu hẹp về `noi_dia`, rà 20 trace làm lại trong 3 ngày trước khi sang bước rollout tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài (B4) | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca như cột simulated [simulated] | % yêu cầu được xem lại > 50% cuối bước rollout 0,25 hoặc phút xem lại đo thật > 5 phút/lần, tính từ event `staff_review_decision` (đợt chạy thử: 13,0% được xem lại trong phạm vi) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% (đợt chạy thử: 21,1% = 27/128 trong phạm vi) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến (A4) | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa, tức 5.784 đ = 0,48× [simulated] | Số việc thành công theo tuần < 50% kế hoạch (kế hoạch 33.750 việc/tháng ở quy mô đầy đủ) | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
