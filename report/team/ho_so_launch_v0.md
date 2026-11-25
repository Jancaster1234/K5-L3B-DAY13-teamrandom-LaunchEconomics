# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: teamrandom · Lớp: L3B

Mọi số lấy từ output `python lab13.py` (chạy trong `src/`); chi tiết ở `bang_chi_phi.md`, `chi_so.md`, `bang_loi.md`, `pilot_plan.yaml`.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu 4.472 đ [simulated] (4.373.585 ÷ 978), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ). Phạm vi noi_dia + hang_nang 3.414 đ [simulated], chưa gồm chi phí cố định và phần nhân viên xử lý thay các yêu cầu không thành công; cộng cố định: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× nếu còn một nửa [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại gấp đôi +51,8% · tỉ lệ xem lại gấp đôi +40,7% · lương tăng 25% +23,1% [simulated]; giá token gấp đôi chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Chi phí cả hệ thống mỗi **yêu cầu** (khác chi phí mỗi việc thành công, đã cộng 222 ca × 12.000 đ nhân viên làm thay) 5.865 đ = 0,49× của 12.000 đ [simulated]. **Bất lợi:** xem lại 100% trong phạm vi thì 11.743 đ/việc thành công = 0,98× (làm lại 9 phút/ca, hoà vốn khi xem lại ≤ 5,1 phút) hoặc 12.415 đ = 1,03× (làm lại 15,3 phút/ca, hoà vốn ≤ 4,8 phút) [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200) · dùng: bỏ qua gợi ý 27,12% (48/177) · an toàn: mở lại 7 ngày 4,25% (51/1.200). Đợt chạy thử không có đối chứng nên chưa nói được tác động | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; tỉ lệ đồng thuận hai bộ nhãn: chờ `bang_loi.md` (mục tiêu ≥ 16/20) | Chưa | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, mde 6 điểm: 859 hiệu dụng = 5.980 yêu cầu thực tế mỗi nhóm (11.960 cả hai; m ≥ 299, DE 6,96); 4 luật dừng (hoàn trùng dừng ngay); kết luận 2027-01-15 chỉ khi đủ mẫu và đủ 7 ngày theo dõi, gia hạn tối đa 2 tuần theo độ đầy đủ dữ liệu; phân tích theo cụm nhân viên. **Bất lợi:** power chỉ 0,64 nếu tác động thật là 5 điểm | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); khối lượng còn một nửa → cố định +2.370 đ/việc, tổng 5.784 đ = 0,48× [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang (982/1.200 yêu cầu mẫu, 3.414 đ/việc thành công chưa cộng cố định [simulated]); loại quoc_te (1,88×) và doi_tac (0,85×).

Trước ngày bắt đầu 2026-12-07:

- Ký chấp nhận mức chênh 6 điểm, biết power chỉ 0,64 ở mức 5 điểm · Giám đốc vận hành · kiểm tra 2026-12-04.
- Sửa khoá chống trùng và đối soát sổ cái (luật dừng 1: 1 ca hoàn trùng xác nhận là tắt trợ lý trong 30 phút) · Trưởng nhóm kỹ thuật · kiểm tra 2026-12-04.

Trong rollout (mỗi bước chỉ mở rộng khi không luật dừng nào bị kích hoạt và Giám đốc vận hành phê duyệt):

- Bật đủ event có `trace_id`, thay phút simulated bằng phút xem lại và làm lại đo thật sau tuần 1 · PM trợ lý hoàn phí · kiểm tra 2026-12-14.
- Giảm xem lại theo bậc (xem lại 100% tốn 0,98×–1,03× [simulated]); đề xuất ngưỡng thận trọng ≤ 4,8 phút mỗi lần xem lại (kịch bản làm lại 15,3 phút; 5,1 phút chỉ đúng khi làm lại 9 phút), chờ TV1 xác nhận · Trưởng nhóm CSKH · kiểm tra 2026-12-14 (cuối bước 0.10).
