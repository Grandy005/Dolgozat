# imports
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
# set driver
driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/Dolgozat/index.html')
# functions

def test1():
    elementOne = driver.find_element(By.ID, 'element-one')
    ActionChains(driver).double_click(elementOne).perform()
    assert 'animation' in elementOne.get_attribute('class')
    driver.save_screenshot('first-element-test.png')
def test2():
    elementTwo = driver.find_element(By.ID, 'element-two')
    ActionChains(driver).move_to_element(elementTwo).perform()
    assert 'box-shadow: 10px 10px;' in elementTwo.get_attribute('style')
    driver.save_screenshot('second-element-test.png')

def test3():
    elementThree = driver.find_element(By.ID, 'element-three')
    elementThree.click()
    assert 'display: none' in elementThree.get_attribute('style')
    driver.save_screenshot('third-element-test.png')

def test4():
    elementFour = driver.find_element(By.ID, 'element-four')
    elementFour.click()
    assert 'background-color: green' in elementFour.get_attribute('style')
    driver.save_screenshot('fourth-element-test.png')

def test5():
    elementFour = driver.find_element(By.ID, 'element-four')
    ActionChains(driver).move_to_element(elementFour).perform()
    driver.save_screenshot('fifth-element-test.png')

# test1: dupla kattintás után szerepel-e az "animation" class
test1()
time.sleep(1)
# ha rámegy az egér, utána létezik-e box-shadow
test2()
time.sleep(1)
# kattintás után eltűnik-e
test3()
time.sleep(1)
# kattintás után a háttere zöld lesz-e
test4()
time.sleep(1)
# ha a 4. elemre egeret viszünk, hogy néz ki? (screenshot kell csak!)
test5()