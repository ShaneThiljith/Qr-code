from flask import Flask, render_template, request, send_file
from backend import generate_qr_code
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    """Render the homepage and handle QR code generation."""
    if request.method == "POST":
        data = request.form.get("data")
        fg_color = request.form.get("fg_color", "#000000")
        bg_color = request.form.get("bg_color", "#FFFFFF")
        file_name = "qrcode.png"

        if not data:
            return "❌ Error: Please provide valid text or URL.", 400

        try:
            generate_qr_code(data, file_name, fg_color, bg_color)
            return send_file(file_name, mimetype="image/png", as_attachment=True)
        except Exception as e:
            return f"⚠️ Error generating QR code: {str(e)}", 500

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
