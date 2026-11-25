# Báo cáo nhóm

## 1. Thông tin nhóm

Nhóm teamrandom, lớp L3B; 4 thành viên và vai trò tại [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá kinh tế và lập kế hoạch pilot cho trợ lý hoàn phí LogiX-VN bằng 1.200 yêu cầu và trace, kết hợp phân tích lỗi và chỉ số an toàn.

## 3. Giải pháp

- A–B: tính chi phí và độ nhạy trong [bảng chi phí](bang_chi_phi.md).
- C: phân loại 20 ca và đề xuất khắc phục trong [bảng lỗi](bang_loi.md); đã có bộ nhãn 20 ca của TV4; chờ TV3 nhập và đối chiếu với bộ nhãn thứ nhất.
- D: thiết kế thử nghiệm đối chứng theo nhân viên trong [kế hoạch pilot](pilot_plan.yaml).
- E: đặc tả chỉ số trong [chỉ số](chi_so.md) và tổng hợp quyết định tại [hồ sơ launch](ho_so_launch_v0.md).

## 4. Kết quả

Chi phí 4.472 đ/việc thành công [simulated]; trong đợt chạy thử, chỉ số chính 82,83% (994/1.200), mở lại 4,25% (51/1.200). Hồ sơ đề xuất Go có điều kiện cho pilot nội địa và hàng nặng; kết quả duyệt chéo chờ hội đồng.

## 5. Khó khăn và cách xử lý

Xem lại 100% làm chi phí đạt 0,98–1,03 lần mức 12.000 đ [simulated]; kế hoạch yêu cầu giảm xem lại theo bậc và đo thời gian thực.

## 6. Tổng hợp đóng góp

Vai trò của 4 thành viên tại [TEAM.md](../../TEAM.md); mỗi người cần bổ sung đóng góp và bằng chứng của mình.

## 7. Hạn chế và hướng cải thiện

Đợt chạy thử không có đối chứng; pilot dự kiến 20 nhân viên mỗi nhóm, power 0,64 nếu tác động thực là 5 điểm. Cần nhận bộ nhãn TV3, tính đồng thuận trên 20 ca, kiểm tra event và đo chi phí thực.

## 8. Tài liệu tham khảo

[Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), kết quả `src/lab13.py`.
