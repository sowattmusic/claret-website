# Changelog

Every version is a commit in the GitHub history, so any of them can be viewed or restored.
Commit IDs are given below; on GitHub, open `https://github.com/sowattmusic/claret-website/tree/<commit>` to browse that version.
To make a version easier to find, create a GitHub Release with the tag name shown (Releases → Draft a new release → choose a tag → target: that commit).

## v2.0 — 10 November 2026: live site synced into the repo

Commit: `169375f` (branch `claude/brave-curie-znvqea`).

The repository now matches what is online at https://claretproductions.com (downloaded on 10 Nov 2026).

- Separate pages per language: English at `/`, French at `/fr/` (previously one page with an EN/FR toggle).
- SEO: new page titles and descriptions, canonical and hreflang links, Open Graph and Twitter tags with absolute URLs, structured data (JSON-LD) for Enzo Claret.
- New share images `img/share-en.jpg` and `img/share-fr.jpg` (1200×630).
- New files: `404.html`, `robots.txt`, `sitemap.xml`, `site.webmanifest`, `favicon.ico`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`.
- Photos, covers, audio and `favicon.svg`: unchanged (byte-for-byte identical).
- `contact.php`: kept from v1.0. Its source can't be downloaded from the web; the live one behaves the same.
- Not in the repo: the server's `.htaccess` (www redirect, 404 page).

## v1.0 — original upload

Commit: `d44f185`.

Single bilingual page (`index.html`) with an EN/FR switch, `contact.php`, images and audio excerpt.
