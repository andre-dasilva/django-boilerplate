from django.shortcuts import render

import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Hello there I am logging')

    context = {
        "message": "Hello, world from MVC"
    }
    return render(request, 'tasks/index.html', context)