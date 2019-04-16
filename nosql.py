import time
import datetime
import random
import keyword
from pymongo import MongoClient
'''
server
'''

client = MongoClient('mongodb://device_user:x123#@s-bp1ed39f826efe34-pub.mongodb.rds.aliyuncs.com:3717/devicebusiness')
db = client.devicebusiness
collection = db.t_device_server
print(collection)
# for i in collection.find():
# 	print(i)
#
#item = collection.find_one({"trade_seq":"00000000000000000000000000000000"})
##3201020000003919
item = collection.find_one({"gun_no":"3201020000003919"})
print(item)



starttime = datetime.datetime.now()
# for num in range(0,10000): 
# 	collection.find_one({"gun_no":"3201020000003919"})
endtime = datetime.datetime.now()
xtime = (endtime - starttime).seconds
print(xtime)

# itemx = {"pile_a":1,"pile_v":2,"charge_status":2}
itemx = {}
itemx["pile_v"]=6
itemx["connecting_status"]=0
itemx["gun_no"]=123
itemx["charged_power"]=0.3
itemx["charged_time"]=3
itemx["soc"]=13
#itme[battery_temperature]=
itemx["left_time"]=19
itemx["trade_seq"]=789
itemx["charged_mountori"]=2.00
itemx["loss_charged_power"]=0.4
itemx["trade_seq"]="32010200000039171903041138440824"
# itmex["time"]=time.time()

# print(itemx["time"])
# print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
xtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# itemx["time"]=xtime
#utcTime = datetime.datetime.now()-datetime.timedelta(hours=8)
utcTime = datetime.datetime.now()   #后修改 语义问题
itemx["time"]=utcTime
# print("utcTime:"+utcTime)
# print(itemx["pile_v"])
# print(itemx["time"])
# print(itemx)
#result = collection.insert_one(itemx)
#print(result)

#--------------insert,begin-------------
#批量处理
# more = []
# for num in range(0,1): 
# 	item_num ={}
# 	item_num["pile_v"]=random.randint(6,60)
# 	item_num["trade_seq"]="32010200000039171903041138440824"
# 	item_num["battery_temperature"]=""
# 	item_num["time"]=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 	# print(item_num)
# 	more.append(item_num)
# print('----------')
# print(len(more))
# collection.insert_many(more)
# ------------insert,end------------------

#----------------del.begin-------------------
#、、32010200000039191903091600270461
# xx=collection.find({"trade_seq":"32010200000039191903091600270461"})
# for doc in xx:
# 	# print(doc)
# 	if(doc. __contains__("battery_temperature")):
# 		print("包含")
# 		if(doc["battery_temperature"] == None):
# 			print(doc["_id"])
# 			print("拿出来是 null")
# 		if(doc["battery_temperature"] == ""):
# 			print(doc["_id"])
# 			print("拿出来是 空字符")
# 	if(doc. __contains__("time")):
# 		print(doc["time"])		
# 	else:
# 		print("不包含")
# 		print("doing")
# 		print(doc["_id"])
# 		del_flag = collection.delete_one({"_id":doc["_id"]})
# 		print(del_flag)
# 	if(doc. __contains__("pile_a")):
		
#---------------del.end-----------------

#-----------------find begin
xx=collection.find({"trade_seq":"32010200000039191903091600270461"})
for doc in xx:
	 print(doc)
#-----------------find end


