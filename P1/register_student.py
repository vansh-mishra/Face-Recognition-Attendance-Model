
import os
import cv2

print(cv2.data.haarcascades)
DATASET_DIR = "person_a/dataset"
CASCADE_PATH = "person_a/haarcascade_frontalface_default.xml"

IMAGE_COUNT = 50
os.makedirs(DATASET_DIR, exist_ok=True)

student_id = input("Enter Student ID: ").strip()
student_name = input("Enter Student Name: ").strip()

if not student_id or not student_name:
    print("Student ID and Name are required.")
    exit()


student_folder = os.path.join(DATASET_DIR, student_id)
os.makedirs(student_folder, exist_ok=True)



face_detector = cv2.CascadeClassifier(CASCADE_PATH)

if face_detector.empty():
    print("Error: Haar Cascade file could not be loaded.")
    exit()

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()


print("\nRegistration started.")
print("Look directly at the camera.")
print("Press 'q' to stop.\n")


count = 0


while True:

    ret, frame = camera.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        face = gray[y:y + h, x:x + w]

        if count < IMAGE_COUNT:

            filename = os.path.join(
                student_folder,
                f"{student_id}_{count + 1}.jpg"
            )

            cv2.imwrite(filename, face)

            count += 1

            print(f"Captured image {count}/{IMAGE_COUNT}")

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
        print("\nRegistration completed successfully.")
        break

    if cv2.waitKey(1) & 0xFF == ord("q"):
        print("\nRegistration stopped by user.")
        break


camera.release()
cv2.destroyAllWindows()

print(f"\nStudent: {student_name}")
print(f"Student ID: {student_id}")
print(f"Images captured: {count}")
print(f"Dataset location: {student_folder}")