import matplotlib.pyplot as plt
import qrcode

bee1 = """
According to all known laws of aviation, there is no way that a bee should be able to fly. 
Its wings are too small to get its fat little body off the ground. The bee, of course, flies 
anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. 
Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast 
is ready! Coming! Hang on a second. Hello? - Barry? - Adam? - Can you believe this is happening? - 
I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money for those.
Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's.
Very proud. Ma! I got a thing going here. You got lint on your fuzz. Ow! That's me! Wave to us! We'll be 
in row 118,000. Bye! Barry, I told you, stop flying in the house! - Hey, Adam. - Hey, Barry. - Is that fuzz gel? - A little. 
Special day, graduation.
"""

qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(bee1)
qr.make(fit=True)

# Generate image
img = qr.make_image(fill='black', back_color='white')

# Display the QR code
plt.figure(figsize=(6, 6))
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.show()

