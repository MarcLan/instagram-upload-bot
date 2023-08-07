from instagrapi import Client
from instagrapi.exceptions import LoginRequired
import logging
from PIL import Image
import glob
import time
import json

# Read data.json
with open("data.json") as file:
	data = json.load(file)

# Convert .png files to .jpg files, because only .jpg files can be uploaded
counter = 0
png_names = glob.glob(data["photo_location"] + "*.png")
for name in png_names:
    counter = counter + 1
    images = Image.open(name)
    #print(images)
    jpg_names = images.save('C:\\code\\content\\images\\' + str(time.strftime("%Y-%m-%d"))+ "-" + str(counter) + '.jpg')
jpg_names = glob.glob('C:\\code\\content\\images\\*.jpg')
#print(jpg_names)

# Login with session
# Enter username and password
cl = Client()
cl.delay_range = [1, 3]
cl.login(data["username"], data["password"])
cl.dump_settings("session.json")
cl.get_timeline_feed()

# Upload photos to Albums
cl.album_upload(jpg_names,'album test')


# Upload photos to Story
print(jpg_names)
for jpg_name in jpg_names:
    cl.photo_upload_to_story(jpg_name, caption='test upload multiple photos')

# Upload video
cl = Client()
path = 'C:\\code\\content\\videos\\2023-08-02.mp4'
caption = 'Your AI girl'
cl.clip_upload(path, caption) 






