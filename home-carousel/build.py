"""Build the Custom Design 146 HTML from slides.json + image-urls.json.

Usage: python3 build.py            -> writes carousel.html
Empty URLs are left as {{pN}} placeholders and listed as warnings.
"""
import html, json, pathlib

here = pathlib.Path(__file__).parent
slides = json.loads((here / "slides.json").read_text())
urls = json.loads((here / "image-urls.json").read_text())
missing = []

def src(key):
    if urls.get(key):
        return html.escape(urls[key], quote=True)
    missing.append(key)
    return "{{" + key + "}}"

out = ['<div class="sk-car">', '  <nav class="sk-chips">']
for s in slides:
    out.append(f'    <a class="sk-chip" href="#sk-{s["id"]}">{html.escape(s["chip"])}</a>')
out += ['  </nav>', '  <div class="sk-track">']
for s in slides:
    out += [f'    <section class="sk-slide" id="sk-{s["id"]}">',
            '      <div class="sk-head">',
            f'        <h2 class="sk-title">{html.escape(s["chip"])}</h2>',
            '        <a class="sk-all" href="/collections">See all</a>',
            '      </div>',
            f'      <img class="sk-hero" src="{src(s["hero"])}" alt="{html.escape(s["chip"])}" loading="lazy">',
            '      <div class="sk-grid">']
    for i, (key, name, slug) in enumerate(s["tiles"]):
        cls = "sk-tile sk-tall" if i == 0 else "sk-tile"
        out.append(f'        <a class="{cls}" href="/collection/{slug}"><img src="{src(key)}" alt="{html.escape(name)}" loading="lazy"></a>')
    out += ['      </div>', '    </section>']
out += ['  </div>', '  <div class="sk-dots">']
for s in slides:
    out.append(f'    <a class="sk-dot" href="#sk-{s["id"]}" aria-label="{html.escape(s["chip"])}"></a>')
out += ['  </div>', '</div>', '']
(here / "carousel.html").write_text("\n".join(out))
print("wrote carousel.html")
if missing:
    print("missing image URLs:", ", ".join(missing))
