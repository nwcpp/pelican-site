Pelican-based website for NWCPP.

Requires that you've installed Python 2.7.
See `The Hitchhiker’s Guide to Python! <http://docs.python-guide.org/en/latest/>`_
for guidelines on installing `Python <https://www.python.org/>`_,
`pip <http://www.pip-installer.org/>`_, and
`virtualenv <https://pypi.python.org/pypi/virtualenv>`_.
on Windows, Mac, and Linux.

Windows Setup
-------------

After installing the prerequisites, do

* Install `PyCrypto <http://pycrypto.org/>`_::

    http://www.voidspace.org.uk/python/modules.shtml#pycrypto

Local Setup
-----------

* Create a new virtualenv, ``nwcpp``
* Install dependencies: ``pip install pelican fabric python-dateutil typogrify ghp-import``

Running Locally
---------------

* Edit pages
* Build pages and serve them on http://localhost:8000/, ``fab reserve``
* Commit pages to Git and push to Github: ``git push origin master``
* Publish website to Github Pages: ``fab gh_pages``
