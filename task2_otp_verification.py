# -*- coding: utf-8 -*-
"""Task2-OTP Verification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ux7q69nWoAThWL7lDyJog6L3c6EkJ9Zf
"""

import os
import math
import random
import smtplib
import ssl
digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp=OTP+"is you OTP"
msg=otp
s =  smtplib.SMTP_SSL("smtp.gmail.com",465)
s.login("backupavadhoot@gmail.com","xwvwbbxsyumcdpss")
s.sendmail("backupavadhoot@gmail.com","backupavadhoot@gmail.com",msg)
a= input("Enter Your OTP >> :")
if a== OTP:
    print ("CONGRATULATION!! Your OTP is Verified")
else:
    print("PLEASE cheack your OTP again and fill it properly")