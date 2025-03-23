import qrcode
from PIL import ImageColor

def generate_qr_code(data, file_name, fg_color="#000000", bg_color="#FFFFFF"):
    """Generates a QR code and saves it as an image file with custom colors."""
    
    if not data:
        print("❌ Error: Data cannot be empty!")
        return

    # Convert named colors to hex if necessary
    try:
        fg_color = ImageColor.getrgb(fg_color)  # Convert color name to RGB tuple
        bg_color = ImageColor.getrgb(bg_color)
    except ValueError:
        print("⚠️ Invalid color input! Using default colors.")
        fg_color = "#000000"
        bg_color = "#FFFFFF"

    # Ensure the file name ends with .png
    if not file_name.lower().endswith(".png"):
        file_name += ".png"

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create the QR code image
    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    img.save(file_name)

    print(f"✅ QR code saved as {file_name}")

if __name__ == "__main__":
    data = input("Enter text or URL to generate QR code: ").strip()
    file_name = input("Enter the file name to save the QR code (e.g., qr_code.png): ").strip()

    # Get user color inputs
    fg_color = input("Enter foreground color (hex or name, default black): ").strip() or "#000000"
    bg_color = input("Enter background color (hex or name, default white): ").strip() or "#FFFFFF"

    generate_qr_code(data, file_name, fg_color, bg_color)
