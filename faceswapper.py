import random
import requests
import base64
import pybase64
from get_request import get_url

def face_swap(directory):
    boris = f"{directory}/user_photo.jpg"
    biden = f"{directory}/user_photo2.jpg"
    url = 'https://httpbin.org/post'

    with open(boris, "rb") as f:
        im_bytes = f.read()

    with open(biden, "rb") as f:
        im_bytes2 = f.read()

    im_b64 = base64.b64encode(im_bytes).decode("utf8")
    im_b64_2 = base64.b64encode(im_bytes2).decode("utf8")

    headers = {
        'authority': '3923-31-223-52-90.ngrok-free.app',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8,ru;q=0.7',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryvwsuIAoQbQBDEoT9',
        'origin': 'https://www.faceswapper.app',
        'referer': 'https://www.faceswapper.app/',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    }

    data = ('------WebKitFormBoundaryZYL30t4GNHERvXPO\r\n'
            'Content-Disposition: form-data; name="photo1"; '
            f'filename={im_bytes}\r\n'
            'Content-Type: image/jpeg\r\n\r\n\r\n'
            ''
            '------WebKitFormBoundaryZYL30t4GNHERvXPO\r\n'
            'Content-Disposition: form-data; name="photo2"; '
            f'filename={im_bytes2}\r\n'
            'Content-Type: image/jpeg\r\n\r\n\r\n'
            ''
            '------WebKitFormBoundaryZYL30t4GNHERvXPO\r\n'
            'Content-Disposition: form-data; '
            f'name="randomNumber"\r\n\r\n{591989248 + random.randint(-1000, 1000)}\r\n'
            ''
            '------WebKitFormBoundaryZYL30t4GNHERvXPO--\r\n')

    files = {'photo1': open(boris, 'rb'),
             'photo2': open(biden, 'rb'),
             'randomNumber': 591989248,
             }
    # print(file["photo1"].read())

    url = get_url()
    test_url = 'https://httpbin.org/post'
    response = requests.post(url, files=files)

    try:
        data = response.text.split("{")
        data = data[1]
        data = data.split(":")[-1]
        data = data.split(",")[-1]
        data = data.replace("\/", "/")
        data = data.replace('"}', '')
        decoded_data = pybase64.b64decode(data)
        img_file = open(f"{directory}/d.jpeg", 'wb')
        img_file.write(decoded_data)
        img_file.close()
    except requests.exceptions.RequestException:
        print(response.text)