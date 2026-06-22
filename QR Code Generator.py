import qrcode

data = input("Enter Text: ")

img = qrcode.make(data)

img.save("qrcode.png")

print("QR Code Generated")
