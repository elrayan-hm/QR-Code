import qrcode

print('Enter your Ref ID: ')
x = input()
print('\n')

data = f"https://uber.com:3000/boites/{x}"


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(data)
qr.make(fit=True)


img = qr.make_image(fill_color="black", back_color="white")


img.save(f"{x}.png")

print ("done !!")
