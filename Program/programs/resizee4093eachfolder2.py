import os
from PIL import Image

# フォルダの指定（カレントディレクトリの並列のフォルダ直下のimgsフォルダ）
folder_path = os.path.join(os.getcwd(), "..", "imgs")

# フォルダ内のサブフォルダを取得
subfolders = [subfolder for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder))]

for subfolder in subfolders:
    # リサイズ後の画像保存先フォルダの指定（imgsフォルダ直下にresized_フォルダを作成）
    output_folder_path = os.path.join(folder_path, "resized_" + subfolder)
    
    # リサイズ後の画像保存先フォルダが存在しない場合は作成する
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    # サブフォルダ内の画像ファイルを取得
    subfolder_path = os.path.join(folder_path, subfolder)
    files = [file for file in os.listdir(subfolder_path) if os.path.isfile(os.path.join(subfolder_path, file))]
    
    for file in files:
        # 画像ファイルのパス
        file_path = os.path.join(subfolder_path, file)

        # 画像の読み込み
        try:
            image = Image.open(file_path)
        except:
            print(f"Error opening image: {file_path}")
            continue

        # 画像のリサイズ
        aspect_ratio = image.width / image.height
        new_height = 4093
        new_width = int(new_height * aspect_ratio)
        resized_image = image.resize((new_width, new_height), Image.ANTIALIAS)

        # リサイズ後の画像を保存
        output_file_path = os.path.join(output_folder_path, file)
        resized_image.save(output_file_path)

print("リサイズが完了しました。")
