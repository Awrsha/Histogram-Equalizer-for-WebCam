<h1 align="center">
  <br>
  <a href="https://github.com/Awrsha/RoboticSoccerPlayGround"><img src="https://s6.uupload.ir/files/hsl_0dhk.png" alt="HSL" width="200"></a>
  <br>
  Humanoid Soccer Robot 
  <br>
</h1>

<b><h4 align="center">.:: Histogram Equalizer for WebCam ::.</h4></b>

<p align="center">
<a href="https://github.com/Awrsha/Histogram-Equalizer-for-WebCam"><img src="https://img.shields.io/badge/Version-1.2.1-brightgreen" alt="HSL" width="100"></a>
<a href="https://github.com/Awrsha/Histogram-Equalizer-for-WebCam"><img src="https://img.shields.io/badge/Platform-linux--64 -blue" alt="HSL" width="130"></a>
<a href="https://github.com/Awrsha/Histogram-Equalizer-for-WebCam"><img src="https://img.shields.io/badge/Platform-windows-cyan" alt="HSL" width="130"></a>
<a href="https://github.com/Awrsha/Histogram-Equalizer-for-WebCam/blob/main/LICENSE.md"><img src="https://img.shields.io/badge/LICENSE-MIT-red" alt="HSL" width="110"></a>
<a href="https://github.com/Awrsha/Histogram-Equalizer-for-WebCam/network/members"><img src="https://img.shields.io/badge/Developers-1-lightgrey" alt="HSL" width="100"></a>
</p>
<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>

# Histogram Equalization for Image

This is a simple implementation of webcam histogram equalization using C++ and Python with NumPy. Histogram equalization is a technique used in image processing to adjust the contrast of an image by redistributing the pixel values. The technique works by mapping the original pixel values to new values that are more evenly distributed across the available range of values.

## Languages  
<code>
<img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/python/python-original-wordmark.svg" width="50" height="50" /> <img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/vscode/vscode-original-wordmark.svg" width="50" height="50"/><img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/numpy/numpy-original.svg" width="50" height="50"/><img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/opencv/opencv-original-wordmark.svg" width="50" height="50" /> <img align="center" src="https://github.com/devicons/devicon/blob/v2.15.1/icons/pycharm/pycharm-original.svg" width="50" height="50"/>
</code>

## Requirements

To run this program, you will need:
- A C++ compiler (for the C++ implementation)
- Python 3.x installed on your machine (for the Python implementation)
- NumPy library for Python

## Installation

1. Install Python 3.x from the official website: [https://www.python.org/downloads/ ↗](https://www.python.org/downloads/)
2. Install NumPy library using pip:
   ```
   pip install numpy
   ```
3. Install Matplotlib library using pip:
   ```
   pip install matplotlib
   ```
4. Install OpenCV library using pip:
   ```
   pip install opencv-python
   ```
5. Install a C++ compiler on your machine. For Windows, you can use Visual Studio or MinGW. For Mac or Linux, you can use GCC or Clang.

## Usage

### C++ Implementation

1. Navigate to the `cpp` directory.
2. Compile the `main.cpp` file using your C++ compiler:
   ```
   g++ main.cpp -o webcam
   ```
3. Run the executable file:
   ```
   ./webcam
   ```
4. The program will start capturing frames from your webcam and display the original and equalized images side by side using OpenCV.

### Python Implementation

1. Navigate to the `python` directory.
2. Use the following command to run the program:
   ```
   python webcam_histogram_equalization.py
   ```
3. The program will start capturing frames from your webcam and display the original and equalized images side by side using OpenCV.

## How it Works

The program captures frames from the user's webcam in real-time using OpenCV. Each frame is loaded as a 3-dimensional NumPy array with dimensions (height, width, channels). The program then calculates the histogram of the input image using the NumPy histogram() function. The histogram is a representation of the distribution of pixel values in the image.

The program then applies histogram equalization to the input image by mapping the original pixel values to new values that are more evenly distributed across the available range of values. The mapping function is calculated using the cumulative distribution function (CDF) of the pixel values in the input image. The CDF is calculated using the NumPy cumsum() function.

The program then applies the mapping function to each pixel in the input image to generate a new NumPy array of the same shape, where each pixel has a new value that is more evenly distributed across the available range of values.

The program then displays the original and equalized images side by side using OpenCV.

## Contributing

This is an open-source project and contributions are welcome. To contribute, please fork this repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Developers 👨🏻‍💻
<p align="center">
<a href="https://github.com/Awrsha"><img src="https://avatars.githubusercontent.com/u/89135083?v=4" width="100;" alt="Awrsha Parvizi"/><br /><sub><b>.:: Amir M. Parvizi ::.</b></sub></a>
</p>

## System & Hardware 🛠  
<br> <summary><b>⚙️ Things I use to get stuff done</b></summary> <ul> <li><b>OS:</b> Windows 11</li> <li><b>Laptop: </b>TUF Gaming</li> <li><b>Code Editor:</b> Visual Studio Code - The best editor out there.</li> <li><b>To Stay Updated:</b> Medium, Linkedin and Instagram.</li> <br /> ⚛️ Checkout Our VSCode Configrations <a href="">Here</a>. </ul> <p align="center">💙 If you like my projects, Give them ⭐ and Share it with friends!</p></p><p align="center"><img height="27" src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg" alt="Github Stats" /></p>
