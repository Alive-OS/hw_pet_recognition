# hw_pet_recognition

## Packages

### Vision

The package deals with visual information. It is publishing video stream into `/usbcam` topic at rate of 10 images per second.

Optinoally can store the video stream as series of images, in such case check `STORING` and `IMAGE_STORAGE` variables in [camera.py](catkin_ws/src/vision/scripts/camera.py)