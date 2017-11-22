#!/usr/bin/env python

import Image
import pytesseract

print(pytesseract.image_to_string(Image.open('testOCR.png')))

