import qrcode

# Texto o URL que deseas convertir en un código QR
contenido = "https://edtechwork.es"  # Cambia esto al texto o URL que desees

# Crea el objeto QRCode
qr = qrcode.QRCode(
    version=1,  # Puedes ajustar la versión según tus necesidades
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,  # Tamaño de los bloques en el código QR
    border=4  # Tamaño del borde del código QR
)

# Agrega los datos al código QR
qr.add_data(contenido)

# Crea la imagen del código QR
imagen = qr.make_image(fill_color="black", back_color="white")

# Guarda la imagen del código QR en un archivo
nombre_archivo = "codigo_qr.png"  # Nombre del archivo de salida
imagen.save(nombre_archivo)

print(f"Se ha generado un código QR en '{nombre_archivo}' con el contenido: {contenido}")
