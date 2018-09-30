# coding: utf-8
# In[ ]:
# Program: ethplorer.ipynb
# Ethplorer holders data fetch
# Output write CSV file named optput.csv
# Author: Kevin Liu
# Date: 2018-09-30
# Ver: 0.3

import requests
import json
import csv

res = requests.get('https://ethplorer.io/service/service.php?refresh=holders&data=0x503F9794d6A6bB0Df8FBb19a2b3e2Aeab35339Ad&page=tab%3Dtab-holders%26pageSize%3D49999&showTx=all')

if res.status_code == 200:
    
    data = json.loads(res.text)
    print('Success get data.')
  
    # Write JSON to CSV

    with open('output.csv', 'w', newline='') as csvfile:
    
        fieldnames = ['address', 'balance', 'share']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
        writer.writeheader()
    
        for csvline in data['holders']:
            writer.writerow(csvline)

    print('CSV output success.')    
    
    csvfile.close
    
else:
    
    print('Connection server fail.')


