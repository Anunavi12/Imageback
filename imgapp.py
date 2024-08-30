import os
import tempfile
from flask import Flask, render_template, request, send_file
from rembg import remove
from PIL import Image

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename != '':
            input_image = Image.open(file)
            output_image = remove(input_image)
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_file:
                output_image.save(temp_file, format='PNG')
                temp_file_path = temp_file.name
            
            return send_file(temp_file_path, as_attachment=True, download_name='output.png')
    
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
