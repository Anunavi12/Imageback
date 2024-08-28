from flask import Flask, render_template, request, redirect, send_file
from rembg import remove
from PIL import Image
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename != '':
            input_image = Image.open(file)
            output_image = remove(input_image)
            
            output_path = "output.png"
            output_image.save(output_path)
            
            return send_file(output_path, as_attachment=True, download_name='output.png')
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
