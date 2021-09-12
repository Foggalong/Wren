# Contribution Guidelines

Thanks for your interest in contributing to Wren! Make sure you're happy submitting your contribution under the [MIT License], working by the [Code of Conduct], and have read the rest of this document.

[MIT License]: https://choosealicense.com/licenses/mit
[Code of Conduct]: https://github.com/Foggalong/Wren/blob/main/.github/CODE_OF_CONDUCT.md

Regardless what kind of contribution you're making, your editor should be using the [.editorconfig], and, of course, it must [build]!

[.editorconfig]: https://github.com/Foggalong/Wren/blob/main/.editorconfig
[build]: https://github.com/Foggalong/Wren/blob/main/build

## Adding Features

Please note that the theme in this repo is a personal project and I have limited capacity to maintain features I won't be personally using. For that reason I may reject pull requests if they're implementing features I don't want or that I would implement differently. That said, I'd still love to see your contributions!

This project strives to be usable with GitHub Pages. If your contribution depends on a Gem which isn't on the [whitelist] make sure it's optional and fails gracefully when used there. Even better, see if your feature can be implemented using a [Liquid] template instead (like [Jekyll Reading Time] was in [reading-time.html])

[whitelist]: https://pages.github.com/versions
[Liquid]: https://shopify.github.io/liquid
[Jekyll Reading Time]: https://github.com/risan/jekyll-reading-time
[reading-time.html]: https://github.com/Foggalong/Wren/blob/main/_includes/reading-time.html

## Markdown

Any changes to markdown need to be [markdownlint] compliant using this [linter config]. GitHub actions will check any contribution submitted against that and report back with errors.

[markdownlint]: https://github.com/DavidAnson/markdownlint
[linter config]: https://github.com/Foggalong/Wren/blob/main/.github/workflows/markdownlint-config.json

## SASS

If you're adding new elements or classes make sure they are appropriately styled, ideally inherited from or similar to other similar elements. Don't hardcode any colours, shadows, or spacing in `content.scss` or `layout.scss`; define [style variables] in `initialize.scss`.

[style variables]: https://github.com/Foggalong/Wren/blob/main/_sass/wren/initialize.scss#L10-L87

## Graphics

With the exception of the profile image and PNG favicon, all graphics are vectors. While Wren's icon designs are based on [Font Awesome], significant changes from upstream have been made to optimize for usage, remove cruft, and reduce filesize.  

[Font Awesome]: https://github.com/Rush/Font-Awesome-SVG-PNG

### Navigation Icons

If you're changing or adding a navigation icon make sure they're saved and aligned to grid at 24×24. The `<svg>` element needs the property `id="nav"` to so it can be brought in my the [navigation.html] Liquid template.

[navigation.html]: https://github.com/Foggalong/Wren/blob/main/_includes/navigation.html#L14
[Home icon]: https://github.com/Foggalong/Wren/blob/main/assets/nav-icons/home.svg

### Social Icons

If you're changing or adding a social icon make sure they're aligned to grid as closely as possible at 16×16. The `<svg>` element needs the property `id="soc"` to so it can be brought in my the [social-list.html] Liquid template.

[social-list.html]: https://github.com/Foggalong/Wren/blob/main/_includes/social-list.html#L42

You'll also need to add a default username object to [wren.social_links] and a default website information to [wren_social_data]. If you were adding Google+ for example, this might be:

```yaml
wren:
  social_links:
    google-plus:
    - username: jekyll
      id: 111311916570668380146

wren_social_data:
  google-plus:
  - name: Google+ 
  - url: plus.google.com/u
```

Note the URL is for the path to a profile link minus the `id`, _not_ the website's root URL (e.g. `plus.google.com`).

[wren_social_data]: https://github.com/Foggalong/Wren/blob/main/_config.yml#L113-L163
[wren.social_links]: https://github.com/Foggalong/Wren/blob/main/_config.yml#L60-L91

### Removing Cruft

I recommend using [Inkscape] with [scour] for editing vector graphics. Before saving the file make sure there are no strokes, objects, or groups left in the design. Any fills should be coloured `#000000` so you can identify and remove them later.

You should then save as an 'optimized SVG' using the following settings:

- Number of significant digits for coordinates: 5
- Shorten colour values
- Convert CSS attributes to XML attributes
- Collapse groups
- Work around renderer bugs
- Remove metadata
- Remove comments
- Format output with linebreaks and indentation
  - Indention character: space
  - Depth of indentation
- Remove unused IDs
- Preserve manually created IDs not ending with digits

[Inkscape]: https://inkscape.org
[scour]: https://github.com/scour-project/scour

After saving the SVG open it in a text editor and make sure:

- no stokes, objects, or groups,
- there's no `<xml>` header element,
- the `xmlns` property is in `<svg>`,
- the `id=$TAG` anchor hasn't disappeared,
- any `fill:`, `fill-rule:`, etc are removed

### Example

The example below is for the [Home icon] and shows how the SVG for a navigation icon should typically look.

```svg
<svg id="nav" width="24" height="24" xmlns="http://www.w3.org/2000/svg">
 <path d="m12 7-8 8v6a1 1 0 0 0 1 1h5v-6h4v6h5a1 1 0 0 0 1-1v-6l-8-8z"/>
 <path d="m12 2-11 11 1.3398 1.3398 9.6602-9.3398 9.5 9.5 1.5-1.5-3-3v-4c0-0.554-0.446-1-1-1h-1c-0.554 0-1 0.446-1 1v1z"/>
</svg>
```
