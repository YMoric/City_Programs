import os
from PIL import Image

# フォルダの指定（カレントディレクトリの親フォルダ直下のimgsフォルダ）
folder_path = os.path.join(os.getcwd(), "..", "imgs")

# リサイズ後のフォルダの指定（カレントディレクトリの親フォルダ直下のresized_imgsフォルダ）
resized_folder_path = os.path.join(os.getcwd(), "..", "resized_imgs")

# フォルダ内のファイルを取得
files = os.listdir(folder_path)

# リサイズ後のフォルダが存在しない場合は作成する
os.makedirs(resized_folder_path, exist_ok=True)

for file in files:
    # ファイルのパス
    file_path = os.path.join(folder_path, file)
    
    # 画像の読み込み
    image = Image.open(file_path)
    
    # 画像のサイズを取得
    width, height = image.size
    
    # 画像が指定の幅より大きい場合に処理を行う
    if width > 720:
        # 縮小後のサイズを計算
        new_width = 720
        new_height = int(height * (new_width / width))
        
        # 画像のリサイズ
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)
        
        # リサイズ後のファイルのパス
        resized_file_path = os.path.join(resized_folder_path, file)
        
        # リサイズ後の画像を保存
        resized_image.save(resized_file_path)
