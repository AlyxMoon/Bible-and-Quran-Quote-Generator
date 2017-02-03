from PIL import Image, ImageDraw, ImageFont
import textwrap

#-----------------------------
# Configuration Options
background_image_path   = 'resources/base.png'
text_font_path          = 'resources/Antonio.ttf'
output_path             = 'data/output.png'

image_width             = 2048
image_height            = 1536

max_chars_per_line      = 70
text_size               = 40
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

def generateImage(bible, quran):
    image = Image.open(background_image_path).convert('RGBA')
    font = ImageFont.truetype(text_font_path, text_size)
    d = ImageDraw.Draw(image)

    bible['text']   = textwrap.wrap(bible['text'], width = max_chars_per_line)
    quran['verse']  = textwrap.wrap(quran['verse'], width = max_chars_per_line)

    # Draw the left side (Quran)
    current_h = (image_height - getParagraphHeight(quran['verse'], text_padding, d, font)) / 2
    for line in quran['verse']:
        w, h = d.textsize(line, font = font)
        d.text((image_width / 4 - w / 2, current_h), line, font = font, fill = text_color)
        current_h += h + text_padding
    w, h = d.textsize(quran['citation'], font = font)
    d.line([(horizontal_line_padding, current_h + text_padding * 2), ((image_width / 2) - horizontal_line_padding, current_h + text_padding * 2)], fill = text_color, width = 2)
    d.text((footer_padding, current_h + text_padding * 5), quran['citation'], font = font, fill = text_color)

    # Draw the right side (Bible)
    current_h = (image_height - getParagraphHeight(bible['text'], text_padding, d, font)) / 2
    for line in bible['text']:
        w, h = d.textsize(line, font = font)
        d.text((image_width * 3 / 4 - w / 2, current_h), line, font = font, fill = text_color)
        current_h += h + text_padding
    w, h = d.textsize(bible['citation'], font = font)
    d.line([(horizontal_line_padding + image_width / 2, current_h + text_padding * 2), (image_width - horizontal_line_padding, current_h + text_padding * 2)], fill = text_color, width = 2)
    d.text((footer_padding + image_width / 2, current_h + text_padding * 5), bible['citation'], font = font, fill = text_color)

    image.save(output_path)
    return output_path