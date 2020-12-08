#!/usr/bin/python3
# Convert a Markdown file into a series of WEBTOON-sized PNGs with pandoc, pdfcrop, and ImageMagick!
import sys, os
from PIL import Image

## get filename from user input
fileString = str(sys.argv[1])
ext_location = fileString.rfind('.')
filename = fileString[:ext_location] if ext_location != -1 else fileString

## use pandoc to create pdf file
os.system('pandoc ' + fileString + ' -s --pdf-engine=xelatex -o ' + filename + '.pdf')

## crop the pdf to remove excess whitespace
os.system('pdfcrop --margins "3 3" ' + filename + '.pdf ' + filename + '.pdf > /dev/null 2>&1')

## use ImageMagick to turn the pdf into a PNG with DPI of 240
os.system('convert -background white -alpha remove -alpha off -quiet -density 240 -crop 800x1330+0+0 -append ' + filename + '.pdf -quality 90 ' + filename + '.png')

## cancerous way to crop the image that I found on StackOverflow (but it works)
im = Image.open(filename + '.png')
i = 0
for h in range(0, im.height, 1280):
    nim = im.crop((0, h, im.width-1, min(im.height, h+1280)-1))
    nim.save(filename + '_' + str(i) + ".png")
    i += 1