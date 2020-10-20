import urllib.request, urllib.parse, urllib.error
import json
import requests
from PIL import Image 
username=input("Enter Username : ")
url='https://www.instagram.com/'+username+'/?__a=1'
data=urllib.request.urlopen(url).read()
info = json.loads(data)
dpUrl=info['graphql']['user']['profile_pic_url_hd']
#print("profile pic URL : ",dpUrl)
print("Full Name : ",info['graphql']['user']['full_name'])
print("Bio : ",info['graphql']['user']['biography'])
print("Posts : ",info['graphql']['user']['edge_owner_to_timeline_media']['count'])
print("Followers : ",info['graphql']['user']['edge_followed_by']['count'])
print("Followed : ",info['graphql']['user']['edge_follow']['count'])


#downloading image with url using requests module
response = requests.get(dpUrl)

file = open("insta_image.jpg", "wb")
file.write(response.content)
print("\n===> Profile pic Downloaded as insta_image.jpg <===")
file.close()

# creating a object for image 
im = Image.open(r"C:\Users\Kailash Venkat\Desktop\pyth4e\insta1\insta_image.jpg")#here use your path where python files are stored.

#this show() uses computer's image viewer
#im.show()

#to convert the jpg image to ppm format
im.save(r"C:\Users\Kailash Venkat\Desktop\pyth4e\insta1\insta_image1.ppm")

#To display image GUI using tkinter package
from tkinter import *     
root = Tk()      
canvas = Canvas(root, width = 300, height = 300)      
canvas.pack()      
img = PhotoImage(file="insta_image1.ppm")      
canvas.create_image(20,20, anchor=NW, image=img)      
mainloop()   


