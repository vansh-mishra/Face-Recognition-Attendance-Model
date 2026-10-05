import cv2
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"
CASCADE_PATH = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"

DATASET_DIR.mkdir(exist_ok=True)

# Load face detector
face_detector = cv2.CascadeClassifier(str(CASCADE_PATH))

if face_detector.empty():
    print("Error: Haar Cascade not loaded.")
    exit()

# Student details
student_id = input("Enter Student ID: ").strip()
student_name = input("Enter Student Name: ").strip()

student_folder = DATASET_DIR / student_id
student_folder.mkdir(exist_ok=True)

# Start webcam
camera = cv2.VideoCapture(0)

count = 0
IMAGE_COUNT = 50

while True:
    ret, frame = camera.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]

        filename = student_folder / f"{student_id}_{count + 1}.jpg"
        cv2.imwrite(str(filename), face)

        count += 1

        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Images: {count}/{IMAGE_COUNT}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Student Registration", frame)

    if count >= IMAGE_COUNT:
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()

print(f"\nRegistration completed for {student_name}")
print(f"Images saved: {count}")
print(f"Location: {student_folder}")