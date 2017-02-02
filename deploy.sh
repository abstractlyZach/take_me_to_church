#!/bin/bash
# deploy.sh
# deploys the current code to heroku
# IMPORTANT: make sure to run this code from the source code directory

# Used this as a resource:
# https://www.linux.com/learn/writing-simple-bash-script

# Used `chmod u+x deploy.sh` to make it executable
# so you can run it with `./deploy.sh`

# reminder
echo "IMPORTANT: run this only from the source code directory!"
echo "Ctrl-C to quit"

# prompt
echo -e "Enter commit message: "
# store commit message in the $message variable
read message

# commit to github
# https://github.com/exzacktlee/take_me_to_church
git add .
git commit -m "$message"
git push -u origin master

# copy the contents of this folder into the other folder, except for the gitignore
cp -r ./* ../tmtc_staging/

# switch to staging directory
cd ../tmtc_staging

# deploy to the heroku server
git add . 
git commit -m "$message"
git push heroku master

# Spins up a dyno on heroku
heroku ps:scale web=1
