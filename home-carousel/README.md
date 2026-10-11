# Home page dish carousel (Custom Design 146)

A no-JavaScript carousel with 5 slides (What's cooking, Warm soups, Saucy, Crispy, Coconut). It uses CSS scroll-snap for swiping, plus chips and dots as anchor links. Each slide has a hero banner, one tall featured tile and 4 square tiles, and each tile links to `/collection/<slug>`.

1. Fill `image-urls.json` with the hosted image URLs from the existing grids.
2. Check the slugs in `slides.json`. Only bulalo, tinolang-manok, ginisang-munggo and pork-steak are confirmed.
3. Run `python3 build.py`, which writes `carousel.html`.
4. Paste `carousel.html` into the HTML of Custom Design 146 and `carousel.css` into its Custom CSS, then preview before turning it on.
