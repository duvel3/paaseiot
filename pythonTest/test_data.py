import json
import pandas as pd

data = json.load(open("../SampleData/LivePaaseiotStreaming_CrowdDetection"))

headers = ["clientid", "payload"]

df = pd.DataFrame(columns = headers)

print(df.head())

for i in data:
    

# print(data[0]["clientid"])
# print(data[0]["payload"])
#print(data)