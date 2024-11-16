# borderless_qrcode.py

import segno

qrcode = segno.make_qr("""
DUMBASS""")
qrcode.save(
    "dumb.png",
    scale=10,
    border=0,
)
