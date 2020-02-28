from selenium import webdriver
from time import sleep

song = input("Enter name of song: ")
artist = input("Enter name of artist: ")
search_string = song + " " + artist

chromedriver = r"C:\Users\Malhaar\Downloads\chromedriver_win32\chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

def launch():
    driver.get("https://www.youtube.com/")
    sleep(1)

def search():
    driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/div/div[1]/input").send_keys(search_string)
    driver.find_element_by_xpath("/html/body/ytd-app/div/div/ytd-masthead/div[3]/ytd-searchbox/form/button").click()
    sleep(1)

def click_video():
    driver.find_element_by_xpath("/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/ytd-thumbnail/a").click()


launch()
search()
click_video()
