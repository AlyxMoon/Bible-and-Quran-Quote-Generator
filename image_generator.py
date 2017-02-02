from PIL import Image, ImageDraw, ImageFont
import textwrap
from mappings import *
from get_verses import getRandomVerse

#-----------------------------
# Configuration Options
background_image_path   = 'resources/base.png'
text_font_path          = 'resources/Antonio.ttf'

image_width             = 2048
image_height            = 1024

max_chars_per_line      = 80
text_size               = 32
text_color              = (255,255,255)
text_padding            = 5
footer_padding          = 20
horizontal_line_padding = 15

# End of configuration Options
#-----------------------------

def getParagraphHeight(text, padding, imageDraw, font):
    height = 0
    for line in text:
        w, h = imageDraw.textsize(line, font = font)
        height += h + 5
    return height

image = Image.open(background_image_path).convert('RGBA')
font = ImageFont.truetype(text_font_path, text_size)
d = ImageDraw.Draw(image)

bible, quran = getRandomVerse()
bible['text'], quran['verse'] = textwrap.wrap(bible['text'], width = max_chars_per_line), textwrap.wrap(quran['verse'], width = max_chars_per_line)
bibleFooter = 'Bible -- {0} {1}:{2}'.format(getBookFromNum(bible['book']), bible['chapter'], bible['verse'])
quranFooter = 'Quran -- {0} | Verse {1}'.format(getSurahFromNum(quran['surah']), quran['ayah'])

# Draw the left side (Quran)
current_h = ((image_width / 2) - getParagraphHeight(quran['verse'], text_padding, d, font)) / 2
for line in quran['verse']:
    w, h = d.textsize(line, font = font)
    d.text((image_width / 4 - w / 2, current_h), line, font = font, fill = text_color)
    current_h += h + text_padding
w, h = d.textsize(quranFooter, font = font)
d.line([(horizontal_line_padding, current_h + text_padding * 2), ((image_width / 2) - horizontal_line_padding, current_h + text_padding * 2)], fill = text_color, width = 2)
d.text((footer_padding, current_h + text_padding * 5), quranFooter, font = font, fill = text_color)

# Draw the right side (Bible)
current_h = ((image_width / 2) - getParagraphHeight(bible['text'], text_padding, d, font)) / 2
for line in bible['text']:
    w, h = d.textsize(line, font = font)
    d.text((image_width * 3 / 4 - w / 2, current_h), line, font = font, fill = text_color)
    current_h += h + text_padding
w, h = d.textsize(bibleFooter, font = font)
d.line([(horizontal_line_padding + image_width / 2, current_h + text_padding * 2), (image_width - horizontal_line_padding, current_h + text_padding * 2)], fill = text_color, width = 2)
d.text((footer_padding + image_width / 2, current_h + text_padding * 5), bibleFooter, font = font, fill = text_color)

image.save('testImage.png')