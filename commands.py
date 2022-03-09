import DatabaseManager
from datatime import datetime

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
