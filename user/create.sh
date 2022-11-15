#!/bin/bash -e

sysadminctl -addUser xargs
mkdir ~xargs/.ssh
chmod 0700 ~xargs/.ssh
cp -a ssh/* ~xargs/.ssh
chown -R xargs ~xargs/.ssh
