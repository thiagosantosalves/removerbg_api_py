""" import random
import os
from rembg import remove
from PIL import Image
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

@app.route('/remove', methods=['POST'])
def image():
    
    try:

        image = request.files['file']

        randomNumber = random.randrange(100,520000)
        print(randomNumber)
        nameFile = str(randomNumber)+'.png'
                
        output_path = './upload/'+nameFile

        original_img = Image.open(image)
        no_bg_img = remove(original_img)
        no_bg_img.save(output_path)

        res = {
            'url': 'http://localhost:5000/files/'+nameFile
        }

        return jsonify(res), 200 

    
    except:
        return jsonify({ 'error': 'Invalid syntax for this request was provided.' }), 400

@app.route('/image_delete', methods=['DELETE'])
def remove_image(): 
    try:
        data = request.get_json()
        path = data.get('path')

        output_path = './upload/'+path

        os.remove(output_path)

        return jsonify({'The {path} file was successfully deleted'}), 200
    except:
        return jsonify({ 'error': 'Invalid syntax for this request was provided.' }), 400

@app.route('/files/<filename>')
def send_image(filename):

    return send_from_directory('../upload', filename)


app.run(port=5000, host='localhost', debug=True) """


# example.py
from rembg.bg import remove
from PIL import Image

# Uncomment the following lines if working with trucated image formats (ex. JPEG / JPG)
# In my case I do give JPEG images as input, so i'll leave it uncommented
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

nameFile = 'teste.png'
    
original_img = Image.open('8k.jpg')
no_bg_img = remove(original_img)

print(no_bg_img)

print('passou da parte do erro')
no_bg_img.save(nameFile)

print('deu certo')