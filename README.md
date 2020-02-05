Certbot FreeNAS Deployer
========================

<a href="https://opensource.org" target="_blank"><img width="150" height="200" align="left" src="https://opensource.org/files/OSIApproved.png" alt="Open Source Initiative Approved License logo"></a>
<a href="https://pypi.python.org/pypi/certbot_freenas_deployer" target="_blank"><img src="https://img.shields.io/pypi/v/certbot_freenas_deployer.svg" alt="Package on PyPI"></a>
<a href="https://travis-ci.org/kpfleming/certbot_freenas_deployer" target="_blank"><img src="https://img.shields.io/travis/kpfleming/certbot_freenas_deployer.svg" alt="Build status on Travis-CI"></a>
<a href="https://certbot-freenas-deployer.readthedocs.io/en/latest/?badge=latest" target="_blank"><img src="https://readthedocs.org/projects/certbot-freenas-deployer/badge/?version=latest" alt="Documentation on ReadTheDocs"></a>

A simple tool to deploy TLS certificates obtained using Certbot to FreeNAS systems.

Open Source software: Apache Software License 2.0

Features
--------

This tool is intended to be used as a \"deploy hook\" in Certbot
configurations, where Certbot is running on a separate system from
FreeNAS (either physically separate, or a jail within the FreeNAS
system). In order for Let\'s Encrypt to be able to validate ownership of
the domain name used for the certificate, you\'ll need to use a suitable
[challenge](https://letsencrypt.readthedocs.io/en/latest/challenges.html)
method. Since the HTTP-01 and TLS-SNI-01 challenge methods would both
require your FreeNAS system to be reachable by the Let\'s Encrypt
servers, and this is generally regarded as a signficant security risk,
it is recommended to use the DNS-01 challenge method with a suitable DNS
authenticator for your DNS provider.

The tool requires (at least) FreeNAS 11.1, which is the version in which
the GUI certificate update API methods were introduced. It also requires
Python 3.5 or a later version.

Credits
-------

This tool was inspired by danb35\'s
[deploy-freenas](https://github.com/danb35/deploy-freenas) script, but
is intended for use with the
[Certbot](https://github.com/certbot/certbot) tool from the [Electronic
Frontier Foundation](https://www.eff.org).

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
