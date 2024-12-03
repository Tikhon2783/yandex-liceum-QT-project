from PIL import Image

im:Image.Image = Image.open('images/cards/card_shirt.png')
new = im.resize((int(im.width * .3), int(im.height * .3)))
print(new.width, new.height)
new.save('images/cards/new.png')
# im.show()
