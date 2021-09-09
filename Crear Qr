import qrcode

#  Creamos un objeto codigo QR
qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4
)
# La informacion que queremos que se guarde en el Qr
info = 'Alejandro Rubio'
# Agregamos la informacion
qr.add_data(info)
qr.make(fit=True)
# Creamos una imagen para el objeto código QR
imagen = qr.make_image()
# Guardemos la imagen con la extension que queramos
imagen.save('Mi nombre.png')
