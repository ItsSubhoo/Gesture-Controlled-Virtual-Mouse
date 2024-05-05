# Gesture Controlled Virtual Mouse with OpenCV and PyAutoGUI
A virtual mouse controller using computer vision, MediaPipe, and PyAutoGUI to track hand movements and interact with a computer without a physical mouse.

## Overview
This project utilizes the webcam to track hand movements in real-time and translates them into cursor movements on the screen. It uses OpenCV for image processing, MediaPipe for hand tracking, and PyAutoGUI for interacting with the mouse. The project features different gestures to control the mouse and perform clicks.

## Features
- Mouse Movement: The cursor follows the position of the index finger in real-time.
- Clicking: Bringing the index and middle fingers together performs a mouse click.
- Volume Control: (Not implemented in the provided code) Control system volume with gestures.
- Smooth Cursor Movement: Smoothes the cursor movement to reduce jitter.
- Getting Started

## Prerequisites
- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI
- NumPy

## Installation

1. Clone the repository
```bash
git clone <YOUR-REPO-URL>
cd <YOUR-REPO-NAME>
```
2. Install dependencies
```bash
pip install opencv-python mediapipe pyautogui numpy 
```
3. Run the script
 ```bash
   python hand_mouse.py
```

## Usage
- Mouse Movement: Raise only the index finger. The cursor will follow its position.
- Clicking: Raise the index and middle fingers. If they are close together, the script simulates a click.
- Volume Control: This feature is mentioned but not fully implemented in the provided code.
- Code Overview
- The script captures webcam input and uses MediaPipe to track hand landmarks. It determines which fingers are raised and performs actions accordingly. The main loop checks for gestures and interacts with the system - 
- mouse through PyAutoGUI.

## Key variables and sections:

- frangex and frangey: Define the region of interest within the webcam feed.
- smoothinig: Controls the smoothness of cursor movement.
-    indexup and midup: Check whether the index and middle fingers are raised.
  -   Cursor movement logic: Translates finger positions to screen coordinates.
  -  Click detection: Checks the distance between the index and middle fingers to determine when to click.
## Contributions
Contributions are welcome. If you would like to contribute, please fork the repository and submit a pull request. Issues and suggestions are also welcome
