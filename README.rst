========================
Certbot FreeNAS Deployer
========================

.. image:: https://img.shields.io/pypi/v/certbot_freenas_deployer.svg
        :target: https://pypi.python.org/pypi/certbot_freenas_deployer

.. image:: https://img.shields.io/travis/kpfleming/certbot_freenas_deployer.svg
        :target: https://travis-ci.org/kpfleming/certbot_freenas_deployer
	:alt: Build Status

.. image:: https://readthedocs.org/projects/certbot-freenas-deployer/badge/?version=latest
        :target: https://certbot-freenas-deployer.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/kpfleming/certbot_freenas_deployer/shield.svg
	:target: https://pyup.io/repos/github/kpfleming/certbot_freenas_deployer/
	:alt: Dependency Updates

A simple tool to deploy TLS certificates obtained using Certbot to FreeNAS systems.

* Open Source software: Apache Software License 2.0
* Documentation: https://certbot-freenas-deployer.rtfd.io.


Features
--------

This tool is intended to be used as a "deploy hook" in Certbot configurations, where Certbot
is running on a separate system from FreeNAS (either physically separate, or a jail within
the FreeNAS system). In order for Let's Encrypt to be able to validate ownership of the domain
name used for the certificate, you'll need to use a suitable challenge_ method. Since the
HTTP-01 and TLS-SNI-01 challenge methods would both require your FreeNAS system to be reachable
by the Let's Encrypt servers, and this is generally regarded as a signficant security risk,
it is recommended to use the DNS-01 challenge method with a suitable DNS authenticator for your
DNS provider.

The tool requires (at least) FreeNAS 11.1, which is the version in which the GUI certificate
update API methods were introduced. It also requires Python 3.5 or a later version.

.. _challenge: https://letsencrypt.readthedocs.io/en/latest/challenges.html

Credits
-------

This tool was inspired by danb35's deploy-freenas_ script, but is intended for use with the
Certbot_ tool from the `Electronic Frontier Foundation`_.

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _deploy-freenas: https://github.com/danb35/deploy-freenas
.. _Certbot: https://github.com/certbot/certbot
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`Electronic Frontier Foundation`: https://www.eff.org
