import requests

# APIキーを設定
OPENAI_API_KEY = 'YOUR_API_KEY_HERE'

# APIエンドポイント
url = 'https://api.openai.com/v1/your_endpoint_here'

# ヘッダーにAPIキーを含めてリクエストを作成
headers = {
    'Authorization': f'Bearer {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',
    'Content-Type': 'application/json'  # 必要に応じて他のヘッダーを追加
}

# リクエストのペイロード（必要に応じて）
payload = {
    'parameter1': 'value1',
    'parameter2': 'value2'
}

# POSTリクエストの例
response = requests.post(url, headers=headers, json=payload)

# 応答を処理
print(response.json())
