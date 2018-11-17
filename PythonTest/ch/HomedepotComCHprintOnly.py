
import requests

import json

URL = "http://chscraper.contentanalyticsinc.com/get_data?url="

lsURL = ("https://www.homedepot.com/p/South-Shore-Mobby-Pure-White-Twin-Size-Trundle-Bed-3880082/205397189")
''', 
         "https://www.homedepot.com/p/LG-Electronics-7-3-cu-ft-Smart-Double-Oven-Electric-Range-Self-Cleaning-Convection-and-Wi-Fi-enabled-in-Stainless-Steel-LTE4815ST/304993885",
         "https://www.homedepot.com/p/Ariens-IKON-X-52-in-23-HP-Kawasaki-Gas-Hydrostatic-Zero-Turn-Riding-Mower-915223/300243716",
         "https://www.homedepot.com/p/HDX-55-Gal-Tough-Storage-Tote-in-Black-HDX55GONLINE-4/205597365")

'''

fl_name = "_"
        
def test_HD_CH():
    

        
    res = requests.get(URL + lsURL)
    
    jData = json.loads(res.text)

    f = open(fl_name, 'w')
    
    
    ''' Step #3 - Checking URL '''
    
    print("Step #3 - Check URL : ") 
    print("    URL : " + jData["url"])
    f.write(jData["url"]+"\n")
    print("    Canonical Link : " + jData["page_attributes"]["canonical_link"])
    f.write(jData["page_attributes"]["canonical_link"]+"\n")
    
    ''' Step #4 - Checking Image's links '''
    print("Step #4 - Check images URL : ")
    print ("    Images counted :" + str(jData["page_attributes"]["image_count"]))
    f.write(str(jData["page_attributes"]["image_count"])+"\n")
    for i in range(0, len(jData["page_attributes"]["image_urls"])):
        print("    Image " + str(i+1) + " URL : " + jData["page_attributes"]["image_urls"][i])
        f.write(jData["page_attributes"]["image_urls"][i]+"\n")
    
    ''' Step #5 - Check Video Links '''
    print("Step #5 - Check video URL : ")
    print ("    Video counted :" + str(jData["page_attributes"]["video_count"]))
    f.write(str(jData["page_attributes"]["video_count"])+"\n")
    if jData["page_attributes"]["video_count"] > 0 :
        for i in range(0, len(jData["page_attributes"]["video_urls"])):
            print("    Video " + str(i+1) + " URL : " + jData["page_attributes"]["video_urls"][i])
            f.write(jData["page_attributes"]["video_urls"][i]+"\n")
    else:
        print("    Video URL : null")
        f.write("null\n")
    
    ''' Step #6 - Checking Title '''    
    print("Step # 6 :")
    print("    Check Product Name : " + jData["product_info"]["product_name"])
    f.write(jData["product_info"]["product_name"]+"\n")
    print("    Check Product Title : " + jData["product_info"]["product_title"])
    f.write(jData["product_info"]["product_title"]+"\n")
    
    ''' Step #7 - Checking Product ID '''
    print("Step #7 - Check Product ID : " + jData["product_id"])
    f.write(jData["product_id"]+"\n")
    
    ''' Step #8 - Checking UPC '''
    print("Step #8 - Check UPC : " + jData["product_info"]["upc"])
    f.write(jData["product_info"]["upc"]+"\n")
    
    ''' Step #9 - Checking price and Currency'''
    print("Step #9 - Check Price and Currency:")
    print("    Price: " + jData["sellers"]["price"])
    f.write(jData["sellers"]["price"]+"\n")
    print("    Price amount: " + str(jData["sellers"]["price_amount"]))
    f.write(str(jData["sellers"]["price_amount"])+"\n")
    print("    Currency: " + jData["sellers"]["price_currency"])
    f.write(jData["sellers"]["price_currency"]+"\n")
    
    ''' Step #10 - Checking Category '''
    print("Step #10 - Check Categories : ")
    print("List of Categories ")
    for i in range(0, len(jData["classification"]["categories"])):
        print( "    "+ jData["classification"]["categories"][i])
        f.write(jData["classification"]["categories"][i]+"\n")
    print("    Check Category Name: " + jData["classification"]["category_name"])
    f.write(jData["classification"]["category_name"]+"\n")
    
    ''' Step #11 - Checking Brand '''
    print("Step # 11 - Check Brand : " + jData["classification"]["brand"])
    f.write(jData["classification"]["brand"]+"\n")
    
    ''' Step #12 - Checking Model '''
    print("Step #12 - Check Model : " + str(jData["product_info"]["model"]))
    f.write(str(jData["product_info"]["model"])+"\n")
    
    '''Step #13 - Checking Stock Status'''
    print("Step #13 -  Check Stock Status : ")
    print("    in_stock : " + str(jData["sellers"]["in_stock"]))
    f.write(str(jData["sellers"]["in_stock"])+"\n")
    print("    in_stock : " + str(jData["sellers"]["site_online"]))
    f.write(str(jData["sellers"]["site_online"])+"\n")
    print("    in_stock : " + str(jData["sellers"]["site_online_in_stock"]))
    f.write(str(jData["sellers"]["site_online_in_stock"])+"\n")
    
    ''' Step #14 - Checking Description'''
    print("Step #14 - Check Description : " + jData["product_info"]["description"])
    f.write(jData["product_info"]["description"]+"\n")
    
    '''Step #15 - Checking Shelf Description'''
    print("Step #15 - Check Shelf Description : " + jData["product_info"]["shelf_description"])
    f.write(jData["product_info"]["shelf_description"]+"\n")
    
    ''' Step # 16 - Checking Long Description'''
    print("Step #16 - Check Long Description : " + jData["product_info"]["long_description"])
    f.write(jData["product_info"]["long_description"]+"\n")
    
    '''Step # 17 - Checking Specification'''
    print("Step #17 - Check Specification : ")
    for k, v in jData["product_info"]["specs"].items():
        print("    " + k + " : " + v)
        f.write(k + " : " + v + "\n")
    
    '''Step #18 - Checking KeyWords'''
    print("Step #18 - Check Keywords :" + jData["page_attributes"]["keywords"])
    f.write(jData["page_attributes"]["keywords"]+"\n")
    
    '''Step #19 - Checking Variants'''
    print("Step #19 - Check Variants :" + str(jData["page_attributes"]["variants"]))
    f.write(str(jData["page_attributes"]["variants"])+"\n")
    
    '''Step #20 - Checking Reviews'''
    print("Step #20 - Check Reviews :" )
    for k, v in jData["reviews"].items():
        print("    " + k + " : " + str(v))
        f.write(k + " : " + str(v) + "\n")
        
    
'''
    f = open("fln", 'w')
    f.write(res.text)
    f.close()
'''
    
    #print(jData)
    
    #print(req.text)
    #f.close()
    
if __name__ == "__main__":
    test_HD_CH()   
      

