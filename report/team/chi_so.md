# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Chỉ số trong đợt chạy thử được tính trên 1.200 yêu cầu; không có nhóm đối chứng để suy ra tác động.

| Loại | Chỉ số | Công thức | Kết quả đợt chạy thử |
| --- | --- | --- | --- |
| Chính | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu thỏa cả hai điều kiện / tổng yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số yêu cầu có quyết định `sua` hoặc `bo` / số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu mở lại trong 7 ngày / tổng yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm trợ lý được mở bằng trợ lý | Số yêu cầu của nhân viên nhóm trợ lý có event `suggestion_shown` / tổng yêu cầu của nhân viên nhóm trợ lý (luật dừng 4 dùng ngưỡng 50%) | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn kiểm tra mẫu có số tiền hoàn lệch / số đơn được kiểm tra mẫu mỗi tuần | Không cần tính |

## Danh sách event đề xuất

Mỗi event mang `trace_id` và `request_id`; cần triển khai và kiểm tra dữ liệu trước khi đo. Đếm yêu cầu duy nhất, đối chiếu mốc 24 giờ và theo dõi đủ 7 ngày; yêu cầu chưa đủ thời gian theo dõi không đưa vào mẫu kết quả đã trưởng thành.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `request_created` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian tạo, loại | Khi nhận yêu cầu |
| `agent_run_completed` | Trợ lý | `trace_id`, `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, phiên bản bảng giá | Sau mỗi lần chạy, kể cả lần lỗi |
| `suggestion_generated` | Trợ lý | `trace_id`, `request_id`, mã gợi ý | Khi tạo gợi ý |
| `suggestion_shown` | Giao diện nhân viên | `trace_id`, `request_id`, `staff_id`, `arm` | Khi nhân viên mở gợi ý của trợ lý |
| `staff_review_decision` | Ứng dụng nhân viên | `trace_id`, `request_id`, quyết định, thời gian và thời lượng xem lại | Khi hoàn tất xem lại |
| `input_validation_failed` | Biểu mẫu khách | `trace_id`, `request_id`, trường lỗi | Khi dữ liệu khách nhập không hợp lệ |
| `handoff_to_staff` | Trợ lý | `trace_id`, `request_id`, `reason`, tóm tắt | Khi chuyển nhân viên |
| `refund_ledger_write` | Dịch vụ sổ cái | `trace_id`, `request_id`, `idempotency_key`, số tiền, đích hoàn, kết quả | Khi ghi lệnh hoàn |
| `request_closed` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian đóng | Khi đóng yêu cầu |
| `request_reopened` | Hệ thống yêu cầu | `trace_id`, `request_id`, thời gian mở lại, lý do | Khi mở lại |
| `staff_rework_completed` | Ứng dụng nhân viên | `trace_id`, `request_id`, thời lượng làm lại | Khi hoàn tất làm lại |
| `quality_sample_checked` | Công cụ kiểm tra chất lượng | `trace_id`, `request_id`, kết quả lỗi, thời gian kiểm tra | Khi kiểm tra mẫu |

**Kiểm tra chéo:**

- Chỉ số chính: `request_created`, `request_closed`, `request_reopened`; dùng thời gian tạo và đóng, kiểm tra không mở lại trong 7 ngày sau đóng.
- Bỏ qua gợi ý: `staff_review_decision`; tử số là quyết định `sua` hoặc `bo`, mẫu số là yêu cầu có quyết định xem lại.
- % yêu cầu được mở bằng trợ lý (luật dừng 4): `suggestion_shown` trên `request_created` của nhân viên nhóm trợ lý.
- Mở lại trong 7 ngày: `request_created`, `request_closed`, `request_reopened`; đếm yêu cầu mở lại trong 7 ngày sau đóng trên tổng yêu cầu đủ thời gian theo dõi.
- Đơn hoàn sai tiền qua kiểm tra mẫu: `quality_sample_checked`; đếm đơn có số tiền lệch trên đơn được kiểm tra.
- Chi phí mỗi việc thành công (luật dừng 3, E2): `agent_run_completed` (token, tool), `staff_review_decision` và `staff_rework_completed` (phút đo thật), chia số yêu cầu đóng không mở lại.
- Hoàn trùng (luật dừng 1): `refund_ledger_write`, cùng `request_id` có ≥ 2 bản ghi thành công.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi (yếu tố nhạy nhất, B1) | +51,8%: chi phí mỗi việc thành công từ 4.472 đ lên 6.787 đ [simulated] | Tỉ lệ `lam_lai` theo tuần trong phạm vi > 7%, tính từ event `staff_rework_completed` (đợt chạy thử: 4,9% = 48/982) | Thu hẹp về `noi_dia`, rà 20 trace làm lại trong 3 ngày trước khi sang bước rollout tiếp | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài (B4) | 11.743 đ = 0,98× của 12.000 đ; 12.415 đ = 1,03× nếu làm lại 15,3 phút/ca như cột simulated [simulated] | % yêu cầu được xem lại > 50% cuối bước rollout 0,25 hoặc phút xem lại đo thật > 5 phút/lần, tính từ event `staff_review_decision` (đợt chạy thử: 13,0% được xem lại trong phạm vi) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% (đợt chạy thử: 21,1% = 27/128 trong phạm vi) | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến (A4) | Cố định 40 triệu đ/tháng: +1.185 đ/việc ở 45.000 yêu cầu/tháng, +2.370 đ/việc nếu còn một nửa, tức 5.784 đ = 0,48× [simulated] | Số việc thành công theo tuần < 50% kế hoạch (kế hoạch 33.750 việc/tháng ở quy mô đầy đủ) | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
