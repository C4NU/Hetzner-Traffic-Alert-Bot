from hcloud import Client

from hcloud.images.domain import Image
from hcloud.servers.domain import Server
from hcloud.server_types.domain import ServerType
from hcloud.volumes.domain import Volume

import telegram
import json 

#with open("keys.json") as f:
#	keys_data = json.load(f)

with open("my_keys.json") as f:
	keys_data = json.load(f)

# Create a client
client = Client(token=keys_data["hetzner"]["token"])

boundServer = client.servers.get_all()
print(boundServer)

server = boundServer[0]
print(server.name)
print("Outgoin Traffic: "+str(server.outgoing_traffic)) # 헤츠너 클라우드에서 뜨는 실제로 쓰고있는 트래픽
print("Ingoing Traffic: "+str(server.ingoing_traffic)) # 들어오는 트래픽?
print("included_traffic: "+str(server.included_traffic)) # 무료 트래픽