from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

def generate_qr_code(data, fg_color="black", bg_color="white"):
    """Generates a QR code image and returns it as a BytesIO object."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create the QR code image with custom colors
    img = qr.make_image(fill=fg_color, back_color=bg_color)
    
    # Save to a BytesIO stream
    img_byte_arr = BytesIO()
    img.save(img_byte_arr)
    img_byte_arr.seek(0)
    
    return img_byte_arr

@app.route("/", methods=["GET", "POST"])
def home():
    """Render the homepage and handle QR code generation."""
    if request.method == "POST":
        data = request.form.get("data")
        fg_color = request.form.get("fg_color", "black")
        bg_color = request.form.get("bg_color", "white")

        if not data:
            return "Error: Please provide valid text or URL", 400

        qr_image = generate_qr_code(data, fg_color, bg_color)
        return send_file(qr_image, mimetype="image/png", as_attachment=True, download_name="qrcode.png")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
