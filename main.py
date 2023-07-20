from PIL import Image
import os

if os.path.isdir(os.getcwd() + "/out/"):
    pass
else:
    os.mkdir(os.getcwd() + "/out/")

files = os.getcwd() + '/convert/'
out = os.getcwd() + '/out/'

for file in os.listdir(files):
    if file.endswith('.png'):
        f = Image.open(files + file).convert("RGB")
        f.save(out + file[:-4] + '.jpg')