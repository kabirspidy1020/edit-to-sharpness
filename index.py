from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os
import cv2
import numpy as np
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
def process_image(filename, operation):
    print("the operation is {} and file name is {}".format(operation, filename))
    img = cv2.imread(f"uploads/{filename}")
    
    if operation == "greyscale":
        imgprocessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"static/{filename}", imgprocessed)
    elif operation == "sketch":
        grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        invert = cv2.bitwise_not(grey_img)
        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        invertedblur = cv2.bitwise_not(blur)
        sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
        cv2.imwrite(f"static/{filename}", sketch)
    elif operation == "bgremove":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        mask = cv2.drawContours(np.zeros_like(gray), contours, -1, (255), thickness=cv2.FILLED)
        result_image = cv2.bitwise_and(img, img, mask=mask)
        cv2.imwrite(f"static/{filename}", result_image)
    else:
        print("Invalid operation")            



@app.route('/')
def home():
    return render_template("index.html")
@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")
@app.route('/edit', methods=["GET","POST"])
def edit():

    if request.method == 'POST':
        operation=request.form.get("operation")
       
        if 'file' not in request.files:
            flash('No file part')
            return "ERROR"
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return "NO files selected"
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            process_image(filename, operation)
            flash(f"the image has been processed and is available at <a href='/static/{filename}' target='_blank'>here</a>")
            return render_template("index.html")
    return render_template("index.html")   




if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0')
