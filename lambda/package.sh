#!/bin/bash

rm -rf package
rm -f lambda.zip

mkdir package

pip install \
-r requirements.txt \
-t package/

cp app.py package/

cd package

zip -r ../lambda.zip .

cd ..