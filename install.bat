@echo off
cls
set installpath=%UserProfile%\Desktop
set installurl=https://codeload.github.com/cat-linux/beaverrecon/zip/master

color 0B
echo Downloading Files...
curl %installurl% -O -J -L -o %installpath%

python -m zipfile -e %installpath%\beaverrecon-master.zip %installpath%

cd %UserProfile%\Desktop\beaverrecon-master
python -m pip install -r requirements.txt --user
cd ..
del %UserProfile%\Desktop\beaverrecon-master.zip
echo cd %UserProfile%\Desktop\beaverrecon-master >> beaverrecon.bat
echo python BeaverRecon.py >> beaverrecon.bat
del install.bat
