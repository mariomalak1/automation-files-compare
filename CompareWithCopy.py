"""
this class handle all operations of comparing two list of files, and copying the difference to specific location
if the user want
"""
import os
import shutil

class CompareWithCopy:
    __firstList = []
    __secondList = []

    def __init__(self, first, second):
        self.__firstList = first
        self.__secondList = second

    def compareLists(self):
        """Compare Two lists, the second with the first
         the files of the first list is will append to the new list
         if they are all not in the second list """
        lis = []
        isFound = False
        if (self.__secondList == []):
            for element in self.__firstList:
                lis.append(element)
        else:
            for element1 in self.__firstList:
                ele1 = CompareWithCopy.truncateDirNameFromItemName(element1)
                for element2 in self.__secondList:
                    if(ele1 == CompareWithCopy.truncateDirNameFromItemName(element2)):
                        isFound = True
                if(not isFound):
                    lis.append(element1)
                isFound = False
        return lis

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

    def __makeCopy(self, listDiff, path_destination, counter=0):
        """this function that handle the copy operation"""
        lengthList = len(listDiff)
        for i in listDiff:
            counter += 1
            self.__copyOneFile(source = i, destination= path_destination, counter = counter, len_lis= lengthList)

    def askForCopyOrCompareOnly(self):
        """this function to ask the user if he wants to copy the difference list
         into a specific location or want to print it only"""
        differenceList = self.compareLists()
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
            for file in differenceList:
                print(file)
        else:
            print("Please Enter Valid Input")
            self.askForCopyOrCompareOnly()
    
    @staticmethod
    def truncateDirNameFromItemName(itemName):
        i = len(itemName) - 1
        newName = ""
        while i > 0 and itemName[i] != '\\':
            newName += itemName[i]
            i -= 1
        return newName[::-1]