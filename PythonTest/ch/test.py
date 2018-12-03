'''
Created on Nov 27, 2018

@author: sergylvov
'''

import requests
import json






URL = "http://chscraper.contentanalyticsinc.com/get_data?url=https://jet.com/product/78c13bd0a7e242ad85008f15c89a8948"






        
def test_CH(prodURL,):
    

        
    res = requests.get(URL)
    
    jData = json.loads(res.text)

    
    for k, v in jData.items():
        print(str(k) + " : " + str(v))

    print(jData["url"])    
    
    
    

    
    #print(jData)
    
    #print(req.text)
    #f.close()


if __name__ == "__main__":
    
    test_CH(URL)
          
      
      

