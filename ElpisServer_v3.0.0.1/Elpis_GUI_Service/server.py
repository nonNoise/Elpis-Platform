from bottle import route, run, template
import os

@route('/')
def index():
    pid = os.getpid()
    return '<b>Hello</b>! %d:%d' % (main,pid)


main = os.getpid()
run(host='localhost', port=1234,reloader=False)