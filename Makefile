
install:
	install mock.conf /etc/httpd/conf.d
	mkdir -p /usr/share/mock-ch
	install mock.wsgi mock.py /usr/share/mock-ch
