# browse-pep

Open a pep in your browser.

## Installation

**browse-pep** is a **pep517** compatible python project. So you can install it
just like any other python project. You can ise [pip][1], [uv][2], [gpep517][3],
[hatch][4] or some other pep517 compliant tool for installing this project.

[1]: https://pip.pypa.io
[2]: https://docs.astral.sh/uv/
[3]: https://github.com/projg2/gpep517
[4]: https://hatch.pypa.io/latest/

Here are installation via pip:

* Clone the source repository or install and extract tarball.
* Checkout to source tree.

Then use:

	pip install --user .

This will install package to your users site. For more information about
installing python packages, see this [PYPA Tutorial][5].

[5]: https://packaging.python.org/en/latest/tutorials/installing-packages/

## Usage

Here is some use examples:

	# no pep is given, defaults to 0
	browse-pep
	# or
	python3 -m browse_pep

	# can given one or more pep for browsing
	browse-pep 8 9 517
	browse-pep 1

## Copying

Licensed under **MIT**. See file **COPYING** for details.
