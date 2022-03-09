import DatabaseManager

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