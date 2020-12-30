#######################################
#  code writen by
#                 Martin Gurasvili
#  licence: free to use and edit 
#######################################

import csv
import time
from selenium import webdriver
import datetime
import shutil

dateTime = datetime.datetime.now()
dateTime = str(dateTime).split(" ")
Time =str(dateTime[1])[0:8]
Time =str(Time).split(":")
Time = Time[0]+"-"+Time[1]+"-"+Time[2]
Excel_name = "Test "+ str(dateTime[0]) + " " + str(Time)  #name of the csv (excel document)

file = open("Config.txt","r")
Email =file.readline()  #Yahoo Email
Password =file.readline()  #yahoo password

print (Email)
print (Password)


url = "https://mail.yahoo.com/d/settings/1?.intl=uk&.lang=en-GB&.partner=none&.src=fp&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAEX4gBrFkqI6C-Nhyz5SaWwI0gh11evTCz92xyVBJwTVG6PrmYQy_iOu7bW8n55LNqMpV1bwNI19Q8omKfTFwKQjXZkUUlclziwA1eEzPvIlQKidb4Zlp1E23CoLT_mhya7rRl8CPqnO5AVDxuO0cuBOhu3zY1ZdOId8K7X2fpwH&guccounter=1"

driver = webdriver.Firefox()  
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
    if (int(no_of_emails[0])) > 3 :
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[1]/div/div[3]/div[3]/a").click()
        print ("show more")
        
    for x in range (1,(int(no_of_emails[0]))+1):
        email = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[1]/div/div[3]/ul/li[{0}]/div/div".format(x)).text
        writer.writerow([str(email)])
        print("Task Complete")
        
shutil.move('{0}.csv'.format(Excel_name), 'DEA')
driver.quit()
