#######################################
#  code writen by
#                 Martin Gurasvili
#  licence: free to use and edit 
#######################################

import csv
import time
from selenium import webdriver

Email="example@yahoo.com"  #Yahoo Email
Password="123password"     #yahoo password

Excel_name = "DeaEmails"  #name of the csv (excel document)

url = "https://mail.yahoo.com/d/settings/1?.intl=uk&.lang=en-GB&.partner=none&.src=fp&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAEX4gBrFkqI6C-Nhyz5SaWwI0gh11evTCz92xyVBJwTVG6PrmYQy_iOu7bW8n55LNqMpV1bwNI19Q8omKfTFwKQjXZkUUlclziwA1eEzPvIlQKidb4Zlp1E23CoLT_mhya7rRl8CPqnO5AVDxuO0cuBOhu3zY1ZdOId8K7X2fpwH&guccounter=1"

driver = webdriver.Chrome(r"chromedriver")    
driver.get(url)
        
driver.find_element_by_id("login-username").send_keys(Email)
        
driver.find_element_by_id("login-signin").click()
        
time.sleep(1)
        
driver.find_element_by_id("login-passwd").send_keys(Password)
        
driver.find_element_by_id("login-signin").click()
        
time.sleep(1)


with open('{0}.csv'.format(Excel_name), 'w', newline='') as file:
    writer = csv.writer(file)
        
    writer.writerow(["Email"])
        
    time.sleep(1)
        
    no_of_emails= driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[1]/div/div[3]/div[2]/span/div").text
    no_of_emails = no_of_emails.split(" ")
        
    print (no_of_emails[0])
    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[1]/div/div[3]/div[3]/a").click()
        
    for x in range (1,(int(no_of_emails[0]))+1):
        email = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[1]/div/div[3]/ul/li[{0}]/div/div".format(x)).text
        writer.writerow([str(email)])
        print("Task Complete")
driver.quit()
