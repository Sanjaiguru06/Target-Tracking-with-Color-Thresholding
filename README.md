# Target Tracking Using Color Thresholding

## Abstract

This project presents a real-time target tracking system based on color thresholding techniques in computer vision. The system identifies and tracks objects of interest by segmenting specific color ranges in the HSV color space and extracting the target's position from video frames. The implementation demonstrates a computationally efficient approach for object tracking without requiring machine learning models, making it suitable for resource-constrained environments and real-time applications.

## Introduction

Object tracking is a fundamental task in computer vision with applications in robotics, surveillance, automation, and human-computer interaction. This project investigates the use of color-based segmentation for detecting and tracking a target in real time.

By utilizing HSV color thresholding, the system isolates objects of a predefined color range and tracks their movement across consecutive frames. The approach provides a simple yet effective solution for scenarios where the target can be distinguished from its surroundings based on color characteristics.

## Objectives

- Develop a real-time target tracking system using computer vision techniques.
- Implement color-based object detection using HSV thresholding.
- Analyze the effectiveness of color segmentation for target localization.
- Evaluate the performance of the tracking system under varying environmental conditions.

## Methodology

The tracking process consists of the following stages:

1. Acquisition of video frames from a camera source.
2. Conversion of image frames from BGR to HSV color space.
3. Application of lower and upper HSV threshold values to generate a binary mask.
4. Noise reduction using image processing techniques.
5. Detection of object contours from the segmented image.
6. Extraction of target coordinates and tracking information.
7. Visualization of the detected target in the video stream.

## Technologies Used

- Python
- OpenCV
- NumPy

## Implementation

The system processes incoming video frames and identifies regions that match predefined color ranges. Contour detection is applied to the segmented image to locate the target object. The largest valid contour is selected as the target, and its position is continuously updated across frames to achieve real-time tracking.

The implementation emphasizes computational efficiency while maintaining reliable detection and tracking performance.

## Results

The developed system successfully detects and tracks colored objects in real time under controlled lighting conditions. Experimental observations indicate that tracking accuracy is influenced by:

- Illumination changes
- Background color interference
- Camera resolution
- HSV threshold selection

The system demonstrates effective performance for applications where target colors are distinguishable from the surrounding environment.

## Applications

- Robotics and autonomous systems
- Industrial object monitoring
- Human-computer interaction
- Educational computer vision projects
- Surveillance and tracking systems

## Future Enhancements

Potential improvements include:

- Multi-object tracking
- Adaptive threshold selection
- Kalman filter-based motion prediction
- Deep learning-based object detection integration
- Improved robustness under dynamic lighting conditions

## Research Contribution

This project explores the application of classical computer vision techniques for real-time target tracking. The study demonstrates that color thresholding can serve as a lightweight and efficient alternative to more computationally intensive tracking approaches in environments where color characteristics provide sufficient target discrimination.

## Author

**Sanjai Guru**  
B.Tech Computer Science and Engineering (Artificial Intelligence and Machine Learning)  
SRM Institute of Science and Technology

## License

This project is intended for academic, research, and educational purposes.
