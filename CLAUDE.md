# CLARET website — notes for Claude Code

Owner: **Enzo Claret** ("Claret"), associate at Sowatt Media / Sowatt Music (Crissier). He leads the artistic side (production, composition, arrangement, artistic direction); his partner Michel Gallone leads the technical side (recording, mixing, mastering).
Contact on the site: enzo@sowattmedia.com · +41 78 628 69 70.

## What the site is

A one-page, bilingual EN/FR portfolio and "business card" so people can hire him. It presents his work for other artists first, with his own music alongside. Copy is written in the first person, plainly; avoid flowery or "AI-sounding" sentences.

Section order in `index.html`:
Header (CLARET wordmark, nav, EN/FR) → Hero → My Story → Gallery → Services → Sowatt band → Selected Work (titled "Productions" in French) → Behind the Record (TDenon) → In Their Words → Press → Contact → Footer.

## Design rules (keep them)

- Feel: an independent record sleeve turned into a contemporary portfolio; 1970s music-magazine cover confidence.
- Colours: warm ivory `#F4EFE6` (main background), near-black `#171515` (type, dark bands), deep wine `#682638` used sparingly (primary button, play buttons, small accents). Tokens are in `:root` at the top of the stylesheet. Single light look, no dark mode.
- Type: **League Gothic** for the oversized CLARET wordmark, section titles and project titles; **Archivo** for everything else (nav, copy, credits). Both from Google Fonts.
- Square edges everywhere (no rounded corners), thin 1px rules, generous margins.
- Covers and photos keep their own colours.
- Hero: wordmark, role line and buttons on the left; portrait on the right, **in colour** (never black and white), blending into the ivory with a soft mask fade (left edge and bottom). "Listen to my work" is the strong wine button; "Work with me" is a quieter underlined link. On mobile: name, roles, Listen button first, then the portrait fading in.
- Selected Work is a record catalogue: large square cover, label row (format · year), big title, artist line, role line, one clear action button. Same structure on every card.

## Content rules (confirmed by Enzo)

- Credits:
  - Ce Soir — Claret & Le Tremplin – Un Seul Juge : Le Public, season anthem, 2025 — producer, composer, arranger and co-writer. Sung by the finalists, including Lady O (winner of The Voice France 2026).
  - DIDICI — Sarabds, four-track EP, 2026 — producer, composer, arranger, keyboards and programming.
  - Colosse aux Pieds d'Argiles — TDenon, album, 2026 — **same credits as DIDICI**.
  - Courant éclair — Jules Loewert, single, 2025 — co-composer.
  - NIHIL — Gravv (YouTube channel, ~25,000 subscribers), ongoing — lead composer. Buttons: "NIHIL 1" and "NIHIL 2".
  - Just the Same — Claret, his own song: **unreleased, out in 2027**, recorded in London 2025 — writer, composer, arranger, producer, recording engineer and lead vocals. No official cover yet: keep the plain wine square with a minimal ivory record, **no text on it**.
- Links: Spotify only on the project cards (no Apple Music buttons). Sarabds' "The Search" is audio only on YouTube, not a music video, so it has no link.
- Full credits: Muso.ai profile https://credits.muso.ai/profile/d6ebee4e-29ee-4048-905b-eb54b84a2853/credits
- My Story facts: born in Sion, grew up in Lutry, making music since age ten; grew up on the Beatles, James Brown, David Bowie; started at Swiss Artists Productions; in August 2025 recorded at Joe Lyons' Palace Garden Studio in London, with songs written only a few days before. Don't mention the "ten finalists".
- Services: record production, songwriting & composition, music for picture, arrangement, artistic direction, recording & vocal production, session planning, live recording & live albums. Transcription and multilingual subtitling (plus live concert recordings) are described in the Sowatt band, not the services list.
- Gallery: four photos only — ties portrait (top left), with ANDREA in London (top right, wide), Le Tremplin stage (bottom left, wide), TDGarden Studios 2024 (bottom right).
- Press: Le Courrier, 27 March 2025, article on the Tremplin 2025 final.
- French wording: use "Productions", not "Réalisations".

## Technical notes

- Every text exists in both languages as `<span lang="en">` / `<span lang="fr">`; the switch sets `data-lang` on `#site`. Always edit both.
- `contact.php` uses PHP `mail()`; the form posts to it with `fetch` and shows messages in both languages. A hidden "website" field traps spam bots.
- The TDenon excerpt (12:01–12:58) is embedded from youtube-nocookie; his testimonial links to 4:54–5:16 of the same video (6F4UV0RGobQ).
- Hosting: N0C (PlanetHoster), the same as michelgallone.ch and Route 108. Upload the files to the domain's document root.

## Still to do

1. Legal notice (Impressum) and privacy policy page — needs Sowatt Media Sàrl's address.
2. Direct Spotify links for Ce Soir, Colosse aux Pieds d'Argiles and Courant éclair (currently Spotify search links).
3. Photo of Enzo with Lady O by Delphine Broggio for the Press section (credit the photographer).
4. Choose the domain; then set absolute URLs for `og:image` and add a sitemap.
5. Later (2027 release): real cover for "Just the Same", release section, newsletter sign-up.
