import requests as rq
import json
url = "https://www.example.com"
res = rq.post(url,data=json.dumps({"key1":"value1","key2":"value2"}))
print(res.url)