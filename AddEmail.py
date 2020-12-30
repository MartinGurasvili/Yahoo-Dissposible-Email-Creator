#######################################
#  code writen by
#                 Martin Gurasvili
#  licence: free to use and edit 
#######################################

from selenium import webdriver
import time
import random
import csv 

How_many_emails_do_you_want = 250    #This is the amount of emails you want to make

Send_Name="sendername"   #Senders name
Desc="Description"      #Description

Email="example@yahoo.com"  #Yahoo Email
Password="123password"     #yahoo password


def createDEA():
    url = "https://mail.yahoo.com/d/settings/1?.intl=uk&.lang=en-GB&.partner=none&.src=fp&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAEX4gBrFkqI6C-Nhyz5SaWwI0gh11evTCz92xyVBJwTVG6PrmYQy_iOu7bW8n55LNqMpV1bwNI19Q8omKfTFwKQjXZkUUlclziwA1eEzPvIlQKidb4Zlp1E23CoLT_mhya7rRl8CPqnO5AVDxuO0cuBOhu3zY1ZdOId8K7X2fpwH&guccounter=1"

    driver = webdriver.Chrome(r"chromedriver")   
    driver.get(url)
    
    driver.find_element_by_id("login-username").send_keys(Email)
    
    driver.find_element_by_id("login-signin").click()
    
    time.sleep(1)
    
    driver.find_element_by_id("login-passwd").send_keys(Password)
    
    driver.find_element_by_id("login-signin").click()
    
    time.sleep(1)
    
    for x in range (0,How_many_emails_do_you_want):
        
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[1]/div/div[3]/div[3]/button').click()
        
        Keyword = str(random.randint(10000, 100000))
        
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[2]/div/div/div/div[1]/div/div[1]/div[2]/div/input').send_keys(Keyword)#keyword
        
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[2]/div/div/div/div[2]/div/div/input').send_keys(Send_Name)#sending name
        
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[2]/div/div/div/div[3]/div/div/input').send_keys(Desc)#description
        
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[2]/div/div/div/div[4]/button[1]/span').click()
    import Excel
    driver.quit()
    
       
createDEA()
