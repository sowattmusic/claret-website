# CLARET — website

Bilingual (English / French) one-page portfolio for **CLARET**, the professional and recording name of Enzo Claret: record producer, songwriter & composer, artistic director, associate at Sowatt Music.

It is a plain static site (HTML, CSS, a little JavaScript) plus one PHP file for the contact form. No build step, no framework.

## Files

| Path | What it is |
|---|---|
| `index.html` | English page (`/`): content, styles and scripts |
| `fr/index.html` | French page (`/fr/`) |
| `404.html` | Custom “page not found” page |
| `robots.txt`, `sitemap.xml` | For search engines |
| `site.webmanifest`, `favicon.*`, `apple-touch-icon.png`, `icon-*.png` | Icons for browsers and phones |
| `contact.php` | Sends contact-form messages to enzo@sowattmedia.com |
| `favicon.svg` | Browser-tab icon |
| `img/` | Portrait, session photo, gallery photos, covers, Sowatt logo, share images (`share-en.jpg`, `share-fr.jpg`) |
| `audio/just-the-same.mp3` | ~20-second excerpt of "Just the Same" |
| `CLAUDE.md` | Project notes for Claude Code (design rules, content rules, open items) |
| `LISEZ-MOI.txt` | Upload instructions in French |

## Preview locally

Run `php -S localhost:8080` in this folder and open http://localhost:8080/ (English) and http://localhost:8080/fr/ (French). Opening the file directly also works, but the `/fr/` links and the contact form need a server.

## Publish on N0C (PlanetHoster)

1. Log in to N0C with the Sowatt account.
2. **Domains**: add the site's domain (or a test subdomain such as `claret.sowattmedia.com`) and note its document root folder.
3. **File Manager**: open that folder and upload the files of this repository (everything except `CLAUDE.md`, `README.md` and `.gitignore`, which are harmless if uploaded).
4. **SSL/TLS**: make sure the free Let's Encrypt certificate is active.
5. Test: switch EN/FR, play the audio excerpt, send yourself a message through the form.

If form messages don't arrive, check the spam folder of enzo@sowattmedia.com, then check in N0C that PHP mail sending is allowed for the domain (messages are sent from `no-reply@<domain>`).

## Language switch

The site has two pages: English at `/` (`index.html`) and French at `/fr/` (`fr/index.html`). The EN/FR buttons link between them. When you add or change text or layout, always update both files.

## History

Every version is a commit in the GitHub history and is described, with its commit ID, in `CHANGELOG.md`. To look at an old version, open `https://github.com/sowattmusic/claret-website/tree/<commit ID>`, or create a GitHub Release for it so it appears under **Tags**. Old versions are not kept in a folder, so they can never be uploaded to the server by mistake.
