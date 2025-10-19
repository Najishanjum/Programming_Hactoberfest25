# Step 1: Install required library
# You can run this in your terminal/command prompt:
# pip install qrcode[pil]

import qrcode

# Step 2: Data to encode
data = "https://space-habitatx.netlify.app/"  # You can put any URL or text here

# Step 3: Create QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code, 1 is smallest
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of the border
)

qr.add_data(data)
qr.make(fit=True)

# Step 4: Generate QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Step 5: Save the QR code image
img.save("my_qr_code.png")

print("QR Code generated and saved as 'my_qr_code.png'")
