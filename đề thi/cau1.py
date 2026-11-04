# Câu 1: Xử lý số nguyên dương n

def dem_chu_so_le(n):
    dem = 0

    while n > 0:
        chu_so = n % 10
        if chu_so % 2 != 0:
            dem += 1
        n //= 10

    return dem


def tinh_s(n):
    tong = 0

    for i in range(1, n + 1):
        tong += 1 / (2 * i)

    return tong


n = int(input("Nhập số nguyên dương n (1 <= n <= 1500): "))

while n < 1 or n > 1500:
    n = int(input("Giá trị không hợp lệ. Nhập lại n (1 <= n <= 1500): "))

print("Số lượng chữ số lẻ:", dem_chu_so_le(n))
print("Giá trị S =", tinh_s(n))
