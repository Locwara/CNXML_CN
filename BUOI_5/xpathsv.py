from lxml import etree

tree = etree.parse("sv.xml")
root = tree.getroot()

print ("1. Lấy tất cả sinh viên")
students = root.xpath("//student")
for student in students:
    print(f"Sinh viên {student.tag}")
    for child in student:
        print(f"{child.tag}: {child.text}")
    print("\n")


print("\n2. Liệt kê tên tất cả sinh viên")

tensv = root.xpath("//student/name/text()")
for ten in tensv:
    print(f"- {ten}")


print("\n3. Lấy tất cả id của sinh viên")

idsvs = root.xpath("//student/id/text()")

for idsv in idsvs:
    print(f"- {idsv}")

print("\n4. Lấy ngày sinh của sinh viên có id = 'SV01'")

sv01 = root.xpath("//student[id='SV01']/date/text()")
print(f"Ngày sinh của SV01: {sv01[0]}")


print("\n5. Lấy các khóa học")

khs = root.xpath("//course")
for kh in khs:
    print(f"Khóa học: {kh.tag}")
    for child in kh:
        print(f"{child.tag} : {child.text}")
    print("\n")

print("\n6. Lấy toàn bộ thông tin của sinh viện đầu tiên")

f_sd = root.xpath("//student[1]")[0]
print(f"ID: {f_sd.find('id').text}")
print(f"Tên: {f_sd.find('name').text}")
print(f"Ngày sinh: {f_sd.find('date').text}")




print("\n7. Lấy mã sinh viên đăng ký khóa học 'Vatly203'")
vl = root.xpath("//enrollment[course='Vatly203']/studentRef")
for v in vl:
    print(f"Id: {v.text}")


print("\n8. Lấy tên sinh viên học môn 'Toan101'")

sv_toan = root.xpath("//student[id=//enrollment[course='Toan101']//studentRef]/name/text()")
for sv in sv_toan:
    print(f"Tên: {sv}")


print("\n9. Lấy tên sinh viên học môn 'Vatly203'")
sv_vatly = root.xpath("//student[id=//enrollment[course='Vatly203']/studentRef]/name/text()")
for sv in sv_vatly:
    print(f"Tên: {sv}")

print("\n10. Lấy ngày sinh của sinh viên có id='SV01'")
date_sv01 = root.xpath("//student[id='SV01']/date/text()")
for d in date_sv01:
    print(f"Ngày sinh: {d}")

print("\n11. Lấy tên và ngày sinh của mọi sinh viên sinh năm 1997")
sv_1997 = root.xpath("//student[starts-with(date,'1997')]")
for sv in sv_1997:
    print(f"Tên: {sv.find('name').text}, Ngày sinh: {sv.find('date').text}")

print("\n12. Lấy tên của các sinh viên có ngày sinh trước năm 1998")
sv_truoc_1998 = root.xpath("//student[number(substring(date,1,4)) < 1998]/name/text()")
for sv in sv_truoc_1998:
    print(f"Tên: {sv}")

print("\n13. Đếm tổng số sinh viên")
tong_sv = root.xpath("count(//student)")
print(f"Tổng số sinh viên: {int(tong_sv)}")

print("\n14. Lấy tất cả sinh viên chưa đăng ký môn nào")
sv_chua_dk = root.xpath("//student[not(id = //enrollment/studentRef)]/name/text()")
for sv in sv_chua_dk:
    print(f"Tên: {sv}")

print("\n15. Lấy phần tử <date> anh em ngay sau <name> của SV01")
date_sau_name = root.xpath("//student[id='SV01']/name/following-sibling::date[1]/text()")
for d in date_sau_name:
    print(f"Ngày sinh (anh em sau <name>): {d}")

print("\n16. Lấy phần tử <id> anh em ngay trước <name> của SV02")
id_truoc_name = root.xpath("//student[name='Lê Thị Hồng Cầm']/preceding-sibling::id[1]/text()")
for i in id_truoc_name:
    print(f"ID (anh em trước <name>): {i}")

print("\n17. Lấy toàn bộ node <course> trong cùng một <enrollment> với studentRef='SV03'")
course_sv03 = root.xpath("//enrollment[studentRef='SV03']/course/text()")
for c in course_sv03:
    print(f"Khóa học: {c}")

print("\n18. Lấy sinh viên có họ là 'Trần'")
sv_tran = root.xpath("//student[starts-with(name,'Trần')]/name/text()")
for sv in sv_tran:
    print(f"Tên: {sv}")

print("\n19. Lấy năm sinh của sinh viên SV01")
nam_sv01 = root.xpath("substring(//student[id='SV01']/date,1,4)")
print(f"Năm sinh: {nam_sv01}")
