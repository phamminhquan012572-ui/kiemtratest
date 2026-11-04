# Câu 4: Quản lý thông tin sách bằng từ điển

from datetime import datetime

n = int(input("Nhập số lượng sách (n > 0): "))
while n <= 0:
    n = int(input("Số lượng phải lớn hơn 0. Nhập lại n: "))

tu_dien_sach = {}
nam_hien_tai = datetime.now().year

# a. Nhập thông tin sách và lưu vào từ điển
for i in range(n):
    print("\nNhập thông tin cuốn sách thứ", i + 1)

    ma_so = input("Mã số sách: ")
    ten_sach = input("Tên sách: ")
    ten_tac_gia = input("Tên tác giả: ")
    nha_xuat_ban = input("Nhà xuất bản: ")

    nam_xuat_ban = int(input("Năm xuất bản: "))
    while nam_xuat_ban > nam_hien_tai:
        nam_xuat_ban = int(input("Năm không hợp lệ, vui lòng nhập lại: "))

    tu_dien_sach[ma_so] = [
        ten_sach,
        ten_tac_gia,
        nha_xuat_ban,
        nam_xuat_ban
    ]

print("\nDanh sách sách trong thư viện:")
for ma_so, thong_tin in tu_dien_sach.items():
    print(ma_so, ":", thong_tin)

# b. Tìm và xóa sách theo mã số
ma_can_xoa = input("\nNhập mã số sách cần xóa: ")

if ma_can_xoa in tu_dien_sach:
    del tu_dien_sach[ma_can_xoa]
    print("Đã xóa cuốn sách có mã số", ma_can_xoa)
else:
    print("Không tìm thấy cuốn sách cần xóa.")

print("Từ điển sau khi xử lý:", tu_dien_sach)
