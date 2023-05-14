import argparse
import numpy as np
import dill as pickle
import cv2
import locate_bubbles
import translate
import typeset
from PIL import Image


def main():
    path1=input("ENTER PATH -")
    img = cv2.imread(path1)
    blurbs = locate_bubbles.get_blurbs(img)
    to_typeset = Image.fromarray(img.copy())

    for blurb in blurbs:
        translated = translate.translate_blurb(blurb)
        #translated = blurb
        typeset.typeset_blurb(to_typeset, translated)

    to_typeset.save('final.jpg')

if __name__ == "__main__":
    main()
