countrycode= {'India' : '3841',
                  'Australia': '4820',
                  'Nepal': '0024'}

print("Country code for India:")
print(countrycode.get('India', 'Not Found'))

print("Country code for Japan:")
print(countrycode.get('Japan', 'Not Found'))