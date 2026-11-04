# BÀI GIẢI ĐỀ THI PYTHON

Thư mục này chứa lời giải cho 5 câu hỏi lập trình Python, mỗi câu được lưu trong một file riêng.

## Danh sách file

| File | Nội dung |
|---|---|
| `cau1.py` | Đếm chữ số lẻ và tính tổng S |
| `cau2.py` | Đếm chữ hoa, kiểm tra chuỗi đối xứng, tính tổng chữ số |
| `cau3.py` | Xử lý danh sách số nguyên |
| `cau4.py` | Quản lý sách bằng từ điển |
| `cau5.py` | Lớp `DienThoai` và hai đối tượng mẫu |
| `kiemtra_tudong.py` | Chạy các ca kiểm thử và tính điểm tự động |

## Chạy từng câu

Mở Terminal tại thư mục này và chạy, ví dụ:

```bash
python cau1.py
```

Thay `cau1.py` bằng tên file câu cần chạy.

## Chạy kiểm tra tự động

Không cần cài thêm thư viện. Chạy lệnh:

```bash
python kiemtra_tudong.py
```

Chương trình sẽ tự động:
- Chạy từng file bài làm với dữ liệu kiểm thử mẫu.
- So sánh kết quả đầu ra với kết quả mong đợi.
- Hiển thị trạng thái ĐẠT hoặc CHƯA ĐẠT cho từng test.
- Tính điểm từng câu và tổng điểm trên thang 10.

## Lưu ý

- Các bài giải được chạy độc lập.
- Kiểm thử tự động hiện tại sử dụng các ca kiểm thử mẫu được xây dựng theo chức năng của 5 file trong thư mục.
- Điểm tự động là kết quả kiểm tra theo các ca mẫu, không thay thế việc đối chiếu định dạng đầu ra và toàn bộ yêu cầu trong đề thi gốc.
