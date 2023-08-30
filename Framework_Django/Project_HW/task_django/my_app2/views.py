from random import randint
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)

def heads_tails(request):
    result = "Heads" if randint(0, 1) else 'Tails'
    logger.info(f'{result=}')
    return HttpResponse(result)


def cube(request):
    result = str(randint(1, 6))
    logger.info(f'{result=}')
    return HttpResponse(result)


def rand_num(request):
    result = str(randint(1, 100))
    logger.info(f'{result=}')
    return HttpResponse(result)
