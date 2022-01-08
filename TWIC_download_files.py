import requests, zipfile, io


print('Initalazing')

last_num = 1417

older_num = 920

for num in range(older_num, last_num+1):
    url = 'https://theweekinchess.com/zips/twic'
    
    url += str(num)
    url += 'g.zip'
    print(url)
    print('\n')

    req = requests.get(url, headers={"User-Agent": "XY"})

    filename = url.split('/')[-1]

    print(filename)

    z = zipfile.ZipFile(io.BytesIO(req.content))
    z.extractall()


# Split URL to get the file name

print('Downloading Completed')