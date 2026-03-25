import cv2
import os

def extract_frame(video_path):

    cap = cv2.VideoCapture(video_path)

    success, frame = cap.read()

    if success:
        frame_path = "static/uploads/frame.jpg"
        cv2.imwrite(frame_path, frame)

        cap.release()
        return frame_path

    cap.release()
    return None