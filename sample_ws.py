#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:17:27 2019

@author: santanu.naskar
"""

from flask import (Flask, request, render_template)
#from werkzeug import secure_filename
import os
import face_recognition

app = Flask(__name__, template_folder="templates")
app.config['UPLOAD_FOLDER'] = 'templates/'
# Create a URL route in our application for "/"
@app.route('/', methods=['GET', 'POST'])
def uploaded_file():
    k = []
    if request.method == 'POST':
        #file = request.files['pic']
        #filename = secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], "img.png"))
        k = checkImageRepo()
        #uploads = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
        #return send_from_directory(directory=uploads, filename='img.png')
        return render_template('results.html', results=k)
    return render_template('home.html')

def checkImageRepo():
    base_dir = "templates/images"
    images = os.listdir(base_dir)
    l = []

    image_match = face_recognition.load_image_file('templates/img.png')

    image_to_be_matched_encoded = face_recognition.face_encodings(image_match)[0]

    for image in images:
        if image == '.DS_Store' or image == 'toTest':
            continue
        cur_image = face_recognition.load_image_file(base_dir + '/' + image)
        current_image_encoded = face_recognition.face_encodings(cur_image)[0]
        result = face_recognition.compare_faces([image_to_be_matched_encoded], current_image_encoded)
        if result[0] == True:
            l.append(image)
    return l
            
# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)