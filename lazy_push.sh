#!/bin/sh
echo "enter commit message using quotes if more than 1 word"
git add .
git commit -m "$1"
git push --all
