# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: teamrandom · Lớp: L3B

Mọi số lấy từ output `python lab13.py` (chạy trong `src/`); chi tiết ở `bang_chi_phi.md`, `chi_so.md`, `bang_loi.md`, `pilot_plan.yaml`.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ [simulated] (4.373.585 đ ÷ 978 việc thành công), gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ); trong phạm vi noi_dia + hang_nang 3.414 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Số ca làm lại gấp đôi +51,8% · tỉ lệ xem lại gấp đôi +40,7% · lương tăng 25% +23,1% [simulated]; giá token gấp đôi chỉ +5,6% | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ [simulated]. **Bất lợi:** xem lại 100% trong phạm vi thì 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút/ca) [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83% (994/1.200) · dùng: bỏ qua gợi ý 27,12% (48/177) · an toàn: mở lại 7 ngày 4,25% (51/1.200). Đợt chạy thử không có đối chứng nên chưa nói được tác động | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại; tỉ lệ đồng thuận hai bộ nhãn: chờ `bang_loi.md` (mục tiêu ≥ 16/20) | Chưa | Trưởng nhóm CSKH |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, mde 6 điểm (859 mỗi nhóm, m ≥ 299, DE 6,96); 3 luật dừng; quyết định 2027-01-15 (đủ dữ liệu mở lại 7 ngày khoảng 2027-01-11). **Bất lợi:** power chỉ 0,64 nếu tác động thật là 5 điểm | Xong, có bằng chứng | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi → 6.787 đ (+51,8%); khối lượng còn một nửa → cố định +2.370 đ/việc, tổng 5.784 đ = 0,48× [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot noi_dia + hang_nang (982/1.200 yêu cầu mẫu, 3.414 đ/việc thành công [simulated]); loại quoc_te (1,88×) và doi_tac (0,85×).

- Ký chấp nhận mức chênh 6 điểm, biết power chỉ 0,64 ở mức 5 điểm · Giám đốc vận hành · kiểm tra 2026-12-04.
- Có kế hoạch giảm xem lại theo bậc (xem lại 100% gần bằng hoặc đắt hơn nhân viên tự làm: 0,98×–1,03× [simulated]); mục tiêu mỗi lần xem lại ≤ 5,1 phút · Trưởng nhóm CSKH · kiểm tra 2026-12-14 (cuối bước 0.10).
- Bật đủ event có `trace_id` và thay phút simulated bằng phút đo thật sau tuần 1 · PM trợ lý hoàn phí · kiểm tra 2026-12-14.
- Sửa khoá chống trùng và đối soát sổ cái cho các ca hoàn trùng trong bảng lỗi trước ngày bắt đầu 2026-12-07 · Trưởng nhóm kỹ thuật · kiểm tra 2026-12-04.
