from flask import Flask, render_template, request
import os
import base64

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    mssv = request.form.get('mssv')
    name = request.form.get('name')
    folder_name = f"{mssv}_{name.replace(' ', '_')}"
    folder_path = os.path.join(UPLOAD_FOLDER, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    for angle in ['front', 'left', 'right', 'up', 'far']:
        data_url = request.form.get(angle)
        if data_url:
            img_data = base64.b64decode(data_url.split(',')[1])
            with open(os.path.join(folder_path, f"{angle}.jpg"), 'wb') as f:
                f.write(img_data)

    return "Upload thành công!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
