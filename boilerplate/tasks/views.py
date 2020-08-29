from django.http import HttpResponse
from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Hello there I am logging')
    return HttpResponse("Hello, world from MVC")