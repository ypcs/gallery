#!/bin/sh
set -e

# This adds new APT repository to your system & installs new GPG key
# => has privileges to replace ANYTHING on your system
#
# Also, when you run "heroku" for the first time, installs
# lots of possibly unsafe scripts/code to your home directory
#
# YOU SHOULD NEVER INSTALL SOMETHING LIKE THIS ON PRODUCTION
# SYSTEM
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
