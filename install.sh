rm -rf dist && mkdir dist
git clone https://github.com/aws/aws-greengrass-core-sdk-python.git
# pip3 install -r requirements.txt --target ../dist/ 
cp -R aws-greengrass-core-sdk-python/
cd .. && rm -rf aws-greengrass-core-sdk-python/
cp ./src/* ./dist
cd ./src
python3 -m pip install --upgrade pip
python3 -m venv venv && source venv/bin/activate 
pip3 install -r requirements.txt --target ../dist/