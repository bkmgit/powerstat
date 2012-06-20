CFLAGS += -Wall

VERSION=0.01.16

BINDIR=/usr/bin
MANDIR=/usr/share/man/man8

powerstat: powerstat.o
	$(CC) $< -lm -o $@

powerstat.8.gz: powerstat.8
	gzip -c $< > $@

dist:
	git archive --format=tar --prefix="powerstat-$(VERSION)/" V$(VERSION) | \
		gzip > powerstat-$(VERSION).tar.gz

clean:
	rm -f powerstat powerstat.o powerstat.8.gz
	rm -f powerstat-$(VERSION).tar.gz

install: powerstat powerstat.8.gz
	mkdir -p ${DESTDIR}${BINDIR}
	cp powerstat ${DESTDIR}${BINDIR}
	mkdir -p ${DESTDIR}${MANDIR}
	cp powerstat.8.gz ${DESTDIR}${MANDIR}
