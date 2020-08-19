import sqlite3

class ShortenLink():
	def __init__(self, url, shorten):
		self.url = url
		self.shorten = shorten

	def shortLink(self):
		return self.createLink()

	def createLink(self):
		try:
			with sqlite3.connect("database.db") as conn:
				cur = conn.cursor()
				cur.execute("INSERT INTO links (link, shorten) VALUES (?, ?)", (self.url, self.shorten))
				conn.commit()
				msg = "Record successfully added"
		except:
			conn.rollback()
			msg = "Error in insert operation"
		finally:
			return({
				"link" : self.url,
				"shorten" : self.shorten,
				"message" : msg
			})
			conn.close()