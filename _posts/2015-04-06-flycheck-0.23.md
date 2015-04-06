---
title: Flycheck 0.23
---

Flycheck 0.23 is released, with a new manual and a new website, some new syntax
checkers, and some new features and improvements.

### Table of contents
{:.no_toc}

- Table of contents
{:toc .toc}

Breaking changes
================

This release includes a new manual and a new website at
<http://www.flycheck.org>.  The old manual at <https://flycheck.readthedocs.org>
is still present, but not updated anymore.

Due to various issues, this release *removes* the syntax checker for Makefiles.
It also removes Zsh support from the Shellcheck syntax checker, because
Shellcheck itself does not support Zsh anymore.

Finally, this release removes Global Flycheck Mode from the Customization
interface, because this setting never actually worked.  For details see
[#595](https://github.com/flycheck/flycheck/issues/595).

New manual and website
======================

Flycheck has a new manual now which is written in native Texinfo format to
archive a high-quality Info manual for online reading in Emacs' built-in Info
viewer.  An online manual in HTML format is still available at
<http://www.flycheck.org>, for MELPA and MELPA Stable packages.  The online
manual is still build automatically for each commit.

Some resources which never really fit into the manual were moved to the website
or into markdown files in the Flycheck source tree.  Specifically, the
comparison between Flycheck and Flymake is only available on the website now, at
<http://www.flycheck.org/flycheck-versus-flymake.html>.  Likewise, contribution
guidelines and the documentation of the test suite are part of the source code
now, at `CONTRIBUTING.md` and `test/README.md` respectively.

The website has a new design which is less cluttered and and puts the focus on
the content.

Language support
================

C/C++
-----

Flycheck now provides new options to enable pedantic warnings and pedantic
errors for Clang and GCC.

Chef
----

Flycheck now allows to select tags when checking Chef recipes, with the new
`flycheck-foodcritic-tags` option.  Furthermore, Flycheck now handles relative
paths in Chef recipes correctly.

Emacs Lisp
----------

Flycheck now automatically initializes packages when checking `user-init-file`
even if `user-init-file` is not contained in `user-emacs-directory`.

Handlebars
----------

Flycheck now checks handlebars templates in Web Mode as well.

Lua
---

In addition to the old `lua` syntax checker Flycheck now includes a syntax
checker for [Luacheck](https://github.com/mpeterv/luacheck).

R
-

Flycheck checks R code with [lintr](https://github.com/jimhester/lintr) now.

Rust
----

Flycheck parses multi-line type errors from `rustc` now, and extracts error IDs
from some `rustc` messages.

SCSS
----

In addition to the `scss` syntax checker, Flycheck now provides a
[SCSS-Lint](https://github.com/brigade/scss-lint) syntax checker.

Syntax checking
===============

Global Flycheck Mode now enables Flycheck Mode even in buffers for which there
is no syntax checker currently.  This ensure that Flycheck seamlessly starts to
work if a new syntax checker becomes available for a buffer, for instance if a
new Emacs package was installed.  The new option `flycheck-global-modes`
provides better control about the major modes in which Global Flycheck Mode
activates Flycheck Mode.

A new command `flycheck-disable-checker` lets you disable syntax checkers for
the current buffer interactively.

Flycheck Mode does not cache the last automatically selected checker for the
current buffer anymore, because this had many unintended side effects and did
not play well with disabled checkers.

Miscellaneous bug fixes and improvements
========================================

Hook variables are now initialized with `add-hook` to make sure that built-in
hooks get added even if the hook variables were set before Flycheck was loaded.

Filenames in errors are now handled correctly even if a syntax checker resolves
symlinks in its output.
