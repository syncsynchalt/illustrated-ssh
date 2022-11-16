all: config.stamp build.stamp

rebuild:
	rm -f build.stamp
	$(MAKE)

openssh-9.1p1:
	curl -O https://cdn.openbsd.org/pub/OpenBSD/OpenSSH/portable/openssh-9.1p1.tar.gz
	tar -zxvf openssh-9.1p1.tar.gz
	cd openssh-9.1p1 && patch -p1 < ../stable.patch

config.stamp:
	cd openssh-9.1p1 && ./configure -C --with-ssl-dir=$$(pwd)/../../openssl/install --prefix=$$(pwd)/../install
	touch config.stamp

build.stamp:
	cd openssh-9.1p1 && make -j 2
	cd openssh-9.1p1 && make -j 2 install
	touch build.stamp
