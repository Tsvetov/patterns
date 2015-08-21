# -*- coding: utf-8 -*-

import functools

__author__ = 'cpn'


"""
Цепочка ответственности на основе сопрограмм
"""


class Event:
    KEYPRESS = 'KEYPRESS'


def coroutine(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        generator = function(*args, **kwargs)
        next(generator)
        return generator
    return wrapper


@coroutine
def key_handler(successor=None):
    while True:
        event = (yield)
        if event.kind == Event.KEYPRESS:
            print ("event")
        elif successor is not None:
            successor.send(event)


