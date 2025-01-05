import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

print('Enter your Ref ID: ')
x = input()
print('\n')


image_path = f"{x}.png"
img = Image.open(image_path)


decoded_objects = decode(img)

if decoded_objects:
    decoded_data = decoded_objects[0].data.decode('utf-8')
    print("Données du code QR :")
    print(decoded_data)
else:
    print("Aucun code QR trouvé dans l'image.")
