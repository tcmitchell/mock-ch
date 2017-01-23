import time

def application(environ, start_response):

#    print "ENV = " + str(environ)
    time.sleep(1)
    start_response('200 OK', [('Content-Type', 'text/plain')])
    msg = ''
    for x in sorted(environ.keys()):
        msg = msg + '%r = %r\n' % (x, environ[x])
    return [msg]
