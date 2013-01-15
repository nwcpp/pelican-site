2013 Website Refresh
####################

:date: 2013-01-15
:author: George Reilly
:status: draft

.. image:: |filename|images/joomla-screenshot.png
    :alt: Old Joomla-based website
    :width: 500px
    :target: |filename|images/joomla-screenshot.png


.. code-block:: apache

    Host github-gvr
        HostName github.com
        User git
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_rsa
        IdentitiesOnly yes

    Host github-nwcpp
        HostName github.com
        User git
        PreferredAuthentications publickey
        IdentityFile ~/.ssh/id_rsa_nwcpp

.. code-block:: bash

    $ git remote -v
    origin	git@github-nwcpp:nwcpp/pelican-site.git (fetch)
    origin	git@github-nwcpp:nwcpp/pelican-site.git (push)

.. _Pelican:
    http://blog.getpelican.com/
.. _Just Host:
    http://www.justhost.com/
.. _Joomla:
    http://www.joomla.org/
.. _Network Solutions:
    https://www.networksolutions.com/
.. _reStructuredText:
    http://docutils.sf.net/rst.html
.. _history with reStructuredText:
    http://www.georgevreilly.com/blog/CategoryView,category,reStructuredText.aspx
.. _Pandoc:
    http://johnmacfarlane.net/pandoc/
.. _html2rest:
    http://pypi.python.org/pypi/html2rest
.. _multiple Github identities:
    http://stackoverflow.com/a/922461/6364
.. _Github repo:
    https://github.com/nwcpp/pelican-site/
.. _publishing to Github pages
    http://docs.getpelican.com/en/3.1.1/tips.html
.. _Google Docs contact form:
    http://www.bloggerbuster.com/2012/04/create-contact-form-with-google-docs.html
.. _Custom domain:
    https://help.github.com/articles/setting-up-a-custom-domain-with-pages
.. _Namecheap DNS configuration:
    http://dreamand.me/github-page/github-page-custom-domain/
