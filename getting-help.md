---
layout: page
title: Getting Help
redirect_from: "/resources.html"
---

## Documentation ##

Flycheck comes with with a [comprehensive manual][manual].  You can read this
manual in Emacs `M-x flycheck-info`, provided that you already installed
Flycheck.  The latest manual is also [available online][manual].

The article [Flymake versus Flycheck][1] provides a detailed comparison of
Flycheck and the older built-in Flymake extension.  If you have used Flymake or
are still using it we recommend that you take a look at this article to see how
Flycheck is an improvement over Flymake and what new features it provides.  We
hope that this article helps you to decide whether you might consider switching
to Flycheck and to learn what is new in Flycheck.

The [Changelog]({{site.baseurl}}/changes.html) lists all changes in all releases
and the development version of Flycheck.

If you think that our documentation is unclear, imprecise, factually incorrect
or could otherwise need improvement please do not hesitate to tell us, by
reporting to our [issue tracker][].

[1]: {{site.baseurl}}/flycheck-versus-flymake.html
[manual]: {{site.baseurl}}/manual/latest/index.html

## Ask questions ##

Please ask questions about Flycheck on [Stack Exchange][sx] or in our
[Gitter chat][gitter].  We try to answer all questions as fast and as precise as
possible.

Please follow our [Code of Conduct][coc] in these places.

## Report bugs and problems ##

Please report bugs and problems to our [issue tracker][].  You can follow the
progress of your issue on our [Waffle board][].

### Windows-only issues ###

As Flycheck does not support Windows officially we generally do *not* attempt
to fix issues that only occur on Windows.  We will move all Windows-only issues
to the [list of open Windows issues][windows], and leave them to Windows
users and developers.  We welcome anyone who wants to fix open Windows issues,
and we will merge pull requests for improved Windows compatibility.  If you know
Windows and Emacs, please take a look at the list of open Windows issues and try
to fix any of these.  Thank you!

[SX]: https://emacs.stackexchange.com/questions/tagged/flycheck
[gitter]: https://gitter.im/flycheck/flycheck
[coc]: {{site.baseurl}}/conduct.html
[Issue Tracker]: https://github.com/flycheck/flycheck/issues
[Waffle board]: https://waffle.io/flycheck/flycheck
[windows]: https://github.com/flycheck/flycheck/labels/B-Windows%20only
