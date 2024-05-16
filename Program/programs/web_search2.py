import requests
import pandas as pd

excel_file = 'Kinton_Data.xlsm'
sheet_number = 1

# Excelファイルからデータを読み込む
df = pd.read_excel(excel_file, sheet_name=sheet_number-1, usecols='B')
company_names = df['会社名'].tolist()

# 検索結果を格納するリスト
results = []

for company_name in company_names:
    # Web検索を実行
    query = f'{company_name} Webサイト'
    url = f'https://www.google.com/search?q={query}'
    response = requests.get(url)
    response.raise_for_status()

    # 検索結果から作成日を取得
    created_date = response.headers.get('date')

    # 結果を辞書として保存
    result = {'会社名': company_name, '作成日': created_date}
    results.append(result)

# 結果をデータフレームに変換して表示
results_df = pd.DataFrame(results)
print(results_df)
