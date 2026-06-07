#!/bin/bash

ip = input "Enter Target IP: " ip
ip = input "Enter NSE Script Name: " script
echo "Running Nmap Scan..."
nmap --script=$script $ip