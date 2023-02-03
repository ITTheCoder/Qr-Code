import pyqrcode
x = input("Url:" )
url = pyqrcode.create(x)
y = input("Dateiformat: ")
if y == 'svg':
    print(url.svg("qr-code\qrcode.svg", module_color=(0,255,0,255), background=(0,0,0,255), scale=50))
if y == 'png':
    print(url.png("qr-code\qrcode.png", module_color=(0,255,0,255), background=(0,0,0,255), scale=50))
if y == 'eps':
    print(url.eps("qr-code\qrcode.eps", module_color=(0,255,0,255), background=(0,0,0,255), scale=50))

