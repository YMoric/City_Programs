
import os
from dotenv import load_dotenv
import openai

# .env ファイルから環境変数を読み込む
load_dotenv()

# APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

# APIを呼び出す例

import os
from dotenv import load_dotenv
import openai

# .env ファイルから環境変数を読み込む
load_dotenv()

# APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

# APIを呼び出す例
response = openai.Completion.create(
    engine='davinci',
    prompt='Once upon a time',
    max_tokens=50
)

# 出力の表示
print(response.choices[0].text)

response = openai.Completion.create(
    engine='davinci',
    prompt='Once upon a time',
    max_tokens=50
)

# 出力の表示
print(response.choices[0].text)
