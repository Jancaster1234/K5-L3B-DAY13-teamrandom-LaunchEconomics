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
| 13 | Ngữ cảnh            | Hệ thống            | Không  | Hệ thống            |
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
- **Ca 13 — Hệ thống:** Khi nhận câu hỏi về phí bảo hiểm ngoài phạm vi, trợ lý trả lời sang phí vận chuyển thay vì thông báo rõ giới hạn xử lý.
- **Ca 19 — Giới hạn hệ thống:** Đơn đã 14 tháng vượt phạm vi dữ liệu 12 tháng, và trợ lý báo rõ giới hạn khi chuyển yêu cầu cho nhân viên.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi            | Phát hiện bằng gì                                                                                                                                              | Khắc phục thế nào                                                                                                               | Ai phụ trách                        |
| -: | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
|  1 | Do người dùng      | Ngay khi gửi biểu mẫu, ghi sự kiện nếu số tài khoản thiếu chữ số theo định dạng của ngân hàng đã chọn.                                        | Chặn tạo lệnh hoàn và yêu cầu khách kiểm tra lại số tài khoản.                                                         | Kỹ sư backend                       |
| 20 | Hệ thống            | Cảnh báo khi cùng một mã nghĩa vụ hoàn phí có từ hai giao dịch hoàn thành công.                                                                     | Dùng khóa chống trùng theo mã nghĩa vụ hoàn phí và trả lại trạng thái giao dịch cũ khi khách gửi lại yêu cầu.  | Kỹ sư backend                       |
|  3 | Ngữ cảnh            | Hằng tuần, đếm yêu cầu mở lại trong 7 ngày vì khách chờ tiền về ngân hàng trong khi giao dịch đã ghi có vào ví LogiX.                        | Hiển thị rõ đích hoàn tiền trước khi xác nhận và chỉ khách cách kiểm tra số dư ví trong thông báo hoàn tiền. | Thiết kế trải nghiệm khách hàng |
| 19 | Giới hạn hệ thống | Ghi sự kiện ngay khi yêu cầu tra cứu một đơn cũ hơn 12 tháng.                                                                                           | Thông báo giới hạn tra cứu, rồi chuyển cho nhân viên kèm mã đơn và tóm tắt yêu cầu.                               | Điều phối viên CSKH               |
| 17 | Ngầm                 | Đối soát hằng ngày các đơn dưới 2 kg và cảnh báo khi phiên bản bảng giá đã dùng khác phiên bản có hiệu lực tại thời điểm tính phí. | Xóa bộ nhớ đệm khi bảng giá đổi, sau đó rà soát và xử lý các khoản hoàn bị tính lệch.                         | Kỹ sư phụ trách bảng giá        |
