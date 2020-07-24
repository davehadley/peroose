#!/usr/bin/env bash
versionsource=$(cat peroose/_version.py);
version=$(python3 -c "${versionsource};print(__version__)");
mkdir testrelease && cd testrelease && python3 -m venv venvrelease && source venvrelease/bin/activate #&& cp -r ../tests ./

if [ $? -ne 0 ]; then
    exit 1
fi

pip install --no-cache-dir --upgrade "peroose>=${version}" && python -m unittest discover tests