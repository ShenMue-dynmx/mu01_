# IK arm
Three-link arm for ik tests
Uses [URDF-VIS](https://github.com/openrr/urdf-viz)

### Dependenices 

``` 
pyautogui
json
requests
numpy
ikpy
``` 
To install all in one go try running 
```
python3 -m pip install  pyautogui numpy
```
requests and json must be already installed with python by default.

## How to launch
Once in ik_arm_genericTest folder:

Fire up one terminal with following command
```    
urdf-viz arm/urdf/arm.urdf
```
Then launch 
``` 
python controller.py 
``` 
from different terminal
