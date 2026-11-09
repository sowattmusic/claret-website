"""Build the public site from src/index.src.html.

Produces, at the repository root:
  index.html        English page  (https://DOMAIN/)
  fr/index.html     French page   (https://DOMAIN/fr/)
  404.html          error page
  sitemap.xml, robots.txt, site.webmanifest
and dist/claret-site-upload.zip with only the files the server needs.

Usage (from the repository root):
  python3 tools/build.py                       # uses SITE_URL below
  python3 tools/build.py https://www.claret.ch # or pass the domain

Edit the content in src/index.src.html (both languages live there as
<span lang="en"> / <span lang="fr">), then run this script.
"""
import json, os, sys, zipfile, datetime
from bs4 import BeautifulSoup
from PIL import Image

# ---- settings ---------------------------------------------------------------
SITE_URL = "https://claretproductions.com"   # final domain, no trailing slash
GOOGLE_VERIFICATION = ""   # optional: content of Google's <meta name="google-site-verification">
BING_VERIFICATION = ""     # optional: content of Bing's <meta name="msvalidate.01">
# -----------------------------------------------------------------------------

if len(sys.argv) > 1:
    SITE_URL = sys.argv[1].rstrip('/')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
TODAY = datetime.date.today().isoformat()

PAGES = {
    'en': {
        'path': 'index.html', 'url': SITE_URL + '/', 'prefix': '', 'locale': 'en_GB',
        'title': 'Enzo Claret (CLARET) – Record Producer & Composer',
        'desc': 'Swiss record producer, songwriter and artistic director working between '
                'Switzerland and London. Credits with TDenon, Sarabds, Le Tremplin and Jules Loewert.',
        'og_alt': 'CLARET – record producer, songwriter and composer, artistic director',
        'share': 'img/share-en.jpg',
        'jobs': ['Record producer', 'Songwriter', 'Composer', 'Artistic director'],
    },
    'fr': {
        'path': 'fr/index.html', 'url': SITE_URL + '/fr/', 'prefix': '../', 'locale': 'fr_CH',
        'title': 'Enzo Claret (CLARET) – Producteur & compositeur',
        'desc': 'Producteur, auteur-compositeur et directeur artistique suisse, entre la Suisse '
                'et Londres. Crédits avec TDenon, Sarabds, Le Tremplin et Jules Loewert.',
        'og_alt': 'CLARET – producteur, auteur-compositeur, directeur artistique',
        'share': 'img/share-fr.jpg',
        'jobs': ['Producteur', 'Auteur-compositeur', 'Compositeur', 'Directeur artistique'],
    },
}

SAME_AS = [
    'https://open.spotify.com/artist/1uDa3JW4VfFCaDoBEyHoE4',
    'https://music.apple.com/ch/artist/claret/1808065472',
    'https://www.instagram.com/itsclaret',
    'https://www.linkedin.com/in/enzo-claret-901866233/',
    'https://credits.muso.ai/profile/d6ebee4e-29ee-4048-905b-eb54b84a2853/credits',
]
LOCAL_PREFIXES = ('img/', 'audio/', 'favicon', 'contact.php', 'apple-touch-icon', 'icon-', 'site.webmanifest')


def json_ld(lang, p):
    person = {
        '@type': 'Person', '@id': SITE_URL + '/#person',
        'name': 'Enzo Claret', 'alternateName': 'CLARET',
        'jobTitle': p['jobs'], 'url': p['url'],
        'image': SITE_URL + '/img/portrait.jpg',
        'email': 'mailto:enzo@sowattmedia.com', 'telephone': '+41786286970',
        'nationality': {'@type': 'Country', 'name': 'Switzerland'},
        'worksFor': {'@type': 'Organization', 'name': 'Sowatt Media Sàrl',
                     'alternateName': 'Sowatt Music', 'url': 'https://sowattmedia.com'},
        'knowsAbout': ['Music production', 'Songwriting', 'Composition', 'Arrangement',
                       'Artistic direction', 'Film scoring', 'Live recording'],
        'sameAs': SAME_AS,
    }
    graph = [
        {'@type': 'WebSite', '@id': SITE_URL + '/#website', 'url': SITE_URL + '/',
         'name': 'CLARET', 'inLanguage': ['en', 'fr'], 'publisher': {'@id': SITE_URL + '/#person'}},
        {'@type': 'ProfilePage', '@id': p['url'] + '#page', 'url': p['url'], 'name': p['title'],
         'description': p['desc'], 'inLanguage': lang, 'isPartOf': {'@id': SITE_URL + '/#website'},
         'mainEntity': {'@id': SITE_URL + '/#person'}, 'dateModified': TODAY},
        person,
    ]
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False, indent=1)


def head_html(lang, p):
    other = 'fr' if lang == 'en' else 'en'
    q = PAGES[other]
    pre = p['prefix']
    tags = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">',
        f'<title>{p["title"]}</title>',
        f'<meta name="description" content="{p["desc"]}">',
        '<meta name="author" content="Enzo Claret">',
        '<meta name="robots" content="index, follow, max-image-preview:large">',
        '<meta name="theme-color" content="#F4EFE6">',
        f'<link rel="canonical" href="{p["url"]}">',
        f'<link rel="alternate" hreflang="en" href="{PAGES["en"]["url"]}">',
        f'<link rel="alternate" hreflang="fr" href="{PAGES["fr"]["url"]}">',
        f'<link rel="alternate" hreflang="x-default" href="{PAGES["en"]["url"]}">',
        f'<link rel="icon" href="{pre}favicon.ico" sizes="48x48">',
        f'<link rel="icon" href="{pre}favicon.svg" type="image/svg+xml">',
        f'<link rel="apple-touch-icon" href="{pre}apple-touch-icon.png">',
        f'<link rel="manifest" href="{pre}site.webmanifest">',
        '<meta property="og:type" content="profile">',
        '<meta property="og:site_name" content="CLARET">',
        f'<meta property="og:title" content="{p["title"]}">',
        f'<meta property="og:description" content="{p["desc"]}">',
        f'<meta property="og:url" content="{p["url"]}">',
        f'<meta property="og:locale" content="{p["locale"]}">',
        f'<meta property="og:locale:alternate" content="{q["locale"]}">',
        f'<meta property="og:image" content="{SITE_URL}/{p["share"]}">',
        f'<meta property="og:image:secure_url" content="{SITE_URL}/{p["share"]}">',
        '<meta property="og:image:type" content="image/jpeg">',
        '<meta property="og:image:width" content="1200">',
        '<meta property="og:image:height" content="630">',
        f'<meta property="og:image:alt" content="{p["og_alt"]}">',
        '<meta property="profile:first_name" content="Enzo">',
        '<meta property="profile:last_name" content="Claret">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{p["title"]}">',
        f'<meta name="twitter:description" content="{p["desc"]}">',
        f'<meta name="twitter:image" content="{SITE_URL}/{p["share"]}">',
        f'<meta name="twitter:image:alt" content="{p["og_alt"]}">',
        f'<link rel="preload" as="image" href="{pre}img/portrait.jpg" fetchpriority="high">',
    ]
    if GOOGLE_VERIFICATION:
        tags.append(f'<meta name="google-site-verification" content="{GOOGLE_VERIFICATION}">')
    if BING_VERIFICATION:
        tags.append(f'<meta name="msvalidate.01" content="{BING_VERIFICATION}">')
    tags.append(f'<script type="application/ld+json">\n{json_ld(lang, p)}\n</script>')
    return '\n'.join(tags)


_size_cache = {}
def img_size(path):
    if path not in _size_cache:
        with Image.open(path) as im:
            _size_cache[path] = im.size
    return _size_cache[path]


def build_page(src, lang):
    p = PAGES[lang]
    other = 'fr' if lang == 'en' else 'en'
    soup = BeautifulSoup(src, 'html.parser')
    html = soup.find('html')
    html['lang'] = lang

    # keep only this language's text
    for el in soup.find_all(attrs={'lang': other}):
        if el.name != 'html':
            el.decompose()

    # head: drop the source's head tags we replace
    head = soup.head
    for t in head.find_all(['title', 'meta']):
        t.decompose()
    for t in head.find_all('link'):
        rel = ' '.join(t.get('rel', []))
        if 'icon' in rel or 'canonical' in rel or 'alternate' in rel or 'manifest' in rel:
            t.decompose()
    new_head = BeautifulSoup(head_html(lang, p), 'html.parser')
    head.insert(0, new_head)

    # language switch
    site = soup.find(id='site')
    site['data-lang'] = lang
    en_href = '../' if lang == 'fr' else './'
    fr_href = 'fr/' if lang == 'en' else './'
    for a, href, code in ((soup.find(id='btn-en'), en_href, 'en'), (soup.find(id='btn-fr'), fr_href, 'fr')):
        a['href'] = href
        if code == lang:
            a['aria-current'] = 'page'
        a['aria-label'] = 'English' if code == 'en' else 'Français'

    # local paths for /fr/
    for tag, attr in (('img', 'src'), ('audio', 'src'), ('a', 'href'), ('link', 'href'), ('form', 'action'), ('source', 'src')):
        for el in soup.find_all(tag):
            v = el.get(attr)
            if v and v.startswith(LOCAL_PREFIXES):
                el[attr] = p['prefix'] + v

    # form placeholder for crawlers / no-JS
    for el in soup.find_all(attrs={'data-ph-en': True}):
        el['placeholder'] = el[f'data-ph-{lang}']

    # images: intrinsic size, loading hints
    for im in soup.find_all('img'):
        src_rel = im['src'].replace('../', '')
        if os.path.exists(src_rel):
            w, h = img_size(src_rel)
            im['width'], im['height'] = str(w), str(h)
        if 'portrait.jpg' in src_rel and im.find_parent(class_='art'):
            im.attrs.pop('loading', None)
            im['fetchpriority'] = 'high'
        else:
            im['loading'] = 'lazy'
        im['decoding'] = 'async'

    out = str(soup)
    out = out.replace("fetch('contact.php'", f"fetch('{p['prefix']}contact.php'")
    if not out.lower().startswith('<!doctype'):
        out = '<!doctype html>\n' + out
    os.makedirs(os.path.dirname(p['path']) or '.', exist_ok=True)
    with open(p['path'], 'w', encoding='utf-8') as f:
        f.write(out)
    return p['path']


def write_static():
    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
               'xmlns:xhtml="http://www.w3.org/1999/xhtml" '
               'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">']
    for lang in ('en', 'fr'):
        sitemap += ['  <url>', f'    <loc>{PAGES[lang]["url"]}</loc>', f'    <lastmod>{TODAY}</lastmod>']
        for l2 in ('en', 'fr'):
            sitemap.append(f'    <xhtml:link rel="alternate" hreflang="{l2}" href="{PAGES[l2]["url"]}"/>')
        sitemap.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{PAGES["en"]["url"]}"/>')
        sitemap.append(f'    <image:image><image:loc>{SITE_URL}/img/portrait.jpg</image:loc></image:image>')
        sitemap.append('  </url>')
    sitemap.append('</urlset>')
    open('sitemap.xml', 'w').write('\n'.join(sitemap) + '\n')
    open('robots.txt', 'w').write(f'User-agent: *\nAllow: /\nDisallow: /contact.php\n\nSitemap: {SITE_URL}/sitemap.xml\n')
    manifest = {'name': 'CLARET – Enzo Claret', 'short_name': 'CLARET', 'start_url': '/',
                'display': 'browser', 'background_color': '#F4EFE6', 'theme_color': '#F4EFE6',
                'icons': [{'src': '/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                          {'src': '/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]}
    open('site.webmanifest', 'w').write(json.dumps(manifest, indent=2, ensure_ascii=False) + '\n')


PUBLIC = ['index.html', 'fr/index.html', '404.html', 'contact.php', '.htaccess', 'robots.txt', 'sitemap.xml',
          'site.webmanifest', 'favicon.ico', 'favicon.svg', 'apple-touch-icon.png', 'icon-192.png', 'icon-512.png']


def package():
    os.makedirs('dist', exist_ok=True)
    path = 'dist/claret-site-upload.zip'
    with zipfile.ZipFile(path, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in PUBLIC:
            z.write(f)
        for folder in ('img', 'audio'):
            for name in sorted(os.listdir(folder)):
                z.write(os.path.join(folder, name))
    return path


if __name__ == '__main__':
    src = open('src/index.src.html', encoding='utf-8').read()
    for lang in ('en', 'fr'):
        print('built', build_page(src, lang))
    write_static()
    print('built sitemap.xml, robots.txt, site.webmanifest')
    print('packaged', package())
    if 'YOUR-DOMAIN' in SITE_URL:
        print('\nWARNING: SITE_URL is still a placeholder. Set the real domain before uploading.')
