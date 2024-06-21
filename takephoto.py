from picamera import PiCamera
from time import sleep

# Khởi tạo PiCamera
camera = PiCamera()

try:
    # Lấy độ phân giải mặc định của camera
    camera.resolution = (2592, 1944)

    # Để tránh nhiễu hình ảnh, chờ giây lấy nét
    camera.start_preview()
    sleep(2)

    # Chụp ảnh và lưu tệp
    camera.capture('/home/pi/Desktop/image.jpg')

    # Hiển thị thông báo chụp ảnh thành công
    print("Chup anh thanh cong!")

finally:
    # Tắt preview và giải phóng tài nguyên
    camera.stop_preview()
    camera.close()