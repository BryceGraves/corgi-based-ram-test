import webbrowser

with open('/home/hugeant/Code/CorgiProgram/CorgisToInject.txt') as f:
    allPhotos = f.read().splitlines()

for currentPhoto in allPhotos:
    webbrowser.open(currentPhoto)
