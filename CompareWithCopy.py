"""
this class handle all operations of comparing two list of files, and copying the difference to specific location
if the user want
"""
import os
import shutil

class CompareWithCopy:
    __firstDict = {}
    __secondDict = {}

    def __init__(self, first, second):
        self.__firstDict = first
        self.__secondDict = second

    def IsFound(self, element):
        if element in self.__secondDict:
            return True
        else:
            return False

    def compareLists(self):
        """Compare Two lists, the second with the first
         the files of the first list is will append to the new list
         if they are all not in the second list """

        dic = {}
        # if the dict is empty, so all elements in first dict will be the difference
        if (not self.__secondDict):
            dic = self.__firstDict
        else:
            for element in self.__firstDict:
                if self.IsFound(element):
                    pass
                else:
                    dic[element] = self.__firstDict[element]
        return dic

    def __copyOneFile(self, source, destination, counter, len_lis):
        """get source --> is the file name in with the folder name get from difference list
           and get destination path that will copy to it
           counter to print number of the copy file from the difference list length
        """
        try:
            shutil.copy(source, destination)
            print(f"File copied successfully, {counter} from {len_lis}")

        # If source and destination are same
        except shutil.SameFileError:
            print("Source and destination represents the same file.")

        # If there is any permission issue
        except PermissionError:
            print("Permission denied.")

        # For other errors
        except:
            print("Error occurred while copying file.")

    def __makeCopy(self, dictDiff, path_destination, counter=0):
        """this function that handle the copy operation"""
        lengthDict = len(dictDiff)
        for i in dictDiff:
            counter += 1
            self.__copyOneFile(source = i, destination= path_destination, counter = counter, len_lis= lengthDict)

    def askForCopyOrCompareOnly(self):
        """this function to ask the user if he wants to copy the difference list
         into a specific location or want to print it only"""
        differenceList = self.compareLists()
        if differenceList:
            response = input("if you want to copy this files press 1, if you want to show differance files only press 2 : ")
            if response == "1":
                while True:
                    path1 = input("Please Enter Destination Path to Save the Difference Files in it : ")
                    if os.path.isdir(path1):
                        self.__makeCopy(differenceList, path1)
                        break
                    else:
                        print("please enter valid destination path")
            elif response == "2":
                counter = 0
                for i in differenceList:
                    counter += 1
                    print(str(counter + 1) + " - " + differenceList[i] + "\\" + i)
            else:
                print("Please Enter Valid Input")
                self.askForCopyOrCompareOnly()
        else:
            print("No Difference between the two list of folders")

