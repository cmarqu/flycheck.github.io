---
title: Colophon
layout: page
---

## Tooling ##

This website is a static website build with [Jekyll][] on Github Pages.  The
pages and posts are written with Markdown.  The Flycheck manual is written with
[Texinfo][], the standard documentation format for Emacs.

[Jekyll]: http://jekyllrb.com
[Texinfo]: https://www.gnu.org/software/texinfo/

## Style and fonts ##

This site uses the Adobe Source family of fonts:

* [Adobe Source Serif Pro](https://github.com/adobe-fonts/source-serif-pro)
  (body text)
* [Adobe Source Sans Pro](https://github.com/adobe-fonts/source-sans-pro)
  (headlines)
* [Adobe Source Code Pro](https://github.com/adobe-fonts/source-code-pro)
  (monospace text and source code)

The CSS is custom, with much inspiration and help by the great book
[Practical Typography][] by [Matthew Butterick][].

[Matthew Butterick]: http://practicaltypography.com/end-credits.html#bio
[Practical Typography]: http://practicaltypography.com/

## Source code, building and deployment ##

The source code of this site is kept at [Github][].  Github Pages builds the
site automatically on every push.

The Texinfo source of the manual is part of the [Flycheck repository][].
A dedicated [Travis CI][] job builds a HTML version of the manual on every push
and commits it to the site repository.

[Github]: https://github.com/flycheck/flycheck.github.io/
[Flycheck repository]: https://github.com/flycheck/flycheck/
[Travis CI]: https://travis-ci.org/flycheck/flycheck
