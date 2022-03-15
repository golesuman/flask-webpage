from django.shortcuts import render
from fastapi import UploadFile
from flask import Flask,request,render_template

# import easyocr
# reader=easyocr.Reader(['en'])
from ocr import core_ocr
import os
path=os.getcwd()

UPLOAD_FOLDER='/static/uploads'
app=Flask(__name__)





# app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER





ALLOWED_EXTENSIONS=set(['png','jpg','jpeg'])
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS


# from flask_uploads import UploadSet,configure_uploads,IMAGES

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_page():  
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('upload.html', msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('upload.html', msg='No file selected')

        if file and allowed_file(file.filename):

            # call the OCR function on it
            extracted_text =core_ocr(file)

            # extract the text and display it
            return render_template('upload.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text,
                                   img_src=UPLOAD_FOLDER + file.filename)
    elif request.method == 'GET':
        return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)