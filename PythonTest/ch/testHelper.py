'''
Created on Jan 10, 2019

@author: sergylvov


'''

import filecmp



def showDifferences(originFile, resultFile):
    
    lResult = ""
    
    fOrigin = open(originFile, 'r')
    fResult = open(resultFile, 'r')
    
    listOfLinesOrigin = fOrigin.readlines()
    listOfLinesResult = fResult.readlines()
    
    if len(listOfLinesOrigin) > len(listOfLinesResult):
        iLen = len(listOfLinesOrigin)
    else:
        iLen = len(listOfLinesResult)
        
    for iL in range(0,iLen - 1):
        if listOfLinesOrigin[iL] != listOfLinesResult[iL]:
            lResult = lResult + originFile + " - Original File : \n" + listOfLinesOrigin[iL] + resultFile + " - Result File : \n" + listOfLinesResult[iL] + "\n"
            
    
    fOrigin.close()
    fResult.close()
    
    return lResult    
    

def result_comparision(origFiles, testResultFileName):
    origFileIndex = 0
    iRes = 0
    sTestResult = ''
    
    returnResult = []
    
    for tstfl in testResultFileName:
        if filecmp.cmp(tstfl, origFiles[origFileIndex]):
            sTestResult = sTestResult + "Product " + str(origFileIndex + 1) + " Tested successfully. No any changes found \n"
        else:    
            sTestResult = sTestResult + "Comparison result for product " + str(origFileIndex + 1) + " not matching with previous result.\n"
            print (showDifferences(origFiles[origFileIndex], tstfl))
            
            iRes = 1
        
        origFileIndex += 1    
            
            
    returnResult.append(iRes)
    returnResult.append(sTestResult)
    
    
    return returnResult



'''
if __name__ == "__main__":
    
    print("Hello World!")
'''

