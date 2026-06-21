# 🎯 Target Tracking with Color Thresholding

## 📌 Overview

This project implements a real-time target tracking system using color thresholding techniques in OpenCV. The system detects and tracks objects of a specified color from a live video stream or recorded video by applying image processing and computer vision techniques.

The project was developed as part of an internship and research work to explore efficient object detection and tracking methods using color segmentation.

---

## 🚀 Features

- Real-time object detection and tracking
- Color-based target identification
- HSV color space thresholding
- Noise reduction using image processing techniques
- Bounding box visualization around detected targets
- Lightweight and efficient implementation

---

## 🛠️ Technologies Used

- Python
- OpenCV
- NumPy

---

## 📖 Working Principle

1. Capture video frames from a webcam or video source.
2. Convert the frame from BGR color space to HSV color space.
3. Apply predefined HSV thresholds to isolate the target color.
4. Generate a binary mask for the detected color.
5. Perform image processing operations to remove noise.
6. Detect contours of the target object.
7. Draw bounding boxes and track the object's movement in real time.

---

## 📂 Project Structure

```
Target-Tracking-with-Color-Thresholding/
│
├── main.py
├── requirements.txt
├── README.md
├── assets/
│   ├── sample_output.png
│   └── demo_video.mp4
└── src/
    └── tracking_modules.py
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/Target-Tracking-with-Color-Thresholding.git
cd Target-Tracking-with-Color-Thresholding
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install opencv-python numpy
```

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

The webcam will open, and the system will begin detecting and tracking objects matching the selected color range.

Press `q` to exit.

---

## 🎯 Applications

- Surveillance systems
- Robotics navigation
- Human-computer interaction
- Industrial automation
- Educational computer vision projects
- Research in object tracking techniques

---

## 📊 Results

The system successfully tracks colored objects in real time under controlled lighting conditions. Performance may vary depending on:

- Lighting environment
- Camera quality
- Object color similarity in the background
- HSV threshold selection

---

## 🔬 Research Contribution

This project explores the effectiveness of color thresholding for target tracking applications. The implementation demonstrates how HSV-based segmentation can be used as a computationally efficient alternative to complex machine learning models for specific tracking tasks.

---

## 📈 Future Improvements

- Multi-object tracking
- Dynamic color selection
- Kalman Filter integration
- Deep Learning-based object detection
- Tracking performance optimization
- GUI for color calibration

---

## 👨‍💻 Author

**Sanjai Guru**
B.Tech CSE (AI & ML)
SRM Institute of Science and Technology

---

## 📜 License

This project is intended for educational, research, and learning purposes.
