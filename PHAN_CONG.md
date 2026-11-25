# Phân công Lab 13 · nhóm teamrandom

> **Dành cho từng thành viên và agent AI của thành viên đó.**
> Agent: đọc mục "Quy tắc chung", bảng "Ai giữ file nào" và đúng mục TV của người đang dùng bạn. Chỉ sửa những file mà mục đó được giao. Thấy cần sửa file của người khác thì báo cho người dùng, không tự sửa.

## Thành viên

| TV | GitHub | Vai ghi trong `TEAM.md` |
| --- | --- | --- |
| TV1 | Jancaster1234 (**trưởng nhóm**) | Người viết code trước giải lao (nhiệm vụ A, B) |
| TV2 | nguyenquangtiep | Người kiểm số; sau giải lao viết code (nhiệm vụ D, E1); giữ hồ sơ |
| TV3 | quanggpham | Người gắn nhãn 1 |
| TV4 | duydang2k4 | Người gắn nhãn 2 |

## Quy tắc chung (cho cả người và agent)

1. Chỉ sửa file mình giữ (xem bảng dưới). Riêng `src/lab13.py`: TV1 sửa `nhiem_vu_a`, `nhiem_vu_b` và các hàm A1/A2; TV2 chỉ sửa `nhiem_vu_d`, `nhiem_vu_e`.
   **Ngoại lệ: TV1 là tech lead**, khi soát thấy lỗi thì được sửa thẳng mọi file qua PR (tên nhánh `tv1/fix-...`, mô tả PR ghi rõ đã sửa gì và vì sao). Người giữ file không sửa ngược lại; luôn `git pull origin main` trước khi làm tiếp, thấy không đồng ý thì nhắn TV1.
2. Không sửa `src/logix_runs.csv`, `src/logix_requests.csv`, `src/lab13_starter.py`.
3. Mọi con số trong hồ sơ phải lấy từ output của `python lab13.py`, chạy trong thư mục `src/`. File [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md) chỉ dùng để đối chiếu; lệch không quá 2% là đạt. Nếu lệch hơn thì báo TV1 hoặc TV2, không chép số từ file hướng dẫn.
4. Mọi số tính từ hai cột `_simulated` phải ghi nhãn `simulated`.
5. Không dùng từ tiếng Anh bị cấm ở quy tắc 5 trong [README.md](README.md), ở bất kỳ file nào.
6. Người phụ trách trong mọi bảng là **một vai trò** có quyền quyết định (ví dụ "PM trợ lý hoàn phí", "Giám đốc vận hành"), không ghi "cả đội".
7. Mỗi câu trả lời không quá ba dòng và có ít nhất một con số.
8. **Gắn nhãn nhiệm vụ C:** TV3 và TV4 tự gắn, không dùng AI, không trao đổi, không mở mục "Nhãn tham khảo cho 20 ca" của file hướng dẫn trước khi gắn xong. Đã so nhãn thì không sửa bộ nhãn độc lập. Agent không được gợi ý hay đoán nhãn cho 20 ca.
9. **Git:** không push thẳng lên `main`. Làm trên nhánh riêng rồi merge vào `main` qua pull request, theo mục "Quy trình git" bên dưới. Không force-push, không rebase nhánh đã push, không xoá commit.
10. Mỗi người ghi công cụ AI đã dùng và cách tự kiểm tra vào báo cáo cá nhân của mình.

## Ai giữ file nào

| File | Người giữ | Ghi chú |
| --- | --- | --- |
| `src/lab13.py` | TV1 (A, B) · TV2 (D, E1) | Mỗi người chỉ sửa hàm của mình |
| `report/team/bang_chi_phi.md` | TV1 | TV2 kiểm số |
| `report/team/bang_loi.md` | TV3 | TV4 gửi bộ nhãn của mình cho TV3 nhập |
| `report/team/pilot_plan.yaml` | TV2 | TV1 soát chéo |
| `report/team/chi_so.md` | TV4 | Riêng mục **E2 · Rủi ro kinh tế** do TV1 viết |
| `report/team/ho_so_launch_v0.md` | TV2 | TV1 soát chéo |
| `report/team/phieu_cham.md` | TV4 | TV3 cùng đọc hồ sơ nhóm bạn |
| `report/team/group_report.md` | TV4 | |
| `TEAM.md` | TV4 | Mỗi người tự điền MSSV, email của mình |
| `report/team/<MSSV>_<HoTen>.md` | Từng người | Copy từ `report/team/MSSV_HoTen.md`, giữ nguyên file mẫu |

## Quy trình git: nhánh riêng, merge vào `main`

Vì mỗi người chỉ sửa file (hoặc hàm, mục) của mình, git gần như luôn tự gộp được. Ba điều giữ cho không bị conflict: **nhánh ngắn**, **merge sớm**, **luôn cập nhật `main` vào nhánh trước khi mở PR**.

**Tên nhánh:** `tv<số>/<việc>`, ví dụ `tv1/khung-lab13`, `tv1/cp1-cp2`, `tv2/cp4-pilot`, `tv3/bang-loi`, `tv4/chi-so`. Mỗi phần việc xong là một nhánh, merge xong thì mở nhánh mới cho phần sau.

**Các bước cho mỗi phần việc**

```bash
# 1. Bắt đầu từ main mới nhất
git checkout main
git pull origin main
git checkout -b tv1/cp1-cp2

# 2. Làm việc, commit nhỏ, chỉ add file của mình (không dùng git add .)
git add src/lab13.py report/team/bang_chi_phi.md
git commit -m "cp1: a1-a4 va mo_hinh"

# 3. Trước khi push: gộp main mới nhất vào nhánh của mình (merge, không rebase)
git fetch origin
git merge origin/main
#    Nếu conflict: xem mục "Khi bị conflict" bên dưới, sửa xong thì
#    git add <file> && git commit

# 4. Push nhánh và mở pull request vào main
git push -u origin tv1/cp1-cp2
gh pr create --base main --fill        # hoặc mở PR trên GitHub

# 5. Merge PR (chọn "Create a merge commit" để giữ commit của từng người làm bằng chứng đóng góp)
gh pr merge --merge --delete-branch    # hoặc bấm "Merge pull request" trên GitHub

# 6. Quay về main mới nhất trước khi làm phần tiếp theo
git checkout main
git pull origin main
```

**Ai merge:** người mở PR tự merge khi PR chỉ đụng file của mình và không có conflict. PR có sửa `src/lab13.py` thì chạy `python lab13.py` trong `src/` trước khi merge; output phải có dòng ĐẠT và chạy hết không lỗi.

**Thứ tự bắt buộc**

- TV1 merge nhánh `tv1/khung-lab13` vào `main` trước 14:10. TV2 chỉ tạo nhánh làm phần D, E1 **sau khi** khung đã vào `main`.
- Merge ngay khi xong một phần (A xong là merge, không đợi xong cả A và B), để người khác kéo được số và code mới nhất.
- Muốn dùng số của người khác (ví dụ TV4 cần số E1 của TV2) thì đợi PR của họ vào `main`, rồi `git fetch origin && git merge origin/main` vào nhánh của mình.

**Khi bị conflict**

- Conflict ở file hoặc phần của mình: giữ phần của người khác nguyên vẹn, chỉ sửa phần của mình, rồi `git add` và `git commit`.
- Conflict ở phần của người khác (ví dụ hàm `nhiem_vu_d` khi mình là TV1): không tự quyết, nhắn người giữ phần đó để cùng sửa.
- Bối rối thì `git merge --abort` để quay về trạng thái trước khi merge, rồi hỏi TV1.

**Agent:** chỉ commit trên nhánh `tv<số>/...` của người dùng, không push thẳng lên `main`, không dùng `--force`, không `git add .`, không sửa file ngoài danh sách được giao để "gỡ" conflict.

## Mốc thời gian

Không chờ từng checkpoint. Cả bốn người làm song song từ 14:10. Mục tiêu: hồ sơ xong khoảng 16:15.

| Giờ | TV1 | TV2 | TV3 | TV4 |
| --- | --- | --- | --- | --- |
| 14:00–14:10 | Cài môi trường, merge khung `lab13.py` vào `main` | Cài môi trường | Cài môi trường | Cài môi trường |
| 14:10–15:00 | A1–A4, B1–B4 trong `lab13.py` | Kiểm số A2 bằng tay; viết `nhiem_vu_d`, `nhiem_vu_e`; dựng khung hồ sơ | Gắn nhãn 20 ca (8–10 phút); dựng khung `bang_loi.md` | Gắn nhãn 20 ca (8–10 phút); điền `TEAM.md`; bảng event trong `chi_so.md` |
| 15:00–16:15 | Điền `bang_chi_phi.md`; viết E2 trong `chi_so.md`; soát `pilot_plan.yaml` và hồ sơ | Điền `pilot_plan.yaml`; ghép số vào `ho_so_launch_v0.md` | So nhãn với TV4; điền `bang_loi.md`; chạy `lab13.py` trên máy mình; soát nhãn `simulated` | Đặc tả chỉ số và số E1 trong `chi_so.md` |
| 16:15–17:00 | Báo cáo cá nhân | Báo cáo cá nhân | Báo cáo cá nhân | Báo cáo cá nhân; chạy checklist cuối |
| 17:00–17:45 | Trả lời hội đồng (chi phí, cỡ mẫu) | Trình bày hồ sơ nhóm mình | Đọc hồ sơ nhóm bạn | Đọc hồ sơ nhóm bạn, ghi `phieu_cham.md` |
| 17:45–18:00 | Merge PR cuối, ghi commit chốt vào `TEAM.md` | | | Điền `group_report.md` |

---

## TV1 · Jancaster1234 · Người viết code (A, B) · trưởng nhóm

**Tài liệu:** file hướng dẫn, mục "Nhiệm vụ A" và "Nhiệm vụ B"; [docs/du_lieu_va_cong_thuc.md](docs/du_lieu_va_cong_thuc.md).

**Việc cần làm**

1. **Commit khung (trước 14:10).** Trong `src/lab13.py`, giữ nguyên phần đầu file, thêm bốn hàm `nhiem_vu_a(runs, reqs)`, `nhiem_vu_b(runs, reqs)`, `nhiem_vu_d(reqs)`, `nhiem_vu_e(reqs)` (hai hàm sau để `pass` cho TV2). Khối `__main__` đọc dữ liệu, gọi `kiem_tra_dap_an_biet_truoc()` rồi gọi lần lượt bốn hàm. Làm trên nhánh `tv1/khung-lab13` và merge vào `main` ngay để TV2 bắt đầu.
2. **A1:** viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`.
3. **A2:** viết `mo_hinh(...)`, trả về dict gồm `token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc`. Tử số tính mọi lần chạy, kể cả lần lỗi; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Có tham số `max_lan_chay` cho B.
4. **A3:** gọi `mo_hinh` cho từng giá trị cột `loai`; in thêm tỉ lệ `status == 'ok'` theo `loai` × `attempt`.
5. **A4:** cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`, ở khối lượng đầy đủ và khi khối lượng giảm một nửa.
6. **B1:** 9 kịch bản đổi từng yếu tố. **B2:** giá token gấp đôi cùng xem lại gấp đôi, xếp hạng ba yếu tố. **B3:** giới hạn 1, 2, 3 lần chạy, tính chi phí cả hệ thống (cộng 12.000 đ cho mỗi yêu cầu không thành công). **B4:** xem lại 100% cho `noi_dia` + `hang_nang` (5 phút cho mỗi yêu cầu có ít nhất một lần chạy ok, 9 phút cho mỗi ca làm lại), tính thêm bản 15,3 phút làm lại và mức hoà vốn.
7. Điền `report/team/bang_chi_phi.md`: A2 đủ 9 dòng (hai dòng xem lại, làm lại có nhãn `simulated`), A3 đủ 4 dòng, A4, B1 đủ 9 dòng, xếp hạng, B3, B4.
8. Viết ít nhất hai dòng rủi ro trong mục **E2 · Rủi ro kinh tế** của `report/team/chi_so.md`, số lấy từ bảng độ nhạy.
9. Soát chéo `pilot_plan.yaml` và `ho_so_launch_v0.md` của TV2.
10. Lúc duyệt chéo: trả lời hội đồng về chi phí mỗi việc thành công và cỡ mẫu. 17:45 merge PR cuối vào `main` sau khi TV4 báo checklist đạt, ghi hash commit chốt vào `TEAM.md`.

**Xong khi**

- `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` và chạy hết không lỗi.
- Chi phí mỗi việc thành công khoảng 4.472 đ [simulated], gấp khoảng 16,3 lần hoá đơn token chia số yêu cầu.
- Mỗi kịch bản "giảm một nửa" làm chi phí giảm đúng nửa mức tăng của kịch bản "gấp đôi".

---

## TV2 · nguyenquangtiep · Người kiểm số, viết code (D, E1), giữ hồ sơ

**Tài liệu:** file hướng dẫn, mục "A2" (để kiểm số), "Nhiệm vụ D", "E1", "E3"; mẫu `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`.

**Việc cần làm**

1. **Kiểm số (trước giải lao):** tính tay ít nhất một con số A2 từ CSV (ví dụ tổng chi phí ÷ số việc thành công), ghi cách tính vào báo cáo cá nhân. Lệch với output của TV1 thì báo TV1 ngay.
2. **`nhiem_vu_d(reqs)`** trong `lab13.py`: hàm `co_mau(p1, p2)`; năm câu D1 (a: chia theo yêu cầu; b: theo nhân viên, m = 75; c: 20 nhân viên mỗi nhóm; d: 6 depot mỗi nhóm; e: mức chênh 6 điểm, tìm m nhỏ nhất); power khi n = 859 mà tác động thật chỉ 5 điểm; tỉ lệ `mo_lai_trong_7_ngay` trên toàn mẫu và trong phạm vi `noi_dia` + `hang_nang`.
3. **`nhiem_vu_e(reqs)`** trong `lab13.py`: ba chỉ số chính, dùng, an toàn. Gửi số cho TV4 điền `chi_so.md`.
4. **`report/team/pilot_plan.yaml`:** ghi D1, D2 vào phần chú thích đầu file; điền mọi dấu `?`; chia theo nhân viên 20 + 20, ghi rõ đánh đổi (mức chênh 6 điểm, power khoảng 0,64 ở mức 5 điểm); ít nhất ba luật dừng (an toàn, chi phí, mức độ sử dụng) đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ, mỗi luật có ngưỡng, thời hạn và vai trò có quyền dừng. Ngưỡng an toàn phải xét tỉ lệ mở lại hiện tại để pilot không bị dừng ngay tuần đầu.
5. **`report/team/ho_so_launch_v0.md`:** dựng khung từ đầu buổi, ghép dần số của A–D. Bảy mục, mỗi mục có con số chính, trạng thái (Xong, có bằng chứng · Chưa · Giả lập) và một vai trò phụ trách. Các mục 1, 2, 3, 7 ghi Giả lập. Dòng cuối là đề xuất, chỉ một trong ba: Go, Go có điều kiện, No-go. Phải nêu cả con số bất lợi và cách xử lý (ví dụ xem lại 100% thì gần bằng hoặc đắt hơn nhân viên tự làm; power thấp ở mức 5 điểm).
6. Lúc duyệt chéo: trình bày hồ sơ nhóm mình trong 1 phút.

**Xong khi**

- `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"` chạy không lỗi (chạy trong `src/`).
- `grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'` không in gì.
- D1 câu a khoảng 1.251 yêu cầu mỗi nhóm; hồ sơ đủ bảy mục và có dòng đề xuất.

---

## TV3 · quanggpham · Người gắn nhãn 1

**Tài liệu:** 20 ca lỗi trong [docs/Ngay13_Lab13_De_bai_hoc_vien.docx](docs/Ngay13_Lab13_De_bai_hoc_vien.docx), mục "Hai mươi ca lỗi"; bảng năm loại lỗi ở đầu mục "Nhiệm vụ C" của file hướng dẫn (chỉ đọc bảng định nghĩa, **không** đọc mục "Nhãn tham khảo" và "Quy tắc cho các ca dễ lẫn" trước khi gắn xong).

**Việc cần làm**

1. **Gắn nhãn độc lập (8–10 phút):** tự gắn cả 20 ca vào năm loại (Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm), theo nguyên nhân gốc, không theo chỗ cần sửa. Không dùng AI, không trao đổi với TV4. Gắn xong, gửi ảnh chụp bộ nhãn lên nhóm chat trước khi so (làm bằng chứng gắn độc lập).
2. **So nhãn với TV4:** nhập cả hai bộ vào `report/team/bang_loi.md`, tính tỉ lệ đồng thuận = số ca trùng ÷ 20. Với mỗi ca không trùng, hai người thống nhất nhãn và ghi một câu quy tắc phân biệt. Dưới 16/20 thì viết lại định nghĩa trước khi đi tiếp.
3. **Bảng khắc phục:** chọn 5 ca, mỗi loại một ca. Mỗi dòng có cách phát hiện **đo được** (event, ngưỡng, tần suất), cách khắc phục và một vai trò phụ trách. Được dùng AI cho bước này.
4. Chạy `python lab13.py` trên máy mình để kiểm tra code chạy được trên máy khác; lỗi thì báo TV1 hoặc TV2.
5. Soát nhãn `simulated` ở mọi file trong `report/team/`; thiếu ở đâu thì báo người giữ file đó.
6. Lúc duyệt chéo: cùng TV4 đọc hồ sơ nhóm bạn, góp ý cho phiếu chấm.

**Xong khi**

- `bang_loi.md` có hai bộ nhãn độc lập, tỉ lệ đồng thuận, quy tắc cho các ca không trùng, bảng khắc phục đủ năm loại.

---

## TV4 · duydang2k4 · Người gắn nhãn 2

**Tài liệu:** như TV3 cho phần gắn nhãn; file hướng dẫn, mục "E1" (danh sách event) và "Duyệt chéo Gate 2a"; mẫu `report/team/chi_so.md`, `report/team/phieu_cham.md`, `report/team/group_report.md`.

**Việc cần làm**

1. **Gắn nhãn độc lập (8–10 phút):** như bước 1 của TV3. Gửi ảnh chụp bộ nhãn lên nhóm chat, rồi gửi bộ nhãn cho TV3 nhập vào `bang_loi.md`. Cùng TV3 thống nhất các ca không trùng.
2. **`TEAM.md`:** tên nhóm (teamrandom), lớp L3B, URL repo, bảng thành viên với vai như mục "Thành viên" ở trên. Nhắc từng người tự điền MSSV, email và phần đóng góp của mình.
3. **`report/team/chi_so.md`** (trừ mục E2 của TV1):
   - Bảng E1: điền số tính thử của ba chỉ số từ output `nhiem_vu_e` của TV2; đề xuất thêm một chỉ số dùng và một chỉ số an toàn (ví dụ kiểm tra mẫu hằng tuần để bắt lỗi ngầm).
   - Danh sách ít nhất sáu event, mỗi event có `trace_id`.
   - Kiểm tra chéo: với mỗi chỉ số, ghi event dùng để tính.
   - Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số".
4. **Duyệt chéo (17:00):** cùng TV3 đọc hồ sơ nhóm n + 1, chấm theo thang ba tiêu chí của hội đồng, ghi `report/team/phieu_cham.md` gồm quyết định, lý do và một câu hỏi.
5. **Checklist cuối (16:45 và 17:45):** chạy hết checklist trong [SUBMISSION.md](SUBMISSION.md#checklist), báo TV1 khi đạt để TV1 merge PR cuối.
6. Điền `report/team/group_report.md`.

**Xong khi**

- `chi_so.md` có ba chỉ số tính thử, hai chỉ số tự đề xuất, ít nhất sáu event có `trace_id`.
- Checklist trong `SUBMISSION.md` đạt hết, trừ dòng nộp LMS (từng người tự nộp).

---

## Việc của cả bốn người

- Copy `report/team/MSSV_HoTen.md` thành `report/team/<MSSV>_<HoTenKhongDau>.md` và điền báo cáo cá nhân. Giữ nguyên file mẫu.
- Điền phần đóng góp của mình trong `TEAM.md`.
- **Tự nộp link repo nhóm trên LMS bằng tài khoản cá nhân trước 23h59 GMT+7 ngày lab.** Ai không nộp thì không có điểm.
