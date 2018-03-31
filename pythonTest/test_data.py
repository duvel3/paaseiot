import json
import pandas as pd

# data = json.load(open("../SampleData/sa_job-input-sa"))
data = json.load(open("../SampleData/LivePaaseiotStreaming_CrowdDetection2"))
# print(data)
headers = ["clientid", "EventProcessedUtcTime", "contouren","afwijking","voorgrond","beweging","helderheid","richting","leftoutcounter","rightoutcounter", "objecten","leftcounter","rightcounter","upcounter","downcounter","undeterminedcounter"]
headers2 = ["clientid:", "EventProcessedUtcTime", "contouren:","afwijking:","voorgrond:","beweging:","helderheid:","richting:","leftoutcounter: ","rightoutcounter: ", "objecten:","leftcounter:","rightcounter:","upcounter:","downcounter:","undeterminedcounter:"]
headers3 = ["type", "clientid", "EventProcessedUtcTime", "anon_mac", "probe_count", "avg_rssi"]
# print(data)
# df = pd.DataFrame(columns = headers)

# print(df.head())
test_data2 = []
test_data3 = []

for d in range(0, len(data)):
    if data[d]["type"] == "CAM":
        test_data = str(data[d]["payload"]["data"])
        for i in headers2:
            test_data = test_data.replace(i, "")
        if "hoeken" in test_data:
            print("bad data")
        else:
            try:
                contouren,afwijking,voorgrond,beweging,helderheid,richting,leftoutcounter,rightoutcounter, objecten,leftcounter,rightcounter,upcounter,downcounter,undeterminedcounter = test_data.split(",")
                test_data2.append([data[d]["clientid"], data[d]["EventProcessedUtcTime"], contouren,afwijking,voorgrond,beweging,helderheid,richting,leftoutcounter,rightoutcounter, objecten,leftcounter,rightcounter,upcounter,downcounter,undeterminedcounter])
            except:
                print(test_data)
        
# print(test_data2)
    else:
        # for i in range(0, len())
        # print(data[d]["clientid"])
        # print("andere data")
        for i in range(0, len(data[d]["payload"]["probes"])):
            test_data3.append([data[d]["type"], data[d]["clientid"], data[d]["EventProcessedUtcTime"], data[d]["payload"]["probes"][i]["anon_mac"], data[d]["payload"]["probes"][i]["probe_count"], data[d]["payload"]["probes"][i]["avg_rssi"]])
        # print(data[d]["payload"]["probes"][i]["anon_mac"])
        # if data[d]["type"] == "CAM":
        #     print(data)
print(test_data3)
        # .replace(" ", "")

# print(test_data)

# clientid, 
    # contouren,afwijking,voorgrond,beweging,helderheid,richting,leftoutcounter,rightoutcounter, objecten,leftcounter,rightcounter,upcounter,downcounter,undeterminedcounter = test_data.split(",")
    # test_data2.append([data[d]["clientid"], data[d]["EventProcessedUtcTime"], contouren,afwijking,voorgrond,beweging,helderheid,richting,leftoutcounter,rightoutcounter, objecten,leftcounter,rightcounter,upcounter,downcounter,undeterminedcounter])
# print(test_data2)

df2 = pd.DataFrame.from_records(test_data3, columns=headers3)
df = pd.DataFrame.from_records(test_data2, columns=headers)

# print(df.head)
df.to_csv("LivePaaseiotStreaming_CrowdDetection2_cam.csv", encoding='utf-8', index=False) 
df2.to_csv("LivePaaseiotStreaming_CrowdDetection2_density.csv", encoding='utf-8', index=False) 
# print(contouren)
# print(data[0]["clientid"])
# print(data[0]["payload"]["data"])
#print(data)