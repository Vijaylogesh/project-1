from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class orangehrm():
    def test(self):

        #Initializing the browser
        driver=webdriver.Chrome()
        base_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(2)

        #Login using Invalid credentials

        Xpath_to_username = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        Entering_username = driver.find_element(By.XPATH, Xpath_to_username)
        Entering_username.click()
        Entering_username.send_keys("Admin")
        Xpath_to_password = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        Entering_password = driver.find_element(By.XPATH, Xpath_to_password)
        Entering_password.click()
        Entering_password.send_keys("admin12565")
        Entering_password.send_keys(Keys.ENTER)
        time.sleep(5)


        #Login to website

        #Login using correct password-----Test-2

        #Entering user name
        Xpath_to_username="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
        Entering_username=driver.find_element(By.XPATH,Xpath_to_username)
        Entering_username.click()
        Entering_username.send_keys("Admin")

        #Entering password
        Xpath_to_password="//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
        Entering_password=driver.find_element(By.XPATH,Xpath_to_password)
        Entering_password.click()
        Entering_password.send_keys("admin123")

        #logging to orangeHRM
        Entering_password.send_keys(Keys.ENTER)
        print("The user is logged in successfully")
        driver.implicitly_wait(5)

        #Adding New employee------Test-3

        #selecting PIM module

        xpath_to_pim_module='//a[@href="/web/index.php/pim/viewPimModule"]'
        clicking_to_pim_module=driver.find_element(By.XPATH,xpath_to_pim_module)
        clicking_to_pim_module.click()
        clicking_add_button=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')
        clicking_add_button.click()

        #entering first name

        Entering_first_name=driver.find_element(By.NAME,"firstName")
        Entering_first_name.send_keys("Project")

        # entering middle name

        Entering_middle_name=driver.find_element(By.NAME,"middleName")
        Entering_middle_name.send_keys(" ")

        # entering last name

        Entering_last_name=driver.find_element(By.NAME,"lastName")
        Entering_last_name.send_keys("AT")



        #Clicking create login deatail
        create_login_deatails=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span')
        create_login_deatails.click()

        # Creating username
        username=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input')
        username.send_keys("Project-AT8")

        # Creating  password
        password=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input")
        password.send_keys("Project@12345")
        confirm_password=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input")
        confirm_password.send_keys("Project@12345")

        #Submitting username and password
        submit=driver.find_element(By.XPATH,"//button[@type='submit']")
        submit.send_keys(Keys.ENTER)

        #Editing the employee data-----Test-4

        #Clicking PIM Module
        xpath_to_pim_module = '//a[@href="/web/index.php/pim/viewPimModule"]'
        clicking_to_pim_module = driver.find_element(By.XPATH, xpath_to_pim_module)
        clicking_to_pim_module.click()

        #Searching for employee name
        Employee_name=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        Employee_name.send_keys("Project AT")
        time.sleep(2)

        #Clicking submit button
        search=driver.find_element(By.XPATH,'//button[@type="submit"]')
        search.click()
        time.sleep(2)


        #Click on edit option
        driver.execute_script("window.scrollBy(0,400);")
        time.sleep(2)
        Edit_option=driver.find_element(By.XPATH,'//i[@class="oxd-icon bi-pencil-fill"]')
        Edit_option.click()

        #Adding nick name
        Nick_name=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input')
        Nick_name.send_keys("abc")

        #Adding Other id
        Other_id=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')
        Other_id.send_keys("1234")

        #Adding DL number
        DL_number=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
        DL_number.send_keys("12345678")

        #Entering expiry date
        Expiry_date=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/i')
        Expiry_date.click()
        date_selection=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
        date_selection.send_keys("2023-12-15")

        #Entering SSN number
        SSN_number=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input')
        SSN_number.send_keys("1234")

        #Entering SIN number
        SIN_number=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input')
        SIN_number.send_keys("5678")

        driver.execute_script ("window.scrollBy(0,300)")

        #Selecting Nationality
        Country_selection=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]')
        Country_selection.send_keys('indian')


        #Selecting Martial status
        Martial_status=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]')
        Martial_status.click()
        Martial_status.send_keys(Keys.ARROW_DOWN)

        #Entering DOB
        Entering_DOB=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')
        Entering_DOB.send_keys("2000-02-13")

        #Selecting gender
        Selecting_gender=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span')
        Selecting_gender.click()

        #Entering Military service
        Military_service=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input')
        Military_service.send_keys("NO")

        #Entering Blood group
        Blood_group=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]')
        Blood_group.send_keys(Keys.ARROW_DOWN)

        #Saving the data
        save_button=driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')
        save_button.click()
        time.sleep(6)



        #Deleting an account------Test-5

        # Clicking PIM Module
        xpath_to_pim_module = '//a[@href="/web/index.php/pim/viewPimModule"]'
        clicking_to_pim_module = driver.find_element(By.XPATH, xpath_to_pim_module)
        clicking_to_pim_module.click()

        #Searching for employee name
        Employee_name = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input')
        Employee_name.send_keys("Project AT")

        #Clicking search icon
        search = driver.find_element(By.XPATH, '//button[@type="submit"]')
        search.click()
        time.sleep(3)

        driver.execute_script("window.scrollBy(0,400);")

        #Deleting an account
        deleting_an_account=driver.find_element(By.XPATH,'//i[@class="oxd-icon bi-trash"]')
        deleting_an_account.click()
        time.sleep(2)
        click_ok=driver.find_element(By.XPATH,'//i[@class="oxd-icon bi-trash oxd-button-icon"]')
        click_ok.click()
        time.sleep(10)



        












abc=orangehrm()
abc.test()