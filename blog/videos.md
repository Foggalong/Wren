---
title: Video Embed Demo
layout: page
permalink: /video-embed-demo
---

Wren's embedded video player template works with Dailymotion, Google Drive, Streamable, Twitch, Vimeo, and YouTube. It's based on [Jekyll Embed Video]'s template collection but combines them into a [single template][Wren's Embed Video].

[Jekyll Embed Video]: https://github.com/nathancy/jekyll-embed-video
[Wren's Embed Video]: https://github.com/Foggalong/Wren/blob/main/_includes/video-player.html

## Dailymotion

Here video IDs are just the URL code, e.g. [dailymotion.com/video/x8429i4][dailymotion]

[dailymotion]: https://www.dailymotion.com/video/x8429i4

{%- include video-player.html site="Dailymotion" id="x8429i4" alt="Former FBI Agent Breaks Down His Own Body Language" -%}

```liquid
{% raw %}{%- include video-player.html site="Dailymotion" id="x8429i4" alt="Former FBI Agent Breaks Down His Own Body Language" -%}{% endraw %}
```

## Google Drive

Using Google Drive videos is a bit more complicated; [check the README][wiki] for instructions on how to make videos available and where to find the embed ID.

[wiki]: https://github.com/nathancy/jekyll-embed-video#embed-google-drive

{%- include video-player.html site="Google Drive" id="0B7L_dMcaZknxVTRndmdSQ0F5OFE/preview" alt="Road Rage" -%}

```liquid
{% raw %}{%- include video-player.html site="Dailymotion" id="x8429i4" alt="Former FBI Agent Breaks Down His Own Body Language" -%}{% endraw %}
```

## Streamable

Here video IDs are just in URL, e.g. [streamable.com/s9ijg][streamable]

[streamable]: https://streamable.com/s9ijg

{%- include video-player.html site="Streamable" id="s9ijg" alt="Disguised Toast" -%}

```liquid
{% raw %}{%- include video-player.html site="Streamable" id="s9ijg" alt="Disguised Toast" -%}{% endraw %}
```

## Twitch

For Twitch the video IDs are the long string which appears in the URL, e.g. [clips.twitch.tv/StylishChillyTubersDancingBaby][twitch]. For security purposes Twitch also asks for the URL on which the website is being embedded, but provided you've defined `site.url` as standard in your config Wren will handle all that.

[twitch]: https://clips.twitch.tv/StylishChillyTubersDancingBaby

{%- include video-player.html site="Twitch" id="StylishChillyTubersDancingBaby" alt="LCK Production" -%}

```liquid
{% raw %}{%- include video-player.html site="Twitch" id="StylishChillyTubersDancingBaby" alt="LCK Production" -%}{% endraw %}
```

## Vimeo

Here video IDs are just the URL number, e.g. [vimeo.com/22439234][vimeo].

[vimeo]: https://vimeo.com/22439234

{% include video-player.html site="Vimeo" id="22439234" alt="The Mountain" %}

```liquid
{% raw %}{% include video-player.html site="Vimeo" id="22439234" alt="The Mountain" %}{% endraw %}
```

## YouTube

IDs are just the `v` value in the URL, e.g. [youtube.com/watch?v=T1itpPvFWHI][youtube]

[youtube]: https://www.youtube.com/watch?v=T1itpPvFWHI

{% include video-player.html site="YouTube" id="T1itpPvFWHI" alt="Introduction | Jekyll - Static Site Generator | Tutorial 1" %}

```liquid
{% raw %}{% include video-player.html site="YouTube" id="T1itpPvFWHI" alt="Introduction | Jekyll - Static Site Generator | Tutorial 1" %}{% endraw %}
```
