from os import link
from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from mediaindir import dl_video, dl_photo

app = Flask(__name__)
app.secret_key = "hakan"

@app.route("/", methods = ["GET","POST"])
def index():

    if request.method == "POST":
        linkvideo = request.form.get("medialink")
        resultlink = dl_video(linkvideo)
        if resultlink["response"] == "success":
            mediaUrl = resultlink["mediaUrl"]
            mediaType = resultlink["type"]
            hakan = dict(resultlink)
            # return render_template("download.html", medialink = mediaUrl, type = mediaType)
            return render_template("download.html", sonucdict = hakan)
        else:
            flash("Lütfen geçerli bir video linki giriniz.","danger")
            return render_template("index.html")
    else:
        return render_template("index.html")


@app.route("/photodownload", methods = ["GET","POST"])
def photoDownload():

    if request.method == "POST":
        linkvideo = request.form.get("medialink")
        resultlink = dl_photo(linkvideo)
        if resultlink["response"] == "success":
            mediaUrl = resultlink["mediaUrl"]
            mediaType = resultlink["type"]
            hakan = dict(resultlink)
            return render_template("download.html", sonucdict = hakan)
            # return render_template("download.html", medialink = mediaUrl, type = mediaType)
        else:
            flash("Lütfen geçerli bir fotoğraf linki giriniz.","danger")
            return render_template("photodownload.html")
    else:
        return render_template("photodownload.html")


@app.route("/storydownload")
def storyDownload():
    return render_template("storydownload.html")

@app.route("/postinfodownload")
def infoDownload():
    return render_template("postinfodownload.html")


@app.route("/download", methods = ["GET","POST"])
def download():
    if request.method == "GET":
        return render_template("download.html")
    else:
        return redirect(url_for("index"))

if (__name__) == "__main__":
    app.run(debug=True)