---
layout: page
title: Resources
---

Manuals
=======

With Flycheck installed you can read the manual of your Flycheck installation
inside Emacs with `M-x flycheck-info`.

{% if site.data.releases.include_latest %}
- [Snapshot]({{site.baseurl}}/manual/latest/index.html) (for MELPA users){% endif %}{% if site.data.releases.versions %}
- [Latest release]({{site.baseurl}}/manual/{{site.data.releases.versions | last}}/index.html) (for
Marmalade and MELPA Stable users)
{% endif %}

{% if site.data.releases.versions %}

All releases:

{% for version in site.data.releases.versions %}
- [Version {{version}}]({{site.baseurl}}/manual/{{version}}/index.html)
{% endfor %}
{% endif %}

Other documents
===============

- [Flymake versus Flycheck]({{site.baseurl}}/flycheck-versus-flymake.html)
  provides a detailed comparison between the built-in Flymake extensions and
  Flycheck.
