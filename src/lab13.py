"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        # Bỏ các lần chạy vượt giới hạn; yêu cầu cần nhiều lần hơn coi như chuyển nhân viên, 0 phút xem lại/làm lại.
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    token, tool = tien_token.sum(), tien_tool.sum()
    tong = token + tool + xem_lai + lam_lai          # tử số: MỌI lần chạy, kể cả lần lỗi
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())  # mẫu số: chỉ việc thành công
    return dict(token=token, tool=tool,
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(token + tool) / len(reqs))


# ---------- Nhiệm vụ A2–A4 · TV1 ----------
CHI_PHI_CO_DINH = 40_000_000   # đồng / tháng
YC_MOI_THANG = 45_000          # yêu cầu hoàn phí / tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']


def nhiem_vu_a(runs, reqs):
    """TV1 · A2 bảng chi phí, A3 tách theo loai, A4 chi phí cố định."""
    # A2
    kq = mo_hinh(runs, reqs)
    print('\n=== A2 · Mô hình chi phí từ trace (xem_lai, lam_lai, tong, cps: simulated) ===')
    for ten, gia_tri in kq.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    print(f'Tool: {runs["tool_calls"].sum():,} lần gọi · xem lại: {reqs["phut_xem_lai_simulated"].sum():,} phút'
          f' · làm lại: {reqs["phut_lam_lai_simulated"].sum():,} phút')
    print(f'cps / hoá đơn mỗi yêu cầu = {kq["cps"] / kq["hoa_don_moi_yc"]:.1f} lần')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  tỉ trọng {k:8s} {kq[k] / kq["tong"] * 100:5.1f}%')
    print(f'  giờ nhân viên (xem lại + làm lại) {(kq["xem_lai"] + kq["lam_lai"]) / kq["tong"] * 100:5.1f}%')
    khong_tc = len(reqs) - kq['thanh_cong']
    he_thong = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'Chi phí cả hệ thống mỗi yêu cầu = ({kq["tong"]:,.0f} + {khong_tc} × {BASELINE:,}) / {len(reqs)}'
          f' = {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× (simulated)')

    # A3
    print('\n=== A3 · Theo loại yêu cầu (cps: simulated) ===')
    print(f'{"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"so 12k":>7s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs['loai'] == loai]
        k = mo_hinh(runs, r)
        so_lan = runs['request_id'].isin(r['request_id']).sum() / len(r)
        print(f'{loai:10s} {len(r):6d} {k["thanh_cong"] / len(r) * 100:8.1f}% {so_lan:7.2f}'
              f' {k["cps"]:9,.0f} {k["cps"] / BASELINE:6.2f}×')
    ok = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    ok['ok'] = (ok['status'] == 'ok').astype(float)
    print('Tỉ lệ lần chạy ok theo loai × attempt (%):')
    print((ok.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean') * 100).round(1))

    # A4
    print('\n=== A4 · Chi phí cố định, phạm vi noi_dia + hang_nang (simulated) ===')
    pv = mo_hinh(runs, reqs[reqs['loai'].isin(PHAM_VI)])
    cps_pv = pv['tong'] / pv['thanh_cong']
    print(f'Phạm vi: {pv["thanh_cong"]} việc thành công / {len(reqs)} yêu cầu mẫu; cps phạm vi = '
          f'{pv["tong"]:,.0f} / {pv["thanh_cong"]} = {cps_pv:,.0f} đ')
    for nhan, he_so in [('45.000 yc/tháng', 1.0), ('Một nửa khối lượng', 0.5)]:
        tc_thang = YC_MOI_THANG * he_so * pv['thanh_cong'] / len(reqs)
        co_dinh = CHI_PHI_CO_DINH / tc_thang
        print(f'{nhan:20s} việc TC/tháng {tc_thang:>9,.0f} · cố định/việc {co_dinh:>6,.0f} đ'
              f' · cps + cố định {cps_pv + co_dinh:>6,.0f} đ = {(cps_pv + co_dinh) / BASELINE:.2f}×')
    return kq


# ---------- Nhiệm vụ B · TV1 ----------
def nhiem_vu_b(runs, reqs):
    """TV1 · B1 đổi từng yếu tố, B2 đổi một cặp, B3 giới hạn số lần chạy, B4 xem lại 100%."""
    goc = mo_hinh(runs, reqs)['cps']

    # B1
    print('\n=== B1 · Đổi từng yếu tố (cps: simulated) ===')
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    print(f'{"Gốc (A2)":25s} {goc:8,.0f}')
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    # B2
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\n=== B2 · Token gấp đôi + xem lại gấp đôi: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%) (simulated) ===')

    # B3
    print('\n=== B3 · Giới hạn số lần chạy, chi phí cả hệ thống (simulated) ===')
    print(f'{"gioi_han":>8s} {"tong_tro_ly":>12s} {"khong_tc":>9s} {"ca_he_thong":>12s} {"cps":>7s}')
    for k in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        print(f'{k:8d} {kq["tong"]:12,.0f} {khong_tc:9d} {kq["tong"] + khong_tc * BASELINE:12,.0f} {kq["cps"]:7,.0f}')

    # B4: xem lại 100% trong phạm vi noi_dia + hang_nang
    print('\n=== B4 · Xem lại 100%, phạm vi noi_dia + hang_nang (simulated) ===')
    pv = reqs[reqs['loai'].isin(PHAM_VI)]
    r_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = r_pv.loc[r_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    tc = int((pv['ket_qua'] == 'thanh_cong').sum())
    token_tool = (r_pv['tokens_in'] / 1000 * GIA_VAO + r_pv['tokens_out'] / 1000 * GIA_RA
                  + r_pv['tool_calls'] * GIA_TOOL).sum()
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    print(f'{len(pv)} yêu cầu · {co_ok} có ít nhất một lần ok · {so_lam_lai} ca làm lại · {tc} việc thành công'
          f' · token + tool {token_tool:,.0f} đ')
    for phut_lam_lai in [9, round(phut_lam_lai_tb, 1)]:
        xem = co_ok * 5 * LUONG_PHUT
        lam = so_lam_lai * phut_lam_lai * LUONG_PHUT
        tong = xem + lam + token_tool
        hoa_von = (BASELINE * tc - token_tool - lam) / (co_ok * LUONG_PHUT)
        print(f'làm lại {phut_lam_lai:4} phút/ca: xem {xem:,.0f} + làm lại {lam:,.0f} + token/tool {token_tool:,.0f}'
              f' = {tong:,.0f} đ → {tong / tc:,.0f} đ/việc = {tong / tc / BASELINE:.2f}×'
              f' · hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')
    print(f'(Trung bình phut_lam_lai_simulated trên các ca lam_lai: {phut_lam_lai_tb:.1f} phút,'
          f' trung vị {reqs.loc[reqs["ket_qua"] == "lam_lai", "phut_lam_lai_simulated"].median():.1f})')


# ---------- Nhiệm vụ D · TV2 ----------
def nhiem_vu_d(reqs):
    """TV2 · D1 cỡ mẫu (a–e), power ở mức chênh 5 điểm, tỉ lệ mở lại 7 ngày hiện tại."""
    # from statsmodels.stats.power import NormalIndPower
    pass


# ---------- Nhiệm vụ E1 · TV2 ----------
def nhiem_vu_e(reqs):
    """TV2 · E1 ba chỉ số tính thử: chính, dùng, an toàn."""
    pass


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')  # để console Windows in được tiếng Việt
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    nhiem_vu_a(runs, reqs)
    nhiem_vu_b(runs, reqs)
    nhiem_vu_d(reqs)
    nhiem_vu_e(reqs)
