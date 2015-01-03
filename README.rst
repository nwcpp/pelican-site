NWCPP Website Source
####################

`Pelican <http://blog.getpelican.com/>`_-based website for the
`Northwest C++ Users' Group <http://nwcpp.org/>`_.
See `2013 Website Refresh <http://nwcpp.org/2013-website-refresh.html>`_
for more background.

Running Pelican requires that you've installed Python 2.7.
(You're welcome to try Python 3.4, but it's untested.)
See `The Hitchhiker’s Guide to Python! <http://docs.python-guide.org/en/latest/>`_
for guidelines on installing `Python <https://www.python.org/>`_,
`pip <http://www.pip-installer.org/>`_, and
`virtualenv <https://pypi.python.org/pypi/virtualenv>`_
on Windows, Mac, and Linux.

Clone the Repo
--------------

* In a terminal window:

    - ``git clone https://github.com/nwcpp/pelican-site``

Create a Virtual Environment
----------------------------

* Install the prerequisites of Python 2.7
  *pip*, *virtualenv*, *Setuptools*, and *easy_install*, per
  `Installing Python on Mac OS X
  <http://docs.python-guide.org/en/latest/starting/install/osx/`_,
  `Installing Python on Linux
  <http://docs.python-guide.org/en/latest/starting/install/linux/`_, or
  `Installing Python on Windows
  <http://docs.python-guide.org/en/latest/starting/install/win/>`_.
* Note: for Windows, be sure to install the *32-bit* Python 2.7,
  even if you are running Win64, or you will have difficulty with PyCrypto.
* Create the ``nwcpp`` virtual environment:

    - ``cd pelican-site``
    - ``virtualenv nwcpp``

* Activate the virtualenv (you'll need to do this every time):

    - ``nwcpp\Scripts\activate.bat``   # Windows
    - ``source nwcpp\bin\activate``    # Linux or Mac


Windows Setup
-------------

* The `Fabric <http://www.fabfile.org/>`_ tool
  requires `PyCrypto <http://pycrypto.org>`_,
  which is tricky to install if you don't have the MSVC 2008 compiler on your system.
* Download the PyCrypto installer for *32-bit Python 2.7* from
  `VoidSpace <http://www.voidspace.org.uk/python/modules.shtml#pycrypto>`_.
* Install PyCrypto: ``easy_install pycrypto-2.6.win32-py2.7.exe``
* Until the `Windows Pull Request <https://github.com/davisp/ghp-import/pull/25>`_ is accepted,
  you will need to install a custom version of the ghp-import tool in your virtualenv:

    - ``git clone https://github.com/chevah/ghp-import``
    - ``cd ghp-import``
    - ``python setup.py develop``


Common Setup
-----------

* Create and activate your virtualenv, as described above.
* Install Pelican and other dependencies:
  ``pip install pelican fabric python-dateutil typogrify ghp-import``

Running Locally
---------------

* Edit pages in your favorite editor. Hint: use a recent post as a starting point.
* Build pages and serve them on http://localhost:8000/, ``fab reserve``
* Commit pages to Git and push to GitHub: ``git push origin master``
* Publish website to `GitHub Pages <https://pages.github.com/>`_: ``fab gh_pages``
* To see all commands, ``fab --list``
