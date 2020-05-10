# CameraModule

Camera interface for desktop user. 
One can click picture and record video using front camera(default) of your machine.
If you want to use external camera, then you have to make simple change in code.
line 4
video=cv2.VideoCapture(0)
change 0 to 1 or 2 or 3, according to which external device you want to use.
