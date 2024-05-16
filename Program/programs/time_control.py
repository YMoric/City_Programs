import requests
import time

def search_with_user_agent(url):
    # リクエスト間隔を設定
    time.sleep(5)

    # ユーザーエージェントを指定
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    # リクエストを送信
    response = requests.get(url, headers=headers)

    # レスポンスを返すなどの処理を行う
    return response.text

# web_searchコードからURLを取得するなどの処理があると仮定
url = "https://www.google.com/search?q=example"

# 検索を実行
result = search_with_user_agent(url)

# 結果を表示するなどの処理を行う
print(result)
