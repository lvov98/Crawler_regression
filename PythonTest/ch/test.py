'''
Created on Nov 27, 2018

@author: sergylvov
'''

import requests
import json






URL = "http://chscraper.contentanalyticsinc.com/get_data?url="

productURLs = "https://www.peapod.com/modal/item-detail/10417, https://www.peapod.com/modal/item-detail/10418, https://www.peapod.com/modal/item-detail/105426"






        
def test_CH(prodURL,):
    

        
    res = requests.get(URL + productURLs)
    
    jData = json.loads(res.text)

    
    for k, v in jData.items():
        print(str(k) + " : " + str(v))
 
    
    
    

    
    #print(jData)
    
    #print(req.text)
    #f.close()


if __name__ == "__main__":
    
    test_CH(URL)
          
      
      

