# 推送
# alias   要推送的用户ID
import requests
url = "https://api.jpush.cn/v3/push"
payload = "{\n\t\"platform\": \"all\"," \
          "\n\t\"audience\" : {\n        \"alias\" :  [ \"2366779543\" ]\n    }," \
          "\n    \"notification\" : {\n        \"ios\" : {\n        \t\"alert\" : {\n        \t\t\"title\" : \"ios\"," \
          "\n        \t\t\"body\" : \"goto idsriko:///login\"\n        \t}," \
          "\n        \t\"badge\" : \"+1\",\n        \t\"extras\" : {\n        \t\t\"goto\" : \"idsriko:///login\"\n        \t}\n        }," \
          "\n        \"android\" : {\n        \t\"alert\" : \"goto idsriko:///login\",\n        \t\"title\" : \"android\"," \
          "\n        \t\"extras\" : {\n        \t\t\"goto\" : \"idsriko:///login\"\n        \t}\n        }\n    }," \
          "\n\t\"options\": {\n        \"apns_production\": false\n    }\n}"
headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic YjA1YzRiZWI1MGUzY2Y3YmY2MThiNDUxOmU1MmZhYTMwYmRlYjc3YmI4YjRjMjllMQ==",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "33abfd22-d992-4dd8-bf71-b298992f2b7f,66ebbc4d-9c06-49d4-94a4-3672eb147287",
    'Host': "api.jpush.cn",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "589",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)