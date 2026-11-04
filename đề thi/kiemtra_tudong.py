import os
import subprocess
import sys

# Thu muc chua cac file cau1.py den cau5.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable

# Moi ca kiem thu gom:
# - ten: ten tinh huong
# - input: du lieu tu dong nhap vao chuong trinh
# - expected: cac noi dung bat buoc phai xuat hien trong ket qua
TESTS = {
    "cau1.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "n = 2 (khong co chu so le)",
                "input": "2\n",
                "expected": [
                    "b) So luong chu so le cua n: 0",
                    "c) Tong S = 0.750000",
                ],
            },
            {
                "ten": "n = 1 (co mot chu so le)",
                "input": "1\n",
                "expected": [
                    "b) So luong chu so le cua n: 1",
                    "c) Tong S = 0.500000",
                ],
            },
            {
                "ten": "Kiem tra nhap n khong hop le",
                "input": "0\n2\n",
                "expected": [
                    "n khong hop le",
                    "b) So luong chu so le cua n: 0",
                    "c) Tong S = 0.750000",
                ],
            },
        ],
    },
    "cau2.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "Chuoi co chu hoa va cac chu so",
                "input": "Abc123cba\n",
                "expected": [
                    "So ky tu chu hoa: 1",
                    "Chuoi khong doi xung",
                    "Tong cac chu so trong chuoi: 6",
                ],
            },
            {
                "ten": "Chuoi doi xung viet thuong",
                "input": "abcba\n",
                "expected": [
                    "So ky tu chu hoa: 0",
                    "Chuoi doi xung",
                    "Tong cac chu so trong chuoi: 0",
                ],
            },
        ],
    },
    "cau3.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "Danh sach co cac so duong chan va k lap lai",
                "input": "2\n4\n2\n-3\n0\n2\n",
                "expected": [
                    "Tong cac so duong chan: 8",
                    "So lan xuat hien cua 2 la: 2",
                ],
            },
            {
                "ten": "Danh sach khong co so duong chan va k khong ton tai",
                "input": "1\n3\n0\n5\n",
                "expected": [
                    "Tong cac so duong chan: 0",
                    "So lan xuat hien cua 5 la: 0",
                ],
            },
        ],
    },
    "cau4.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "Nhap hai sach va xoa sach S01",
                "input": "2\nS01\nPython co ban\nNguyen Van A\nNXB Tre\n2024\nS02\nLap trinh Python\nTran Thi B\nNXB Giao Duc\n2023\nS01\n",
                "expected": [
                    "Da xoa cuon sach co ma so S01",
                    "'S02':",
                ],
            },
            {
                "ten": "Nhap mot sach va nhap ma khong ton tai",
                "input": "1\nS03\nPython\nNguyen Van C\nNXB Tre\n2022\nS99\n",
                "expected": [
                    "Khong tim thay cuon sach can xoa",
                    "'S03':",
                ],
            },
        ],
    },
    "cau5.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "Kiem tra thong tin hai dien thoai",
                "input": "",
                "expected": [
                    "DT01",
                    "iPhone 15 Pro",
                    "Apple",
                    "3274 mAh",
                    "28990000",
                    "DT02",
                    "Galaxy S24 Ultra",
                    "Samsung",
                    "5000 mAh",
                    "29990000",
                ],
            },
        ],
    },
}


def run_case(file_path, input_data):
    try:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"

        result = subprocess.run(
            [PYTHON, file_path],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=8,
            encoding="utf-8",
            errors="replace",
            cwd=BASE_DIR,
            env=env,
        )

        return result.returncode, result.stdout, result.stderr

    except subprocess.TimeoutExpired:
        return -1, "", "Chuong trinh chay qua 8 giay (co the dang lap vo han)."
    except Exception as error:
        return -2, "", str(error)


def grade():
    tong_diem = 0.0

    print("=" * 65)
    print("             CHUONG TRINH TU DONG KIEM TRA PYTHON")
    print("=" * 65)
    print("Thu muc bai lam:", BASE_DIR)

    for filename, cau in TESTS.items():
        path = os.path.join(BASE_DIR, filename)

        print("\n" + "-" * 65)
        print("KIEM TRA", filename)

        if not os.path.isfile(path):
            print("[THIEU FILE] Khong tim thay", filename)
            print("Diem cau: 0/{:.2f}".format(cau["diem"]))
            continue

        dung = 0
        tong_test = len(cau["cases"])

        for index, case in enumerate(cau["cases"], 1):
            code, output, error = run_case(path, case["input"])

            output_lower = output.casefold()
            missing = [
                item for item in case["expected"]
                if item.casefold() not in output_lower
            ]

            passed = code == 0 and len(missing) == 0

            if passed:
                dung += 1
                print("[DAT] Test {}: {}".format(index, case["ten"]))
            else:
                print("[CHUA DAT] Test {}: {}".format(index, case["ten"]))

                if code != 0:
                    print("  Ma ket thuc chuong trinh:", code)

                if error.strip():
                    print("  Loi chi tiet:", error.strip())

                if missing:
                    print("  Chua tim thay ket qua mong doi:")
                    for item in missing:
                        print("   -", item)

                if output.strip():
                    print("  Ket qua chuong trinh:")
                    for line in output.strip().splitlines():
                        print("   ", line)
                else:
                    print("  Chuong trinh khong in ra ket qua.")

        diem = cau["diem"] * dung / tong_test
        tong_diem += diem

        print("Ket qua cau: {}/{} test".format(dung, tong_test))
        print("Diem cau: {:.2f}/{:.2f}".format(diem, cau["diem"]))

    print("\n" + "=" * 65)
    print("TONG DIEM: {:.2f}/10".format(tong_diem))
    print("=" * 65)
    print("Luu y: Diem duoc tinh dua tren cac ca kiem thu mau trong file nay.")


if __name__ == "__main__":
    grade()
