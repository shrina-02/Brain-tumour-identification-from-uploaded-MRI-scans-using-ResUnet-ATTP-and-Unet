import os
from flask import Flask, render_template, request, redirect, url_for
import cv2 as cv
from displayTumor import DisplayTumor
from predictTumor import predictTumor

UPLOAD_FOLDER = "static/results"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

uploaded_file_name = None  # store uploaded filename globally


@app.route("/", methods=["GET", "POST"])
def index():
    global uploaded_file_name
    step0_file, step2_file, prediction_text = None, None, None

    if request.method == "POST":
        # --- Upload File ---
        if "file" in request.files:
            file = request.files["file"]
            if file and file.filename != "":
                uploaded_file_name = file.filename
                save_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file_name)
                file.save(save_path)
                return redirect(url_for("index"))

        # --- Step 0: Initial Segmentation ---
        elif "step0" in request.form and uploaded_file_name:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file_name)
            img = cv.imread(file_path)

            tumor = DisplayTumor()
            tumor.readImage(img)
            tumor.removeNoise()
            tumor.displayTumor()

            step0_result = tumor.getImage()
            step0_file = "step0_result.jpg"
            cv.imwrite(os.path.join(app.config["UPLOAD_FOLDER"], step0_file), step0_result)

        # --- Prediction Only ---
        elif "predict" in request.form and uploaded_file_name:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file_name)
            img = cv.imread(file_path)

            res = predictTumor(img)
            prob = float(res[0][0])
            if prob > 0.5:
                prediction_text = f"Tumor Detected (Confidence: {prob:.2f})"
            else:
                prediction_text = f"No Tumor Detected (Confidence: {1 - prob:.2f})"

        # --- Step 2: Noise Cleared Image ---
        elif "step2" in request.form and uploaded_file_name:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], uploaded_file_name)
            img = cv.imread(file_path)

            tumor = DisplayTumor()
            tumor.readImage(img)
            tumor.removeNoise()
            step2_result = tumor.curImg  # noise cleared version

            step2_file = "step2_result.jpg"
            cv.imwrite(os.path.join(app.config["UPLOAD_FOLDER"], step2_file), step2_result)

    return render_template(
        "index.html",
        uploaded_file=uploaded_file_name,
        step0_file=step0_file,
        step2_file=step2_file,
        prediction_text=prediction_text,
    )


if __name__ == "__main__":
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
