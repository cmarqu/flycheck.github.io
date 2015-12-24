---
layout: default
title: Syntax checking for GNU Emacs
---

Flycheck <small>Syntax checking for GNU Emacs</small>
=====================================================

Flycheck is a modern on-the-fly syntax checking extension for GNU Emacs,
intended as replacement for the older Flymake extension which is part of GNU
Emacs.

It uses various syntax checking and linting tools to automatically check the
contents of buffers while you type, and reports warnings and errors directly in
the buffer, or in an optional error list:

[![Annotated screenshot of Flycheck](manual/latest/images/flycheck-annotated.png)](manual/latest/images/flycheck-annotated.png)

Features
--------

- Supports over 30 programming and markup languages with more than 60 different
  syntax checking tools
- Fully automatic, fail-safe, on-the-fly syntax checking in background
- Nice error indication and highlighting
- Optional error list popup
- Many customization options
- [Comprehensive documentation]({{ "/resources.html" | prepend: site.baseurl}})
- A simple interface to define new syntax checkers
- A “doesn't get in your way” guarantee
- Many [3rd party extensions]({{ "/extensions.html" | prepend: site.baseurl}})

Help
----

Flycheck comes with a comprehensive manual.  You can read this manual in Emacs
with `M-x flycheck-info`, provided that you already installed Flycheck.  The
latest manual is [available online](manual/latest/index.html).

If you have questions about Flycheck or need help with a particular problem
please ask a question on
[Stack Exchange](https://emacs.stackexchange.com/questions/tagged/flycheck).  If
you found a bug in Flycheck please report it to our
[issue tracker](https://github.com/flycheck/flycheck/issues).

Latest news
-----------

<div class="post-list">
<dl>
{% for post in site.posts limit: 5 %}
<dt>{{ post.date | date_to_string }}</dt>
<dd><a href="{{site.baseurl}}{{post.url}}">{{ post.title | escape }}</a></dd>
{% endfor %}
</dl>
</div>
