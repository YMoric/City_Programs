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
    if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".gif"):
        filepath = os.path.join(cmyk_folder, filename)
        # ファイルを開いてモードを確認する
        image = Image.open(filepath)
        mode = image.mode

        if mode == "RGB":
            # すでにRGBモードのファイルの場合は複製してファイル名に"_rgb"を追加するだけ
            new_filename = os.path.splitext(filename)[0] + "_rgb" + os.path.splitext(filename)[1]
            new_filepath = os.path.join(rgb_folder, new_filename)
            os.makedirs(os.path.dirname(new_filepath), exist_ok=True)
            shutil.copyfile(filepath, new_filepath)
        elif mode == "P" and "transparency" in image.info:
            # パレットイメージの場合、RGBA形式に変換してファイル名を変更してRGBフォルダに保存
            rgba_image = image.convert("RGBA")
            new_filename = os.path.splitext(filename)[0] + "_tranparent" + os.path.splitext(filename)[1]
            new_filepath = os.path.join(rgb_folder, new_filename)
            rgba_image.save(new_filepath)
            rgba_image.close()
        else:
            # CMYKからRGBに変換してファイル名を変更してRGBフォルダに保存
            rgb_image = image.convert("RGB")
            new_filename = os.path.splitext(filename)[0] + "_rgb" + os.path.splitext(filename)[1]
            new_filepath = os.path.join(rgb_folder, new_filename)
            rgb_image.save(new_filepath)
            rgb_image.close()

        # メモリを解放
        image.close()
