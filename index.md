---
layout: index
---

Flycheck <small>Syntax checking for GNU Emacs</small>
=====================================================

Flycheck is a modern on-the-fly syntax checking extension for GNU Emacs,
intended as replacement for the older Flymake extension which is part of GNU
Emacs.

It uses various syntax checking and linting tools to automatically check the
contents of buffers while you type, and reports warnings and errors directly in
the buffer, or in an optional error list:

[![Flycheck screencast](images/screencast.gif)](images/screencast.gif)

{% if site.data.releases.versions %}
*Latest release: {{site.data.releases.versions | last}}*
{% endif %}

Features
--------

Manual
------

{% if site.data.releases.include_latest %}
- [Snapshot](manual/latest/index.html) (for MELPA users){% endif %}{% if site.data.releases.versions %}
- [Latest release](manual/{{site.data.releases.versions | last}}/index.html) (for
Marmalade and MELPA Stable users)
{% endif %}

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
