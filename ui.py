import cv2
import time
from detector import AnomalyDetector

def run_app():
    detector = AnomalyDetector()

    cap = cv2.VideoCapture(0)  # USB camera

    last_save = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        anomaly, detections = detector.detect(frame)

        # Draw detections
        for name, conf, (x1, y1, x2, y2) in detections:
            color = (0, 0, 255) if name == "bottle" else (0, 255, 0)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame,
                        f"{name} {conf:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        color,
                        2)

        # UI overlay
        if anomaly:
            cv2.putText(frame,
                        "⚠ ANOMALY DETECTED: BOTTLE",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 0, 255),
                        3)

            # Save image every 3 seconds max
            now = time.time()
            if not hasattr(run_app, "last_save"):
                run_app.last_save = 0

            if now - run_app.last_save > 3:
                filename = f"anomaly_{int(now)}.jpg"
                cv2.imwrite(filename, frame)
                print("Saved:", filename)
                run_app.last_save = now

        else:
            cv2.putText(frame,
                        "SYSTEM NORMAL",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        3)

        cv2.imshow("Anomaly Detector UI", frame)

        # press q to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    run_app()