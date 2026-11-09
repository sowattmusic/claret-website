# CLARET — SEO guide

What is already built into the site, and the few steps only you can do (they need your accounts).

## Already done in the site

- **Two real pages:** English at `/`, French at `/fr/`. Each contains only its own language, with its own title and description, so Google indexes both and shows the right one to French and English searchers. They are linked to each other with `hreflang` tags.
- **Titles and descriptions:**
  - EN: *Enzo Claret (CLARET) – Record Producer & Composer*
  - FR: *Enzo Claret (CLARET) – Producteur & compositeur*
- **Structured data (JSON-LD):** tells Google who you are — Enzo Claret, alias CLARET, your roles, Sowatt Media, and your Spotify, Apple Music, Instagram, LinkedIn and Muso.ai profiles. This helps Google connect your name to all those profiles.
- **Share previews** for Facebook, Instagram, WhatsApp, LinkedIn, X and iMessage: a 1200×630 image (`img/share-en.jpg`, `img/share-fr.jpg`) with your portrait and the CLARET wordmark, plus title and description.
- **Icons** for browser tabs, iPhone home screen and Android (`favicon.ico`, `favicon.svg`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png`, `site.webmanifest`).
- **`sitemap.xml`** and **`robots.txt`** for search engines.
- **`.htaccess`** (Apache on N0C): forces https, one single address (no www), compression, browser caching, clean URLs, a designed 404 page.
- **Speed:** image sizes declared (no layout jumps), the hero portrait loads first, other images load lazily.

## 1. Set the domain (once)

The final address must be written into the site before it goes online.

1. Open `tools/build.py` and set `SITE_URL`, e.g. `SITE_URL = "https://claret.ch"` (no slash at the end).
   - The `.htaccess` sends `www.` to the address without `www.`. If you prefer `www.`, see the comment in `.htaccess`.
2. Run `python3 tools/build.py` (or ask Claude Code to do it).
3. Upload the contents of `dist/claret-site-upload.zip` to the domain's folder on N0C and extract it.

## 2. Google Search Console

1. Go to https://search.google.com/search-console and sign in with a Google account you'll keep (e.g. sowattmusic@gmail.com).
2. **Add property → Domain** and type your domain (without https).
3. Google gives you a **TXT record**. Add it in the DNS settings of the domain (in N0C: *Domains → DNS zone*, or wherever the domain was bought). Then click **Verify**. It can take a few minutes to a few hours.
   - Alternative: choose **URL prefix** instead, pick "HTML tag", copy the code inside `content="…"` into `GOOGLE_VERIFICATION` in `tools/build.py`, rebuild and upload.
4. Left menu **Sitemaps** → enter `sitemap.xml` → **Submit**.
5. **URL inspection** → paste `https://yourdomain/` → **Request indexing**. Do the same for `https://yourdomain/fr/`.
6. Check back after a few days: *Pages* (indexing), *Performance* (searches that show your site).

## 3. Bing Webmaster Tools (also covers DuckDuckGo, Ecosia, Yahoo)

1. Go to https://www.bing.com/webmasters and sign in.
2. Choose **Import from Google Search Console** — it copies the site and sitemap in one click.
   (Otherwise: add the site, verify with the XML file, meta tag `BING_VERIFICATION` or DNS, then submit `sitemap.xml`.)
3. In Bing, open **URL Submission** and submit both pages.

## 4. Check the share previews

After the site is online, paste your address into each tool to see (and refresh) the preview:

- Facebook / Instagram / WhatsApp: https://developers.facebook.com/tools/debug/ → *Scrape Again*
- LinkedIn: https://www.linkedin.com/post-inspector/
- X (Twitter): post the link in a draft; the large image card appears automatically.
- Google rich results check: https://search.google.com/test/rich-results
- Speed: https://pagespeed.web.dev/

## 5. What makes the biggest difference now: links to your site

For a personal name, Google mostly decides from other sites that point to yours. Add your new address to:

- [ ] Instagram bio (@itsclaret) and LinkedIn profile (*Contact info → Website*)
- [ ] Muso.ai profile (website field)
- [ ] Spotify for Artists and Apple Music for Artists bio
- [ ] sowattmedia.com — a team / "Enzo Claret" link to the site
- [ ] Route 108's site (members page)
- [ ] YouTube channel (Gravv collaboration, your own channel if any)
- [ ] Ask artists you worked with (TDenon, Sarabds, Jules Loewert, Le Tremplin) to credit and link CLARET in their bios or video descriptions
- [ ] Le Courrier and future press: ask for a link to the site in online articles

Use the same name everywhere: **Enzo Claret (CLARET)**.

## 6. Keep it fresh

- Add each new production to Selected Work as soon as it's out (then rebuild and upload).
- In 2027, a release section for "Just the Same" with its own cover and Spotify link.
- A legal notice and privacy page also count as trust signals for Google (still to do).
