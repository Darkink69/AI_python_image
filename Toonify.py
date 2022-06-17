import requests
import timeit
r = requests.post(
    "https://api.deepai.org/api/toonify",
    files={
        'image': open('image2.jpg', 'rb'),
    },
    headers={'api-key': 'b2f1bc7c-65b7-4323-8509-810078010168'}
)
print(r.json())

# Download result photo
img_data = requests.get(r.json()['output_url']).content
with open('toony_out.jpg', 'wb') as handler:
    handler.write(img_data)

