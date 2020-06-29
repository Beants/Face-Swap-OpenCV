# 换脸程序
# Face-Swap-OpenCV 

![face swap sample](https://raw.githubusercontent.com/BruceMacD/Face-Swap-OpenCV/master/images/face_swapped.png)

This is a basic face-swap implementation using OpenCV. Check out the code for a step-by-step explanation.


## 使用（Usage）

* 命令行运行
    ```
    ./face_swap.py -i data/headshot1.jpg -i data/headshot2.jpg
    ```
* web 运行
    ```
    ./app.py
    ```
## Requirements
[requirements.txt](./requirements.txt)
* 安装依赖
    ```
    pip install -r requirement.txt
    ```
## Sources
> Fork form https://github.com/BruceMacD/Face-Swap-OpenCV

Based on the work of Satya Mallick

https://www.learnopencv.com/face-swap-using-opencv-c-python/

Facial landmarks

https://www.pyimagesearch.com/2017/04/03/facial-landmarks-dlib-opencv-python/

Head shot 1

https://www.pexels.com/photo/adult-attractive-beautiful-beauty-415829/

Head shot 2

https://www.pexels.com/photo/man-wearing-black-zip-up-jacket-near-beach-smiling-at-the-photo-736716/

![delauney triangulation](https://github.com/BruceMacD/Face-Swap-OpenCV/blob/master/images/delauney_landmarks.png)
