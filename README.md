# Certbot FreeNAS Deployer

<a href="https://opensource.org"><img height="150" align="left" src="https://opensource.org/files/OSIApprovedCropped.png" alt="Open Source Initiative Approved License logo"></a>
[![Package on PyPI](https://img.shields.io/pypi/v/certbot_freenas_deployer.svg)](https://pypi.python.org/pypi/certbot_freenas_deployer)
[![Build status on Travis CI](https://img.shields.io/travis/kpfleming/certbot_freenas_deployer.svg)](https://travis-ci.org/kpfleming/certbot_freenas_deployer)
[![Documentation on ReadTheDocs](https://readthedocs.org/projects/certbot-freenas-deployer/badge/?version=latest)](https://certbot-freenas-deployer.readthedocs.io/en/latest/?badge=latest)

A simple tool to deploy TLS certificates obtained using Certbot to FreeNAS systems.

Open Source software: Apache Software License 2.0

## &nbsp;

# Features

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

# Credits

This tool was inspired by danb35\'s
[deploy-freenas](https://github.com/danb35/deploy-freenas) script, but
is intended for use with the
[Certbot](https://github.com/certbot/certbot) tool from the [Electronic
Frontier Foundation](https://www.eff.org).

This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter) and the
[audreyr/cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
project template.
