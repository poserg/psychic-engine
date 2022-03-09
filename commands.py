import DatabaseManager
from datatime import datetime
import sys

db = DatabaseManager('bookmarks.db')

class CreateBookmarksTableCommand:
	def execute(self):
		db.create_table(
			'bookmarks',
			{
				'id': 'integer primary key autoincrement',
				'titile': 'text not null',
				'url': 'text not null',
				'notes': 'text', 
				'date_added': 'text not null',
			})


class AddBookmakrCommand:
	def execute(self, data):
		data['date_added'] = datetime.utcnow().isoformat()
		db.add('bookmarks', data)
		return 'Bookmark added!'

class ListBookmakrCommand:
	def __init__(self, order_by='date_added'):
		self.order_by = order_by

	def execute(self):
		return db.select('bookmarks', order_by=self.order_by).fetchall()

class DeleteBookmarkCommand:

	def execute(self, data):
		db.delete('bookmarks', {'id': data})
		return 'Bookmark deleted!'

class QuitCommand:

	def execute(self):
		sys.exit()
