"""Example views. Feel free to delete this app."""

import logging

from django import http
from django.shortcuts import render, render_to_response

#from session_csrf import anonymous_csrf

def home(request, template=None):
    """Main example view."""
    return render_to_response('example/home.html')
