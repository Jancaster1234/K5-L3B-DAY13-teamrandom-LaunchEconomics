# Team

## Thông tin nhóm

- Tên nhóm: teamrandom
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-teamrandom-LaunchEconomics`
- URL repo: https://github.com/Jancaster1234/K5-L3B-DAY13-teamrandom-LaunchEconomics · Nhánh nộp và commit chốt: chờ nhóm trưởng xác nhận

## Thành viên

| STT | Họ tên          | MSSV            | Email                      | GitHub          | Vai trò                                        |
| --: | ----------------- | --------------- | -------------------------- | --------------- | ----------------------------------------------- |
|   1 | Chờ tự điền   | Chờ tự điền | Chờ tự điền            | Jancaster1234   | Viết code A, B; trưởng nhóm                 |
|   2 | Nguyễn Quang Tiệp | 2A202603946 | nguyenquangtiep175@gmail.com             | nguyenquangtiep | Kiểm số; viết code D, E1; giữ hồ sơ       |
|   3 | Phạm Quang Dũng | 2A202603896     | phamquangdung188@gmail.com | quanggpham      | Người gắn nhãn 1                            |
|   4 | Đặng Quang Duy   | 2A202603984 | dqduy4444@gmail.com            | duydang2k4      | Người gắn nhãn 2; chỉ số, báo cáo nhóm |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## HoVaTen-MSSV

### Phần việc phụ trách

### Đóng góp cụ thể

### Bằng chứng

Mỗi thành viên tự bổ sung họ tên, MSSV, email và đóng góp có bằng chứng; commit chốt do trưởng nhóm xác nhận.

## Phạm Quang Dũng-2A202603896

### Phần việc phụ trách

- Người gắn nhãn 1, phụ trách bảng lỗi và cách khắc phục ở CP3.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca và đối chiếu với TV4. Hai bộ nhãn trùng 17/20 ca (85%).
- Ghi nhãn thống nhất, giải thích 3 ca lệch và hoàn thiện bảng khắc phục cho 5 ca.
- Chạy kiểm tra `lab13.py` trên máy cá nhân. Script chạy hết và ba phép thử A1 đều đạt.

### Bằng chứng

- [Bảng lỗi và giải pháp](report/team/bang_loi.md), commit `d4fa8cb` và `69bc498`.

## Nguyễn Quang Tiệp-2A202603946

### Phần việc phụ trách

- TV2: người kiểm số; viết code nhiệm vụ D, E1; giữ `pilot_plan.yaml` và `ho_so_launch_v0.md`; trình bày hồ sơ khi duyệt chéo.

### Đóng góp cụ thể

- Kiểm số A2 độc lập từ CSV: 4.373.585 ÷ 978 = 4.472 đ [simulated], khớp output của TV1.
- Viết `nhiem_vu_d` (D1 a–e: 1.251 · 3.103 · < 1.000 · < 300 · m ≥ 299; power 0,64) và `nhiem_vu_e` (82,83% · 27,12% · 4,25%).
- Điền `pilot_plan.yaml` (chia theo nhân viên 20 + 20, mde 6 điểm, 4 luật dừng) và hồ sơ launch v0 (7 mục, Go có điều kiện).

### Bằng chứng

- [Báo cáo cá nhân](report/team/2A202603946_NguyenQuangTiep.md); PR #5 (commit `505af1d`), PR #9 (commit `1534a88`, `a2965f8`).

## Đặng Quang Duy-2A202603984

### Phần việc phụ trách

- Người gắn nhãn 2 (TV4); phụ trách đặc tả chỉ số, event và tổng hợp báo cáo nhóm.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca; khi đối chiếu với TV3, hai bộ nhãn trùng 17/20 ca (85%) và thống nhất quy tắc cho 3 ca lệch.
- Đối chiếu 3 chỉ số tính thử, đề xuất thêm 2 chỉ số và rà soát 10 event theo 4 luật dừng trong kế hoạch pilot.
- Tổng hợp báo cáo nhóm và chuẩn bị phiếu duyệt chéo theo thang 30 điểm; phiếu chờ hồ sơ nhóm được phân công.

### Bằng chứng

- [Bảng lỗi](report/team/bang_loi.md), [đặc tả chỉ số](report/team/chi_so.md) và [báo cáo nhóm](report/team/group_report.md); commit `9846ce7` (cập nhật bộ nhãn, chỉ số và báo cáo) và `6ba192b` (hoàn thiện chỉ số, báo cáo nhóm và báo cáo cá nhân).
