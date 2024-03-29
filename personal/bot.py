# Hetzner Cloud API module
from hcloud import Client
from hcloud.images.domain import Image
from hcloud.servers.domain import Server
from hcloud.server_types.domain import ServerType
from hcloud.volumes.domain import Volume
# Schedule module
import schedule
# JSON module
import json
# time module
import time
# math module 
import math
# Python Telegram module
import telegram

# Open Json file - use this section when clone project.

with open("my_keys.json") as f:
	keys_data = json.load(f)

# Initialize Telegram Bot
bot = telegram.Bot(token=keys_data["telegram"]["token"])
chatID = keys_data["telegram"]["chatID"]

bot.sendMessage(chat_id=chatID, text="Starting Bot...")
# Create a client - remove hashtag
# client = Client(token=keys_data["hetzner"]["token"])

client_1 = Client(token=keys_data["hetzner"]["canu1832.dymension"])
client_2 = Client(token=keys_data["hetzner"]["ic4x-1.dymension"])
client_3 = Client(token=keys_data["hetzner"]["ic4x-2.dymension"])
client_4 = Client(token=keys_data["hetzner"]["canu1832.avail"])

def GetServer(client):
	boundServer = client.servers.get_all() # Servers on List
	server = boundServer[0] # Get first server from list

	return server # return first server

def ByteToTB(byteTraffic):
	result = byteTraffic
	for i in range(0, 4):
		result = result / 1024
	
	string = "트래픽 사용량: "+str(round(result,3))+"TB"

	return string

def TotalUsage(freeTraffic, outgoingTraffic):
	result = outgoingTraffic / freeTraffic * 100
	
	string = "전체 대비 사용량 %: "+str(round(result,2))+"%"
	return string

server_1 = GetServer(client_1) # get first server
server_2 = GetServer(client_2) 
server_3 = GetServer(client_3) 
server_4 = GetServer(client_4) 

def SendAlerts():
	name_1 = server_1.name
	traffic_1 = ByteToTB(server_1.outgoing_traffic)
	usagePercent_1 = TotalUsage(server_1.included_traffic, server_1.outgoing_traffic)

	text = name_1+"\n"+traffic_1+"\n"+usagePercent_1
	print(text)
	bot.sendMessage(chat_id=chatID, text=text)

	name_2 = server_2.name
	traffic_2 = ByteToTB(server_2.outgoing_traffic)
	usagePercent_2 = TotalUsage(server_2.included_traffic, server_2.outgoing_traffic)

	text = name_2+"\n"+traffic_2+"\n"+usagePercent_2
	print(text)
	bot.sendMessage(chat_id=chatID, text=text)

	name_3 = server_3.name
	traffic_3 = ByteToTB(server_3.outgoing_traffic)
	usagePercent_3 = TotalUsage(server_3.included_traffic, server_3.outgoing_traffic)

	text = name_3+"\n"+traffic_3+"\n"+usagePercent_3
	print(text)
	bot.sendMessage(chat_id=chatID, text=text)
	
	name_4 = server_4.name
	traffic_4 = ByteToTB(server_4.outgoing_traffic)
	usagePercent_4 = TotalUsage(server_4.included_traffic, server_4.outgoing_traffic)

	text = name_4+"\n"+traffic_4+"\n"+usagePercent_4
	print(text)
	bot.sendMessage(chat_id=chatID, text=text)

schedule.every().day.at("09:00").do(SendAlerts)
schedule.every().day.at("21:00").do(SendAlerts)

schedule.every(5).seconds.do(SendAlerts)

while True:
	schedule.run_pending()
	time.sleep(1)
