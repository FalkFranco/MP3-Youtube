from pytube import YouTube
import os

yt = YouTube(str(input("Ingresar la URL del video: ")))

video = yt.streams.filter(only_audio=True).first()

print("Ingresar el destino de descarga: ")
destination = str(input(">> ")) or '.'

out_file = video.download(output_path=destination)

base, ext = os.path.splitext(out_file)

new_file = base + '.mp3'
os.rename(out_file, new_file)

print(yt.title + " ha sido descargado exitosamente en formato mp3.")

