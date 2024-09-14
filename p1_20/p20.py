# pip  #  to download packages

# qrcode generator 

import qrcode
name = input("Enter your name: ")
# img = qrcode.make(f"Hello {name}")
img = qrcode.make(name)
type(img)  # qrcode.image.pil.PilImage
img.save(f"{name}.png")