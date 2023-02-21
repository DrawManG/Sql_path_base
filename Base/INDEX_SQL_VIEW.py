import sqlite3 as sl

class index_sql_view():
    def getting(path,name_base):
        con = sl.connect(path)
        with con:
            data = con.execute(f"SELECT * FROM {name_base}")
            for row in data:
                print(row)
path = "data.db"
name_base = "Pather"
index_sql_view.getting(path,name_base)