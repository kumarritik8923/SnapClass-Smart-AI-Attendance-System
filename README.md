# SnapClass: AI-Powered Smart Attendance System

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://snapclass-rkc.streamlit.app/)

## Overview
**SnapClass** is a full-stack, multi-modal Artificial Intelligence application designed to eliminate the friction of manual attendance tracking in educational institutions. By leveraging advanced Computer Vision (Facial Recognition) and Natural Language Processing (Zero-Shot Voice Cloning), SnapClass allows educators to mark attendance for an entire classroom instantly using group photos or continuous audio streams. 

Built with a modular, component-based architecture, it features distinct portals for Teachers and Students, secure cloud database integration, and real-time analytics.

---

## Live Demo
Test the live application here: **[SnapClass Web App](https://snapclass-rkc.streamlit.app/)**

*(Note: For the best results, ensure you are in a well-lighted room when registering your face, and record at least 5 seconds of clear audio for voice registration.)*

---

## ✨ Key Features

### AI-Based Group Attendance
- Detects and recognizes multiple students from a single classroom/group image.
- Eliminates sequential biometric attendance marking.
- Automates attendance workflow.

### Face Recognition Authentication
- Student login using facial recognition.
- Face embeddings generated using deep learning techniques.
- Automatic identification of registered users.

### Optional Voice Verification
- Voice embedding support for additional biometric verification.
- Can be used as a secondary authentication layer.

### QR-Based Course Enrollment
- Quick enrollment into subjects using QR codes.
- Reduces manual enrollment overhead.

### Attendance Dashboard
- Subject-wise attendance tracking.
- Total vs attended lectures visualization.
- Interactive student dashboard.

### Real-Time Registration
- New users can register directly through camera input.
- Automatic profile creation using biometric data.

---

## 🛠️ Tech Stack

**Frontend & UI**
*   [Streamlit](https://streamlit.io/): Core application framework.
*   **Custom CSS:** Implemented via Streamlit markdown for a polished, responsive UI (custom fonts, modern inputs, custom cards).

**Backend & Database**
*   [Supabase](https://supabase.com/): PostgreSQL database hosting and API.
*   **Bcrypt:** For secure teacher password hashing.

**Artificial Intelligence Engines**
*   **Computer Vision:** `dlib`, `face_recognition_models`, `scikit-learn` (Support Vector Machine classification).
*   **Audio Processing:** `resemblyzer` (VoiceEncoder), `librosa` (Audio segmentation and processing).

**Data & Utility**
*   `numpy` & `pandas`: Data manipulation and dataframe rendering.
*   `Pillow`: Image processing.
*   `segno`: QR Code generation.

---

## 🔄 System Workflow

The following flowchart illustrates the core lifecycle of an attendance session:
```text
[Teacher Creates Subject] ---> Generates QR Code/Join Link
                                      |
                                      v
[Student Registers] ---------> Scans QR Code ---> [Enrolled in Subject]
(Face + Voice Saved)
                                      |
                                      v
[Teacher Initiates Class] ---> Uploads Group Photo(s) OR Records Audio
                                      |
                                      v
[AI Processing Pipeline Triggered]
      ├── Face Pipeline:
      │      Face Detection
      │      -> Face Embedding Extraction
      │      -> Embedding Similarity Comparison
      │      -> Student Identification
      │
      └── Voice Pipeline:
             Audio Preprocessing using librosa
             -> Voice Embedding Generation using Resemblyzer
             -> Similarity Matching
                                      |
                                      v
[Confidence Review] ---------> Teacher reviews AI output via Interactive Dialog
                                      |
                                      v
[Database Sync] -------------> Logs saved securely to Supabase Attendance Tables
