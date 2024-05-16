import os
import shutil
from PIL import Image

# フォルダのパス
cmyk_folder = "../CMYK"  # CMYKフォルダのパス
rgb_folder = "../RGB"  # RGBフォルダのパス

# RGBフォルダが存在しない場合は作成する
if not os.path.exists(rgb_folder):
    os.makedirs(rgb_folder)

# CMYKフォルダ内のファイルを処理する
for filename in os.listdir(cmyk_folder):
    filepath = os.path.join(cmyk_folder, filename)
    img = Image.open(filepath)

    # CMYKモードの場合
    if img.mode == "CMYK":
        # RGB形式に変換
        rgb_image = img.convert("RGB")

        # ファイル名を変更してRGBフォルダに保存
        new_filename = os.path.splitext(filename)[0] + "_rgb" + os.path.splitext(filename)[1]
        new_filepath = os.path.join(rgb_folder, new_filename)
        rgb_image.save(new_filepath)

        # メモリを解放
        rgb_image.close()

    # RGBAパレット形式の場合
    elif img.mode == "P" and "transparency" in img.info:
        # RGBA形式に変換
        rgba_image = img.convert("RGBA")

        # ファイル名を変更してRGBフォルダに保存
        new_filename = os.path.splitext(filename)[0] + "_transparent" + os.path.splitext(filename)[1]
        new_filepath = os.path.join(rgb_folder, new_filename)
        rgba_image.save(new_filepath)

        # メモリを解放
        rgba_image.close()

    # RGBモードの場合
    elif img.mode == "RGB":
        # ファイルを複製してファイル名を変更してRGBフォルダに保存
        new_filename = os.path.splitext(filename)[0] + "_rgb" + os.path.splitext(filename)[1]
        new_filepath = os.path.join(rgb_folder, new_filename)
        shutil.copyfile(filepath, new_filepath)

    # その他のモードの場合
    else:
        # ファイルを複製してRGBフォルダに保存
        new_filepath = os.path.join(rgb_folder, filename)
        shutil.copyfile(filepath, new_filepath)

    # メモリを解放
   
