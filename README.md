# WhatInQR

# What in WhatInQR?
WhatInQR extracts the string contained in the QR code using a PC camera

# Installation
## Install from source.
```
$ git clone https://github.com/fujiwara-e/WhatInQR.git
```
## Install Required Packages
```
$ pip install pyzbar numpy opencv-python
```
if you don't have libzbar.so
```
$ brew install zbar (For MAC)
$ sudo apt install libzbar0 (For Linux)
```

# Usage
```
$ python WhatInQR
```
A window will appear, displaying the image being captured by the camera.




