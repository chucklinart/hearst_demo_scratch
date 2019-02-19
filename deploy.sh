#!/bin/sh

rsync -av --exclude-from=.rsync_excludes $(pwd)/ chuck@185.10.68.194:/home/chuck/sites/hearst
