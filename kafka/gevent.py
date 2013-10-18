import gevent
import gevent.event
import gevent.queue
import gevent.pool
import gevent.socket
import gevent.coros
import kazoo.handlers.gevent import SequentialGeventHandler

from .common import _KafkaDriver

class KafkaGeventDriver(_KafkaDriver):
    def __init__(self):
        self.socket = gevent.socket
        self.sleep = gevent.sleep
        self.Queue = gevent.queue.Queue
        self.Event = gevent.event.Event
        self.kazoo_handler = SequentialGeventHandler
        self.Lock = gevent.coros.Semaphore

    def Proc(self, target=None, args=(), kwargs=None):
        return gevent.Greenlet(target, *args, **(kwargs or {}))

