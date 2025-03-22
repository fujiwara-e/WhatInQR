import cv2
from pyzbar.pyzbar import decode
import numpy as np
import subprocess
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera")
    exit()

detected_codes = set()
while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not read frame")
        break

    decoded_objects = decode(frame)

    for obj in decoded_objects:
        qr_data = obj.data.decode('utf-8')

        if qr_data not in detected_codes:
            detected_codes.add(qr_data)
            print("Contents:", qr_data)
        points = obj.polygon
        if len(points) == 4:  
            pts = np.array([[p.x, p.y] for p in points], dtype=np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        n_points = obj.polygon
        x, y = n_points[0].x, n_points[0].y  
        x, y = int(x), int(y)  
        cv2.putText(frame, qr_data, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()