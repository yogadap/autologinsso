import pyttsx3
import os,random,sys,time
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from countdown import countdown

print("bot berjalan\n")
browser = webdriver.Chrome(ChromeDriverManager().install())
bukalist = open("linksso.txt")
bacafile = bukalist.readlines()
targeturl = bacafile[0]
browser.get(targeturl)
bukafileakun = open("akun.txt")
bacaakun = bukafileakun.readlines()
username = bacaakun[0]
password = bacaakun[1]
AkunID = browser.find_element_by_id('username')
AkunID.send_keys(username)
Akunpassword = browser.find_element_by_id('password')
Akunpassword.send_keys(password)
Akunpassword.send_keys(Keys.ENTER)
time.sleep(2)
tabbaru = browser.find_element_by_css_selector('body')
tabbaru.send_keys(Keys.CONTROL + 't')
browser.get('http://gw.hotspot.ui.ac.id/cas/gateway.php')
print("Berhasil Login")
browser.minimize_window()


