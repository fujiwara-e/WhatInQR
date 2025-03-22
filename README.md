# WhatInQR

## What is WhatInQR?
WhatInQR extracts the string contained in the QR code using a PC camera.

## Installation
### Install from source.
```
$ git clone https://github.com/fujiwara-e/WhatInQR.git
```
### Install Required Packages
I recommend using venv
```
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip install pyzbar numpy opencv-python
```
pyzbar depends on zbar. if you don't have libzbar.so
```
$ brew install zbar (For MAC)
$ sudo apt install libzbar0 (For Linux)
```

## Usage
```
$ python3 WhatInQR.py
```
A window will appear, displaying the image being captured by the camera.

If you are using it for the first time, you will get a popup asking for accessibility permissions.




