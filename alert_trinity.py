import cv2
import time
import requests
from pathlib import Path
from use.trinity_requests import Sender

class VideoWriter:
    def __init__(self, filename, duration):
        self.frame_shape = (640,360)
        self.writer = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 15, self.frame_shape)
        self.duration = duration
        self.start_time = time.time()

    def write(self, frame):
        if time.time() - self.start_time > self.duration:
            self.writer.release()
            return True
        else:
            frame = cv2.resize(frame, self.frame_shape)
            self.writer.write(frame)
            return False

class AlertTrinity:
    def __init__(self):
        self.alerts = []
        self.sender = Sender()

    def _send_alert(self, alert):
        self.sender.send(alert)

    def updateVideo(self, frame):
        alerts_incomplete = []
        for alert in self.alerts:
            if alert['frame'] is None:
                frame = cv2.resize(frame, (640,360))
                cv2.imwrite(alert['img_path'], frame)
                alert['frame'] = True
            isComplete = alert['videoWriter'].write(frame)
            if isComplete:
                self._send_alert(alert)
            else:
                alerts_incomplete.append(alert)
        self.alerts = alerts_incomplete

    def upload_image(self, dir_, frame):
        dir_base = './output/'
        now = time.time()
        alert = {
                'alert_type': dir_,
                'img_path': f'{dir_base}{dir_}/{now}.jpg',
                'video_path': f'None',
                'img_url': f'https://192.168.150.104:8081/output/{dir_}/{now}.jpg',
                'video_url': f'None',
                'time': int(now),
                'frame':True,
                'data':{}
                }
        frame = cv2.resize(frame, (640,360))
        cv2.imwrite(alert['img_path'], frame)
        Path(f"{dir_base}{dir_}/").mkdir(parents=True, exist_ok=True)
        self._send_alert(alert)

    def trigger_alert(self, dir_, duration, data={}):
        dir_base = './output/'
        now = time.time()
        alert = {
                'alert_type': dir_,
                'img_path': f'{dir_base}{dir_}/{now}.jpg',
                'video_path': f'{dir_base}{dir_}/{now}.avi',
                'img_url': f'https://192.168.150.104:8081/output/{dir_}/{now}.jpg',
                'video_url': f'https://192.168.150.104:8081/output/{dir_}/{now}.avi',
                'time': int(now),
                'frame':None,
                'data':data
                }
        Path(f"{dir_base}{dir_}/").mkdir(parents=True, exist_ok=True)
        #duration = max(duration, 5)
        alert['videoWriter'] = VideoWriter(alert['video_path'], duration)
        self.alerts.append(alert)


if __name__ == '__main__':
    print(get_token().content)
    #print(send(1,2))

    #alert = AlertTrinity()
    #cap = cv2.VideoCapture('/home/graymatics/dev/hpe-remote/hydrabad/src/walk.mp4')
    #count = 0
    #while True:
    #    count += 1
    #    _, frame = cap.read()
    #    alert.updateVideo(frame)
    #    if count == 200:
    #        alert.trigger_alert('/home/graymatics/dev/hpe-remote/hydrabad/src/output/', 3)
