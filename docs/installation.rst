.. highlight:: shell

============
Installation
============


Stable release
--------------

To install Certbot FreeNAS Deployer, run this command in your terminal:

.. code-block:: console

    $ pip install certbot_freenas_deployer

This is the preferred method to install Certbot FreeNAS Deployer, as it will always install the most recent stable release.

If you have multiple Python versions installed on your system, and Python 3.x is
*not* the default version (the version which is run when you execute 'python'), then
you will need to ensure that you use the Python 3 version of 'pip' when you install
this package. Commonly this version is called 'pip3', so the following command can be
run in your terminal:

.. code-block:: console

   $ pip3 install certbot_freenas_deployer

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for Certbot FreeNAS Deployer can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/kpfleming/certbot_freenas_deployer

Or download the `tarball`_:

.. code-block:: console

    $ curl -OL https://github.com/kpfleming/certbot_freenas_deployer/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install

If you have multiple Python versions installed on your system, and Python 3.x is
*not* the default version (the version which is run when you execute 'python'), then
you will need to ensure that you use Python 3 when you install
this package. Commonly this version is called 'python3', so the following command can be
run in your terminal:

.. code-block:: console

   $ python3 setup.py install

.. _Github repo: https://github.com/kpfleming/certbot_freenas_deployer
.. _tarball: https://github.com/kpfleming/certbot_freenas_deployer/tarball/master
