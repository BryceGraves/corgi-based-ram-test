import webbrowser

with open('.CorgisToInject.txt') as f:
    allPhotos = f.read().splitlines()

for currentPhoto in allPhotos:
    webbrowser.open(currentPhoto)
