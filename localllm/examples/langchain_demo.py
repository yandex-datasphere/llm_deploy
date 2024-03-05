from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI, AzureChatOpenAI
import requests

iam_token = "--- iam token here ---"
folder_id = "--- folder id here ---"
node_id = "--- node id here ---"
base_url = "https://node-api.datasphere.yandexcloud.net/v1"

print("Trying to call the node to get model name...")
res = requests.get(base_url+"/models",headers={
                      "x-node-id" : node_id,
                      "x-folder-id" : folder_id,
                      "Authorization" : f"Bearer {iam_token}"
                  })
js = res.json()
print("Supported models:")
for x in js['data']:
    print(f" + {x['id']}")
    model = x['id']

print(f"Calling langchain model {model}")

chat = ChatOpenAI(api_key=iam_token,
                  model = model,
                  openai_api_base = base_url,
                  default_headers={
                      "x-node-id" : node_id,
                      "x-folder-id" : folder_id
                  })

messages = [
    SystemMessage(
        content="Ты весёлая девушка, которая любит рассказывать анекдоты."
    ),
    HumanMessage(
        content="Расскажи анекдот про программиста и лампочку."
    ),
]

res = chat.invoke(messages)

print(res)
