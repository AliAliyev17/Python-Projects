import requests
from datetime import datetime
from bs4 import BeautifulSoup as bs


def image_post_downloader(url):
	#Finds url of an image in post and returns it as string
	if url[:8]!='https://':
		return "Invalid URL"
	page = requests.get(url)
	soup = bs(page.content, "lxml")
	content = requests.get(soup.find("meta", property="og:image")['content'])
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
	today = datetime.now()
	file_name = today.strftime("%d %H %M %S")
	with open("d:/Instagram/" + file_name + ".mp4", "wb") as file:
		file.write(content.content)
	print("Video download succesful.")


