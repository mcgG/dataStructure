import socket
import time
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ

# select: System Call ----> watch the readiness of a unix-file (socket) io
# non-blocking socket

selector = DefaultSelector()

class Future:               # ~= Promise, return the caller scope a Promise

    def __init__(self):
        self.callbacks = []

    def resolve(self):      # on future event callback
        for func in self.callbacks:
            func()

class Task:                 # responsible for calling next() on generators
                            # in charge fo the async functions
    def __init__(self, gen, eventLoop):
        self.gen = gen
        self.step()

    def step(self):         # go to next step/next yield
        try:
            f = next(self.gen)
            f.callbacks.append(self.step)
        except StopIteration as e:
            eventLoop.n_task -= 1
            print('-----------------------------', 'Byte Received', e, '\n\n')


class EventLoop(object):

    def __init__(self):
        self.n_task = 0

    def add_task(self, generator):
        self.n_task += 1
        Task(generator, self)

    def start(self):
        while self.n_task:
            # retrun readable or writable event
            events = selector.select()
            for event, mask in events:
                fut = event.data
                fut.resolve()

def async_get(path):
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 8080))
    except BlockingIOError as e:
        print('------', e)
    request = 'GET %s HTTP/1.0\r\n\r\n' % path

    print('11111111111111')

    f = Future()



    # register selector event, socket's fs, write event, and pass future as param
    selector.register(s.fileno(), EVENT_WRITE, data=f)
    # yield will interrupt the function
    yield f
    print('222222222222222')
    # the socket is writable
    selector.unregister(s.fileno())
    s.send(request.encode())

    totalReceived = []
    while True:
        f = Future()
        selector.register(s.fileno(), EVENT_READ, data=f)
        yield f

        # s is readable
        selector.unregister(s.fileno())
        received = s.recv(1000)
        if received:
            totalReceived.append(received)
        else:
            body = (b''.join(totalReceived).decode())
            print('------------------------------')
            print(body)
            return len(body)

if __name__ == '__main__':
    start = time.time()
    eventLoop = EventLoop()

    for i in range(20):
        eventLoop.add_task(async_get('/seckill/get'))
    eventLoop.start()
    print('Total cost', time.time() - start)
