---
layout: page
title: 3rd party extensions
---

The Emacs community has produced a number of extensions to Flycheck.  This page
lists all that we know of and can safely recommend to our users.

If you do know extensions not in this list, or would like to see your own
extension here, please feel free to
[add it](https://github.com/flycheck/flycheck.github.io/edit/master/extensions.md).

User interface
==============

- [flycheck-color-mode-line](https://github.com/flycheck/flycheck-color-mode-line)
  colors the mode line according to the Flycheck status.
- [flycheck-pos-tip](https://github.com/flycheck/flycheck-pos-tip) shows
  Flycheck error messages in a graphical popup.
- [flycheck-status-emoji](https://github.com/liblit/flycheck-status-emoji)
  adds cute emoji (e.g. 😱 for errors) to Flycheck’s mode line status.

Language integration
====================

- [flycheck-cask](https://github.com/flycheck/flycheck-cask) makes Flycheck use
  Cask packages for Emacs Lisp syntax checking in
  [Cask](https://github.com/cask/cask) projects.
- [flycheck-rust](https://github.com/flycheck/flycheck-rust) configures Flycheck
  according to the Cargo settings and layouts of the current Rust project.
- [flycheck-haskell](https://github.com/flycheck/flycheck-haskell) configures
  Flycheck from the Cabal settings and sandbox in Haskell projects.

Additional languages and syntax checkers
========================================

- [flycheck-clojure](https://github.com/clojure-emacs/squiggly-clojure) provides
  syntax checking for Clojure.
- [flycheck-d-unittest](https://github.com/flycheck/flycheck-d-unittest) adds a
  Flycheck checker to run unit tests for D programs on the fly.
- [flycheck-google-cpplint](https://github.com/flycheck/flycheck-google-cpplint)
  adds a syntax checker for Google's C++ style checker.
- [flycheck-irony](https://github.com/Sarcasm/flycheck-irony) adds a Flycheck
  syntax checker for C, C++ and Objective C using
  [Irony Mode](https://github.com/Sarcasm/irony-mode).
- [flycheck-ledger](https://github.com/purcell/flycheck-ledger) adds a syntax
  checker for the [Ledger](http://ledger-cli.org/) accounting tool.
- [flycheck-mercury](https://github.com/flycheck/flycheck-mercury) adds a
  Flycheck syntax checker for the [Mercury language](http://mercurylang.org/).
- [flycheck-ocaml](https://github.com/flycheck/flycheck-ocaml) adds a syntax
  checker for OCaml.
- [flycheck-package](https://github.com/purcell/flycheck-package) checks
  emacs lisp package source code for common problems.
- [flycheck-pyflakes](https://github.com/Wilfred/flycheck-pyflakes) adds a
  Python syntax checker using Pyflakes.
