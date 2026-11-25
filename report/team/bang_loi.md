# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Phạm Quang Dũng · Người gắn nhãn 2: duydang2k4 (theo phiếu do thành viên cung cấp)

| Ca | Nhãn người 1       | Nhãn người 2       | Trùng? | Nhãn thống nhất    |
| -: | --------------------- | --------------------- | ------- | --------------------- |
|  1 | Do người dùng      | Do người dùng      | Có     | Do người dùng      |
|  2 | Hệ thống            | Hệ thống            | Có     | Hệ thống            |
|  3 | Giới hạn hệ thống | Ngữ cảnh            | Không  | Ngữ cảnh            |
|  4 | Giới hạn hệ thống | Giới hạn hệ thống | Có     | Giới hạn hệ thống |
|  5 | Ngầm                 | Ngầm                 | Có     | Ngầm                 |
|  6 | Do người dùng      | Do người dùng      | Có     | Do người dùng      |
|  7 | Hệ thống            | Hệ thống            | Có     | Hệ thống            |
|  8 | Hệ thống            | Hệ thống            | Có     | Hệ thống            |
|  9 | Do người dùng      | Do người dùng      | Có     | Do người dùng      |
| 10 | Ngữ cảnh            | Ngữ cảnh            | Có     | Ngữ cảnh            |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có     | Giới hạn hệ thống |
| 12 | Ngầm                 | Ngầm                 | Có     | Ngầm                 |
| 13 | Ngữ cảnh            | Hệ thống            | Không  | Giới hạn hệ thống |
| 14 | Do người dùng      | Do người dùng      | Có     | Do người dùng      |
| 15 | Hệ thống            | Hệ thống            | Có     | Hệ thống            |
| 16 | Ngữ cảnh            | Ngữ cảnh            | Có     | Ngữ cảnh            |
| 17 | Ngầm                 | Ngầm                 | Có     | Ngầm                 |
| 18 | Ngữ cảnh            | Ngữ cảnh            | Có     | Ngữ cảnh            |
| 19 | Ngầm                 | Giới hạn hệ thống | Không  | Giới hạn hệ thống |
| 20 | Hệ thống            | Hệ thống            | Có     | Hệ thống            |

**Tỉ lệ đồng thuận:** 17 / 20 = 85%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Ca 3 — Ngữ cảnh:** Trợ lý hoàn tiền về ví LogiX đúng thiết kế, nhưng khách kỳ vọng tiền về tài khoản ngân hàng.
- **Ca 13 — Giới hạn hệ thống:** Nguyên nhân gốc là yêu cầu hoàn phí bảo hiểm thuộc công ty bảo hiểm đối tác, ngoài phạm vi trợ lý; trợ lý trả lời chung chung là cách xử lý giới hạn kém, cần sửa ở cột khắc phục (báo rõ không xử lý được và chuyển đúng nơi), không đổi loại lỗi. Quy tắc: ngoài phạm vi thì là giới hạn, kể cả khi trợ lý xử lý giới hạn đó kém. Nhãn thống nhất ca này chốt lại sau khi đối chiếu mục "Quy tắc cho các ca dễ lẫn" của file hướng dẫn; hai bộ nhãn độc lập giữ nguyên.
- **Ca 19 — Giới hạn hệ thống:** Đơn đã 14 tháng vượt phạm vi dữ liệu 12 tháng, và trợ lý báo rõ giới hạn khi chuyển yêu cầu cho nhân viên.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| -: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `input_validation_failed` (trường = số tài khoản, sai độ dài hoặc sai định dạng theo ngân hàng đã chọn), đếm hằng ngày; cảnh báo khi > 2% yêu cầu/ngày | Kiểm tra độ dài và định dạng số tài khoản theo từng ngân hàng ngay trên biểu mẫu, chặn tạo lệnh hoàn và yêu cầu khách nhập lại trước khi gửi | PM trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát mỗi giờ event `refund_ledger_write`: cùng `request_id` có ≥ 2 bản ghi hoàn thành công; ngưỡng 0 ca (1 ca là kích hoạt luật dừng 1 trong `pilot_plan.yaml`) | Bắt buộc khoá chống trùng (`idempotency_key` theo mã đơn) cho mọi lệnh hoàn; yêu cầu gửi lại thì trả về trạng thái lệnh cũ, không tạo lệnh mới | Trưởng nhóm kỹ thuật |
| 3 | Ngữ cảnh | Hằng tuần, tỉ lệ `request_reopened` với lý do "chưa nhận tiền" trong khi `refund_ledger_write` đã ghi hoàn về ví LogiX; cảnh báo khi > 1% số yêu cầu hoàn về ví | Hỏi khách chọn đích hoàn (ví hoặc ngân hàng) trước khi xác nhận; tin nhắn hoàn tiền ghi rõ "đã hoàn về ví LogiX" và cách xem số dư | PM trợ lý hoàn phí |
| 19 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = ngoai_12_thang`, đếm theo tuần; cảnh báo khi > 3% yêu cầu/tuần hoặc có ca chuyển không kèm tóm tắt (ngưỡng 0 ca) | Giữ cách báo rõ giới hạn và chuyển nhân viên kèm mã đơn, tóm tắt; nhân viên tra kho dữ liệu lưu trữ ngoài 12 tháng | Trưởng nhóm CSKH |
| 17 | Ngầm | Hằng ngày so phiên bản bảng giá ghi trong `agent_run_completed` với bản đang hiệu lực, ngưỡng 0 đơn lệch; kèm `quality_sample_checked` 100 đơn/tuần so với bảng giá hiện hành, ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace; rà 212 đơn đã tính lệch và hoàn bù | Kế toán trưởng |
