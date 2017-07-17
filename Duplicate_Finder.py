import os
import filecmp
import sys
import shutil

class Duplicate_Finder:

    def file_list_finder(self,path_to_directory):
        file_paths = []
        for root, directories, files in os.walk(path_to_directory):
            for filename in files:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.
        return file_paths

    def file_handler(self,root_directory,destination_directory):
        file_list_one = self.file_list_finder(root_directory)
        file_list_two = self.file_list_finder(destination_directory)
        file_list_three = []
        for x in file_list_one:
            for y in file_list_two:
                name_one = x.split('\\')[len(x.split('\\'))-1]
                name_two = y.split('\\')[len(y.split('\\'))-1]
                if name_one == name_two:
                    file_list_two.remove(y)
                    file_list_three.append(y)
        print("Duplicate Files Count= "+str(len(file_list_three)))
        return file_list_two


    def path_retriever(self):
        try:
            root_directory = input("Please Enter The Root Directory Path=")
            destination_directory = input("Please Enter The Destination Directory Path=")
            print("Done 1")
        except:
            print("Position1 error=" + sys.exc_info[0])


        print("root = \n"+root_directory)
        print("target = \n"+destination_directory)

        try:
            file_list_three = self.file_handler(root_directory,destination_directory)
            print("Done 2")
        except:
            print("Position2 error="+sys.exc_info[0])

        # try:
        #     self.file_renamer(file_list_three)
        #     print("Done 3")
        # except:
        #     print("Position3 error=" + sys.exc_info[0])

DF = Duplicate_Finder()
DF.path_retriever()
