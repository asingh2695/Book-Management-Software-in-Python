import sqlite3


class Database:
	def __init__(self):    #self has been passed to avoid any error
	#def _init_(self,db):
		#conn=sqlite3.connect(db)
		self.conn = sqlite3.connect("books.db")
		self.curr = self.conn.cursor()
		self.curr.execute(
			"CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY , title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
		self.conn.commit()

	def insert(self,title, author, year, isbn):
		self.curr.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", (title, author, year, isbn))
		self.conn.commit()

	def view(self):
		self.curr.execute("SELECT * FROM book")
		rows = self.curr.fetchall()
		return rows

	def search(self,title="", author="", year="", isbn=""):
		self.curr.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
		rows = self.curr.fetchall()
		return rows

	def delete(self,id):
		self.curr.execute("DELETE FROM book WHERE id=?", (id,))
		self.conn.commit()

	def update(self,id, title, author, year, isbn):
		self.curr.execute("UPDATE book SET title=?, author=?,year=?,isbn=? WHERE id=?", (title, author, year, isbn, id))
		self.conn.commit()

	def __del__(self):
		self.conn.close()