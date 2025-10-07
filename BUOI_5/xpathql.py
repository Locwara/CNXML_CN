from lxml import etree
tree = etree.parse("quanlybanan.xml")
root = tree.getroot()

print("\n1. Lấy tất cả bàn")
bans = root.xpath("//BANS/BAN")
for b in bans:
    print("Bàn")
    for child in b:
        print(f"-{child.tag}: {child.text}")

print("\n2. Lấy tất cả nhân viên")
nhanviens = root.xpath("//NHANVIENS/NHANVIEN/TENV/text()")
for nv in nhanviens:
    print(f"Tên nhân viên: {nv}")

print("\n3. Lấy tất cả tên món")
mons = root.xpath("//MONS/MON/TENMON/text()")
for m in mons:
    print(f"Tên món: {m}")

print("\n4. Lấy tên nhân viên có mã NV02")
ten_nv02 = root.xpath("//NHANVIEN[MANV='NV02']/TENV/text()")
for t in ten_nv02:
    print(f"Tên nhân viên NV02: {t}")

print("\n5. Lấy tên và số điện thoại của nhân viên NV03")
nv03 = root.xpath("//NHANVIEN[MANV='NV03']")
for n in nv03:
    print(f"Tên: {n.find('TENV').text}, SĐT: {n.find('SDT').text}")

print("\n6. Lấy tên món có giá > 50,000")
mon_50k = root.xpath("//MON[number(GIA) > 50000]/TENMON/text()")
for m in mon_50k:
    print(f"Tên món: {m}")

print("\n7. Lấy số bàn của hóa đơn HD03")
soban_hd03 = root.xpath("//HOADON[SOHD='HD03']/SOBAN/text()")
for s in soban_hd03:
    print(f"Số bàn: {s}")

print("\n8. Lấy tên món có mã M02")
ten_m02 = root.xpath("//MON[MAMON='M02']/TENMON/text()")
for t in ten_m02:
    print(f"Tên món M02: {t}")

print("\n9. Lấy ngày lập của hóa đơn HD03")
ngay_hd03 = root.xpath("//HOADON[SOHD='HD03']/NGAYLAP/text()")
for n in ngay_hd03:
    print(f"Ngày lập: {n}")

print("\n10. Lấy tất cả mã món trong hóa đơn HD01")
ma_hd01 = root.xpath("//HOADON[SOHD='HD01']//CTHD/MAMON/text()")
for m in ma_hd01:
    print(f"Mã món: {m}")

print("\n11. Lấy tên món trong hóa đơn HD01")
tenmon_hd01 = root.xpath("//MON[MAMON=//HOADON[SOHD='HD01']//MAMON]/TENMON/text()")
for t in tenmon_hd01:
    print(f"Tên món: {t}")

print("\n12. Lấy tên nhân viên lập hóa đơn HD02")
ten_nv_hd02 = root.xpath("//NHANVIEN[MANV=//HOADON[SOHD='HD02']/MANV]/TENV/text()")
for t in ten_nv_hd02:
    print(f"Tên nhân viên: {t}")

print("\n13. Đếm số bàn")
tongban = root.xpath("count(//BAN)")
print(f"Tổng số bàn: {int(tongban)}")

print("\n14. Đếm số hóa đơn lập bởi NV01")
dem_hd_nv01 = root.xpath("count(//HOADON[MANV='NV01'])")
print(f"Số hóa đơn NV01 lập: {int(dem_hd_nv01)}")

print("\n15. Lấy tên tất cả món có trong hóa đơn của bàn số 2")
mon_ban2 = root.xpath("//MON[MAMON=//HOADON[SOBAN='2']//MAMON]/TENMON/text()")
for m in mon_ban2:
    print(f"Tên món: {m}")

print("\n16. Lấy tất cả nhân viên từng lập hóa đơn cho bàn số 3")
nv_ban3 = root.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='3']/MANV]/TENV/text()")
for n in nv_ban3:
    print(f"Tên nhân viên: {n}")

print("\n17. Lấy tất cả hóa đơn mà nhân viên nữ lập")
hd_nu = root.xpath("//HOADON[MANV=//NHANVIEN[GIOITINH='Nữ']/MANV]/SOHD/text()")
for h in hd_nu:
    print(f"Số hóa đơn: {h}")

print("\n18. Lấy tất cả nhân viên từng phục vụ bàn số 1")
nv_ban1 = root.xpath("//NHANVIEN[MANV=//HOADON[SOBAN='1']/MANV]/TENV/text()")
for n in nv_ban1:
    print(f"Tên nhân viên: {n}")

print("\n19. Lấy tất cả món được gọi nhiều hơn 1 lần trong các hóa đơn")
mon_nhieu = root.xpath("//MON[MAMON=//CTHD[number(SOLUONG) > 1]/MAMON]/TENMON/text()")
for m in mon_nhieu:
    print(f"Tên món: {m}")

print("\n20. Lấy tên bàn + ngày lập hóa đơn tương ứng SOHD='HD02'")
ban_ngay_hd02 = root.xpath("//BANS/BAN[SOBAN=//HOADON[SOHD='HD02']/SOBAN]/TENBAN/text()")
ngay_hd02 = root.xpath("//HOADON[SOHD='HD02']/NGAYLAP/text()")
for b in ban_ngay_hd02:
    for n in ngay_hd02:
        print(f"Tên bàn: {b}, Ngày lập: {n}")
