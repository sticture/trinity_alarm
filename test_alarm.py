from trinity_requests import Sender

sender = Sender()
alert = {
    'alert_type': '208',
    'time': '0',
    'img_url': '0',
    'video_url': '0',
    'data': {
        "name": "test alarm"
    }
}
sender.send(alert)
