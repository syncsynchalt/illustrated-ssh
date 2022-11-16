all: config.stamp build.stamp

rebuild:
	rm -f build.stamp
	$(MAKE)

config.stamp:
	cd openssl-3.0.7 && ./configure --prefix=$$(pwd)/../install
	touch config.stamp

openssl-3.0.7:
	curl -O https://www.openssl.org/source/openssl-3.0.7.tar.gz
	tar -zxvf openssl-3.0.7.tar.gz
	cd openssl-3.0.7 && patch -p1 < ../stable.patch

build.stamp:
	cd openssl-3.0.7 && make -j 2 install
	touch build.stamp
