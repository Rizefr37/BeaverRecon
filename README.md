# BeaverRecon
The tool is finally decently stable if theres any errors please open a issue

Current Version: 0.8.1

## Installing
The tool runs on windows and linux 

### Linux

#### Debian Based
```
git clone https://github.com/Cat-Linux/BeaverRecon.git
cd BeaverRecon
chmod +x install.sh && ./install.sh
python3 BeaverRecon.py
```

#### Redhat Based
```
sudo yum update -y && yum upgrade -y
sudo yum install git curl python3 python3-pip -y
git clone https://github.com/Cat-Linux/BeaverRecon.git
cd BeaverRecon
python3 -m pip install -r requirements.txt
python3 BeaverRecon.py
```
#### Termux
```
pkg update  && pkg upgrade
pkg install git curl python
git clone https://github.com/Cat-Linux/BeaverRecon.git
cd BeaverRecon
pip install -r requirements.txt
python BeaverRecon.py
```

### Windows 10
PS: you need winrar installed for this other wise you can just do this manually

Download the latest python version from here: https://www.python.org/

make sure to add to path when installing python

once done download the install.bat from files

you can install it manually or download it via cmd or powershell

```
curl https://raw.githubusercontent.com/cat-linux/beaverrecon/master/install.bat -o %UserProfile%\Desktop\install.bat
```
PS: this command downloads it to your desktop

once the bat is downloaded just run it

once its done a file named beaverrecon.bat is created, just run that and its done.

i had to make this installation process even more simpler than it already was because some people lacked the brain cells to install it

## About
BeaverRecon is a person OSINT tool that scrapes sites for information

### Tools
❌ - Down 
✅ - Up and Fully Implemented 
☑️ - Up But Not Fully Implemented
⚠️ - Yet To Be Added

- ✅ - http://ip-api.com/json/
- ✅ - http://instagram.com/
- ✅ - https://thatsthem.com/
- ✅ - http://scylla.sh/
- ✅ - https://emailrep.io/
- ❌ - http://hashes.org/
- ✅ - http://haveibeenpwned.com/
- ✅ - https://pwndb2am4tzkvold.onion.ws
- ✅ - http://validnumber.com
- ✅ - http://telnyx.com
