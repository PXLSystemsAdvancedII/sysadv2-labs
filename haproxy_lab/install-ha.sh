#!/bin/bash
sudo apt update
sudo apt install -y haproxy hatop
sudo rm /etc/haproxy/haproxy.cfg
sudo cp ./haproxy.cfg /etc/haproxy
sudo service haproxy start
sudo service haproxy status
