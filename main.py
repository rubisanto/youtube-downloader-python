# installer le module pytube
# $ python -m pip install git+https://github.com/pytube/pytube
# installation autopep8

from pytube import YouTube
# la vidéo a télécharger
url = "https://youtu.be/JmAKhNf7NEw"


# fonction pour la callback
def on_dowload_progress(stream, chunk, bytes_remaining):
    # octets déjà téléchargés
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize
    # afficher en convertissant pour éviter les virgules sur les pourcentages
    print(f"PROGRESSION DU TELECHARGEMENT: {int(percent)}%")


youtube_video = YouTube(url)

# # afficher le pourcentage de téléchargement
youtube_video.register_on_progress_callback(on_dowload_progress)

# afficher le titre
print("TITRE: " + youtube_video.title)
# nombre de vues
print("NOMBRE DE VUES: ", youtube_video.views)

# afficher tous les flux
print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print(" ", stream)

# télécharger le stream
# stream = youtube_video.streams.get_by_itag(18)
# choisir la meilleure résolution en progressive true

stream = youtube_video.streams.get_highest_resolution()
print("STREAM VIDEO: ", stream)

print("TELECHARGEMENT...")
stream.download()


print("TELECHARGEMENT TERMINE")
