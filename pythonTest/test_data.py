import json
import pandas as pd

# data = json.load(open("../SampleData/sa_job-input-sa"))
data = json.load(open("../SampleData/LivePaaseiotStreaming_CrowdDetection"))

headers = ["clientid", "EventProcessedUtcTime", "contouren","afwijking","voorgrond","beweging","helderheid","richting","leftoutcounter","rightoutcounter", "objecten","leftcounter","rightcounter","upcounter","downcounter","undeterminedcounter"]
headers2 = ["clientid:", "EventProcessedUtcTime", "contouren:","afwijking:","voorgrond:","beweging:","helderheid:","richting:","leftoutcounter: ","rightoutcounter: ", "objecten:","leftcounter:","rightcounter:","upcounter:","downcounter:","undeterminedcounter:"]

# print(data)
# df = pd.DataFrame(columns = headers)

# print(df.head())
test_data2 = []

for d in range(0, len(data)):
    test_data = str(data[d]["payload"]["data"])
    for i in headers2:
        test_data = test_data.replace(i, "")
        # .replace(" ", "")

# print(test_data)

# clientid, 
    contouren,afwijking,voorgrond,beweging,helderheid,richting,leftoutcounter,rightoutcounter, objecten,leftcounter,rightcounter,upcounter,downcounter,undeterminedcounter = test_data.split(",")
    test_data2.append([data[d]["clientid"], data[d]["EventProcessedUtcTime"], contouren,afwijking,voorgrond,beweging,helderheid,richting,leftoutcounter,rightoutcounter, objecten,leftcounter,rightcounter,upcounter,downcounter,undeterminedcounter])
# print(test_data2)

df = pd.DataFrame.from_records(test_data2, columns=headers)

# print(df.head)
df.to_csv("LivePaaseiotStreaming_CrowdDetection.csv", encoding='utf-8', index=False) 
# print(contouren)
# print(data[0]["clientid"])
# print(data[0]["payload"]["data"])
#print(data)