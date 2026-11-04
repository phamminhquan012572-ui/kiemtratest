# Câu 3: Xử lý danh sách số nguyên

danhsach = []

# a. Nhập danh sách, kết thúc khi nhập 0
while True:
    x = int(input("Nhập phần tử (nhập 0 để kết thúc): "))

    if x == 0:
        break

    danhsach.append(x)

print("Danh sách vừa nhập:", danhsach)

# b. Tính tổng các số dương chẵn
tong = 0
for x in danhsach:
    if x > 0 and x % 2 == 0:
        tong += x

print("Tổng các số dương chẵn:", tong)

# c. Đếm số lần xuất hiện của phần tử k
k = int(input("Nhập giá trị k cần tìm: "))
dem = 0

for x in danhsach:
    if x == k:
        dem += 1

print("Số lần xuất hiện của", k, "là:", dem)
