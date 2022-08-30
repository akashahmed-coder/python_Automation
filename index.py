import undetected_chromedriver.v2 as uc
from time import sleep
from csv import reader
from selenium.webdriver.common.by import By
import requests
from multiprocessing import freeze_support
freeze_support()
import keyboard

youtube_channel = input("enter youtube channel link:")
with open('info.txt', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
info = list_of_rows
for i in range(len(info)):
        index = info[i][0]
        thisId = info[i][1]


response = requests.get("https://codemailbyakash.herokuapp.com/user")
userId =  response.json()[int(index)]["userId"]
status = response.json()[int(index)]["status"]



# how_much = input("how much subsribe added this channel")
 
def Connecting_To_Browser(id_str, pass_str):
    
    try:
        driver.find_element(By.XPATH,'//input[@type="email"]').send_keys(id_str)
        driver.find_element(By.XPATH,'//*[@id="identifierNext"]').click()
        sleep(2)

        driver.find_element(By.XPATH,'//input[@type="password"]').send_keys(pass_str)
        driver.find_element(By.XPATH,'//*[@id="passwordNext"]').click() 
        sleep(2)
        def find_email():
            return driver.find_element(By.XPATH , "//c-wiz/div/div[2]/div/c-wiz/c-wiz/div/div[3]/div/div/header/div[1]/div/button/figure/img")
        if find_email():
            driver.get(str(youtube_channel))
            sleep(2)
            try:
                sleep(2)
                driver.find_element(By.CLASS_NAME,"style-scope ytd-subscribe-button-renderer").click()
                sleep(2)
                         
            except:
                print("invalid email:")
            
            driver.get("chrome://settings/clearBrowserData")
            sleep(2)
            clearButton = driver.execute_script("return document.querySelector('settings-ui').shadowRoot.querySelector('settings-main').shadowRoot.querySelector('settings-basic-page').shadowRoot.querySelector('settings-section > settings-privacy-page').shadowRoot.querySelector('settings-clear-browsing-data-dialog').shadowRoot.querySelector('#clearBrowsingDataDialog').querySelector('#clearBrowsingDataConfirm')")
            #click on the clear button now
            clearButton.click()
            print(id_str)
            sleep(2)             
            # driver.quit()

        # if driver.find_element_by_id == True:
        #     print(id_str)
        
        # driver.quit()
    except:
        print("no")


with open('id_pass.txt', 'r') as read_obj:
    csv_reader = reader(read_obj)
    list_of_rows = list(csv_reader)
total_Len = len(list_of_rows)

ids_pass_list = list_of_rows

if __name__ == '__main__':
    freeze_support()    
    thisid = int(thisId)
    if thisid == userId and status == "start":
        driver = uc.Chrome() 
        for i in range(len(ids_pass_list)):
            
                         
                driver.get('http://accounts.google.com')    
                id_str = ids_pass_list[i][0]
                id_pass = ids_pass_list[i][1]
                Connecting_To_Browser(id_str, id_pass)
    else:
        print("invalid user")
        print("please contact your software manager")
        sleep(10)
        