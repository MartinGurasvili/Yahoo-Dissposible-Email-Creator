#######################################
#  code writen by
#                 Martin Gurasvili
#  licence: free to use and edit 
#######################################

from selenium import webdriver
import time


Email="bethann19372@yahoo.com"  #Yahoo Email
Password="Golf1234byronva1"     #yahoo password

no_deleted=2    #This is the amount of emails you want to delete


url = "https://mail.yahoo.com/d/settings/1?.intl=uk&.lang=en-GB&.partner=none&.src=fp&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAEX4gBrFkqI6C-Nhyz5SaWwI0gh11evTCz92xyVBJwTVG6PrmYQy_iOu7bW8n55LNqMpV1bwNI19Q8omKfTFwKQjXZkUUlclziwA1eEzPvIlQKidb4Zlp1E23CoLT_mhya7rRl8CPqnO5AVDxuO0cuBOhu3zY1ZdOId8K7X2fpwH&guccounter=1"

driver = webdriver.Chrome(r"chromedriver")   
driver.get(url)
    
driver.find_element_by_id("login-username").send_keys(Email)
    
driver.find_element_by_id("login-signin").click()
    
time.sleep(1)
    
driver.find_element_by_id("login-passwd").send_keys(Password)
    
driver.find_element_by_id("login-signin").click()
    
time.sleep(1)
#driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[1]/div/div[3]/div[3]/a").click()
print("deleted")
for x in range (1,no_deleted+1):
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[1]/div/div[3]/ul/li[1]/div/div").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div/section/div/article/div/div[2]/div/div/div/div[3]/button/span").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[7]/div/div/div/div[4]/button[1]").click()
import Excel
driver.quit()

