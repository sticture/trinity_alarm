from trinity_requests import Sender
import json
import requests


def send_alarm(payload):
    url = "https://tiothub/HTTPProtAdaptorService/data/services/pushData"

#     payload = json.dumps({
#     "deviceId":"1",
#     "eventTime":"1562079524",
#     "alertMessage":"Object Detection",
#     "eventType ":"315",
#     "severity":"P1",
#     "geocoordinates":{
#         "latitude":12.12332,
#         "longitude":"77.2222",
#         "location":"Shivajinagar,Banglore"
#     },
#     "visualInfo":{
#         "imageUrl":[
#             "http://14.53.45.23:68/img1.jpg",
#             "http://14.53.45.23:68/img2.jpg"
#         ],
#         "videoUrl":[
#             "http://14.53.45.23:68/video1.mp4",
#             "http://14.53.45.23:68/video2.mp4"
#         ]
#     },
#     "objectDetails ":{
#         "vehicleNumber":"KA12 2244",
#         "type ":"CAR",
#         "colour":"9538512588",
#         "listedAs":"Theft",
#         "images":[
#             "http://14.53.45.23:68/img1.jpg",
#             "http://14.53.45.23:68/img2.jpg"
#         ]
#     }
# })
    headers = {
        'Content-Type': 'application/json',
        'deviceId': '00-18-8A-34-06-A1'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    return response


