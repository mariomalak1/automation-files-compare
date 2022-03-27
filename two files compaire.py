import os
import shutil
####
### functions here
def List_Elements(dir1, counter = 0):
    lis1 = []
    folders = os.listdir(dir1)
    for folder in folders:
        if (os.path.isdir(dir1+"\\"+folder)):
            for element in (os.listdir(dir1 +"\\" +folder)):
                lis1.append(element)
        else:
            lis1.append(folder)
    return lis1
### the files in folder 1 if itsn't in folder 2 it will be added to it
### so this files is in folder 1 
def Compare_Lists(list1 , list2, counter = 0):
    lis = []
    if (list2 == []):
        for element in list1:
            lis.append(element)
    else:
        for element in list1:
            for element2 in list2:
                if element == element2:
                    counter = 0
                    break
                else:
                    counter += 1
                if counter == (len(list2)):
                    counter = 0
                    lis.append(element)
    return lis

def copy(source, destination, counter, len_lis):
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

### function to get file source and copy it
def Get_File_source_Copy(i,dir1 , path_destenation , counter , len_lis ):
    folders = os.listdir(dir1)
    for j in folders:
        if (os.path.isdir(dir1+"\\"+j)):
            for element in (os.listdir(dir1 +"\\" +j)):
                if(i == element):
                    copy((dir1 +"\\" + j + "\\" +element),path_destenation , counter, len_lis)
        else:
            if(i == j):
                copy((dir1 +"\\" +j),path_destenation, counter, len_lis)

def copy_operation(lis_dif , path_destenation , dir1 , counter = 0):
    for i in lis_dif:
        counter += 1
        Get_File_source_Copy(i,dir1 , path_destenation , counter , len(lis_dif))
def Copy_Dif():
    folder1 = input("please enter first path of your folder or your files : ")
    folder2 = input("please enter second path of your folder or your files : ")
    path1 = input("please enter path to save the diffrence files in it : ")
    lis1 = List_Elements(folder1)
    lis2 = List_Elements(folder2)
    lis3 = Compare_Lists(lis1 , lis2)
    copy_operation(lis3, path1 , folder1)
Copy_Dif()
