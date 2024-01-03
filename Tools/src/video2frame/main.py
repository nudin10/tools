import cv2
from time import time
from uuid import uuid4
from utils.common import get_project_root_path

def FrameCapture(video_name: str, frame_rate: int):
    rand = str(uuid4())
    path =  get_project_root_path() / "src" / "video2frame"
    output_path = path / "output" / f"{rand}"
    output_path.mkdir(exist_ok=True)
    input_path = path / "input" / video_name
    cap = cv2.VideoCapture(str(input_path))
    count = 0
    prev = 0
    capturing = True

    while capturing:
        time_elapsed = time() - prev
        capturing, image = cap.read()
        if time_elapsed > 1./frame_rate:
            prev = time()
        cv2.imwrite(str(output_path / f"frame_{count}.jpg"),image)
        count += 1
