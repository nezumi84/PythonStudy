import requests as rq
url = "https://www.example.com"
res = rq.post(url,data={"key1":"value1","key2":"value2"})
print(res.url)