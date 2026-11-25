# Kiểm số A2 · Nguyễn Quang Tiệp (2A202603946)

Tính tay chi phí mỗi việc thành công để đối chiếu output `python lab13.py` của TV1. Tổng cột lấy bằng SUM/COUNTIF trên hai file CSV; các phép nhân, cộng, chia tính tay.

**Công thức:** chi phí mỗi việc thành công = (token + tool + xem lại + làm lại) ÷ số việc thành công

## Số liệu đầu vào

| Nguồn | Cột | Tổng |
| --- | --- | ---: |
| `logix_runs.csv` (1.624 lần chạy, gồm cả lần lỗi) | `tokens_in` | 5.771.712 |
| | `tokens_out` | 734.774 |
| | `tool_calls` | 5.600 |
| `logix_requests.csv` (1.200 yêu cầu) | `phut_xem_lai_simulated` | 890 |
| | `phut_lam_lai_simulated` | 1.132 |
| | `ket_qua` = `thanh_cong` | 978 |

## Tính tay

| Khoản | Cách tính | Kết quả (đ) |
| --- | --- | ---: |
| Token | 5.771.712 ÷ 1.000 × 26 + 734.774 ÷ 1.000 × 130 | 245.585 |
| Tool | 5.600 × 15 | 84.000 |
| Xem lại | 890 × 2.000 | 1.780.000 [simulated] |
| Làm lại | 1.132 × 2.000 | 2.264.000 [simulated] |
| Tổng | cộng bốn khoản | 4.373.585 [simulated] |
| **Chi phí mỗi việc thành công** | 4.373.585 ÷ 978 | **4.472** [simulated] |

## Đối chiếu

Output của TV1: 4.472 đ. Lệch 0% → **ĐẠT**. Tử số tính mọi lần chạy kể cả lần lỗi; mẫu số chỉ đếm 978 việc thành công.
