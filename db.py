import sqlite3 as sql3

class DBMS:
	def __init__(self, db_name='cai_database'):
		""" no need to add the .db extenstion in the db_name """
		self.DB_NAME = db_name + '.db'

	def connect(self, db_name):
		self.connection = sql3.connect(database=db_name)
		self.cursor = self.connection.cursor()
		self.cursor.execute('PRAGMA foreign_keys = ON;')

	def is_connected(self):
		return bool(self.connection)

	def is_table(self, name):
		if self.is_connected():
			row = self.cursor.execute("select 1 from sqlie_master where type = 'table' and name = ?;", (name,))
			return self.cursor.fetchone() is  None

	def close(self):
		self.connection.close()

	def create_profile_table(self):
		if self.is_connected():
			self.cursor.execute("create table if not exists profile (tup_id text primary key, email text not null, fname text not null, lname text not null, pasword text not null);")

	def create_leaderboard_table(self):
		if self.is_connected():
			self.cursor.execute("create table if not exists leaderboard (record_id integer primary key, tup_id text, score integer, date date, seconds_elapsed integer);")

	def save_profile(self, details):
		if not self.is_connected():
			return

		if not self.is_table('profile'):
			self.create_profile_table()

		self.cursor.execute("insert into profile (tup_id text primary key, email text not null, fname text not null, lname text not null, password text not null) values (?, ?, ?, ?, ?);", details)

		self.connection.commit()

	def save_record(self, record_details):
		if not self.is_connected():
			return

		if not self.is_table('leaderboard'):
			self.create_leaderboard_table()

		self.cursor.execute("insert into leaderboard (record_id integer primary key, tup_id text not null, score integer not null, date date not null, seconds_elapsed integer not null) values (?, ?, ?, ?, ?);", record_details)

		self.connection.commit()
