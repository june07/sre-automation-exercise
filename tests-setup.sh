#!/bin/sh
curl -o - http://ftp.uk.debian.org/debian/dists/stable/main/Contents-i386.gz | gunzip > tests/Contents-i386
curl -o - http://ftp.uk.debian.org/debian/dists/stable/main/Contents-arm64.gz | gunzip > tests/Contents-arm64
curl -o - http://ftp.uk.debian.org/debian/dists/stable/main/Contents-amd64.gz | gunzip > tests/Contents-amd64

