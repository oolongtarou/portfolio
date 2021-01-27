import os
import glob
from PIL import Image

# 関数定義
def image_resize(input_folder, extension, magnification):
    dir = input_folder
    files = glob.glob(dir + '*.' + extension)
    resized_dir = dir + 'resized/'

    os.makedirs(resized_dir, exist_ok=True)

    for f in files:
        img = Image.open(f)
        img_resize = img.resize((int(img.width * magnification), int(img.height * magnification)))
        title, ext = os.path.splitext(f)
        img_resize.save(resized_dir + os.path.basename(f))


# 関数呼び出し
# image_resize('画像フォルダ', '画像の拡張子', 倍率)
image_resize()