# Câu 2: Xử lý chuỗi ký tự

s = input("Nhập chuỗi s: ")

# a. Đếm số ký tự chữ hoa
dem_hoa = 0
for ky_tu in s:
    if ky_tu.isupper():
        dem_hoa += 1

print("Số ký tự chữ hoa:", dem_hoa)

# b. Kiểm tra chuỗi đối xứng
if s == s[::-1]:
    print("Chuỗi đối xứng.")
else:
    print("Chuỗi không đối xứng.")

# c. Tính tổng các chữ số trong chuỗi
tong = 0
for ky_tu in s:
    if ky_tu.isdigit():
        tong += int(ky_tu)

print("Tổng các chữ số trong chuỗi:", tong)
