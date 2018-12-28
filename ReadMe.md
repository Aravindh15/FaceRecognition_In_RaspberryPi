# FaceRecognition_In_RaspberryPi
Author:[YuHang Gong](759076276@qq.com),[Tong Yun](1325695163@qq.com),[Han Zhang](1714402938@qq.com),[Yan Wang](dieqi317@gmail.com),[Zhen Bi] (467665083@qq.com) <br>
Date: 2018 12 28 <br>
## Introduction
The program use Raspberry Pi to recognize face and match faces in Database <br>
IF missmatching,the red LED will shine;if matching, the green LED will shine and  the buzzer will ring. <br>
We reference to this project [Dlib_face_recognition_from_camera](https://github.com/coneypo/Dlib_face_recognition_from_camera ) .Some modifications have been made to the recognition algorithm.Then we transplant it to raspberry pi and finish the I/O design.

## Method
After collecting facial features, begin recognize:
```
$ python3 face_reco_from_camera.py
```

## Details
### I/O Connection
We will use such I/O:

- Raspberry Pi
- 15Pins camera
- 3 LED module
- Active buzzer

We assign pin like that:

- GPIO.1 (pin 12) for buzzer
- GPIO.0 (pin 11) for led_red
- GPIO.2 (pin 13) for led_yellow
- GPIO.3 (pin 15) for led_green

### Code
The more details you can see from code.


