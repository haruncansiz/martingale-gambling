import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:/Users/harun/Desktop/Projects/Martingale/chromedriver.exe')

#load website
driver.get("https://www.wtfskins.com/roulette")
#maxime tab
driver.maximize_window()

#accept tos and 18
driver.find_element_by_xpath("/html/body/app-root/div/div/div/div/app-login-page/div/div/div[3]/div[1]/label/input").click()
driver.find_element_by_xpath("/html/body/app-root/div/div/div/div/app-login-page/div/div/div[3]/div[2]").click()
driver.find_element_by_xpath("/html/body/app-root/div/div/div/div/app-login-page/div/div/div[4]/div").click()

#login to wtfskins trough my auth token
driver.execute_script("window.localStorage.setItem('wtfskins_auth_token', '333a313339363637913a7b33323333653566652d653561342d343535322d383638352d3037353036343635613862377d')")
time.sleep(2)

#navigate to roulette
driver.find_element_by_xpath("/html/body/app-root/div/app-nav-bar/div/div/div/div[2]/div[3]/div[2]/app-localization-string").click()

def martingale(bet_amount, previous_color):
    if(check_balance() == 0.00):
        return

    current_hash = get_hash()
    current_color = "red"
    while current_hash == get_hash():
        time.sleep(1)
    
    input_wager = driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div/div/app-roulette-game/div[1]/div/app-wager-bar/div/div[1]/div[1]/input")
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(Keys.BACKSPACE)
    input_wager.send_keys(str(bet_amount))

    time.sleep(3)
    red = driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div/div/app-roulette-game/div[1]/div/app-roulette-bet-option-select/div[1]/div[2]/div[1]")
    grey = driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div/div/app-roulette-game/div[1]/div/app-roulette-bet-option-select/div[3]/div[2]/div[1]")
    
    if(previous_color == "red"):
        current_color = "grey"
        grey.click()
    elif(previous_color == "grey"):
        current_color = "red"
        red.click()

    time.sleep(18)

    try:
        skin = driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div/div/app-roulette-game/div[2]/app-roulette-user-inventory/div/app-asset-container/app-asset")
        hover = ActionChains(driver).move_to_element(skin)
        hover.perform()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div/div/app-roulette-game/div[2]/app-roulette-user-inventory/div/app-asset-container/app-asset/div/div[2]/div/div[2]/app-localization-string").click()
        driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div/div/app-roulette-game/div[2]/app-roulette-user-inventory/div/app-asset-container/app-asset/div/div[2]/div[2]/button[1]").click()
        martingale(0.001, current_color)
    except NoSuchElementException:
        print("Kristall")
        martingale(bet_amount * 2, current_color)

def get_hash():
    return driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div/div/app-roulette-game/div[1]/div/div[2]").text 

    
def check_wager_clickable(wager_button):
    classes = wager_button.get_attribute("class")
    for class_name in classes:
        if(class_name == "disabled"):
            return False
    return True

def check_balance():
    return driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div/div/app-roulette-game/div[1]/div/div[2]")

time.sleep(1)
martingale(0.001, "grey")




