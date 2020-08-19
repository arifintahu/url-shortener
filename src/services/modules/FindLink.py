import sqlite3

class FindLink():
	def __init__(self, shorten):
		self.shorten = shorten

	def getLink(self):
		try:
			with sqlite3.connect("database.db") as conn:
				conn.row_factory = sqlite3.Row
				cur = conn.cursor()
				cur.execute("SELECT * FROM links WHERE shorten = ?", (self.shorten,))
				rows = cur.fetchall()
				msg = "Select successfully"
				result = [dict(row) for row in rows]
		except:
			result = []
			msg = "Error in select operation"
		finally:
			return ({ 
				"data" : result,
				"msg" : msg 
			})
			conn.close()