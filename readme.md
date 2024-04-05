# Generador de códigos QR

Este script en Python utiliza la librería `qrcode` para generar un código QR a partir de un texto especificado. El código QR se guarda como una imagen PNG.

## Instalación

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. Instala la librería `qrcode` usando pip:

pip install qrcode[pil]


El parámetro `[pil]` es opcional y se utiliza para instalar la dependencia necesaria para generar imágenes con la librería `PIL`.

## Uso

1. Importa la librería `qrcode`:

```python
import qrcode
```

2. Define el texto que quieres codificar en el código QR:
```python
texto = "URL"
```
3. Crea un objeto QRCode con los parámetros deseados:
```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
```
> [!NOTE]
> + version: Define la versión del código QR (1-40).
> + error_correction: Define el nivel de corrección de errores.
> + box_size: Define el tamaño de cada cuadro del código QR.
> + border: Define el ancho del borde del código QR.

4. Agrega los datos al código QR y genera el código:
```python
qr.add_data(texto)
qr.make(fit=True)
```

5. Genera la imagen del código QR y redimensiona si es necesario:
```python
img = qr.make_image(fill_color="black", back_color="white")
img = img.resize((1000, 1000))
```

6. Guarda la imagen del código QR:
```python
img.save("QR.png")
```

