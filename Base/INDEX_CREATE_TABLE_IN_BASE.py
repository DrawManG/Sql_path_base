import sqlite3 as sl
class index_create_table_in_base():
    def getting(path_sql):
        try:

            con = sl.connect(path_sql)
            con.execute("""
                CREATE TABLE Pather (
                   
                   namefile STRING,
                   pathfile STRING

                );
                    """)
        except:
            print("table already exists")



path = "data.db"
index_create_table_in_base.getting(path)