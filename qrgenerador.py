import qrcode
texto = "URL"
qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10, 
    border=2,  
)
qr.add_data(texto)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img = img.resize((1000, 1000))
img.save("QR.png")
