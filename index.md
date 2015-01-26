---
layout: index
---

Flycheck <small>Syntax checking for GNU Emacs</small> ![](images/logo.png){: .title-logo}
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
