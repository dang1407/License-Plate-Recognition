import requests

url = "http://192.168.149.36:5000/predict_license_plate"

# Đường dẫn tới tệp ảnh cần gửi
image_path = "./3.jpg"

# Đọc nội dung tệp ảnh thành bytes
with open(image_path, "rb") as image_file:
    image_data = image_file.read()

# Tạo dữ liệu đa phần (multipart/form-data) với tệp ảnh
files = {"image": ("image.jpg", image_data, "image/jpeg")}

# Gửi yêu cầu HTTP POST với dữ liệu đa phần
response = requests.post(url, files=files)

# Xử lý phản hồi từ máy chủ
if response.status_code == 200:
    print("Yêu cầu thành công!")
    print("Kết quả:", response.text)
else:
    print("Yêu cầu thất bại với mã lỗi:", response.status_code)