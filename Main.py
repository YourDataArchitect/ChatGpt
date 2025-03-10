from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import pandas as pd
import undetected_chromedriver as uc
import time
import os 


class ChatGPT:
    def __init__(self):
        self.current_folder = os.path.dirname(os.path.abspath(__file__))
        self.chrome_driver = os.path.join(self.current_folder, "chromedriver.exe")
        self.login_page = 'https://chatgpt.com/'
        self.driver = None
        self.username =  input("Enter username : ")
        self.password =  input("Enter password : ")
    
        
    def launch_driver(self):
        'This function for launching browser driver'
        print(f'-- >> Login page {self.login_page}')
        # Config Driver Options
        user_agents_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.120 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36",
        "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
        "Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_6_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; U; Android 8.0; en-us; Nexus 9 Build/OPR6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Linux; Android 9; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 Edg/92.0.902.55",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15"]
        
        options = uc.ChromeOptions()
        options.add_argument(f'user-agent={random.choice(user_agents_list)}')
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument('--disable-infobars')  # Disables "Chrome is being controlled" info bar
        options.add_argument('--window-size=1920,1080')  # Sets window size for better compatibility
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--ignore-ssl-errors")
        # options.add_argument("--headless")
        options.add_argument("--log-level=3")
        options.headless = False
    
        # using undedicted selenium 
        self.driver = uc.Chrome(
                        use_subprocess=False,
                        options=options,
                        driver_executable_path = self.chrome_driver)
        
        self.driver.get(self.login_page)
        return self.driver

    def handling_token(self):
        'This function for handling authentication and token page'
        token_number = input('Please check your email to extract the token number and enter it here:')
        input_xpath = '//input'
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, input_xpath))).send_keys(token_number)
        
        submit_button = '//button[@type="submit"]'
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, submit_button))).click()

        return self.driver 

    def login(self):
        'This function for lon in page'
        # press login button
        print('press login button') 
        login_button_xpath = '//div[@class="flex items-center gap-2 pr-1 leading-[0]"]//*[contains(text(),"Log in")]'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_button_xpath))).click()
        
        # input username 
        username_box_input_xpath = '//input[@id="email-input"]'
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, username_box_input_xpath))).send_keys(self.username)

        # press continue button
        cotinue_buttom_xpath = '//input[@class="continue-btn"]'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, cotinue_buttom_xpath))).click()

        # input password
        password_xpath = '//input[@id="password"]'
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, password_xpath))).send_keys(self.password)

        # press submit button
        submit_button_xpath = '//button[@type="submit"]'
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath))).click()
        
        return driver
        

        # please check your email and Enter Token send to your email address
        
    
if __name__ == "__main__":
    
    # Init the driver
    ChatGPT_instant = ChatGPT()
    driver = ChatGPT_instant.launch_driver()
    
    # handling login page
    driver = ChatGPT_instant.login()
    
    # handling token page 
    driver = ChatGPT_instant.handling_token()

    # Ask questions and save questions and answers to csv file 
    output_list = []
    while True : 
        item = {}
        prompt = input('Please Enter your Prompt : ')
        driver.find_element(By.XPATH,'//br[@class="ProseMirror-trailingBreak"]').send_keys(prompt)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="flex gap-x-1.5"]'))).click()
        
        # extract data output and save to csv file
        time.sleep(5)
        print('waiting answer')
        Answer = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//p[@data-start="0"]')))[-1].text
        print(Answer)
        
        response = input('Is there another questions ,\n if yes please enter [y],\n if No more questions please enter [n] : ')
        if response == 'n' or 'N' : 
            break
        elif response == 'y' or 'Y' : 
            item['prompt'] = prompt
            item['answer'] = Answer
            output_list.append(item)
            continue

    # saving output to csv file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file_path = os.path.join(current_dir,'out_put.csv')

    df = pd.DataFrame(output_list)
    df.to_csv(csv_file_path)
    print(f'The output file is saved to this path [{csv_file_path}] ')
    

        