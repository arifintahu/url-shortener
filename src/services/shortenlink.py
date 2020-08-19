from src.services.modules.ShortenLink import ShortenLink
from src.services.findlink import findlink

def shortenlink(url, shorten):
	isShorten = findlink(shorten)
	if isShorten:
		return ({ "msg" : "exist" })
	else:
		link = ShortenLink(url, shorten)
		return link.shortLink()