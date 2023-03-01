"""
    The Main Functions and the Logic of the Program is Here
"""
import CreateElementList, CompareWithCopy

class CompareProgram:
    @staticmethod
    def runProgram():
        dir1 = CreateElementList.CreateElementList("First")
        dir2 = CreateElementList.CreateElementList("Second")
        compare = CompareWithCopy.CompareWithCopy(
            dir1.listAllElementsInDirs(), dir2.listAllElementsInDirs())
        compare.askForCopyOrCompareOnly()