from flask import Flask, render_template,redirect,url_for, Response, request
import pandas as pd


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/jupyter')
def jupyter():
    return render_template('jupyter.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/file_convertor')
def fileconvertor():
    return render_template('fileconvertor.html')

@app.route('/datacleaner')
def datacleaner():
    return render_template('datacleaner.html')

@app.route("/upload", methods=["POST"])
def upload():
  file = request.files["file"]
  format = request.form["format"]

  if file and format:
    if "csv" in str(file):
          df = pd.read_csv(file)
    elif "xsl" in str(file):
            df=pd.read_excel(file)
    elif "json" in str(file):
            df=pd.read_json(file)
    elif "txt" in str(file):
            df = pd.read_csv(file, sep="\t")

    if format == "csv":
      response = Response(df.to_csv(), mimetype="text/csv")
    elif format == "excel":
      response = Response(df.to_excel())
    elif format == "txt":
      response = Response(df.to_string(), mimetype="text/plain")
    elif format == "json":
      response = Response(df.to_json(), mimetype="application/json")

    response.headers["Content-Disposition"] = "attachment; filename=file.{}".format(format)

    return response

if __name__ == "__main__":
  app.run(debug=True)

@app.route("/clean", methods=["POST"])
def clean():
  file = request.files["file"]
  if file:
    if "csv" in str(file):
          df = pd.read_csv(file)
          type="csv"
    elif "xsl" in str(file):
            df=pd.read_excel(file)
            type="excel"
    elif "json" in str(file):
            df=pd.read_json(file)
            type="json"
    elif "txt" in str(file):
            df = pd.read_csv(file, sep="\t")
            type="txt"

    cols = len(df.axes[1])

    if type == "csv":
      response = Response(df.to_csv(), mimetype="text/csv")
    elif type == "excel":
      response = Response(df.to_excel())
    elif type == "txt":
      response = Response(df.to_string(), mimetype="text/plain")
    elif type == "json":
      response = Response(df.to_json(), mimetype="application/json")

    response.headers["Content-Disposition"] = "attachment; filename=file.{}".format(type)

    return response

if __name__ == "__main__":
  app.run(debug=True)

@app.route('/sitemap')
def sitemap():
    return render_template('sitemap.xml')

if __name__ == '__main__':
    app.run(debug=True)
