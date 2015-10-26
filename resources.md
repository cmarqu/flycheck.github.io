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
- [Latest release {{site.data.releases.versions | last}}]({{site.baseurl}}/manual/{{site.data.releases.versions | last}}/index.html) (for
Marmalade and MELPA Stable users)
{% endif %}

{% if site.data.releases.versions %}

All releases:

{% for version in site.data.releases.versions reversed %}
- [Version {{version}}]({{site.baseurl}}/manual/{{version}}/index.html){% endfor %}
{% endif %}

Other documents
===============

- The [Changelog]({{site.baseurl}}/changes.html) lists all changes in all
  releases and the development version of Flycheck.
- [Flymake versus Flycheck]({{site.baseurl}}/flycheck-versus-flymake.html)
  provides a detailed comparison between the built-in Flymake extensions and
  Flycheck.

Getting help
============

- Ask questions or get help on
  [Stack Exchange](https://emacs.stackexchange.com/questions/tagged/flycheck)
- Report bugs to the
  [Issue Tracker](https://github.com/flycheck/flycheck/issues)
