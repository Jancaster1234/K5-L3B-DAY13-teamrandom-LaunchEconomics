# Báo cáo cá nhân — Bùi Phan Thanh Phúc (2A202603981)

## 1. Thông tin thành viên

- Họ tên: Bùi Phan Thanh Phúc
- MSSV: 2A202603981
- Email: thanhphuccrkh@gmail.com
- GitHub: Jancaster1234
- Vai trong nhóm: TV1, người viết code (nhiệm vụ A, B); nhóm trưởng

## 2. Phần việc phụ trách

Viết `src/lab13.py` phần A1–A4 và B1–B4, điền `report/team/bang_chi_phi.md` và mục E2 (rủi ro kinh tế) trong `report/team/chi_so.md`. Phân việc và quy trình git cho nhóm, soát chéo hồ sơ của các thành viên khác, chấm hồ sơ nhóm 4mems khi làm hội đồng, trả lời hội đồng phần chi phí và cỡ mẫu, chốt bài nộp.

## 3. Đóng góp cụ thể

- **Phân việc và quy trình:** viết `PHAN_CONG.md` (vai, file phụ trách, mốc giờ, quy trình nhánh → pull request → merge vào `main` để tránh conflict); dựng khung `lab13.py` gồm bốn hàm `nhiem_vu_a/b/d/e` để TV2 viết phần D, E1 song song.
- **A1:** ba hàm kinh tế của việc chạy lại; ba phép thử in ĐẠT (1,20 · 1,25 · 1,25).
- **A2:** hàm `mo_hinh` (tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm việc thành công): 4.373.585 đ ÷ 978 = **4.472 đ** mỗi việc thành công [simulated], gấp 16,3 lần hoá đơn token + tool chia số yêu cầu (274,7 đ). Chi phí cả hệ thống, cộng 222 yêu cầu nhân viên làm thay: 5.865 đ = 0,49× của 12.000 đ [simulated].
- **A3, A4:** tách theo loại (noi_dia 0,22× · hang_nang 0,69× · quoc_te 1,88× · doi_tac 0,85× [simulated]); tỉ lệ chạy đúng của quoc_te 30,0% → 11,4% → 2,2% cho thấy chạy lại không giúp. Chi phí cố định: 4.599 đ = 0,38× ở 45.000 yêu cầu/tháng, 5.784 đ = 0,48× khi khối lượng còn một nửa [simulated].
- **B1–B4:** 9 kịch bản độ nhạy (làm lại +51,8% · xem lại +40,7% · lương +23,1%), kịch bản cặp +46,3%, giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ), xem lại 100% ra 11.743 đ = 0,98× hoặc 12.415 đ = 1,03× với mức hoà vốn 5,1 và 4,8 phút [simulated].
- **E2:** ba dòng rủi ro kinh tế lấy số từ bảng độ nhạy, mỗi dòng có dấu hiệu theo dõi gắn với event và một vai trò phụ trách.
- **Soát chéo và sửa:** đổi ngày quyết định pilot sang 2027-01-15 vì dữ liệu mở lại 7 ngày chỉ đủ khoảng 2027-01-11; chốt nhãn thống nhất ca 13 là Giới hạn hệ thống; bổ sung event, ngưỡng và tần suất cho bảng khắc phục; thêm nhãn simulated còn thiếu ở dòng đề xuất; sau câu hỏi của hội đồng, thêm ngưỡng chi phí riêng cho hang_nang (> 12.000 đ) và tách chi phí theo loại trong luật dừng 3.
- **Duyệt chéo:** chấm hồ sơ nhóm 4mems theo C6–C8 (30/30, Go có điều kiện), chỉ ra điều kiện 3 của họ dùng 859 (mẫu hiệu dụng) thay vì 5.980 yêu cầu thực tế. Soạn `HOI_DAP_BAO_VE.md` để nhóm chuẩn bị trả lời hội đồng.

## 4. Bằng chứng

- Code: `src/lab13.py`, hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, `mo_hinh`, `nhiem_vu_a`, `nhiem_vu_b`. Commit `40ab1ec` (khung và A1, PR #2), `c279b67` (A2–A4, PR #3), `16f8dec` (B1–B4 và E2, PR #4).
- Hồ sơ: [bang_chi_phi.md](bang_chi_phi.md), mục E2 trong [chi_so.md](chi_so.md).
- Soát và sửa: commit `616d2b3` (PR #6), `8590c41` (PR #13), `0f4e41d` (PR #17), `c4fec82` (PR #22).
- Duyệt chéo: [phieu_cham.md](phieu_cham.md), commit `53ac9fa` (PR #19).
- Phân việc: `PHAN_CONG.md`, commit `e9bca70` (PR #1); hỏi đáp bảo vệ: `HOI_DAP_BAO_VE.md`, commit `44adb3c`, `fe4f201`.
- Output `python lab13.py`: in "Ba phép thử đáp án biết trước: ĐẠT", mọi số A2, A3, A4, B1–B4 lệch 0% so với bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (B4 lệch 1 đ do làm tròn: 12.415 so với 12.414).

## 5. Công cụ AI đã dùng

- **Claude Code (Claude):** viết code `lab13.py` phần A, B; soạn nội dung `bang_chi_phi.md`, E2, `PHAN_CONG.md`, `HOI_DAP_BAO_VE.md`; soát hồ sơ của các thành viên theo `RUBRIC.md` và đề xuất chỗ sửa; đọc hồ sơ nhóm 4mems để lập bản nháp phiếu chấm; dựng một trang demo tương tác (không nằm trong bài nộp).
- **Cách tự kiểm tra:**
  - Chạy `python lab13.py`: ba phép thử A1 phải in ĐẠT trước khi làm tiếp.
  - So từng số A2, A3, A4, B1–B4 với bảng đối chiếu trong file hướng dẫn, lệch không quá 2%.
  - Kiểm tính chất tuyến tính: kịch bản "giảm một nửa" làm chi phí giảm đúng nửa mức tăng của "gấp đôi" (40,7% → 20,3%).
  - Đối chiếu với phần kiểm số tay của TV2 (`kiem_so_a2_NguyenQuangTiep.md`, 4.472 đ).
  - Mỗi lần sửa hồ sơ: `yaml.safe_load` đọc được `pilot_plan.yaml`, không còn dấu `?`, quét không có từ bị cấm ở quy tắc 5 của `README.md`, và mọi người phụ trách là một vai trò cụ thể.
- Không dùng AI để gắn nhãn 20 ca lỗi (phần đó do TV3, TV4 gắn độc lập). Điểm và lý do trong phiếu chấm nhóm 4mems lấy từ số trong hồ sơ của họ; nhóm đọc lại trước khi nộp.

## 6. Tự đánh giá

Hoàn thành phần A, B đúng số đối chiếu và merge sớm để TV2 có số dùng cho hồ sơ. Điều rút ra lớn nhất: chi phí mỗi việc thành công thấp nhất không đồng nghĩa với rẻ nhất cho công ty (giới hạn 1 lần chạy đẩy thêm 85 yêu cầu sang nhân viên), và phải luôn ghi rõ con số đã cộng chi phí cố định hay phần nhân viên làm thay chưa. Khi soát chéo, chỗ dễ sai nhất không phải công thức mà là các mốc thời gian và ngưỡng phải khớp nhau giữa `pilot_plan.yaml` và hồ sơ. Điểm cần làm tốt hơn: câu hỏi của hội đồng về ngưỡng chi phí gộp cho thấy nhóm nên kiểm luật dừng trên từng loại yêu cầu ngay từ đầu, không chỉ trên số gộp.
