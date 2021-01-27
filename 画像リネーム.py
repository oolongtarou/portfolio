import os
import glob
from PIL import Image


# 関数定義
def image_rename(image_folder, extension):
    dir = image_folder
    files = glob.glob(dir + '*.' + extension)
    
    for i, file in enumerate(files):
        os.rename(file, image_folder + str(i + 1) + '.' + extension)



# 関数呼び出し
image_rename()