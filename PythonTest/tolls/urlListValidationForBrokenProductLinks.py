'''
Created on Nov 8, 2018
This Python 3 script opening file with list of URLs which was reported as failed during crawling
and checking each product URL on valid link error 404 or other not 2XX status code

@author: sergylvov
'''

import requests


def createListOfURLfromFile(urlFileName):
    
    f = open(urlFileName, 'r')
    urlList = []
    
    for line in f: 
        urlList.append(line) 
    
    return urlList


def runRequestToEachURL(urlList):
    
    resultDic = {}
    
    
    for productURL in urlList:
        res = requests.get(productURL)
        
        if res.status_code not in resultDic:
            resultDic[res.status_code] = 1
        else:
            resultDic[res.status_code] += 1
    return resultDic

if __name__ == "__main__":
    
    fileName = "test_file.txt"
     
    resultForUrlList = createListOfURLfromFile(fileName)
    errorsResult = runRequestToEachURL(resultForUrlList)
    
    for k, v in errorsResult.items():
        print('Error "{}" reported on {} product URL'.format(k,v))
     