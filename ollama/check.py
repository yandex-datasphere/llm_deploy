import requests
import json

# ! Также вместе с ollama можно использовать pip install langchain-ollama

# В эти поля вам необходимо вставить свои данные
# Вмсето IAM токена, который действителен 12 часов, можно использовать статический API-ключ
# В этом случае замените заголовок запроса на "Authorization": "Api-key " + api_key
iam_token = "___"
folder_id = "___"
node_id = "___"
#alias_name = "datasphere.user.___"

base_url = "https://node-api.datasphere.yandexcloud.net"
url = base_url + '/api/generate'
model = "qwen:0.5b"

payload = {
    "model": model,
    "prompt": "Hello",
    "stream": False,
}

default_headers={
    "x-node-id" : node_id,
    #"x-node-alias" : alias_name,
    "x-folder-id" : folder_id,
    "Authorization": "Bearer " + iam_token
}

response = requests.post(
        url=url,
        data=json.dumps(payload),
        headers=default_headers,
        timeout=300,
    )

print(response.json())