import requests

# ローカルAPIエンドポイントを指定
api_endpoint = "http://localhost:5000/api/resource"  # ここではポート番号5000を仮定しています

# リクエストのヘッダーに必要な情報を含める
headers = {
    'Authorization': 'Bearer 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',
    'Content-Type': 'application/json'
}

# リクエストのペイロード（必要に応じて）
payload = {
    'parameter1': 'value1',
    'parameter2': 'value2'
}

# ローカルAPIエンドポイントに対してリクエストを送信
response = requests.post(api_endpoint, headers=headers, json=payload)

# 応答を処理
print(response.json())
