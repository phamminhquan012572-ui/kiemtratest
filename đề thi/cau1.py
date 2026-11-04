# CAU 1: Xu ly so nguyen duong n

# a) Nhap n va kiem tra dieu kien 1 <= n <= 1500
n = int(input("a) Nhap so nguyen duong n (1 <= n <= 1500): "))

while n < 1 or n > 1500:
    print("n khong hop le, vui long nhap lai!")
    n = int(input("a) Nhap lai n (1 <= n <= 1500): "))


# b) Dem so chu so le cua n
def dem_chu_so_le(n):
    dem = 0

    while n > 0:
        chu_so = n % 10

        if chu_so % 2 != 0:
            dem += 1

        n = n // 10

    return dem


# c) Tinh tong S = 1/2 + 1/4 + ... + 1/(2*n)
def tinh_tong_s(n):
    tong = 0

    for i in range(1, n + 1):
        tong = tong + 1 / (2 * i)

    return tong


# In ket qua rieng cho tung y a, b, c
print("\n========== KET QUA CAU 1 ==========")
print("a) Gia tri n hop le:", n)
print("b) So luong chu so le cua n:", dem_chu_so_le(n))
print("c) Tong S =", format(tinh_tong_s(n), ".6f"))
