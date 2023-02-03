from PIL import Image
from pyzbar.pyzbar import decode

x = input("Speicherort des Qr-Codes: ")
data = decode(Image.open(x))
print(data)