import csv
import json
from traceback import print_exc


# with open('business.json', encoding="utf8") as json_file:
#     data = json.load(json_file)
#     print(data)


# print([*json.loads(line)].values())
# break
# biz.append(json.loads(line))
    

# for line in open('business.json', 'r', encoding="utf8"):
#     print([*json.loads(line).values()])
#     print(line)
#     break
with open('business.csv', mode='w', encoding="utf8") as business_file:
    business_writer = csv.writer(business_file, delimiter='|')
    business_writer.writerow(["name", "latitude", "longitude", "categories"])
    for line in open('business.json', 'r', encoding="utf8"):
        stripped_list = []
        data_list = [*json.loads(line).values()]
        stripped_list.append(data_list[1])
        stripped_list.append(data_list[6])
        stripped_list.append(data_list[7])
        stripped_list.append(data_list[-2])
        print(stripped_list)
        business_writer.writerow(stripped_list)

        break


# index = 0
# with open('business.csv', mode='w', encoding="utf8") as business_file:
#     business_writer = csv.writer(business_file, delimiter='|')
#     business_writer.writerow(["business_id", "name", "address", "city", "state", "postal_code", "latitude", "longitude", "stars", "review_count", "is_open", "attributes", "categories", "hours"])
    
#     for line in open('business.json', 'r', encoding="utf8"):
#         try:
#             data_list = [*json.loads(line).values()]
#             # if(len(data_list) != 14):
#             #     print(data_list)
#             if data_list[13] is None:
#                 continue
#             for datum in data_list:
#                 datum = str(datum)
#                 if (len(datum) < 1):
#                     print(datum, len(datum))
#                     # datum = 'None'
            
            

#             business_writer.writerow(data_list)
#             if index > 2:
#                 break
#             index += 1
#         except Exception as ex:
#             print("Error!")
#             print(ex)
#             continue
            