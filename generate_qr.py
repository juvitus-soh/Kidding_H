import qrcode

# URL where your webpage will be hosted (replace with your Render URL later)
url = "https://your-app-name.onrender.com"

# Create QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Generate and save the QR code as an image
qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image.save("hyrre_qr_code.png")

print("QR code generated and saved as 'hyrre_qr_code.png'")