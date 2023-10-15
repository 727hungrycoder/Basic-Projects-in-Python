# pip install qrcode

import qrcode as qr

image = qr.make("https://www.youtube.com/watch?v=fqF9M92jzUo")

image.save("qr.png")
