gtsrvd
======

WIP

Ever want to host a localhost server on the public internet, but
can't easily or conveniently punch through your NAT? Yes, that aspect of the
future is broken. OR IS IT..?!

gtsrvd seeks to solve this problem in a similar way as ngrok or serveo.
By a simple command, we acquisition a subdomain, set up a proxy, and
host content to the public internetz. How is this? Well firstly, you do it,
we just automate it :). You host a box (ec2?) on your favorite cloud provider,
run what should be a broadly well known ssh command, and you win!

Getting started
===============

You'll need your cloud provider keys set up so the daemon can acquire
subdomains and route properly. Assuming a domain of `blastedstudios.com`
and ssh'd to an ec2 instance with hostname `publicbox` and happy dns set up
already, from publicbox (with public port 80) run::

    pipenv install
    DOMAIN=blastedstudios.com pipenv run gtsrvd.app

Then from any hapless host (behind NAT, for maximum effect), run::

    ssh -R 8080:localhost:80 gtrkt@publicbox.blastedstudios.com

This should create a domain gtrkt.blastedstudios.com, then traffic will
flow to your proxy box over ssh to your localhost. What a winner.

Testing
-------

To run unit tests, flake8, and coverage reports, run::

    make test

Deploying
---------

Deploy gtsrvd to your cloud box with suitable roles to allow for subdomain
tweaking. I know you like how it ends in a `d` which implies daemon, so
hopefully soon I'll include the simplistic systemd unit I've used to automate
this, possibly an ansible config and docker container.

TODO
----

* Add paramiko server to auto-add new route53 routes and proxy
* Treat forwarding ssh like the special snowflake it is
* Possibly treat port 80 uniquelly, possible forcing (via cli arg) ssl
* Add ansible/docker support
* Support different clouds (gcp/azure)

LICENSE
-------

Copyright 2018 Jon Robison

See LICENSE file for info