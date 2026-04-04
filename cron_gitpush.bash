#!/bin/bash
# backup /etc directory
cd /etc
git add --all
git commit -a -m `date +"%Y-%m-%d-%H:%M:%S"`
git push
