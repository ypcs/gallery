#!/bin/sh
set -e

BASEDIR="$(realpath $(dirname $(dirname $0)))"
VE_DIR="${BASEDIR}/ve"

echo "I: Initialize virtual environment..."
virtualenv --no-site-packages -p python3 "${VE_DIR}"

echo "I: Install dependencies from requirements.txt..."
${VE_DIR}/bin/pip install -r "${BASEDIR}/requirements.txt"

echo ". ${VE_DIR}/bin/activate" >> ~/.bashrc
