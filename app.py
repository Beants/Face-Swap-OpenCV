#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py.py    
@Contact :   beantsxu@gmail.com
@License :   (C)Copyright 2020-2020, 

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/6/28 5:41 下午   beants      1.0         None
'''
import os

import cv2
from flask import Flask, request, render_template, send_file

#
from components.service import do_swap

#
app = Flask(__name__)

boy_img = cv2.imread("images/boy.jpg")
girl_img = cv2.imread("images/girl.jpg")


@app.route('/')
def hello_world():
    return render_template("index.html")
    # return  'a'


@app.route('/swap', methods=['POST'])
def swap():
    for i in os.listdir('res'):
        if os.path.exists('res/' + i):
            os.remove('res/' + i)
    img = request.files['img']
    img.save('temp.jpg')
    img = cv2.imread('temp.jpg')
    is_boy = request.form['is_boy']
    # is_boy = True
    if is_boy:
        # img_1_face_to_img_2
        file_name = do_swap(img, boy_img)
    else:
        file_name = do_swap(img, girl_img)
    return send_file(file_name, mimetype="image/jpg")


if __name__ == '__main__':
    app.run(port='2345', host='0.0.0.0')
