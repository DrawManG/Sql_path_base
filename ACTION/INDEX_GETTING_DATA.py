import glob
import os


class index_getting_data():

    def test(folder_path ):
        file_list = []
        for file in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file)
            if os.path.isfile(file_path):
                file_list.append((file, file_path))
    def Initial_func(path):
        full_path,filenames = index_getting_data.walker(path)
        list = index_getting_data.create_sql_list(full_path,filenames)
        return list

    def func(*args):

        return args

    def create_sql_list(full_path,filenames):
        table = []
        for i in  range(len(full_path)):
            args = index_getting_data.func(filenames[i],full_path[i])
            table.append(args)
        return table
    def walker(path_dir):
        full_path = []
        filenames = []
        import os

        for root, dirs, files in os.walk(path_dir):
            for filename in files:
                try:
                    full_path.append(root+dirs[0]+"\\"+files[0])
                    filenames.append(filename)
                except:
                    pass
        return full_path,filenames


path = "C:/Users/DHOUSE/Desktop/New folder/"



#index_getting_data.Initial_func(path)
index_getting_data.test(path)