

import requests

print('Initalazing')

last_num = 1417

older_num = 923

for num in range(older_num, last_num+1):
    url = 'https://theweekinchess.com/zips/twic'
    
    url += str(num)
    url += 'g.zip'
    print(url)
    print('\n')

    req = requests.get(url)

    filename = url.split('/')[-1]

    # Writing the file to the local file system
    with open(filename, 'wb') as output_file:
        output_file.write(req.content)

# Split URL to get the file name

print('Downloading Completed')