from tkinter import *
from Instagram_image_downloader import *

root = Tk()
root.geometry("560x100")
def img_d():
	image_post_downloader(url_widget_image.get())

def vid_d():
	video_post_downloader(url_widget_video.get())

label_image = Label(root, text="Image URL")
label_image.grid(row=0)

label_image = Label(root, text="Video URL")
label_image.grid(row=1)

url_widget_image = Entry(root, width=65)
url_widget_image.grid(row=0, column=1)

url_widget_video = Entry(root, width=65)
url_widget_video.grid(row=1, column=1)

button_image = Button(root, text="Download Image", command=img_d)#image_post_downloader(url_widget_image.get()))
button_image.grid(row=0, column=2)

button_video = Button(root, text="Download Video", command=vid_d)#video_post_downloader(url_widget_video.get()))
button_video.grid(row=1, column=2)

root.mainloop()