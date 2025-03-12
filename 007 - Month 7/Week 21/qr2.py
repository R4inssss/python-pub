# borderless_qrcode.py

import segno

qrcode = segno.make_qr("""
https://www.youtube.com/watch?v=dQw4w9WgXcQ""")
qrcode.save(
    "QR2.png",
    scale=10,
    border=0,
)
