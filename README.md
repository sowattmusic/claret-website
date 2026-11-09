# CLARET — website

Bilingual (English / French) one-page portfolio for **CLARET**, the professional and recording name of Enzo Claret: record producer, songwriter & composer, artistic director, associate at Sowatt Music.

It is a plain static site (HTML, CSS, a little JavaScript) plus one PHP file for the contact form. No build step, no framework.

## Files

| Path | What it is |
|---|---|
| `index.html` | The whole site: content in both languages, styles and scripts |
| `contact.php` | Sends contact-form messages to enzo@sowattmedia.com |
| `favicon.svg` | Browser-tab icon |
| `img/` | Portrait, session photo, gallery photos, covers, Sowatt logo |
| `audio/just-the-same.mp3` | ~20-second excerpt of "Just the Same" |
| `CLAUDE.md` | Project notes for Claude Code (design rules, content rules, open items) |
| `LISEZ-MOI.txt` | Upload instructions in French |

## Preview locally

Open `index.html` in a browser. Everything works except the contact form, which needs PHP (it works once the site is on N0C).

## Publish on N0C (PlanetHoster)

1. Log in to N0C with the Sowatt account.
2. **Domains**: add the site's domain (or a test subdomain such as `claret.sowattmedia.com`) and note its document root folder.
3. **File Manager**: open that folder and upload the files of this repository (everything except `CLAUDE.md`, `README.md` and `.gitignore`, which are harmless if uploaded).
4. **SSL/TLS**: make sure the free Let's Encrypt certificate is active.
5. Test: switch EN/FR, play the audio excerpt, send yourself a message through the form.

If form messages don't arrive, check the spam folder of enzo@sowattmedia.com, then check in N0C that PHP mail sending is allowed for the domain (messages are sent from `no-reply@<domain>`).

## Language switch

Every piece of text exists twice, as `<span lang="en">…</span><span lang="fr">…</span>`. The EN/FR buttons set `data-lang` on `#site`, and CSS hides the other language. When you add or change text, always update both languages.
