#!/bin/bash

function create() {
    cd
    python3 create.py $1
    cd /Users/uyentran/Desktop/Admin/MyProjects/$1
    git init
    git remote add origin https://github.com/uyentrannn/$1.git
    touch README.md
    git add .
    git commit -m "Inital commit"
    git push -u origin master
    code .
}