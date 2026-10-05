# 🤖 SmartVision AI
## AI-Based Face Recognition Attendance System

> An intelligent attendance management system that uses computer vision and machine learning to automatically recognize registered students and mark their attendance in real time.

---

## 📌 Project Overview

**SmartVision AI** is an AI-powered face recognition attendance system developed as a B.Tech Artificial Intelligence and Machine Learning semester project.

The system uses a webcam to detect and recognize registered students. Once a student is successfully identified, the system automatically records their attendance along with the date and time.

The project combines:

- Computer Vision
- Machine Learning
- Image Processing
- Python
- OpenCV
- Flask
- SQLite
- HTML/CSS/JavaScript

The primary goal is to replace manual attendance processes with a faster, automated, and scalable attendance management solution.

---

# 🎯 Problem Statement

Traditional attendance systems require teachers to manually call student names or maintain attendance records.

This process can be:

- Time-consuming
- Error-prone
- Difficult to maintain
- Vulnerable to proxy attendance
- Difficult to analyze over time

SmartVision AI addresses these problems by automatically identifying students using facial recognition and recording attendance digitally.

---

# 💡 Proposed Solution

The proposed system follows this workflow:

```text
Student Registration
        ↓
Face Detection
        ↓
Face Dataset Generation
        ↓
Model Training
        ↓
Real-Time Face Recognition
        ↓
Student Identification
        ↓
Attendance Verification
        ↓
Database Storage
        ↓
Dashboard / Attendance Report
```

---

# 🚀 Key Features

### 👤 Student Registration

- Register students using their basic information.
- Capture multiple face images through a webcam.
- Automatically detect and crop the face.
- Convert images to grayscale.
- Store generated face samples for model training.

### 🧠 Face Recognition

- Detect faces using OpenCV.
- Recognize registered students using LBPH.
- Display the recognized student's name/ID.
- Handle unknown faces.
- Use recognition confidence/distance thresholds.

### 📋 Automated Attendance

- Automatically mark attendance after successful recognition.
- Record date and time.
- Prevent duplicate attendance for the same student on the same day.

### 🗄️ Database Management

The system stores:

- Student information
- Student ID
- Name
- Email
- Branch
- Attendance date
- Attendance time
- Attendance status

### 📊 Dashboard

The dashboard provides:

- Total students
- Present students
- Absent students
- Attendance percentage
- Attendance records
- Search/filter functionality

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │       Webcam        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Face Detection    │
                    │   OpenCV Haar       │
                    │      Cascade        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Image Processing   │
                    │ Crop + Grayscale    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Face Recognition  │
                    │        LBPH         │
                    └──────────┬──────────┘
                               │
                    ┌──────────┴──────────┐
                    │                     │
                    ▼                     ▼
              Recognized              Unknown
                    │                     │
                    ▼                     ▼
             Check Database          Reject
                    │
                    ▼
          ┌─────────────────────┐
          │ Attendance Database │
          │       SQLite        │
          └──────────┬──────────┘
                     │
                     ▼
          ┌─────────────────────┐
          │  Flask Dashboard    │
          └─────────────────────┘
```

---

# 🧠 Machine Learning Approach

## 1. Face Detection

The system first detects faces from the webcam stream using the **Haar Cascade Classifier**.

```text
Webcam Frame
     ↓
Convert to Grayscale
     ↓
Haar Cascade
     ↓
Face Bounding Box
```

The detected face is then cropped from the original frame.

---

## 2. Image Preprocessing

Each detected face is processed before training.

```text
Original Image
      ↓
Face Detection
      ↓
Face Cropping
      ↓
Grayscale Conversion
      ↓
Image Normalization
      ↓
Training Dataset
```

---

## 3. Face Recognition using LBPH

The project uses **Local Binary Pattern Histogram (LBPH)** for face recognition.

LBPH analyzes local texture patterns of a face and generates feature histograms that can be compared with trained face samples.

Simplified workflow:

```text
Face Image
    ↓
Divide into Local Regions
    ↓
Calculate Local Binary Patterns
    ↓
Generate Histograms
    ↓
Compare with Trained Model
    ↓
Predict Student ID
```

---

# 🧩 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Face detection and image processing |
| Haar Cascade | Face detection |
| LBPH | Face recognition |
| NumPy | Numerical operations |
| Flask | Backend web framework |
| SQLite | Database |
| HTML | Web structure |
| CSS | Web styling |
| JavaScript | Frontend interaction |
| Chart.js | Data visualization |
| Git | Version control |
| GitHub | Collaboration and project management |

---

# 📂 Project Structure

```text
SmartVision-AI/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── face_detection/
│   ├── capture_faces.py
│   └── detector.py
│
├── face_recognition/
│   ├── train_model.py
│   ├── recognize.py
│   └── trainer.yml
│
├── database/
│   ├── database.py
│   └── attendance.db
│
├── templates/
│   ├── index.html
│   ├── register.html
│   ├── attendance.html
│   └── dashboard.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── dataset/
├── tests/
└── reports/
```

---

# 👥 Team Responsibilities

| Team Member | Responsibility |
|---|---|
| Person A | Face Detection & Student Registration |
| Person B | ML Face Recognition & Model Training |
| Person C | Database & Attendance Management |
| Person D | Flask Web Application & Dashboard |

### Person A — Face Detection & Registration

- Webcam integration
- Face detection
- Face cropping
- Grayscale conversion
- Dataset generation
- Student registration

### Person B — ML & Face Recognition

- LBPH model training
- Model serialization
- Real-time face recognition
- Unknown-face detection
- Recognition threshold tuning

### Person C — Database & Attendance

- SQLite database
- Student table
- Attendance table
- CRUD operations
- Duplicate attendance prevention

### Person D — Flask & Dashboard

- Flask application
- Frontend interface
- Dashboard
- Attendance visualization
- Backend integration

---

# 🔗 Module Dependencies

```text
Person A
   │
   │ Face Dataset
   ▼
Person B
   │
   │ Recognized Student ID
   ▼
Person C
   │
   │ Attendance Records
   ▼
Person D
   │
   ▼
Final Dashboard
```

Development should still happen in parallel using mock/test data so that one unfinished module does not block the entire team.

---

# 🗃️ Database Design

## Students Table

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT,
    branch TEXT
);
```

## Attendance Table

```sql
CREATE TABLE attendance (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    name TEXT,
    date TEXT,
    time TEXT,
    status TEXT
);
```

---

# 🔄 Attendance Logic

```text
Recognized Student
       ↓
Get Student ID
       ↓
Check Today's Attendance
       ↓
Already Present?
     /       \
   YES       NO
   ↓          ↓
 Ignore     Insert Record
```

This prevents multiple attendance entries for the same student on the same day.

---

# 🛠️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/vansh-mishra/SmartVision-AI.git
cd SmartVision-AI
```

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📦 Requirements

Example:

```text
opencv-contrib-python
numpy
Flask
Pillow
```

Generate the requirements file using:

```bash
pip freeze > requirements.txt
```

---

# ▶️ Running the Project

Start the Flask application:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000
```

---

# 📝 Student Registration Workflow

```text
1. Open Registration Page
          ↓
2. Enter Student Information
          ↓
3. Start Webcam
          ↓
4. Detect Face
          ↓
5. Capture Multiple Samples
          ↓
6. Store Dataset
          ↓
7. Train Model
```

---

# 🎥 Attendance Workflow

```text
1. Start Attendance
          ↓
2. Webcam Starts
          ↓
3. Detect Face
          ↓
4. Extract Face
          ↓
5. LBPH Recognition
          ↓
6. Identify Student
          ↓
7. Check Database
          ↓
8. Mark Attendance
          ↓
9. Display Result
```

---

# 🧪 Testing

### Test Case 1: Registered Student

**Input:** Registered student's face

**Expected:** Student recognized and attendance marked.

### Test Case 2: Duplicate Attendance

**Input:** Same student appears again.

**Expected:** Student recognized but duplicate attendance prevented.

### Test Case 3: Unknown Student

**Input:** Unregistered face.

**Expected:** `Unknown Face` and attendance is not marked.

### Test Case 4: Multiple Students

**Input:** Multiple registered students.

**Expected:** Each student is recognized individually and attendance is recorded correctly.

### Test Case 5: Different Lighting

**Input:** Face under different lighting conditions.

**Expected:** System attempts recognition without crashing.

---

# 🔐 Privacy & Security Considerations

Facial data is sensitive and should be handled carefully.

- Do not upload facial datasets to public GitHub repositories.
- Keep `dataset/` in `.gitignore`.
- Keep database files out of public repositories where appropriate.
- Collect facial data only with appropriate consent.
- Use anonymized/test data when demonstrating publicly.
- Restrict access to registered student information.

---

# ⚠️ Current Limitations

- Recognition accuracy can decrease under poor lighting.
- Extreme face angles may affect recognition.
- Face masks may reduce accuracy.
- LBPH is less powerful than modern deep-learning face recognition models.
- The system is primarily designed for controlled classroom environments.
- A basic webcam can affect recognition quality.

---

# 🔮 Future Scope

## Advanced Face Recognition

Possible upgrades:

- FaceNet
- ArcFace
- DeepFace
- InsightFace

## Anti-Spoofing

Detect whether the camera is seeing:

```text
Real Person
     vs
Photo / Video
```

## Cloud Database

Possible options:

- PostgreSQL
- MySQL
- Supabase
- Firebase

## Advanced Dashboard

Add:

- Attendance percentage
- Monthly attendance
- Student-wise analytics
- Department-wise analytics
- Attendance trends
- CSV/PDF export

## Notifications

Automatically send:

- Low attendance alerts
- Daily attendance reports
- Absence notifications

## Deployment

The system can eventually be deployed using:

- Docker
- Cloud hosting
- Cloud database
- CI/CD pipeline

---

# 📊 Expected Output

```text
┌──────────────────────────────────────┐
│       SMART ATTENDANCE SYSTEM        │
├──────────────────────────────────────┤
│                                      │
│  Total Students       60             │
│  Present              47             │
│  Absent               13             │
│  Attendance           78.3%          │
│                                      │
├──────────────────────────────────────┤
│ ID     Name       Time      Status   │
│ 101    Vansh      09:02     Present  │
│ 102    Rahul      09:04     Present  │
│ 103    Aman       09:05     Present  │
│                                      │
└──────────────────────────────────────┘
```

---

# 📈 Project Development Roadmap

```text
Phase 1  → Project Setup
     ↓
Phase 2  → Face Detection
     ↓
Phase 3  → Dataset Generation
     ↓
Phase 4  → Model Training
     ↓
Phase 5  → Face Recognition
     ↓
Phase 6  → Database Integration
     ↓
Phase 7  → Flask Dashboard
     ↓
Phase 8  → Testing
     ↓
Phase 9  → Documentation
     ↓
Phase 10 → Final Deployment
```

---

# 🧑‍💻 GitHub Commit Strategy

Use meaningful commit messages.

```text
feat: add face detection module
feat: implement face sample capture
feat: implement LBPH training
feat: add real-time face recognition
feat: create attendance database
feat: prevent duplicate attendance
feat: create Flask dashboard
feat: integrate recognition with attendance
test: validate complete attendance workflow
docs: update project documentation
```

Avoid meaningless commit messages such as:

```text
final
final2
new
update
working
last commit
final_final
```

---

# 📌 Minimum Viable Product

The first working version must contain:

- [x] Student registration
- [x] Face detection
- [x] Face dataset generation
- [x] Model training
- [x] Face recognition
- [x] Unknown-face handling
- [x] Attendance marking
- [x] Duplicate prevention
- [x] SQLite database
- [x] Basic dashboard

Advanced features should only be added after the complete MVP is stable.

---

# 🎓 Academic Relevance

This project demonstrates practical knowledge of:

### Artificial Intelligence

- Computer Vision
- Pattern Recognition
- Machine Learning

### Data Processing

- Image preprocessing
- Feature extraction
- Dataset management

### Software Development

- Python
- Flask
- Backend development
- Database management

### Engineering Practices

- Git
- GitHub
- Modular architecture
- Testing
- Documentation
- Team collaboration

---

# 🧠 Learning Outcomes

After completing this project, the team will understand:

1. How face detection works.
2. How face datasets are generated.
3. How LBPH-based face recognition works.
4. How to connect ML models with applications.
5. How to store attendance using databases.
6. How Flask can serve an ML application.
7. How to design modular software.
8. How to collaborate using Git and GitHub.
9. How to test an AI-based application.
10. How to document and present an AIML project.

---

# 🚀 Future Vision

SmartVision AI can evolve from a basic attendance system into a complete **AI-powered classroom analytics platform**.

```text
Face Recognition
       +
Attendance Analytics
       +
Anti-Spoofing
       +
Student Performance Data
       +
AI Reports
       +
Cloud Infrastructure
       =
Smart Classroom Analytics Platform
```

---

# 👨‍💻 Team

**Project:** SmartVision AI  
**Domain:** Artificial Intelligence & Machine Learning  
**Project Type:** B.Tech Semester Project

### Team Members

- Person A - Face Detection & Registration
- Person B - ML & Face Recognition
- Person C - Database & Attendance
- Person D - Flask & Dashboard

---

# 📄 License

This project is developed for academic and educational purposes.

Before using the system with real people's biometric data, obtain appropriate consent and follow applicable privacy and data-protection requirements.

---

# ⭐ Acknowledgement

This project uses open-source technologies including Python, OpenCV, Flask, NumPy, SQLite, HTML, CSS, and JavaScript.

---

## 💡 Project Tagline

> **"See. Recognize. Record. Simplify Attendance."**
