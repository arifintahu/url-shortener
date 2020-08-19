from src.services.modules.FindLink import FindLink

def findlink(shorten):
	result = FindLink(shorten).getLink()
	if len(result["data"])>0 :
		return result["data"][0]["link"]
	else:
		return 0 