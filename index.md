---
layout: index
---

Flycheck <small>Syntax checking for GNU Emacs</small>
=====================================================

[![Flycheck screencast](images/screencast.gif)](images/screencast.gif)

{% if site.data.releases.versions %}
*Latest release: {{site.data.releases.versions | last}}*
{% endif %}

Flycheck is a modern on-the-fly syntax checking extension for GNU Emacs.

Features
--------

Installation
------------

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
{% for post in site.posts | slice: 0, 5 %}
<dt>{{ post.date | date_to_string }}</dt>
<dd><a href="{{site.baseurl}}{{post.url}}">{{ post.title | escape }}</a></dd>
{% endfor %}
</dl>
</div>
