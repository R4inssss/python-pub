from PIL import Image
im = Image.open("velociraptor-hero.webp").convert("RGB")
im.save("vcss.jpg", "jpeg")