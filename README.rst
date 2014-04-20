`Pelican <http://blog.getpelican.com/>`_-based website for `NWCPP <http://nwcpp.org/>`_.

Running Pelican requires that you've installed Python 2.7.
See `The Hitchhiker’s Guide to Python! <http://docs.python-guide.org/en/latest/>`_
for guidelines on installing `Python <https://www.python.org/>`_,
`pip <http://www.pip-installer.org/>`_, and
`virtualenv <https://pypi.python.org/pypi/virtualenv>`_
on Windows, Mac, and Linux.

Windows Setup
-------------

* Install the prerequisites of Python 2.7, *pip*, *virtualenv*,
  *Setuptools*, and *easy_install*, per `Installing Python on Windows
  <http://docs.python-guide.org/en/latest/starting/install/win/>`_.
* The `Fabric <http://www.fabfile.org/>`_ tool
  requires `PyCrypto <http://pycrypto.org>`_,
  which is tricky to install if you don't have the MSVC 2008 compiler on your system.
* Download the PyCrypto installer for your flavor of Python from
  `VoidSpace <http://www.voidspace.org.uk/python/modules.shtml#pycrypto>`_.
* Do not run the PyCrypto installer yet, until you've created your virtualenv.

Local Setup
-----------

* Create a new virtualenv, ``nwcpp``
* Windows only: ``easy_install pycrypto-2.6.win32-py2.7.exe``
  (or whatever you downloaded)
* Install Pelican and other dependencies:
  ``pip install pelican fabric python-dateutil typogrify ghp-import``

Running Locally
---------------

* Edit pages in your favorite editor.
* Build pages and serve them on http://localhost:8000/, ``fab reserve``
* Commit pages to Git and push to GitHub: ``git push origin master``
* Publish website to GitHub Pages: ``fab gh_pages``

