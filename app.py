from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename
import pandas as pd
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DATA_DIRECTORY = os.path.join(APP_ROOT, "data")
ALLOWED_EXTENSIONS = {'csv'}

if not os.path.isdir(DATA_DIRECTORY):
    os.mkdir(DATA_DIRECTORY)

app = Flask(__name__)
app.config['DATA_DIRECTORY'] = DATA_DIRECTORY
app.config['SECRET_KEY'] = 'redsfsfsfsfis'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == 'POST':
        if "dataset-upload-input" not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files["dataset-upload-input"]
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            destination = os.path.join(app.config['DATA_DIRECTORY'], filename)
            file.save(destination)

            df = pd.read_csv(destination)
            print(df.columns.values)

            return render_template("index.html", tables=[df.to_html(classes='table table-striped table-bordered', header=True, max_rows=1000, table_id="dataset-table")], filename=filename)
    return render_template("blank.html")


# @app.route("/download")
# def download():
#     send_from_directory(DATA_DIRECTORY, path, as_attachment=True)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
