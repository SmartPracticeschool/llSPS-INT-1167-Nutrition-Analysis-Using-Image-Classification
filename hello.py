from __future__ import division, print_function
from flask import Flask, redirect, url_for, request, render_template, jsonify
import json
from werkzeug.utils import secure_filename
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import sys
import os


app = Flask(__name__, static_url_path='')

def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(64, 64))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict_classes(x)
    return preds


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['image']

        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(C:\Users\jayan\Desktop\model\mymodel.h5)
        model = load_model('mymodel.h5')
        preds = model_predict(file_path, model)
        print("preds : "+str(preds))
        ls=["Fruits","Snacks","Vegetables"]
        p=preds.flatten()
        result = ls[p[0]]
        if result=="Fruits":
            return ("Proteins : 65 Calories : 1")
        elif result=="Snacks":
            return ("Proteins : 140 Calories : 5")
        else:
            return ("Proteins : 2 Calories : 33")
    return None


if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=True)



