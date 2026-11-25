# Báo cáo cá nhân — Nguyễn Quang Tiệp (2A202603946)

## 1. Thông tin thành viên

- Họ tên: Nguyễn Quang Tiệp
- MSSV: 2A202603946
- Email: nguyenquangtiep175@gmail.com
- GitHub: nguyenquangtiep
- Vai trong nhóm: TV2, người kiểm số; sau giải lao viết code nhiệm vụ D, E1; giữ hồ sơ launch v0

## 2. Phần việc phụ trách

Kiểm số A2 bằng tay; viết `nhiem_vu_d` và `nhiem_vu_e` trong `src/lab13.py`; giữ `report/team/pilot_plan.yaml` và `report/team/ho_so_launch_v0.md`; trình bày hồ sơ nhóm lúc duyệt chéo Gate 2a.

## 3. Đóng góp cụ thể

- **Kiểm số A2:** tính tay độc lập (tổng cột lấy bằng SUM/COUNTIF trên hai file CSV), không dùng hàm `mo_hinh` của TV1; chi tiết ở [kiem_so_a2_NguyenQuangTiep.md](kiem_so_a2_NguyenQuangTiep.md). Token 245.585 đ + tool 84.000 đ (5.600 lần gọi × 15 đ) + xem lại 890 phút × 2.000 đ + làm lại 1.132 phút × 2.000 đ = 4.373.585 đ; chia 978 việc thành công = **4.471,97 đ ≈ 4.472 đ** [simulated], khớp output của TV1. Hoá đơn (token + tool) ÷ 1.200 = 274,7 đ.
- **Nhiệm vụ D (`nhiem_vu_d`):** viết `co_mau(p1, p2)` và năm câu D1: a 1.251 yêu cầu mỗi nhóm; b DE 2,48 → 3.103 mỗi nhóm, cần 84 người > 40; c n hiệu dụng luôn < 1.000; d luôn < 300, chỉ 6 cụm; e m ≥ 299 yêu cầu mỗi người (DE 6,96), 5.980 yêu cầu thực tế mỗi nhóm. Power khi n = 859 mà tác động thật 5 điểm: 0,64. Tỉ lệ mở lại 7 ngày 4,25% toàn mẫu, 3,97% trong phạm vi.
- **Nhiệm vụ E1 (`nhiem_vu_e`):** ba chỉ số tính thử: chính 82,83% (994/1.200), dùng 27,12% (48/177), an toàn 4,25% (51/1.200); gửi TV4 điền `chi_so.md`.
- **`pilot_plan.yaml`:** chia theo nhân viên 20 + 20, mde 6 điểm, phạm vi noi_dia + hang_nang; bốn luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ (hoàn trùng: 1 ca xác nhận là tắt trợ lý trong 30 phút); ngưỡng an toàn so với đối chứng ≥ 2 điểm, trần 6%, để không dừng ngay tuần đầu; điều kiện kết thúc, luật gia hạn tối đa đến 2027-01-29 chỉ vì thiếu dữ liệu, phân tích ở cấp nhân viên.
- **`ho_so_launch_v0.md`:** bảy mục, mỗi mục có con số chính, trạng thái và vai trò phụ trách; đề xuất Go có điều kiện, nêu hai số bất lợi: xem lại 100% tốn 0,98×–1,03× [simulated] và power 0,64 ở mức 5 điểm.
- Sửa lại theo góp ý soát chéo của TV1 (PR #6, #13): ngày quyết định 2027-01-15, `interim_looks`, mục 5 bảng lỗi.

## 4. Bằng chứng

- Kiểm số A2 tính tay: [kiem_so_a2_NguyenQuangTiep.md](kiem_so_a2_NguyenQuangTiep.md), 4.373.585 ÷ 978 = 4.472 đ [simulated], khớp output TV1.
- PR #5 (commit `505af1d`): `nhiem_vu_d`, `nhiem_vu_e`, bản đầu `pilot_plan.yaml` và hồ sơ.
- PR #9 (commit `1534a88`, `a2965f8`): sửa diễn đạt D1c–e, tách luật dừng hoàn trùng, điều kiện kết thúc, phân tích theo cụm, tách các loại chi phí.
- File: [pilot_plan.yaml](pilot_plan.yaml), [ho_so_launch_v0.md](ho_so_launch_v0.md), hàm `nhiem_vu_d`, `nhiem_vu_e` trong [lab13.py](../../src/lab13.py).
- `python lab13.py` in "Ba phép thử đáp án biết trước: ĐẠT" và chạy hết; `yaml.safe_load` đọc được `pilot_plan.yaml`, không còn dấu `?` ngoài chú thích.

## 5. Công cụ AI đã dùng

Dùng Claude Code để đọc đề, viết code `nhiem_vu_d`, `nhiem_vu_e`, soạn `pilot_plan.yaml`, hồ sơ và rà soát lại luật dừng. Tự kiểm tra bằng cách: chạy `python lab13.py` và đối chiếu từng số D1, E1 với file hướng dẫn (lệch dưới 2%); tính tay số A2 để đối chiếu; chạy `yaml.safe_load` và lệnh tìm dấu `?`; so output phần A, B trước và sau khi sửa để chắc không đổi số của TV1.

## 6. Tự đánh giá

Hoàn thành đủ phần D, E1, pilot plan và hồ sơ; số khớp đáp án tham khảo. Điều rút ra: cỡ mẫu hiệu dụng (859) khác số yêu cầu thực tế cần thu (5.980) vì yêu cầu của cùng một nhân viên giống nhau, và luật dừng phải xét tỉ lệ hiện tại để pilot không dừng oan ngay tuần đầu.
