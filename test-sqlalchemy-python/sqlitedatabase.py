# from multiprocessing import connection
# import sqlite3

# connection = sqlite3.connect('new_ab.db')
# cursor = connection.cursor()

# create_table = "CREATE TABLE IF NOT EXISTS users (id int, username text, userpassword text)"
# cursor.execute(create_table)

# create_table_student = "CREATE TABLE IF NOT EXISTS faculty (id int, username text, userpassword text)"
# user = (1, 'dimpal', 'palak')
# insert_query = "INSERT INTO users (id, username, userpassword) VALUES (?, ?, ?)"
# cursor.execute(insert_query, user)

# user_list = [(2, 'amit', 'palak1'), (3, 'mannu', 'abcd')]
# cursor.executemany(insert_query, user_list)

# select_query = "SELECT * FROM users"
# for row in cursor.execute(select_query):
#     print(row)

# connection.commit()
# connection.close()



