from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import datetime
import time
import sys
import os
from PIL import Image
import pywhatkit
# import importlib  
# mac_imessage = importlib.import_module('mac_imessage')


from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def send_imessage(phone_number, message_body):
    os.system('osascript send_imessage.applescript {} "{}"'.format( phone_number, message_body ) )


# driver = webdriver.Chrome(service=s, options=options)

def check_image(address):
	im = Image.open(address).convert("RGB")

	# get pixels
	pixels = [im.getpixel((i, j)) for j in range(im.height) for i in range(im.width)]

	# or
	pixels = [i for i in im.getdata()]

	#check if tuple of pixel value exists in array-pixel

	return((225, 239, 251) in pixels) #True if exists, False if it doesn't

def screenshot():
	datetime_obj = datetime.datetime.now()
	datetime_str = str(datetime_obj)+".png"

	add = f""
	driver.save_screenshot(add)

	available = check_image(add)

	if available:
		print(available)
		os.system('afplay /System/Library/Sounds/Sosumi.aiff')
		os.system('afplay /System/Library/Sounds/Sosumi.aiff')
		os.system('afplay /System/Library/Sounds/Sosumi.aiff')	
		# Defining the Phone Number and Message
		# phone_number = "+"
		# message = "yes"
		send_imessage( '', 'Hello' )
		# mac_imessage.send(
	 #    message='Hello',
	 #    phone_number='',
	 #    medium='iMessage'
    	# )

		# Sending the WhatsApp Message
		pywhatkit.sendwhatmsg_instantly(phone_number, message)

		# Displaying a Success Message
		print("WhatsApp message sent!")
		return
	os.remove(add)


# driver = webdriver.Chrome(ChromeDriverManager().install())

count = 0
while(True):
	try:
		count += 1
		print(count, datetime.datetime.now())
		options = webdriver.FirefoxOptions()
		driver = webdriver.Firefox(options=options)
		# driver = webdriver.Chrome()
		# Get search results for a given date range
		driver.get("")
		title = driver.title
		driver.implicitly_wait(0.5)

		email = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[1]/input')

		email.click()
		email.send_keys("")
		password = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[2]/input')
		password.click()
		password.send_keys("")
		click = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[3]/div/div[1]/div/form/div[3]/label/div')
		click.click()
		signin = driver.find_element(By.XPATH, '/html/body/div[5]/main/div[3]/div/div[1]/div/form/p[1]/input')
		signin.click()
		driver.implicitly_wait(2)
		time.sleep(.5)
		driver.implicitly_wait(2)
		cont = driver.find_element(By.XPATH, '/html/body/div[4]/main/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/ul/li/a')
		cont.click()

		
		# cont = driver.find_element(By.LINK_TEXT, "/en-am/niv/schedule/66838619/continue_actions")

		# cont.click()
		re = driver.find_element(By.XPATH, '/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[3]/a/h5')
		re.click()
		re2 = driver.find_element(By.XPATH, '/html/body/div[4]/main/div[2]/div[2]/div/section/ul/li[3]/div/div/div[2]/p[2]/a')
		re2.click()
		date_app = driver.find_element(By.XPATH, '/html/body/div[4]/main/div[4]/div/div/form/fieldset/ol/fieldset/div/div[1]/div[3]/li[1]/input')
		time.sleep(.5)
		driver.implicitly_wait(2)
		date_app.click()
		time.sleep(1)

		screenshot()
		for x in range(7):
			date_app = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div/a/span')
			date_app.click()
			time.sleep(.5)
			screenshot()
		time.sleep(10)
		driver.close()
	except:
	# 	print('error')
	# 	driver.close()
		continue
sys.exit()


date_app = driver.find_element(By.CLASS_NAME, 'undefined')
date_app = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/table/tbody/tr[3]/td[3]/a')
date_app.click()
date_app.click()
date_app.click()


sys.exit("hi")
start_date.clear()
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys(Keys.BACKSPACE)
start_date.send_keys("01/01/2023")
driver.implicitly_wait(60)
time.sleep(1)

submit_button = driver.find_element(by=By.NAME, value="ctl00$PlaceHolderMain$generalSearchForm$txtGSEndDate")
submit_button.click()
end_date.clear()
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys(Keys.BACKSPACE)
end_date.send_keys("01/31/2023")
driver.implicitly_wait(60)
time.sleep(5)

submit_button = driver.find_element(by=By.ID, value="ctl00_PlaceHolderMain_btnNewSearch")
submit_button.click()
driver.implicitly_wait(60)
time.sleep(5)











def get_results(value):
	permit = driver.find_element(by=By.ID, value=value)
	driver.implicitly_wait(10)
	print(value)
	print('test')
	permit.click()
	get_cost()
	time.sleep(5)
	driver.back()


def get_cost():
	col1 = []
	col2 = []
	driver.implicitly_wait(100)

	#GET COLUMN 1
	l=driver.find_elements(by=By.XPATH, value=".//*[@class= 'MoreDetail_ItemColASI MoreDetail_ItemCol1']")
	if len(l) > 0:
		for i in l:
			driver.implicitly_wait(100)
			q=i.find_elements(by=By.XPATH, value="./*[@class= 'ACA_SmLabelBolder font11px']")
			for v in q:
				driver.implicitly_wait(100)
				col1.append(v.get_attribute("innerHTML"))
				#print(v.get_attribute("innerHTML"))

	#GET COLUMN 2
	l=driver.find_elements(by=By.XPATH, value=".//*[@class= 'MoreDetail_ItemColASI MoreDetail_ItemCol2']")
	if len(l) > 0:
		for i in l:
			driver.implicitly_wait(100)
			q=i.find_elements(by=By.XPATH, value="./*[@class= 'ACA_SmLabel ACA_SmLabel_FontSize']")
			for v in q:
				driver.implicitly_wait(100)
				col2.append(v.get_attribute("innerHTML"))
				#print(v.get_attribute("innerHTML"))


	if len(col1) > 0:
		for i in range(len(col1)):
			field_1 = col1[i]
			field_2 = col2[i]
			print(f"{field_1}  {field_2}")
	

#get permits 1-10
for x in ["%.2d" % i for i in range(2,12)]:
	get_results("ctl00_PlaceHolderMain_dgvPermitList_gdvPermitList_ctl" + x + "_hlPermitNumber")
