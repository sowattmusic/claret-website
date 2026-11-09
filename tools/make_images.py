"""Generate social share cards (1200x630) and app icons from the site's portrait and fonts.
Run from the repository root:  python3 tools/make_images.py
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

IVORY = (244, 239, 230); INK = (23, 21, 21); WINE = (104, 38, 56); MUTED = (91, 85, 82)
F = os.path.join(os.path.dirname(__file__), 'fonts')
LG = lambda s: ImageFont.truetype(os.path.join(F, 'LeagueGothic.ttf'), s)
A6 = lambda s: ImageFont.truetype(os.path.join(F, 'Archivo-600.ttf'), s)

def spaced(d, xy, text, font, fill, track):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + track

def card(lang, out):
    W, H = 1200, 630
    im = Image.new('RGB', (W, H), IVORY)
    # portrait on the right, fading into ivory
    p = Image.open('img/portrait.jpg').convert('RGB')
    pw = 600
    s = H / p.height
    p = p.resize((int(p.width * s), H), Image.LANCZOS)
    left = (p.width - pw) // 2
    p = p.crop((left, 0, left + pw, H))
    mask = Image.new('L', (pw, H), 255)
    md = ImageDraw.Draw(mask)
    fade = 260
    for x in range(fade):
        md.line([(x, 0), (x, H)], fill=int(255 * (x / fade) ** 1.6))
    im.paste(p, (W - pw, 0), mask)
    d = ImageDraw.Draw(im)
    x0 = 64
    kick = 'SWITZERLAND · LONDON' if lang == 'en' else 'SUISSE · LONDRES'
    spaced(d, (x0, 64), kick, A6(20), INK, 3)
    d.line([(x0, 100), (x0 + 520, 100)], fill=INK, width=2)
    d.text((x0 - 6, 108), 'CLARET', font=LG(250), fill=INK)
    d.rectangle([x0, 392, x0 + 72, 398], fill=WINE)
    roles = (['Record producer', 'Songwriter & composer', 'Artistic director'] if lang == 'en'
             else ['Producteur', 'Auteur-compositeur', 'Directeur artistique'])
    y = 420
    for r in roles:
        d.text((x0, y), r, font=A6(34), fill=INK); y += 44
    foot = 'ENZO CLARET · SOWATT MUSIC'
    spaced(d, (x0, 566), foot, A6(18), WINE, 2.5)
    im.save(out, quality=88, optimize=True, progressive=True)

def icon(size, out, pad=0.0):
    im = Image.new('RGB', (size, size), WINE)
    d = ImageDraw.Draw(im)
    f = LG(int(size * 0.86))
    bb = d.textbbox((0, 0), 'C', font=f)
    w, h = bb[2] - bb[0], bb[3] - bb[1]
    d.text(((size - w) / 2 - bb[0], (size - h) / 2 - bb[1]), 'C', font=f, fill=IVORY)
    im.save(out)
    return im

if __name__ == '__main__':
    card('en', 'img/share-en.jpg')
    card('fr', 'img/share-fr.jpg')
    icon(180, 'apple-touch-icon.png')
    icon(192, 'icon-192.png')
    icon(512, 'icon-512.png')
    big = icon(256, '/tmp/_ico.png')
    big.save('favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])
    print('images done')
