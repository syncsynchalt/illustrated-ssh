# The Illustrated SSH Connection

Will be published at https://ssh.xargs.org

- `site/`: page source for the finished product
- `server/server`: server script
- `client/client`: client script
- `openssh/`: custom build of openssh (randomness removed)
- `openssl/`: custom build of openssl (randomness removed)
- `captures/`: PCAP and keylog files

### Build instructions

If you'd like a working example that reproduces the exact handshake documented on the site:

```
git clone https://github.com/syncsynchalt/illustrated-ssh.git
cd illustrated-ssh/
cd openssl/
make
cd ../openssh/
make
```

Then open two terminals and run `./server` in the server/ subdir and `./client-rsa` or `./client-pass` in the client/ subdir.  The password for `client-pass` is `secure-password`.

This has been shown to work on MacOS 12 and only has a few easy-to-find dependencies: gcc or clang, make, patch,
etc.
