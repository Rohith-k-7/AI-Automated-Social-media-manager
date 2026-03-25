# from flask import Flask, render_template, request
# import os
# from agents.caption_agent import generate_caption
# from agents.hashtag_agent import generate_hashtags
# from agents.music_agent import suggest_music
# from agents.scheduler_agent import generate_schedule

# app = Flask(__name__)

# UPLOAD_FOLDER = "static/uploads"
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# @app.route("/", methods=["GET", "POST"])
# def index():

#     if request.method == "POST":

#         file = request.files["image"]

#         if file:

#             filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
#             file.save(filepath)

#             caption = generate_caption(filepath)
#             hashtags = generate_hashtags(filepath)
#             music = suggest_music(filepath)
#             schedule = generate_schedule(filepath)

#             return render_template(
#                 "index.html",
#                 image=filepath,
#                 caption=caption,
#                 hashtags=hashtags,
#                 music=music,
#                 schedule=schedule
#             )

#     return render_template("index.html")


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request
import os

from agents.caption_agent import generate_caption
from agents.hashtag_agent import generate_hashtags
from agents.music_agent import suggest_music
from agents.scheduler_agent import generate_schedule
from utils.video_processor import extract_frame

app = Flask(__name__)   # ✅ MUST be here

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        file = request.files["image"]

        if file:

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)

            # detect video
            if file.filename.lower().endswith((".mp4", ".mov", ".avi")):
                input_path = extract_frame(filepath)
            else:
                input_path = filepath

            caption = generate_caption(input_path)
            hashtags = generate_hashtags(input_path)
            music = suggest_music(input_path)
            schedule = generate_schedule(input_path)

            return render_template(
                "index.html",
                image=filepath,
                caption=caption,
                hashtags=hashtags,
                music=music,
                schedule=schedule
            )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)