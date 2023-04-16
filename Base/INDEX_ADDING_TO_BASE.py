import sqlite3 as sl
from ACTION.INDEX_GETTING_DATA import index_getting_data
class index_adding_to_base():
    def getting(path,base_name):
        try:
            sql = f'INSERT INTO {base_name} (namefile, pathfile) values(?, ?)'
            con = sl.connect(path)
            data = index_getting_data.Initial_func(path_folder)
            with con:
                con.executemany(sql, data)
        except:
            con = sl.connect(path)
            data = index_getting_data.Initial_func(path_folder)
            with con:
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS Pather (namefile text, pathfile text);')
                cur.executemany(sql, data)
                con.commit()

path_folder = "C:/Python27/"
path = "data.db"
base_name = "Pather"
index_adding_to_base.getting(path,base_name)