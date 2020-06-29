import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs

img_url = "https://www.instagram.com/p/CB_AEMTng3b/?igshid=1s8hvlw6u9e68"
video_url = "https://www.instagram.com/p/CBJhwVIpvOC/?igshid=ff0xz5e0t1qa"

def image_post_downloader(url):
	#Finds url of an image in post and returns it as string
	if url[:8]!='https://':
		return "Invalid URL"
	page = requests.get(url)
	soup = bs(page.content, "lxml")
	content = requests.get(soup.find("meta", property="og:image")['content'])
	#file_name = ''.join([string.ascii_letters[randint(0, 51)] for i in range(10)])
	#file_name = soup.find("meta", property="og:description")["content"]
	today = datetime.now()
	file_name = today.strftime("%d %H_%M_%S")
	with open("d:/Instagram/" + str(file_name) + ".jpg", "wb") as file:
		file.write(content.content)
	print("Image download succesful.")

def video_post_downloader(url):
	#Finds url of a video in post and returns it as string.
	if url[:8]!='https://':
		return "Invalid URL"
	page = requests.get(url)
	soup = bs(page.content, "lxml")
	content = requests.get(soup.find("meta", property="og:video")['content'])
	#file_name = ''.join([string.ascii_letters[randint(0, 51)] for i in range(10)])
	#file_name = soup.find("meta", property="og:description")["content"]
	today = datetime.now()
	file_name = today.strftime("%d %H %M %S")
	with open("d:/Instagram/" + file_name + ".mp4", "wb") as file:
		file.write(content.content)
	print("Video download succesful.")


