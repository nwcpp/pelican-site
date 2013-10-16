Pelican-based website for NWCPP.

Local Setup
-----------

* Install `pip <http://www.pip-installer.org/>`_ and
  `virtualenv <https://pypi.python.org/pypi/virtualenv>`_.
* Create a new virtualenv, ``nwcpp``
* Install dependencies: ``pip install pelican typogrify ghp-import``

Running Locally
---------------

* ``make devserver``
* Edit pages
* Commit pages to Git and push to Github: ``git push origin master``
* Publish website to Github Pages: ``make github``
