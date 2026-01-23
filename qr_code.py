import qrcode

url = input("Enter the link: ")
file_path = "Pictures/qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code created successfully! ")