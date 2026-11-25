# Báo cáo nhóm

## 1. Thông tin nhóm

Nhóm teamrandom, lớp L3B, gồm 4 thành viên. [Thông tin và vai trò từng thành viên](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá kinh tế và lập kế hoạch pilot cho trợ lý hoàn phí LogiX-VN trên 1.200 yêu cầu và 1.624 lần chạy, kết hợp phân tích lỗi và chỉ số an toàn.

## 3. Giải pháp

- A–B tính chi phí và 9 kịch bản độ nhạy. [Bảng chi phí](bang_chi_phi.md).
- C so 2 bộ nhãn độc lập, trùng 17/20 (85%), ghi quy tắc cho 3 ca khác nhau và cách khắc phục cho 5 loại lỗi. [Bảng lỗi](bang_loi.md).
- D chia ngẫu nhiên theo nhân viên, 20 người mỗi nhóm và 4 luật dừng. [Kế hoạch pilot](pilot_plan.yaml).
- E tính thử 3 chỉ số, đề xuất thêm 2 chỉ số và 10 event, ghi 3 rủi ro kinh tế. [Đặc tả chỉ số](chi_so.md) và [hồ sơ launch](ho_so_launch_v0.md).

## 4. Kết quả

Chi phí toàn mẫu là 4.472 đ/việc thành công [simulated]. Chỉ số trong đợt chạy thử là 82,83% đóng đúng hạn và không mở lại, 27,12% bỏ qua gợi ý và 4,25% mở lại trong 7 ngày.

Nhóm đề xuất Go có điều kiện cho pilot nội địa và hàng nặng (982/1.200 yêu cầu mẫu). [Phiếu duyệt chéo chờ hồ sơ nhóm được phân công](phieu_cham.md).

## 5. Khó khăn và cách xử lý

Xem lại 100% đưa chi phí mỗi việc thành công lên 0,98–1,03 lần mức nhân viên tự làm 12.000 đ [simulated]. Kế hoạch yêu cầu giảm xem lại theo bậc và đo số phút thực tế.

Trình chạy `.venv` trong phiên giới hạn quyền báo `No Python at ...` do không truy cập được Python Windows. Lệnh `.\.venv\Scripts\python.exe lab13.py` chạy từ `src/` với quyền truy cập Python Windows đã chạy hết và in 3 phép thử đạt.

## 6. Tổng hợp đóng góp

- TV1 tính A–B và viết 3 dòng rủi ro kinh tế. [Bảng chi phí](bang_chi_phi.md) và [mục E2](chi_so.md#e2--rủi-ro-kinh-tế).
- TV2 tính D và E1, lập kế hoạch với 4 luật dừng và tổng hợp hồ sơ 7 mục. [Kế hoạch pilot](pilot_plan.yaml) và [hồ sơ launch](ho_so_launch_v0.md).
- TV3 nhập 2 bộ nhãn, ghi kết quả đối chiếu và 5 dòng khắc phục. [Bảng lỗi](bang_loi.md).
- TV4 cung cấp bộ nhãn 20 ca, viết đặc tả chỉ số và tổng hợp báo cáo nhóm. [Báo cáo cá nhân](2A202603984_DangQuangDuy.md).

## 7. Hạn chế và hướng cải thiện

Đợt chạy thử thiếu nhóm đối chứng. Pilot với 20 nhân viên mỗi nhóm có power 0,64 nếu tác động thực là 5 điểm. Trước khi bắt đầu, cần kiểm tra sự kiện và chuẩn bị thu số phút thực tế từ tuần 1.

## 8. Tài liệu tham khảo

[Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md), [hướng dẫn lab](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md), kết quả `src/lab13.py`.

## 9. Soát hồ sơ nộp

- Repo đúng tên lớp L3B và mở công khai. Đủ 6 file hồ sơ, YAML đọc được bằng `yaml.safe_load`, có 4 luật dừng đủ bốn vế và không còn dấu hỏi ngoài chú thích.
- 3 phép thử A1 đạt, 3 số E1 khớp báo cáo. Mỗi mục trong 7 mục hồ sơ có một vai trò phụ trách. Hồ sơ có đề xuất Go có điều kiện và qua kiểm tra từ cấm. Không thấy tệp môi trường hay khóa truy cập trong các thay đổi TV4.
- TV1 cần bổ sung nhãn `simulated` cho tỷ trọng giờ nhân viên 92,5% và token + công cụ 7,5% ở A2. [Bảng chi phí](bang_chi_phi.md).
- TV2 cần cập nhật mục 5 của hồ sơ theo kết quả 17/20, ghi nhãn cho hai tỉ số chi phí của nhóm ngoài phạm vi và đưa đề xuất xuống cuối hồ sơ. [Hồ sơ launch](ho_so_launch_v0.md).
- Còn thiếu hồ sơ duyệt chéo, bằng chứng chạy trên máy thứ 2 và thông tin cùng báo cáo cá nhân của TV1–TV3. Mỗi thành viên tự nộp link LMS.
