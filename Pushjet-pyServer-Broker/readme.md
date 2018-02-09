Pushjet Server Broker [![License](http://img.shields.io/badge/license-BSD-blue.svg?style=flat)](/LICENSE)[![Build Status](https://travis-ci.org/KenN7/Pushjet-Server-Broker.svg?branch=master)](https://travis-ci.org/KenN7/Pushjet-Server-Broker)
=====================
This part of pushjet manages the communication between clients that are 
listening to pushjet and the server. It uses ZeroMQ for the messaging 
which allows the server to be scaled at ease. The method for sending out 
messages is called pub/sub. It makes sure that only the messages that 
matter are processed by the right connections. 

This modified version works with python

## Installation 
```sh
pip install -r requirements.txt
```

## Launch
python broker.py (-r "relay socket") (-p "publish socket")
