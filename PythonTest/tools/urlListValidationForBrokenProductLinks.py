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
    f.close()
    return urlList


def runRequestToEachURL(urlList):
    
    resultDic = {}
    
    recordNumber = 0
    
    for productURL in urlList:
        recordNumber += 1
        
        try:
            '''Full request'''
            res = requests.get(productURL,timeout=10)
            
            '''Request Head only'''
            #res = requests.head(productURL,timeout=10)   
        
            if res.status_code not in resultDic:
                resultDic[res.status_code] = 1
            else:
                resultDic[res.status_code] += 1
            print(str(res.status_code) + " - " + str(recordNumber))
        except requests.exceptions.Timeout:
            print("Time out for URL: {} ".format(productURL))
        except requests.exceptions.ConnectionError:
            print("Connection error during request for URL: {} ".format(productURL))
        except requests.exceptions.RequestException as e:
            print("Exception {} generated during request for URL {}".format(e, productURL))
            
        
    return resultDic

if __name__ == "__main__":
    
    fileName = "test_file.txt"
     
    resultForUrlList = createListOfURLfromFile(fileName)
    errorsResult = runRequestToEachURL(resultForUrlList)
    
    for k, v in errorsResult.items():
        print('Response Code "{}" reported on {} product URL'.format(k,v))
    
    exceptionNumber = len(resultForUrlList) - len(errorsResult)
    
    print("Exceptions for {} URLs was generated".format(exceptionNumber))