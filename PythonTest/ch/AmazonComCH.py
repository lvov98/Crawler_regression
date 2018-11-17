
import requests
import filecmp
import json

from datetime import datetime
from tkinter import messagebox





URL = "http://chscraper.contentanalyticsinc.com/get_data?url="

test_products_URLs = ("https://www.amazon.com/gp/product/B00MDU11EY",
                    "https://www.amazon.com/gp/product/B000GAWSDG",
                    "https://www.amazon.com/American-Crew-POMADE-HOLD-SHINE/dp/B000X2DMEG",
                    "https://www.amazon.com/dp/B0758XXCSC")




        
def test_HD_CH(prodURL, fl_name):
    

        
    res = requests.get(URL + prodURL)
    
    jData = json.loads(res.text)

    f = open(fl_name, 'w')
    
    
    ''' Step #3 - Checking URL '''
    
    print("Step #3 - Check URL : ") 
    print("    URL : " + jData["url"])
    f.write("Step #3 - Checking URL : \n")
    f.write(jData["url"]+"\n")
    print("    Canonical Link : " + jData["page_attributes"]["canonical_link"])
    f.write(jData["page_attributes"]["canonical_link"]+"\n")
    
    ''' Step #4 - Checking Image's links '''
    print("Step #4 - Check images URL : ")
    print ("    Images counted :" + str(jData["page_attributes"]["image_count"]))
    f.write("Step #4 - Checking Image's links : \n")
    f.write(str(jData["page_attributes"]["image_count"])+"\n")
    for i in range(0, len(jData["page_attributes"]["image_urls"])):
        print("    Image " + str(i+1) + " URL : " + jData["page_attributes"]["image_urls"][i])
        f.write(jData["page_attributes"]["image_urls"][i]+"\n")
    
    ''' Step #5 - Check Video Links '''
    print("Step #5 - Check video URL : ")
    print ("    Video counted :" + str(jData["page_attributes"]["video_count"]))
    f.write("Step #5 - Checking Video's links : \n")
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
    f.write("Step #6 - Checking Titles : \n")
    f.write(jData["product_info"]["product_name"]+"\n")
    print("    Check Product Title : " + jData["product_info"]["product_title"])
    f.write(jData["product_info"]["product_title"]+"\n")
    
    ''' Step #7 - Checking ASIN and Product ID '''
    print("Step #7 - Check Product ID : " + jData["product_id"])
    print("Check ASIN : " + jData["product_info"]["asin"])
    print("Check Site Product ID : " + jData["site_product_id"])
    f.write("Step #7 - Checking ASIN and Product ID : \n")
    f.write(jData["product_id"]+"\n")
    f.write(jData["product_info"]["asin"]+"\n")
    f.write(jData["site_product_id"]+"\n")
    
    ''' Step #8 - Checking UPC '''
    try:
        print("Step #8 - Check UPC : " + jData["product_info"]["upc"])
        f.write("Step #8 - Checking UPC : \n")
        f.write(jData["product_info"]["upc"] + "\n")
        
    except:
        print("Step #8 - Check UPC : Null")
        f.write("Step #8 - Checking UPC : \n")
        f.write("NULL" + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + "\n")
        
    ''' Step #9 - Checking price and Currency'''
    print("Step #9 - Check Price and Currency:")
    print("    Price: " + jData["sellers"]["price"])
    f.write("Step #9 - Checking Price and Currency : \n")
    f.write(jData["sellers"]["price"]+"\n")
    print("    Price amount: " + str(jData["sellers"]["price_amount"]))
    f.write(str(jData["sellers"]["price_amount"])+"\n")
    print("    Currency: " + jData["sellers"]["price_currency"])
    f.write(jData["sellers"]["price_currency"]+"\n")
    
    ''' Step #10 - Checking Category '''
    print("Step #10 - Check Categories : ")
    print("List of Categories ")
    f.write("Step #10 - Checking Categories : \n")
    for i in range(0, len(jData["classification"]["categories"])):
        print( "    "+ jData["classification"]["categories"][i])
        f.write(jData["classification"]["categories"][i]+"\n")
    print("    Check Category Name: " + jData["classification"]["category_name"])
    f.write(jData["classification"]["category_name"]+"\n")
    
    ''' Step #11 - Checking Best Seller Category'''
    print("Step # 11 - Best Seller Category : " + str(jData["page_attributes"]["best_seller_category"]))
    f.write("Step #11 - Best Seller Category : \n")
    f.write(str(jData["page_attributes"]["best_seller_category"]) + "\n")
    
    ''' Step #12 - Checking Brand '''
    print("Step # 12 - Check Brand : " + jData["classification"]["brand"])
    f.write("Step #12 - Checking Brand : \n")
    f.write(jData["classification"]["brand"]+"\n")
    
    ''' Step #13 - Checking Model '''
    print("Step #13 - Check Model : " + str(jData["product_info"]["model"]))
    f.write("Step #13 - Checking Model : \n")
    f.write(str(jData["product_info"]["model"])+"\n")
    
    '''Step #14 - Checking Stock Status'''
    print("Step #14 -  Check Stock Status : ")
    f.write("Step #14 - Checking Stock Status : \n")
    print("    in_stock : " + str(jData["sellers"]["in_stock"]))
    f.write(str(jData["sellers"]["in_stock"])+"\n")
    print("    in_stock : " + str(jData["sellers"]["site_online"]))
    f.write(str(jData["sellers"]["site_online"])+"\n")
    print("    in_stock : " + str(jData["sellers"]["site_online_in_stock"]))
    f.write(str(jData["sellers"]["site_online_in_stock"])+"\n")
    
    ''' Step #15 - Checking Description'''
    print("Step #15 - Check Description : " + jData["product_info"]["description"])
    f.write("Step #15 - Checking Description : \n")
    f.write(jData["product_info"]["description"]+"\n")
    
    '''Step #16 - Checking Bullets'''
    print("Step #16 - Check Bullets : " + jData["product_info"]["bullets"])
    print("Check Bullets Count : " + str(jData["product_info"]["bullet_feature_count"]))
    f.write("Step #16 - Checking Bullets : \n")
    f.write(jData["product_info"]["bullets"]+"\n")
    f.write(str(jData["product_info"]["bullet_feature_count"])+"\n")
    
    ''' Step # 17 - Checking Long Description'''
    print("Step #17 - Check Long Description : " + str(jData["product_info"]["long_description"]))
    f.write("Step #17 - Checking Long Description : \n")
    f.write(str(jData["product_info"]["long_description"])+"\n")
    
    '''Step # 18 - Checking Specification'''
    try: 
        print("Step #18 - Check Specification : ")
        f.write("Step #18 - Checking Specification : \n")
        for k, v in jData["product_info"]["specs"].items():
            print("    " + k + " : " + v)
            f.write(k + " : " + v + "\n")
    except:
        print("Step #18 - Check Specification : ")
        print("Specification : Null")
        f.write("Step #18 - Checking Specification : \n")
        f.write("Null" + str(datetime.now().strftime('%Y_%m_%d_%H_%M_%S')) + "\n")
        
    
    '''Step #19 - Checking KeyWords'''
    print("Step #19 - Check Keywords :" + jData["page_attributes"]["keywords"])
    f.write("Step #19 - Checking Keywords : \n")
    f.write(jData["page_attributes"]["keywords"]+"\n")
    
    '''Step #20 - Checking Variants'''
    print("Step #20 - Check Variants :" + str(jData["page_attributes"]["variants"]))
    f.write("Step #20 - Checking Variants : \n")
    f.write(str(jData["page_attributes"]["variants"])+"\n")


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
            iRes = 1
        
        origFileIndex += 1    
            
            
    returnResult.append(iRes)
    returnResult.append(sTestResult)
    
    
    return returnResult
    
if __name__ == "__main__":
    
    today = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    
    testResultFiles = []
    
    origFiles = ["Amazon.com/orig_1.txt", "Amazon.com/orig_2.txt", "Amazon.com/orig_3.txt", "Amazon.com/orig_4.txt"]
    
    '''*******************************'''
    
    FILE_FLAG = 0
    
    ''' 
    To generate new original files with data to keep for future comparison please set FILE_FLAG = 0
    To generate new test files with data to compare with original data files please set FILE_FLAG = 1
    '''
    
    statusmessage = ""
    
    if FILE_FLAG == 0 :
        files_name = "Amazon.com/orig_"
        statusmessage = statusmessage + "You creating master data files"
    else:
        files_name = "Amazon.com/test_file_" + today + "_item_"
        statusmessage = statusmessage + "You creating test files for daily comparison"
    
    if messagebox.askokcancel("Status Message", statusmessage) :
        file_name_index = 1
        for each_prod_url in test_products_URLs:
            file_to_generate = files_name + str(file_name_index) + ".txt"
            test_HD_CH(each_prod_url,file_to_generate )
            testResultFiles.append(file_to_generate)
            file_name_index += 1   
        if FILE_FLAG == 0 :
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            print("%%   New Original Test Data Files Generated   %%")
            print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        else:
            iResult = result_comparision(origFiles, testResultFiles)
        
            if iResult[0] == 0:
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("%%%%%%         Test Passed            %%%%%")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print(iResult[1])
            else:
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("%%%%%%         Test Failed            %%%%%")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print("%%%%%%         Test Failed             %%%%")
                print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
                print(iResult[1])
          
      
      

