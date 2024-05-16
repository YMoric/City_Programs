import pandas as pd
from bs4 import BeautifulSoup
import requests

# エクセルファイルのパス
excel_file = 'Kinton_Data.xlsm'

# シート番号
sheet_number = 1

# エクセルデータを読み込む
df = pd.read_excel(excel_file, sheet_name=sheet_number-1, usecols='B,E')

# Webサイトの有無と作成日を格納するためのリスト
websites = []
creation_dates = []

# 各行のデータに対して処理を実行
for index, row in df.iterrows():
    company_name = row['会社名']
    address = row['住所']
    
    # 住所を使用してWebサイトを検索
    query = f'{company_name} {address} website'
    url = f'https://www.google.com/search?q={query}'
    
    # Google検索結果のHTMLを取得
    response = requests.get(url)
    html = response.text
    
    # Beautiful Soupを使用してHTMLを解析
    soup = BeautifulSoup(html, 'html.parser')
    
    # 検索結果の最初のリンクを取得
    link = soup.find('a')
    
    # リンクが存在する場合、WebサイトのURLと作成日を取得
    if link:
        website_url = link['href']
        website_creation_date = link.find_next('span').text if link.find_next('span') else 'Unknown'
    else:
        website_url = 'N/A'
        website_creation_date = 'N/A'
    
    # 結果をリストに追加
    websites.append(website_url)
    creation_dates.append(website_creation_date)
    
    # データのない行が出現したら処理を終了
    if pd.isnull(company_name) and pd.isnull(address):
        break
    
# 結果をデータフレームに格納
df['Webサイト'] = websites
df['作成日'] = creation_dates

# 結果をエクセルファイルとして保存
output_file = 'Webサイト情報.xlsx'
df.to_excel(output_file, index=False)
print('処理が完了しました。')
