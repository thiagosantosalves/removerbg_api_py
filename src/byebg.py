import random
import os
from rembg import remove
from PIL import Image
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
            'url': 'http://24.199.99.39:5000/files/'+nameFile
        }

        return jsonify(res), 200 

    
    except:
        return jsonify({ 'error': 'Invalid syntax for this request was provided.' }), 400

@app.route('/removefile', methods=['POST'])
def remove_image(): 
    
        data = request.get_json()
        path = data.get('path')
        output_path = './upload/'+path
        os.remove(output_path)

        return jsonify({'The file was successfully deleted'}), 200

@app.route('/files/<filename>')
def send_image(filename):

    return send_from_directory('../upload', filename)


app.run(port=5000, host='24.199.99.39', debug=True)
