import os
import sys
import shutil
from glob import glob

from wand.image import Image, Color
from PIL import Image as Image2

def convert_pdf(filename, output_path, resolution=150):
    """ Convert a PDF into images.

        All the pages will give a single png file with format:
        {pdf_filename}-{page_number}.png

        The function removes the alpha channel from the image and
        replace it with a white background.
    """
    all_pages = Image(filename=filename, resolution=resolution)
    for i, page in enumerate(all_pages.sequence):
        with Image(page) as img:
            img.format = 'png'
            img.background_color = Color('white')
            img.alpha_channel = 'remove'

            image_filename = os.path.splitext(os.path.basename(filename))[0]
            if i == 0:
                image_filename = '{}.png'.format(image_filename)
            else:
                image_filename = '{}-{}.png'.format(image_filename, i)
            image_filename = os.path.join(output_path, image_filename)

            img.save(filename=image_filename)

def pdf2png(rootdir):
    """Convert all PDF files in rootdir to PNG files

    Parameter
    =========
    rootdir : str
        directory of the PDF files
    """
    filenames = glob(os.path.join(rootdir, "*.pdf"))
    for filename in filenames:
        convert_pdf(filename, rootdir, resolution=150)

def create_thumbnail(rootdir):
    """Create thumbnail for png files in rootdir
    """
    pngfiles = glob(os.path.join(rootdir, "*.png"))
    for pngfile in pngfiles:
        img = Image2.open(pngfile)
        img.thumbnail((520, 412, ))

        # export thumbnail
        basedir = os.path.split(pngfile)[0]
        filename = (os.path.basename(pngfile)).replace(".png", "")
        filename = ".".join(["-".join([filename, "thumbnail"]), "png"])
        img.save(os.path.join(basedir, filename))

if __name__=="__main__":
    #pdf2png(sys.argv[1])
    create_thumbnail(sys.argv[1])

