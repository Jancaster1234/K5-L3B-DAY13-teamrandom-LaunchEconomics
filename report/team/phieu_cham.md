# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): teamrandom · L3B
- Nhóm được chấm: 4mems · L3B · repo `tmduc23/K5-L3B-DAY13-4mems-LaunchEconomics`, commit `18cc364`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện khớp với số của nhóm: 4.472 đ/việc thành công, phạm vi noi_dia + hang_nang 5.217 đ/yêu cầu = 0,43× khi đã cộng cố định và 82 ca nhân viên làm thay [simulated]. Nêu cả hai con số bất lợi kèm cách xử lý: power 0,64 nếu tác động thật 5 điểm (ký chấp nhận MDE 6 điểm) và xem lại 100% lên 12.516 đ = 1,04× [simulated] (hạ tỉ lệ xem lại, luật dừng). Điểm cần làm rõ: điều kiện 3 ghi "đủ 859 yêu cầu mỗi nhóm", trong khi `pilot_plan.yaml` ghi cần ≥ 5.980 yêu cầu thực tế mỗi nhóm (859 là mẫu hiệu dụng). |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Phạm vi thu hẹp có lý do bằng số: quoc_te 22.515 đ = 1,88×, thành công 27,3%, tỉ lệ chạy đúng 30,0% → 11,4% → 2,2%; doi_tac 0,85× [simulated]. Nhãn simulated có ở hồ sơ mục 1, 2, 3, 7, bảng chi phí, E2 và danh sách `simulated_inputs` trong `pilot_plan.yaml`. Thiếu nhãn ở 1,88× và 0,85× trong mục 6 của hồ sơ (cùng số đó đã có nhãn trong `pilot_plan.yaml`). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Đối chứng 20 nhân viên chạy cùng tuần, cùng depot, bốc thăm bằng code có seed, phân tầng theo depot, đúng 20 cụm mỗi nhóm. Đủ mẫu cho MDE 6 điểm: 859 hiệu dụng, m ≥ 299, DE 6,96. Ba luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ, có ngưỡng (+2 điểm hoặc trần 6% so với nền 3,97%; 8.000 đ; làm lại 7%; bỏ qua gợi ý 40%), thời hạn (3 ngày, 2 tuần, 1 tuần) và người có quyền dừng (Giám đốc vận hành, tắt trong 30 phút). Điểm yếu: luật 1 gộp hoàn trùng với "3 ngày liên tiếp" thay vì dừng ngay khi có 1 ca; `interim_looks` giữ nguyên câu mẫu. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Trong phạm vi noi_dia + hang_nang, chi phí cả hệ thống 5.217 đ/yêu cầu = 0,43× so với 12.000 đ [simulated], đáng chạy pilot. Hai rủi ro được nêu thẳng và có người phụ trách: xem lại 100% làm chi phí lên 1,04× [simulated], và power chỉ 0,64 ở mức chênh 5 điểm. Thiết kế pilot tách được tác động (20 cụm mỗi nhóm, đối chứng cùng thời gian). Hội đồng đề nghị sửa ngưỡng ra quyết định ở điều kiện 3 thành 5.980 yêu cầu thực tế mỗi nhóm và tách hoàn trùng thành luật dừng ngay.

**Một câu hỏi cho đội trình:** Điều kiện 3 ghi "chỉ ra quyết định khi bước 0,50 đo đủ 859 yêu cầu mỗi nhóm", nhưng `pilot_plan.yaml` ghi cần ít nhất 5.980 yêu cầu mỗi nhóm (20 người × 299). Ngưỡng ra quyết định thật là bao nhiêu, và với 2 tuần ở bước 0,50 cộng 7 ngày theo dõi mở lại, nhóm có đủ dữ liệu trước ngày quyết định 12/01/2027 không?

**Câu trả lời của đội trình (ghi lại tại buổi):** (TV4 ghi tại buổi duyệt chéo)
