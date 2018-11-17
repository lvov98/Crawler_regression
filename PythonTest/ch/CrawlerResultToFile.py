'''
Created on Oct 23, 2018

This Test CH Executing Crawler for Provided Product URL and recording result into text file 

@author: sergylvov
'''

import requests

URL = "http://chscraper.contentanalyticsinc.com/get_data?url="

lsURL = ("https://www.homedepot.com/p/South-Shore-Mobby-Pure-White-Twin-Size-Trundle-Bed-3880082/205397189")
''', 
         "https://www.homedepot.com/p/LG-Electronics-7-3-cu-ft-Smart-Double-Oven-Electric-Range-Self-Cleaning-Convection-and-Wi-Fi-enabled-in-Stainless-Steel-LTE4815ST/304993885",
         "https://www.homedepot.com/p/Ariens-IKON-X-52-in-23-HP-Kawasaki-Gas-Hydrostatic-Zero-Turn-Riding-Mower-915223/300243716",
         "https://www.homedepot.com/p/HDX-55-Gal-Tough-Storage-Tote-in-Black-HDX55GONLINE-4/205597365")
'''
class test_HomeDepot_ch():
        
    def testName(self):
        item_num = 1
        flName = "hdItem_"
        
        for hd_item in lsURL:
            req = requests.get(URL + hd_item)
            fln = flName + str(item_num)            
            f = open(fln, 'w')
            f.write(req.text)
            f.close()
            item_num += 1       




if __name__ == "__main__":
    test_HomeDepot_ch.testName()
    
    