---
title: Welcome to Wren
author: Renny Wrennington
layout: post
tags: [jekyll]
date: '2021-09-12 20:50:16'
modified_date: '2021-09-13 15:23:01'
first_published_on: Ghost
first_published_url: wren.ghost.org
---

The first thing you'll notice is the post-meta gives more info. [Minima][Minima's post-meta] has the date, modified date, and page authors. Wren improves the modified date formatting[^1], shows the reading time, any tags and authors (both linked to post-list pages), and then finally indicates if the post was originally published elsewhere (given in the frontmatter by service name, or name and URL).

[Minima's post-meta]: https://github.com/jekyll/minima/blob/master/_layouts/post.html#L9-L26

Wren uses [kramdown] rather than [GitHub Flavoured Markdown] for rendering markdown which means that we've access to footnotes[^2], abbreviation syntax from PHP, inline attributes to *change style*{: style="font-family: "Times New Roman", Times, serif; font-stretch: condensed; font-style: italic; text-decoration: underline wavy firebrick;" } without inline HTML, and more. See the [source] for this page to see how it's done.

[kramdown]: https://github.com/gettalong/kramdown
[GitHub Flavoured Markdown]: https://github.github.com/gfm/
[source]: https://github.com/Foggalong/Wren/blob/main/_posts/2021-09-12-welcome-to-wren.md
*[PHP]: PHP Hypertext Preprocessor

![Photo of Me]({{ '/images/profile.jpg' | relative_url }}){: class="left" width="90px" }

Minima's default SASS does have some default stylings for images, but Wren extends that and uses kramdown's image syntax so that our images can be left aligned with text wrap by adding `{: class="left" }` after than standard markdown.

![Photo of Me]({{ '/images/profile.jpg' | relative_url }}){: class="right" width="90px" }

We can similarly right align using `{: class="right" }`. In both cases Wren will automatically add appropriate margins so that the page doesn't get too cluttered. If you're using a thin form-factor the UI will also respond by switching off text-wrapping.

From one medium to another, embedding a video from an external source like

{% include video-player.html site="YouTube" id="T1itpPvFWHI" alt="Intro Video" %}

is as simple as

```liquid
{% raw %}{% include video-player.html site="YouTube" id="T1itpPvFWHI" alt="Jekyll Intro" %}{% endraw %}
```

where `T1itpPvFWHI` is the video ID in the [YouTube URL]. This isn't restricted to YouTube either; it works with [Twitch, Vimeo, and more][demo]!

[YouTube URL]: https://www.youtube.com/watch?v=T1itpPvFWHI
[Jekyll Embed Video]: https://github.com/nathancy/jekyll-embed-video
[demo]: {{ 'video-embed-demo' | relative_url }}

-----

[^1]: It adds an asterisk after the date when a post's been modified and the date of modification appears on hover.
[^2]: Which you've already seen, but there's another one!
