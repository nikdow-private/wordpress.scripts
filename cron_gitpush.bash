#!/bin/bash
# backup /etc directory
cd /etc
git add --all
git commit -a -m `date +"%Y-%m-%d-%H:%M:%S"`
git push https://nikdow-private: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@github.com/nikdow-private/nikdow_etc.git master
