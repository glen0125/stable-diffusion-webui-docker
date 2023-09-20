import base64
import requests
from PIL import Image
import io

# payload = {
#     "prompt": "blue sky with clouds, a red umbrella, and a green apple, beautiful beach, sunset",
#     "steps": 20
# }

# response = requests.post(url=f'http://aigc:7862/sdapi/v1/txt2img', json=payload)
# r = response.json()

# for i in r['images']:
#     image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
#     image.save('a.png')

payload = {
  "sd_model_checkpoint": "chilloutmix",
}

response = requests.post(url=f'http://aigc:7860/sdapi/v1/options', json=payload)
print(response)

print(response.json())