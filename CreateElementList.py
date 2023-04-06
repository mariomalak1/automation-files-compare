"""
this a class that handle all operations of get all items in specific folders that user enter
"""
import os
class CreateElementList:
    __DictOfAllElements = {}
    __order = ""

    def __init__(self, order):
        self.__order = order

    # this function takes directory name and list all elements in it, if the elements is has a folder also
    # then it will list all elements in this folder and push all items in this folder in the list
    # if the folder has also another folder

    def __allItemsInDirs(self, dirName, counter = 0):
        itemsInFolders = {}
        if counter >= 9:
            print("You Enter Location of Folder That Has more than 8 folders one inside other, Please Enter a Specific folder from this")
            return None
        else:
            try:
                for item in os.listdir(dirName):
                    item_path = (dirName + "\\" + item)
                    if os.path.isdir(item_path):
                        counter += 1
                        itemsInFolders += self.__allItemsInDirs(item_path, counter)
                    else:
                        itemsInFolders[item] = item_path
                return itemsInFolders

            except FileNotFoundError:
                print("Folder Not Found")
                return itemsInFolders
            except:
                print("There's an Error")
                return itemsInFolders

    def listAllElementsInDirs(self):
        print(f"Now Enter Your Locations One After One, and If You Finsh The {self.__order} Folders Press s to Stop")
        counter = 0
        while True:
            location = input(f"Enter Location No.{counter + 1} or s to Stop : ")
            counter += 1
            if location != 's':
                dic = self.__allItemsInDirs(location)
                if dic is not None:
                    self.__DictOfAllElements |= dic
                else:
                    break
            else:
                break
        return dic
