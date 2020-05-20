try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)

print('Setup complete')
filepath = 'test_2.png'

def process_pdf(filepath):
    f = open("folder/locked.txt", "a")

    images = convert_from_path(filepath)
    # images = convert_from_bytes(open(filepath, 'rb').read())
    print(len(images))
    for i in images:
        i.save(''.join(['folder/unlock', str(images.index(i)), '.png']), 'png')
        f.write(pytesseract.image_to_string(Image.open(''.join(['folder/unlock', str(images.index(i)), '.png']))))
    f.close()

    


def process_img_pytess(filepath):
    return pytesseract.image_to_string(Image.open(filepath))

def process_img_opencv(filepath):
    pass

process_pdf('unlock.pdf')