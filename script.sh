#!/usr/bin/env bash

echo "Crawling $1..." 
wget -qr -A.html,.htm,.php - $1
grep -r -n $2 $1/

read -p "Press Enter to continue" </dev/tty