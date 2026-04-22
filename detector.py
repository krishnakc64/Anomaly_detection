from ultralytics import YOLO

class AnomalyDetector:
    def __init__(self):
        # Load pretrained YOLOv8 model
        self.model = YOLO("yolov8n.pt")

        # anomaly class
        self.anomaly_class = "bottle"

    def detect(self, frame):
        results = self.model(frame, verbose=False)

        anomaly = False
        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                name = self.model.names[cls_id]
                conf = float(box.conf[0])

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                detections.append((name, conf, (x1, y1, x2, y2)))

                if name == self.anomaly_class:
                    anomaly = True

        return anomaly, detections