from trinity_requests import Sender
import json
import requests

# sender = Sender()
# alert = {
#     'alert_type': '208',
#     'time': '0',
#     'img_url': '0',
#     'video_url': '0',
#     'data': {
#     }
# }
# sender.send(alert)


def send_alarm():
    url = "https://tiothub/HTTPProtAdaptorService/data/services/pushData"

    payload = json.dumps({
        "cameraId": "1",
        "cameraNumber": "00-18-8A-34-06-A1",
        "pointName": "Cam-0",
        "eventTime": "2/16/2018 11:37:55 AM",
        "alertMessage": "Road blockage",
        "alertType": 0,
        "eventDetails1": "DVM Motion Detected(MiskStreet1EntryCamera)",
        "eventDetails2": "siteid=1,cameraid=1,clipkey={8ad8e7c5-c86e-4f2f-8727-8882e4f8fd25}",
        "eventDetails3": "Motion",
        "eventDetails4": "Active",
        "eventDetails5": None
    })
    headers = {
        'Content-Type': 'application/json',
        'deviceId': '00-18-8A-34-06-A1'
    }

    response = requests.request("POST", url, headers=headers, data=payload,verify=False)
    return response

print(send_alarm().content)