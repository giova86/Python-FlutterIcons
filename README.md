# Icon Generator

Questo script Python utilizza **ImageMagick** per generare automaticamente le icone necessarie per applicazioni iOS e Android a partire da un'immagine sorgente.

## 🛠 Requisiti

Assicurati di avere installati:

- Python 3.x
- [ImageMagick](https://imagemagick.org/) (comando `magick` deve essere disponibile nel terminale)

Puoi installare ImageMagick con:

```bash
# macOS con Homebrew
brew install imagemagick
```

```bash
# Ubuntu/Debian
sudo apt-get install imagemagick
```

## 📥 Installazione

Clona questo repository o scarica lo script generate_icons.py.

```bash
git clone https://github.com/tuo-username/icon-generator.git
cd icon-generator
```

## ▶️ Utilizzo

Assicurati di avere un'immagine sorgente (idealmente 1024x1024 px) in formato PNG.

Esegui lo script con:

```bash
python generate_icons.py "nome_immagine.png"
```

Esempio:

```bash
python generate_icons.py "Asset 4@4x.png"
```

## 🖼️ Output

Lo script genererà:

✅ Icone per iOS in formato PNG con i nomi richiesti per l'Asset Catalog.

✅ Icone per Android nelle cartelle mipmap-*.

Esempio struttura generata:

```bash
Icon-App-20x20@1x.png
Icon-App-20x20@2x.png
Icon-App-60x60@3x.png
...
mipmap-mdpi/ic_launcher.png
mipmap-hdpi/ic_launcher.png
...
```
