import requests
import os

r = requests.post(
    "https://api.deepai.org/api/torch-srgan",
    files={
        'image': open('image.jpg', 'rb'),
    },
    headers={'api-key': 'b2f1bc7c-65b7-4323-8509-810078010168'}
)
print(r.json())

img_data = requests.get(r.json()['output_url']).content
with open('image_out.jpg', 'wb') as handler:
    handler.write(img_data)