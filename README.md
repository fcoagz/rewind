# pyrewind
pyrewind es una potente biblioteca de Python diseñada para facilitar la obtención y descarga de vídeos que se han eliminado previamente, así como la descarga de vídeos actuales. pyrewind utiliza herramientas como pytube.

## Instalación
```sh
pip install pyrewind
```

## Uso
Utiliza la clase `YouTube` pasando la URL del video como argumento al constructor:

```python
from rewind import YouTube

# Crea una instancia del objeto YouTube con la URL del video deseado
youtube_obj = YouTube('https://www.youtube.com/watch?v=VIDEO_ID')
```

Accede a las propiedades del video obtenido:

```python
print(youtube_obj.title)         # Título del video
print(youtube_obj.publish_date)  # Fecha de publicación
```
Descarga el video utilizando el método download:
```python
youtube_obj.download()
```
No es necesario especificar la ruta ya que la guardaría en un directorio creado por él y el vídeo estaría dentro.
## Contribución
Las contribuciones son bienvenidas! Si encuentras algún problema o te gustaría agregar nuevas funciones a PyRewind, siéntete libre de abrir un "issue" o enviar una solicitud de extracción.