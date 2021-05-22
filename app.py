from flask import Flask, render_template,request,make_response,jsonify, send_file, redirect, send_from_directory
# import jwt
from werkzeug.utils import secure_filename
import os
import zipfile
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = './sample_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Main home page and file uploading linker code
@app.route("/uploader",methods=['GET','POST'])
def upload_file():
    # Switch between home page and file uploading if request comes as post then file upload code is triggered
    if request.method =='POST':
        # Getting the attached file from request
        file = request.files['file']
        # Applying default filename which is picked by pifu library
        filename = "test.png"
        # Saving file to the disk
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        '''
        Following lines of code are to execute functions of pifu library
        we are using subprocess module to run cli arguments for pifu library
        '''
        # Conversion of 2d model to 3d render(mesh object)
        subprocess.run(["python",'-m', "apps.simple_test.py"])
        # Cleaning the obtained mesh object
        subprocess.run(["python", "./apps/clean_mesh.py ", "-f", "./results/pifuhd_final/recon"])
        # To create .mp4 out of the render images
        subprocess.run(["python", "-m", "apps.render_turntable", "-f", "./results/pifuhd_final/recon", "-ww", "512","-hh","512"])
        # Redirecting to download page for file download
        return redirect("/downloadfile")
    return  render_template('home.html')

# Download API
@app.route("/downloadfile", methods = ['GET'])
def download_file():
    return render_template('download.html')

@app.route('/return-files')
def return_files_tut():
    # path to directory where the resultant files are stored
    dir = './results/pifuhd_final/recon'
    # creating a zipfile for all the resultant files
    zipf = zipfile.ZipFile('render_model.zip', 'w', zipfile.ZIP_DEFLATED)
    files = os.listdir(dir)
    for file in files:
        zipf.write(dir+ '/'+file)
    zipf.close()
    return send_file('render_model.zip',
                     mimetype='zip',
                     attachment_filename='render_model.zip',
                     as_attachment=True)

@app.errorhandler(400)
def bad_request(exception):
    return make_response(jsonify({"error:",str(exception)},400))

@app.errorhandler(500)
def server_error(exception):
    return make_response(jsonify({"error:",str(exception)},500))

if __name__ == "__main__":
    app.run()