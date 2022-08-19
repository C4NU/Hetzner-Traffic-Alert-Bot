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

class HetznerTrafficAlertBot:
	#Initializer
	def __init__(self):
		#Open Json file
		with open("keys.json") as f:
			keys_data = json.load(f)
		#Initialize Hetzner Traffic Alert Bot Class
		self.bot = telegram.Bot(token=keys_data["telegram"]["token"])
		self.chatID = keys_data["telegram"]["chatID"]
		#Send Telegram Message "Starting Bot"
		self.bot.sendMessage(chat_id=self.chatID, text="Starting Bot...")
		#Initialize client object
		self.client = Client(token=keys_data["hetzner"]["token"])
		#Get List of BoundServer
		self.boundServer = self.client.servers.get_all()
		#Get First server from Bound Server List
		#If you have a lot of server from project, use list to get server.
		self.server = self.boundServer[0] # Get first server from list

	#Byte To TerraByte Calculator Method
	def ByteToTB(byteTraffic):
		#Get Byte Size of Traffic
		result = byteTraffic
		#Calculate Byte To TerraByte
		for i in range(0, 4):
			result = result / 1024
		#Make Text for send Message
		string = "Usage of Traffic: "+str(round(result,3))+"TB"
		#Return Text
		return string

	#Total Usage Percentage Calculator Method
	def TotalUsage(freeTraffic, outgoingTraffic):
		#Calculate Total Usage Percentage of Traffics
		result = outgoingTraffic / freeTraffic * 100
		#Make Text for send Message
		string = "Usage %: "+str(round(result,2))+"%"
		#Return Text
		return string
	
	#Send Alerts to telegram
	def SendAlerts(self):
		#Get name of server
		name = self.server.name
		#Calculate Current outgoing traffic of your server
		traffic = self.ByteToTB(self.server.outgoing_traffic)
		#Calculate usage percentage of your server
		usagePercent = self.TotalUsage(self.server.included_traffic, self.server.outgoing_traffic)
		#Make Text message for telegram
		text = name+"\n"+traffic+"\n"+usagePercent
		#log
		print(text)
		#Send Message
		self.bot.sendMessage(chat_id=self.chatID, text=text)

def main():
	#Initialize HetznerTrafficAlertBot class
	hetznerTraffic = HetznerTrafficAlertBot()

	#Set Schedule, you can adjust. Google python schedule
	schedule.every().day.at("09:00").do(hetznerTraffic.SendAlerts)
	schedule.every().day.at("21:00").do(hetznerTraffic.SendAlerts)
	
	#Runnig Bot
	while True:
		schedule.run_pending()
		time.sleep(1)

if __name__ == '__main__':
    main()