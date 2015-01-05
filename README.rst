NWCPP Website Source
####################

`Pelican <http://blog.getpelican.com/>`_-based website for the
`Northwest C++ Users' Group <http://nwcpp.org/>`_.
Read `2013 Website Refresh <http://nwcpp.org/2013-website-refresh.html>`_
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

* Note: for Windows, be sure to install the *32-bit* Python 2.7,
  even if you are running Win64,
  or you will have difficulty with `PyCrypto <http://pycrypto.org>`_.
* Install the prerequisites of Python 2.7
  *pip*, *virtualenv*, *Setuptools*, and *easy_install*, per
  `Installing Python on Mac OS X
  <http://docs.python-guide.org/en/latest/starting/install/osx/>`_,
  `Installing Python on Linux
  <http://docs.python-guide.org/en/latest/starting/install/linux/>`_, or
  `Installing Python on Windows
  <http://docs.python-guide.org/en/latest/starting/install/win/>`_.
* Create the ``nwcpp`` virtual environment.
  The ``virtualenv`` command line below shows it being created in ``pelican-site/nwcpp``,
  but you can put it anywhere.:
  If you use `virtualenvwrapper <https://virtualenvwrapper.readthedocs.org/en/latest/>`_
  on Mac or Linux, the recommended place is ``~/Envs``;
  if you use `virtualenvwrapper-powershell
  <https://pypi.python.org/pypi/virtualenvwrapper-powershell/>`_ or 
  `virtualenvwrapper-win <https://github.com/davidmarble/virtualenvwrapper-win/>`_ (``cmd.exe``)
  on Windows, use ``%USERPROFILE%\Envs``.

    - ``cd pelican-site``
    - ``virtualenv nwcpp``

* *Activate* the virtualenv (you'll need to do this *every time*).
  This prefixes the virtualenv's ``bin`` or ``Scripts`` directory to your ``PATH``:

    - ``nwcpp\Scripts\activate.bat``   # Windows
    - ``source nwcpp\bin\activate``    # Linux or Mac


Windows Setup
-------------

* The `Fabric <http://www.fabfile.org/>`_ tool
  requires `PyCrypto <http://pycrypto.org>`_,
  which is tricky to install if you don't have the MSVC 2008 compiler on your system.

    - Download the PyCrypto installer for *32-bit Python 2.7* from
      `VoidSpace <http://www.voidspace.org.uk/python/modules.shtml#pycrypto>`_.
    - Install PyCrypto: ``easy_install pycrypto-2.6.win32-py2.7.exe``

* As of 2015-01-04, you will need custom builds of
  `Pelican <http://blog.getpelican.com/>`_ and
  `ghp-import <https://github.com/davisp/ghp-import/>`_.

    - `Pelican Pull Request #1581 <https://github.com/getpelican/pelican/pull/1581>`_:
      Download https://github.com/georgevreilly/pelican/archive/win-fixes.zip
    - `Ghp-import Pull Request #25 <https://github.com/davisp/ghp-import/pull/25>`_:
      Download https://github.com/chevah/ghp-import/archive/win-support.zip
    - Unzip the two zipfiles into a temporary directory.
    - ``cd ghp-import-win-support``
    - ``python setup.py install``
    - ``cd ..\pelican-win-fixes``
    - ``python setup.py install``


Common Setup for Windows, Mac, and Linux
----------------------------------------

* Create and activate your virtualenv, as described above.
* Install Pelican and other dependencies:
  ``pip install pelican fabric python-dateutil typogrify ghp-import``


Running Locally
---------------

* Edit pages in your favorite editor. Hint: use a recent post as a starting point.
* Build pages and serve them on http://localhost:8000/:
  ``fab reserve``
* Commit pages to Git and push to GitHub: ``git push origin master``
* Publish website to `GitHub Pages <https://pages.github.com/>`_: ``fab gh_pages``.
  The updated website will be visible in a few seconds at http://nwcpp.org/
* To see all commands in the fabfile: ``fab --list``
