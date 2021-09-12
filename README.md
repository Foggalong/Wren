# Wren

[![Jekyll CI Status]][jekyll-ci-link]
[![CodeFactor Rating]][codefactor-link]
[![MIT Licensed]][license-link]

[Jekyll CI Status]: https://img.shields.io/github/workflow/status/Foggalong/Wren/Jekyll%20CI?label=Jekyll%20CI
[jekyll-ci-link]: https://github.com/Foggalong/Wren/actions/workflows/codeql-analysis.yml
[CodeFactor Rating]: https://img.shields.io/codefactor/grade/github/foggalong/wren/main?color&label=CodeFactor
[codefactor-link]: https://www.codefactor.io/repository/github/foggalong/wren
[MIT Licensed]: https://img.shields.io/badge/License-MIT-brightgreen.svg
[license-link]: #licenses

A paper-style theme for [Jekyll]. Check out the GitHub pages [deployment] to see what the default looks like and read on for information on usage and customisation. Be aware that this **beta** software so will contain bugs; use it at your own risk.

[Jekyll]: https://jekyllrb.com
[deployment]: https://foggalong.github.io/Wren
[wiki]: https://github.com/Foggalong/Wren/wiki

## Features

- 📱 Responsive, [customisable] design
- 🕔 See post reading time
- 🏷️ Browse posts by category
- 📺 Embedded YouTube videos
- 📃 Optional [pagination]
- 📰 Atom/RSS feed of posts
- 📈 In-built search engine optimization

[customisable]: #custom-styling
[pagination]: #pagination

## Installing

Whether you fork this repo or start from scratch there are two supported options for using Wren as your theme. Which works better for you will depend on your personal priorities.

### Theme Gem

Use the `jekyll-wren` gem, fetched automatically from [RubyGems] or downloaded from the [releases page] and installed locally. Either way you'll need to add

```yaml
theme: jekyll-wren
```

to your [config] and

```ruby
gem "jekyll-wren", "~> 0.3"
```

to your [Gemfile] plugins list.

The upsides are that builds will be quicker and you'll have more control over the version through the Gemfile. The downside is that it will prevent building with GitHub Pages' builder since Wren isn't on the [whitelist] (though you'll still be able to build locally and push to a GitHub pages branch/repo).

[RubyGems]: https://rubygems.org
[releases page]: https://github.com/Foggalong/Wren/releases/latest
[config]: https://github.com/Foggalong/Wren/blob/main/_config.yml#L22-L23
[Gemfile]: https://github.com/Foggalong/Wren/blob/main/Gemfile#L22-L28

### Remote Theme

It's possible to use the theme directly from this repo. You'll need to add

```yaml
plugins:
  - jekyll-remote-theme

remote_theme: foggalong/wren@v0.3-beta
```

to your [config] and then

```ruby
gem "jekyll-remote-theme", "~> 0.4"
```

to your [Gemfile] plugins list.

The upside is that this will work with GitHub Pages' builder ([Jekyll Remote Theme] is on the [whitelist]). The downsides are that builds will be slower and your [version control] is slightly weaker; you're tied to `HEAD` or a specific version.

[Jekyll Remote Theme]: https://github.com/benbalter/jekyll-remote-theme
[version control]: https://github.com/benbalter/jekyll-remote-theme#declaring-your-theme

## Config Options

The [config.yml] in this repo can be used as a template for your own Wren instance. The file is thoroughly commented so it's worth having a read to know all the options available.

[config.yml]: https://github.com/Foggalong/Wren/blob/main/_config.yml]

## Custom Styling

Like [Minima] (on which Wren's [SASS] is built) there are a whole bunch of variables which you can change to personalise the theme. To do this you just add lines such as

```scss
$background-color: #3d9da3;
```

to [`assets/style.scss`] and you're good to go. The list of what's customisable is slightly different (and longer!) than Minima so have a look at the full list of [style variables].

[Minima]: https://github.com/jekyll/minima
[`assets/style.scss`]: https://github.com/Foggalong/Wren/blob/main/assets/style.scss
[style variables]: https://github.com/Foggalong/Wren/blob/main/_sass/wren/initialize.scss#L10-L87

## Pagination

If the following two [config.yml] lines aren't commented, Wren will use [Jekyll Paginate][Paginate] to split the posts page into multiple pages of `paginate` many posts with url `paginate_path`.

```yaml
paginate: 5
paginate_path: "/blog/:num"
```

Note that due to [Paginate]'s technical limitations this will only happen on the main posts page, not other post lists such as the categories page. It's generally quite limited in how it works compared to [Paginate v2], but the latter isn't on the [whitelist].

Another caveat is that, if you're using Paginate, the main post list page **must** have filename `index.html`; that's why in this repo it's `blog/index.html`. If you're not using Paginate though, Wren allows you to put that file anywhere and called whatever you like without problems.

[Paginate v2]: https://github.com/sverrirs/jekyll-paginate-v2

## Error Pages

Wren includes [`error.html`], a layout for formatting error pages; they're centered, have different spacing, and slightly different `<h1>` formatting. In [`errors/`] there are some examples; those aren't in the theme-gem (see [#25]) but to use them just copy to your website's repo. See this [tutorial] for configuring error pages on GitHub pages, Apache, and Nginx.

[`error.html`]: https://github.com/Foggalong/Wren/blob/main/_layouts/error.html
[`errors/`]: https://github.com/Foggalong/Wren/tree/main/errors
[#25]: https://github.com/Foggalong/Wren/issues/25
[tutorial]: https://jekyllrb.com/tutorials/custom-404-page

## Philosophy

I ❤️ [Wrens]. They're smol, quick, and rotund. When I was little we had a family of them come nest in our garden and they sang the most brilliant songs. Oh wait? You're saying this was supposed to be the project's philosophy? Let's just just say it's to be small, fast, and round.

[Wrens]: https://en.wikipedia.org/wiki/Wren

## Licenses

Wren is released under the [MIT License] and is built with [Jekyll] and a whole host of other MIT licensed projects.

[MIT License]: https://choosealicense.com/licenses/mit

In order to remain compatible with GitHub Pages Wren only uses plugins from the [whitelist]. Massive props to [Remote Theme], [Feed], [Paginate], and [SEO] for doing their thing in the background without me needing to worry about it. Further features are achieved through [Liquid] templates, some of which are based on existing Ruby plugins. These include [Reading Time], [Embed Video], [Tag Cloud].

[whitelist]: https://pages.github.com/versions
[Remote Theme]: https://github.com/benbalter/jekyll-remote-theme
[Feed]: https://github.com/jekyll/jekyll-feed
[Paginate]: https://github.com/jekyll/jekyll-paginate
[SEO]:  https://github.com/jekyll/jekyll-seo-tag
[Liquid]: https://github.com/Shopify/liquid
[Reading Time]: https://github.com/risan/jekyll-reading-time
[Embed Video]: https://github.com/nathancy/jekyll-embed-video
[Tag Cloud]: https://superdevresources.com/tag-cloud-jekyll

Style wise, Wren's [SASS] is forked from [Minima] which proved crucial in knowing what did and didn't need to be covered by Jekyll themes. The icons (apart from are based on designs from [Font Awesome], redrawn for the smaller form factor. Credit also to Antoine Boulanger's guide on [SVG Favicons].

[SASS]: https://sass-lang.com
[Font Awesome]: https://github.com/Rush/Font-Awesome-SVG-PNG
[SVG Favicons]: https://medium.com/swlh/are-you-using-svg-favicons-yet-a-guide-for-modern-browsers-836a6aace3df

The only part of Wren _not_ MIT licensed is the [default profile image], a [CC-BY-NC] licensed [photo] of a Bewick Wren taken by [Minette Layne].

[default profile image]: images/profile-hq.jpg
[photo]: https://flic.kr/p/4E9FY2
[Minette Layne]: https://www.flickr.com/people/minette_layne
[CC-BY-NC]: https://creativecommons.org/licenses/by-nc/2.0
