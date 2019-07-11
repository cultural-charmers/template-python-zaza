#!/usr/bin/env sh

cd hooks
for hook in install config-changed start stop upgrade-charm update-status; do ln -s hooks.py $hook; done
cd ..
git init
git add .
git commit -a -m "Initial Cookiecutter Commit."
