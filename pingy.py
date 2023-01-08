#! /usr/bin/python3

import csv
import subprocess

# Open the CSV file
with open('ip_addresses.csv', 'r') as csvfile:
  # Read the CSV file into a list of rows
  rows = csv.reader(csvfile)

  # Iterate over the rows in the CSV file
  for row in rows:
    # Get the IP address from the row
    ip_address = row[0]

    # Use the ping command to send two ICMP echo packets to the IP address
    result = subprocess.run(['ping', '-c', '2', ip_address], stdout=subprocess.DEVNULL)
    #print(result)

    # Check the return code of the ping command
    if result.returncode == 0:
      # The ping command was successful, so the IP address is up
      print(f'{ip_address} is up')
    else:
      # The ping command failed, so the IP address is down
      print(f'{ip_address} is down')
