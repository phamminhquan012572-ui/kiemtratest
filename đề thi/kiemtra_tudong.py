import math
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PYTHON = sys.executable

TESTS = {
    "cau1.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "n = 2",
                "input": "2\n",
                "expected": ["Số lượng chữ số lẻ: 1", "Giá trị S = 0.75"],
            },
            {
                "ten": "n = 1",
                "input": "1\n",
                "expected": ["Số lượng chữ số lẻ: 1", "Giá trị S = 0.5"],
            },
        ],
    },
    "cau2.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "Chuỗi có chữ hoa và chữ số",
                "input": "Abc123cba\n",
                "expected": ["Số ký tự chữ hoa: 1", "Chuỗi không đối xứng", "Tổng các chữ số trong chuỗi: 6"],
            },
            {
                "ten": "Chuỗi đối xứng",
                "input": "Abba\n",
                "expected": ["Số ký tự chữ hoa: 2", "Chuỗi đối xứng", "Tổng các chữ số trong chuỗi: 0"],
            },
        ],
    },
    "cau3.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "Danh sách có số dương chẵn",
                "input": "2\n4\n-3\n0\n2\n",
                "expected": ["Tổng các số dương chẵn: 6", "Số lần xuất hiện của 2 là: 1"],
            },
            {
                "ten": "Giá trị k không có trong danh sách",
                "input": "1\n3\n0\n5\n",
                "expected": ["Tổng các số dương chẵn: 0", "Số lần xuất hiện của 5 là: 0"],
            },
        ],
    },
    "cau4.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "Nhập hai sách và xóa một sách",
                "input": "2\nS01\nPython cơ bản\nNguyen Van A\nNXB Tre\n2024\nS02\nLap trinh Python\nTran Thi B\nNXB Giao Duc\n2023\nS01\n",
                "expected": ["Đã xóa cuốn sách có mã số S01", "'S02':"],
            },
        ],
    },
    "cau5.py": {
        "diem": 2,
        "cases": [
            {
                "ten": "Thông tin hai điện thoại",
                "input": "",
                "expected": ["DT01", "iPhone 15 Pro", "DT02", "Galaxy S24 Ultra", "3274 mAh", "5000 mAh"],
            },
        ],
    },
}


def run_case(file_path, input_data):
    try:
        result = subprocess.run(
            [PYTHON, file_path],
            input=input_data,
            text=True,
            capture_output=True,
            timeout=5,
            encoding="utf-8",
            errors="replace",
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "Chương trình chạy quá 5 giây"


def grade():
    tong_diem = 0.0
    print("=" * 58)
    print("          CHƯƠNG TRÌNH TỰ ĐỘNG KIỂM TRA PYTHON")
    print("=" * 58)

    for filename, cau in TESTS.items():
        path = os.path.join(BASE_DIR, filename)
        print(f"\n[{filename}]")

        if not os.path.isfile(path):
            print("  [THIẾU FILE] Không tìm thấy file bài làm.")
            continue

        dung = 0
        tong_test = len(cau["cases"])

        for index, case in enumerate(cau["cases"], 1):
            code, output, error = run_case(path, case["input"])
            passed = code == 0 and all(
                expected.casefold() in output.casefold()
                for expected in case["expected"]
            )

            if passed:
                dung += 1
                print(f"  [ĐẠT] Test {index}: {case['ten']}")
            else:
                print(f"  [CHƯA ĐẠT] Test {index}: {case['ten']}")
                if error.strip():
                    print("    Lỗi:", error.strip().splitlines()[-1])
                elif output.strip():
                    print("    Kết quả nhận được:")
                    for line in output.strip().splitlines()[-5:]:
                        print("     ", line)
                else:
                    print("    Chương trình không tạo ra kết quả.")

        diem = cau["diem"] * dung / tong_test
        tong_diem += diem
        print(f"  Kết quả câu: {dung}/{tong_test} test | Điểm: {diem:.2f}/{cau['diem']}")

    print("\n" + "=" * 58)
    print(f"TỔNG ĐIỂM: {tong_diem:.2f}/10")
    print("=" * 58)
    print("Lưu ý: Đây là điểm theo các ca kiểm thử mẫu, không thay thế")
    print("việc đối chiếu yêu cầu và định dạng đầu ra trong đề gốc.")


if __name__ == "__main__":
    grade()
