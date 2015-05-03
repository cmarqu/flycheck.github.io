---
title: Colophon
layout: page
---

Tooling
=======

This website is a static website build with [Jekyll][] on Github Pages.  The
pages and posts are written with Markdown.  The Flycheck manual is written with
[Texinfo][], the standard documentation format for Emacs.

[Jekyll]: http://jekyllrb.com
[Texinfo]: https://www.gnu.org/software/texinfo/

Style and fonts
===============

The main font on this website is [Lato][] by Łukasz Dziedzic.  It appears in the
entire body text and the headlines. The monospace font is
[Adobe Source Code Pro][].  It is used for `inline code` and code snippets.

The CSS is custom, with much inspiration and help by the great book
[Practical Typography][] by [Matthew Butterick][].

[Lato]: http://www.latofonts.com
[Adobe Source Code Pro]: https://github.com/adobe-fonts/source-code-pro
[Matthew Butterick]: http://practicaltypography.com/end-credits.html#bio
[Practical Typography]: http://practicaltypography.com/

Source code, building and deployment
====================================

The source code of this site is kept at [Github][].  Github Pages builds the
site automatically on every push.

The Texinfo source of the manual is part of the [Flycheck repository][].
A dedicated [Travis CI][] job builds a HTML version of the manual on every push
and commits it to the site repository.

[Github]: https://github.com/flycheck/flycheck.github.io/
[Flycheck repository]: https://github.com/flycheck/flycheck/
[Travis CI]: https://travis-ci.org/flycheck/flycheck
