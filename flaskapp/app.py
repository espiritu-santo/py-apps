#!/venv/bin python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  3 22:29:19 2023

@author: jen
"""

#Import the flask module
from flask import Flask, url_for, request, redirect, render_template, flash
from werkzeug.utils import secure_filename
import os
from pathlib import Path
import subprocess
import multiprocessing as mp

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'csv'}
UPLOAD_FOLDER = 'uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_files(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET", "POST"])
def upload_file():
    [f.unlink() for f in Path(UPLOAD_FOLDER).glob("*") if f.is_file()] 
    if request.method == "POST":
        f = request.files['csvfile']
        if f.filename == ' ':
            return flash('No csv file selected')
        if f and allowed_files(f.filename):
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for("success", filename=filename))
    return render_template("File_Upload.html")

@app.route('/success', methods=["GET", "POST"])
def success(filename=None):
    if request.method == "GET":
        return f"<h1>The file *{request.args['filename']}* has been uploaded successfully!</h1>" \
                '<a href= "/viewInstr">Instructions</a>'
    return

@app.route('/viewInstr')
def viewInstr():
    fp = '/Downloads/coords.txt'
    if os.path.exists(fp):
        os.remove(fp)
    return render_template("success.html")

def web():
    app.run(debug=True, use_reloader=False,  host='localport', port=8079)

@app.route('/caller')    
def caller():
   # app.run(debug=True, use_reloader=False, host='localhost', port=8080)
   # subprocess.call(['python',' dataio.py./'], shell=True)
   subprocess.call(['export PYTHONSTARTUP=~/flaskapp/.pythonrc'], shell=True)
   subprocess.call(['python'], shell=True)

if __name__== '__main__':
    proc1 = mp.Process(target=web, daemon=False).start()
    # proc2 = mp.Process(target=caller, daemon=False).start()
