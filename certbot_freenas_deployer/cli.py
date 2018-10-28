# -*- coding: utf-8 -*-

import click
import logging
import requests
import http.client as http_client
import sys
import time
import os
import pkg_resources


class freenas_api_endpoint:
    def __init__(self, *, url, tls_verify, user, password):
        self.url = url
        self.tls_verify = tls_verify
        self.user = user
        self.password = password

    def request(self, *, verb=None, api=None, params=None, json=None):
        return requests.request(
            verb,
            url=self.url + '/api/v1.0/system/' + api,
            headers={'Content-Type': 'application/json'},
            auth=(self.user, self.password),
            verify=self.tls_verify,
            params=params,
            json=json,
        )


@click.command()
@click.option('url', '--url', help='URL of FreeNAS system')
@click.option('tls_verify', '--tls-verify/--no-tls-verify', default=True,
              help='Enable or disable verification of existing TLS certificate during deployment (default: enabled)')
@click.option('user', '--user', help='Name of user with root privileges on FreeNAS system')
@click.option('password', '--password', help='Password for specified user')
@click.option('certfile', '--certfile', help='Path to certificate file (usually fullchain.pem)')
@click.option('keyfile', '--keyfile', help='Path to private key file (usually privkey.pem)')
@click.option('debug', '--debug/--no-debug', default=False,
              help='Enable or disable debugging output of API requests to FreeNAS system (default: disabled)')
@click.option('quiet', '--quiet/--no-quiet', default=False,
              help='Enable or disable output of progress messages (default: disabled)')
def main(url, tls_verify, user, password, certfile, keyfile, debug, quiet):
    """A tool for deploying TLS certificates obtained by certbot to FreeNAS 11.1 (or later) systems."""

    if url is None:
        click.echo('A URL for a FreeNAS system must be provided.')
        click.echo("Run '%s --help' for information on how to use this tool." % (sys.argv[0]))
        sys.exit(2)

    if user is None or password is None:
        click.echo('Both a user and its password must be provided.')
        click.echo("Run '%s --help' for information on how to use this tool." % (sys.argv[0]))
        sys.exit(2)

    if certfile is not None and keyfile is None:
        click.echo('If a certificate file path is provided, '
                   'the corresponding private key file path must also be provided.')
        click.echo("Run '%s --help' for information on how to use this tool." % (sys.argv[0]))
        sys.exit(2)

    if certfile is None and keyfile is not None:
        click.echo('If a private key file path is provided, '
                   'the corresponding certificate file path must also be provided.')
        click.echo("Run '%s --help' for information on how to use this tool." % (sys.argv[0]))
        sys.exit(2)

    if certfile is None and keyfile is None:
        if os.environ.get('RENEWED_LINEAGE'):
            dir = os.environ.get('RENEWED_LINEAGE')
            certfile = os.path.join(dir, 'fullchain.pem')
            keyfile = os.path.join(dir, 'privkey.pem')
        else:
            click.echo('Automatic certificate and private key file discovery only '
                       'supported when this tool is run as a certbot renewal hook.')
            click.echo("Run '%s --help' for information on how to use this tool." % (sys.argv[0]))
            sys.exit(2)

    if debug:
        quiet = False

    ep = freenas_api_endpoint(url=url, tls_verify=tls_verify, user=user, password=password)

    logging.basicConfig()

    if debug:
        http_client.HTTPConnection.debuglevel = 1
        logging.getLogger().setLevel(logging.DEBUG)
        requests_log = logging.getLogger("requests.packages.urllib3")
        requests_log.setLevel(logging.DEBUG)
        requests_log.propagate = True

    res = ep.request(
        verb='GET',
        api='version/'
        )

    if res.status_code == 200:
        active_version = pkg_resources.parse_version(res.json()['fullversion'])
        required_version = pkg_resources.parse_version('FreeNAS-11.1')
        if active_version < required_version:
            click.echo("FreeNAS version %s does not support the necessary API "
                       "operations for this tool; FreeNAS 11.1 or later is required"
                       % (active_version))
            sys.exit(1)
        if not quiet:
            click.echo('Certificate import successful')
    else:
        if not quiet:
            click.echo('Unable to determine FreeNAS version')
            click.echo(res)
        sys.exit(1)

    certname = "le-%s" % (int(time.time()))

    with open(certfile, 'r') as file:
        cert = file.read()

    with open(keyfile, 'r') as file:
        key = file.read()

    res = ep.request(
        verb='POST',
        api='certificate/import/',
        json={
            'cert_name': certname,
            'cert_certificate': cert,
            'cert_privatekey': key,
        },
    )

    if res.status_code == 201:
        if not quiet:
            click.echo('Certificate import successful')
    else:
        if not quiet:
            click.echo('Certificate import failed')
            click.echo(res)
        sys.exit(1)

    res = ep.request(
        verb='GET',
        api='certificate/',
        params={'limit': 0},
    )

    if res.status_code == 200:
        if not quiet:
            click.echo('Certificate list successful')
    else:
        if not quiet:
            click.echo('Certificate list failed')
            click.echo(res)
        sys.exit(1)

    cert = next((c for c in res.json() if c['cert_name'] == certname), None)

    if cert is None:
        click.echo('Unable to find new cert in cert list')
        sys.exit(1)

    res = ep.request(
        verb='PUT',
        api='settings/',
        json={
            'stg_guicertificate': cert['id'],
        },
    )

    if res.status_code == 200:
        if not quiet:
            click.echo('Certificate activation successful')
    else:
        if not quiet:
            click.echo('Certificate activation failed')
            click.echo(res)
        sys.exit(1)

    try:
        res = ep.request(
            verb='POST',
            api='settings/restart-httpd-all/',
        )
    except requests.exceptions.ConnectionError:
        # this error is expected since the request restarted the HTTP server
        pass

    sys.exit(0)


if __name__ == "__main__":
    main()  # pragma: no cover
