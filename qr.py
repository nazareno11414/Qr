# pip install qrcode[pil]
import qrcode

# Dimensiones del Qr
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Agregar datos al código QR
qr.add_data('https://www.youtube.com/watch?v=Ubxb1u3izeM&ab_channel=chayanneVEVO')
qr.make(fit=True)

# Crear una imagen del código QR
img = qr.make_image(fill='black', back_color='white')

# Guardar la imagen
img.save('codigo_qr.png')
