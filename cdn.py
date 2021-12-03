import requests, json, time, utils, os

os.system(utils.check_linux())

print("Made by Jhin Scripter (@20cmDuro)\n~Stealer's Team\n")
print(open("welcome.txt", "r").read())
x = 0

print("Loading the config...")
try:
	config = json.load(open("config.json"))
	u1 = config["victimchannelid"]
	u2 = config["tempuserid"]
	token = config["token"]
	iconimg = config["groupicon"]
	delay = config["delay"]
	delaytime = config["delaytime"]
	removetemp = config["removetempuser"]
except:
	print("The configuration file is broken!")
	exit(1)

print(f"Starting... {u1}/{u2}")

def main():
	while True:
		res = requests.put(f"https://canary.discord.com/api/v9/channels/{u1}/recipients/{u2}", json={"name": utils.rdn_namegen(), "icon": iconimg}, headers={"content-type": "application/json", "authorization": token}).text
		y = json.loads(res)
		if "You are being rate limited." in res:
			print("[Rate limited] waiting...")
			time.sleep(int(y["retry_after"])+1)
		else:
			wid = y["id"]
			if removetemp:
				requests.delete(f"https://canary.discord.com/api/v9/channels/{wid}/recipients/{u2}", headers={"authorization": token})
			requests.patch(f"https://canary.discord.com/api/v9/channels/{wid}", json={"name": utils.rdn_namegen(), "icon": iconimg}, headers={"content-type": "application/json", "authorization": token})
			print(f"Created {wid} with success!")
		if delay:
			time.sleep(delaytime)

try:
	main()
except KeyboardInterrupt:
	print(open("goodbye.txt", "r").read())