import datetime
from pyres import ResQ 
import sys, traceback
from pyres.failure.redis import RedisBackend
_backend = RedisBackend
def create(*args, **kwargs):
    return _backend(*args, **kwargs)

def count(resq):
    return _backend.count(resq)

def all(resq, start, count):
    return _backend.all(resq, start, count)

def clear(resq):
    return _backend.clear(resq)

def requeue(resq, failure_object):
    queue = failure_object._queue
    payload = failure_object._payload
    return resq.push(queue,payload)
    