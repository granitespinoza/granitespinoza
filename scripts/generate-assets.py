"""Original, deterministic profile graphics. Requires Pillow for PNG output."""
from pathlib import Path
from html import escape
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets'
OUT.mkdir(exist_ok=True)
FONT_DIR = Path('/System/Library/Fonts')
fonts = list(FONT_DIR.rglob('Helvetica.ttc')) + list(FONT_DIR.rglob('Arial.ttf'))
if not fonts:
    raise RuntimeError('Provide a TrueType/OTF font in FONT_DIR.')

def font(size):
    return ImageFont.truetype(str(fonts[0]), size)

for theme, bg, fg, muted in [('dark', '#101827', '#f1f5f9', '#a9b7c9'), ('light', '#edf4fa', '#142238', '#506078')]:
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="350" viewBox="0 0 1200 350" role="img" aria-labelledby="title desc">
<title id="title">Granit Espinoza — Software Engineer and Product Builder</title>
<desc id="desc">Full-stack, SaaS and Digital Health. Decorative product, services and data blocks.</desc>
<rect width="1200" height="350" rx="22" fill="{bg}"/>
<path d="M55 50H145" stroke="#26b8c6" stroke-width="5"/>
<g font-family="Arial, Helvetica, sans-serif">
<text x="55" y="102" font-size="15" letter-spacing="3" fill="{muted}">GRANIT ESPINOZA SALAZAR</text>
<text x="55" y="165" font-size="43" font-weight="700" fill="{fg}">Software Engineer</text>
<text x="55" y="215" font-size="39" font-weight="700" fill="{fg}">&amp; Product Builder.</text>
<text x="55" y="265" font-size="19" fill="{muted}">Full-stack · SaaS · Digital Health</text>
<text x="55" y="307" font-size="14" fill="{muted}">From real problems to useful products.</text>
<g stroke="#26b8c6" stroke-width="2" fill="none">
<rect x="855" y="73" width="265" height="58" rx="12"/>
<rect x="855" y="163" width="265" height="58" rx="12"/>
<rect x="855" y="253" width="265" height="58" rx="12"/>
<path d="M987 131V163M987 221V253"/>
</g>
<g font-size="18" text-anchor="middle" fill="{fg}">
<text x="987" y="109">PRODUCT</text><text x="987" y="199">SERVICES</text><text x="987" y="289">DATA</text>
</g></g></svg>'''
    (OUT / f'banner-{theme}.svg').write_text(svg)

# LinkedIn cover: leave the lower-left area clear for the profile photo.
im = Image.new('RGB', (1584, 396), '#101827')
d = ImageDraw.Draw(im)
d.line((620, 62, 710, 62), fill='#26b8c6', width=5)
d.text((620, 90), 'GRANIT ESPINOZA SALAZAR', font=font(25), fill='#a9b7c9')
d.text((620, 135), 'Software Engineer', font=font(48), fill='#f1f5f9')
d.text((620, 190), '& Product Builder.', font=font(48), fill='#f1f5f9')
d.text((620, 266), 'Full-stack  /  SaaS  /  Digital Health', font=font(25), fill='#a9b7c9')
for y, label in [(85, 'PRODUCT'), (175, 'SERVICES'), (265, 'DATA')]:
    d.rounded_rectangle((1295, y, 1515, y+58), radius=12, outline='#26b8c6', width=2)
    d.text((1405, y+29), label, anchor='mm', font=font(20), fill='#f1f5f9')
    if y < 265:
        d.line((1405, y+58, 1405, y+90), fill='#26b8c6', width=2)
im.save(OUT / 'linkedin-cover.png')
print('Generated two SVG banners and a LinkedIn PNG cover.')
