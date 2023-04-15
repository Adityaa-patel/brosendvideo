# Import the necessary libraries
import os
import time
from selenium import webdriver
from instagram_private_api import Client, ClientCompatPatch
pip install instagram-private-api

# Set up the client with your Instagram API credentials
api = Client(username='your_username', password='your_password')
# Authenticate the client using the ClientCompatPatch method
api = ClientCompatPatch(api)

# Set up the Selenium web driver
driver = webdriver.Chrome()

# Navigate to the Instagram website and log in
driver.get('https://www.instagram.com/accounts/login/')
# Add the username and password to the input fields
driver.find_element_by_name('username').send_keys('your_username')
driver.find_element_by_name('password').send_keys('your_password')
# Click the login button
driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()

# Wait for the login process to complete
time.sleep(5)

# Navigate to the reel that you want to download
driver.get('https://www.instagram.com/reel/reel_id/')
# Extract the URL of the reel
reel_url = driver.find_element_by_css_selector('.tWeCl').get_attribute('src')

# Download the reel using the Instagram Private API client
try:
    video_bytes = api.video_download(reel_url)
except Exception as e:
    print('Failed to download video:', e)
    exit()

# Save the video to disk
try:
    with open('video.mp4', 'wb') as f:
        f.write(video_bytes)
except Exception as e:
    print('Failed to save video to disk:', e)
    exit()

# Upload the video to Instagram and get the media ID
try:
    response = api.upload_video('video.mp4')
    media_id = response['upload_id']
except Exception as e:
    print('Failed to upload video:', e)
    exit()

# Define the user ID of the recipient of the video
user_id = 'recipient_user_id'

# Send the video back to the user
try:
    api.direct_share(media_id, [user_id], message='Here is the video you requested!')
except Exception

# Set up the client with your Instagram API credentials
api = Client(username='your_username', password='your_password')

from selenium import webdriver

# Set up the Selenium web driver
driver = webdriver.Chrome()

# Navigate to the Instagram website and log in
driver.get('https://www.instagram.com/accounts/login/')
# Add the username and password to the input fields
driver.find_element_by_name('username').send_keys('your_username')
driver.find_element_by_name('password').send_keys('your_password')
# Click the login button
driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()

# Navigate to the reel that you want to download
driver.get('https://www.instagram.com/reel/reel_id/')
# Extract the URL of the reel
reel_url = driver.find_element_by_css_selector('.tWeCl').get_attribute('src')

# Download the reel using the Instagram Private API client
video_bytes = api.video_download(reel_url)

# Save the video to disk
with open('video.mp4', 'wb') as f:
    f.write(video_bytes)
# Send the video back to the user
api.direct_share(media_id, ['user_id'], message='Here is the video you requested!')
# Delete the video from your storage
import os
os.remove('video.mp4')
