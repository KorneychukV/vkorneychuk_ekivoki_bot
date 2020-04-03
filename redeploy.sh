#!/bin/bash
git add .
echo "Input commit comment:"
read commit_comment
git commit -m commit_comment
git push
