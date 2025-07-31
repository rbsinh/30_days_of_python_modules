[![Black Logo](https://raw.githubusercontent.com/psf/black/main/docs/_static/logo2-readme.png)](https://black.readthedocs.io/en/stable/)

<h2 align="center">The Uncompromising Code Formatter</h2>

<p align="center">
<a href="https://github.com/psf/black/actions"><img alt="Actions Status" src="https://github.com/psf/black/workflows/Test/badge.svg"></a>
<a href="https://black.readthedocs.io/en/stable/?badge=stable"><img alt="Documentation Status" src="https://readthedocs.org/projects/black/badge/?version=stable"></a>
<a href="https://coveralls.io/github/psf/black?branch=main"><img alt="Coverage Status" src="https://coveralls.io/repos/github/psf/black/badge.svg?branch=main"></a>
<a href="https://github.com/psf/black/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
<a href="https://pypi.org/project/black/"><img alt="PyPI" src="https://img.shields.io/pypi/v/black"></a>
<a href="https://pepy.tech/project/black"><img alt="Downloads" src="https://static.pepy.tech/badge/black"></a>
<a href="https://anaconda.org/conda-forge/black/"><img alt="conda-forge" src="https://img.shields.io/conda/dn/conda-forge/black.svg?label=conda-forge"></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

> “Any color you like.”

_Black_ is the uncompromising Python code formatter. By using it, you agree to cede
control over minutiae of hand-formatting. In return, _Black_ gives you speed,
determinism, and freedom from `pycodestyle` nagging about formatting. You will save time
and mental energy for more important matters.

Blackened code looks the same regardless of the project you're reading. Formatting
becomes transparent after a while and you can focus on the content instead.

_Black_ makes code review faster by producing the smallest diffs possible.

Try it out now using the [Black Playground](https://black.vercel.app). Watch the
[PyCon 2019 talk](https://youtu.be/esZLCuWs_2Y) to learn more.

---

**[Read the documentation on ReadTheDocs!](https://black.readthedocs.io/en/stable)**

---

## Installation and usage

### Installation

_Black_ can be installed by running `pip install black`. It requires Python 3.9+ to run.
If you want to format Jupyter Notebooks, install with `pip install "black[jupyter]"`.

If you can't wait for the latest _hotness_ and want to install from GitHub, use:

`pip install git+https://github.com/psf/black`

### Usage

To get started right away with sensible defaults:

```sh
black {source_file_or_directory}
```

You can run _Black_ as a package if running it as a script doesn't work:

```sh
python -m black {source_file_or_directory}
```

Further information can be found in our docs:

- [Usage and Configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/index.html)

_Black_ is already [successfully used](https://github.com/psf/black#used-by) by many
projects, small and big. _Black_ has a comprehensive test suite, with efficient parallel
tests, and our own auto formatting and parallel Continuous Integration runner. Now that
we have become stable, you should not expect large formatting changes in the future.
Stylistic changes will mostly be responses to bug reports and support for new Python
syntax. For more information please refer to
[The Black Code Style](https://black.readthedocs.io/en/stable/the_black_code_style/index.html).

Also, as a safety measure which slows down processing, _Black_ will check that the
reformatted code still produces a valid AST that is effectively equivalent to the
original (see the
[Pragmatism](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#ast-before-and-after-formatting)
section for details). If you're feeling confident, use `--fast`.

## The _Black_ code style

_Black_ is a PEP 8 compliant opinionated formatter. _Black_ reformats entire files in
place. Style configuration options are deliberately limited and rarely added. It doesn't
take previous formatting into account (see
[Pragmatism](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#pragmatism)
for exceptions).

Our documentation covers the current _Black_ code style, but planned changes to it are
also documented. They're both worth taking a look at:

- [The _Black_ Code Style: Current style](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html)
- [The _Black_ Code Style: Future style](https://black.readthedocs.io/en/stable/the_black_code_style/future_style.html)

Changes to the _Black_ code style are bound by the Stability Policy:

- [The _Black_ Code Style: Stability Policy](https://black.readthedocs.io/en/stable/the_black_code_style/index.html#stability-policy)

Please refer to this document before submitting an issue. What seems like a bug might be
intended behaviour.

### Pragmatism

Early versions of _Black_ used to be absolutist in some respects. They took after its
initial author. This was fine at the time as it made the implementation simpler and
there were not many users anyway. Not many edge cases were reported. As a mature tool,
_Black_ does make some exceptions to rules it otherwise holds.

- [The _Black_ code style: Pragmatism](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html#pragmatism)

Please refer to this document before submitting an issue just like with the document
above. What seems like a bug might be intended behaviour.

## Configuration

_Black_ is able to read project-specific default values for its command line options
from a `pyproject.toml` file. This is especially useful for specifying custom
`--include` and `--exclude`/`--force-exclude`/`--extend-exclude` patterns for your
project.

You can find more details in our documentation:

- [The basics: Configuration via a file](https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html#configuration-via-a-file)

And if you're looking for more general configuration documentation:

- [Usage and Configuration](https://black.readthedocs.io/en/stable/usage_and_configuration/index.html)

**Pro-tip**: If you're asking yourself "Do I need to configure anything?" the answer is
"No". _Black_ is all about sensible defaults. Applying those defaults will have your
code in compliance with many other _Black_ formatted projects.

## Used by

The following notable open-source projects trust _Black_ with enforcing a consistent
code style: pytest, tox, Pyramid, Django, Django Channels, Hypothesis, attrs,
SQLAlchemy, Poetry, PyPA applications (Warehouse, Bandersnatch, Pipenv, virtualenv),
pandas, Pillow, Twisted, LocalStack, every Datadog Agent Integration, Home Assistant,
Zulip, Kedro, OpenOA, FLORIS, ORBIT, WOMBAT, and many more.