#!/usr/bin/env python3

from aws_cdk import core

from url_shortener.url_shortener_stack import UrlShortenerStack


app = core.App()
UrlShortenerStack(app, "url-shortener")

app.synth()
