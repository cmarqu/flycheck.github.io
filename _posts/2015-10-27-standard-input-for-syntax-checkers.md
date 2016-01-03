---
title: Standard input for syntax checkers
---

With the recent commit
[`4a05e4c`](https://github.com/flycheck/flycheck/commit/4a05e4c4271cf78e10a3a9242a8ff389f2b1faf5)
Flycheck syntax checkers can now receive the buffer contents on standard input.
This solves frequent issues with build tools being confused by temporary files
created by Flycheck and thus replaces temporary files as the recommended
mechanism for passing buffer contents to syntax checkers.

Changing a syntax checker definition to use standard input is straight forward:

* Add `:standard-input t` to the syntax checker definition.
* Remove `filename` cells from `:error-patterns`.

When reading from standard input most syntax checking tools don’t include proper
file names in their error output.  Many actually “invent” filenames such as
“stdin” or “-” for standard input.  Flycheck can’t link these filenames to the
buffer anymore and discards errors as not referring to the current buffer.

Removing `filename` cells from `:error-patterns` and replacing it with a
constant match for whatever magic filename the tool invents for standard input
solves this because Flycheck automatically links errors without filenames to the
current buffer.  If your syntax checker uses an `:error-parser` you’ll need an
`:error-filter` with `flycheck-remove-error-file-names` instead:  This function
removes all matching filenames from errors, and thus has the same effect as
omitting `filename` from error patterns.

We’re in the process of
[converting built-in syntax checkers](https://github.com/flycheck/flycheck/issues/767)
to use standard input, and we encourage you to use this feature for your own
syntax checkers as well.  If you’d like to help with the conversion, please feel
free to join the issue on Github.  We’re looking forward to merge your pull
request!

Thank you for your support!
