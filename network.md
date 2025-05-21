# Network 

## Manager Configuration
Since the manager will have a static IP address that will need to be configured first. Use the [nmtui](https://www.mankier.com/1/nmtui) utility to configure the ethernet port.

## Fixed Network Devices

Network Mask __255.255.255.0__

|IP|Hardware|Purpose|
|--|--------|-------|
|192.168.10.1 | HP2530-48G (J9775A)| Network Switch |
|192.168.10.2 | Mac Book | System Admin |
|192.168.10.3 | Raspberry pi| DHCP|

## DHCP Range

192.168.10.100 -> 192.168.10.255
