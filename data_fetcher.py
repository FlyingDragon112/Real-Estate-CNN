import requests
import pandas as pd
import time
data = pd.read_csv("data/test2.csv")

# https://github.com/dietrichmax/docker-staticmaps
counter = 0
for i in range(0,len(data)):
    l1 = data['lat'][i]
    l2 = data['long'][i]
    query = f"http://localhost:3000/api/staticmaps?width=512&height=512&center={l1},{l2}&zoom=30&basemap=satellite"
    response = requests.get(query)
    with open(f"test_images/{data['id'][i]}.png", "wb") as f:
        f.write(response.content)
    time.sleep(0.8)
    counter += 1
    print(f'{counter}/{len(data)}',end='\r')

data = pd.read_csv("data/train(1).csv")

# https://github.com/dietrichmax/docker-staticmaps
counter = 0
for i in range(0,len(data)):
    l1 = data['lat'][i]
    l2 = data['long'][i]
    query = f"http://localhost:3000/api/staticmaps?width=512&height=512&center={l1},{l2}&zoom=30&basemap=satellite"
    response = requests.get(query)
    with open(f"images/{data['id'][i]}.png", "wb") as f:
        f.write(response.content)
    time.sleep(0.8)
    counter += 1
    print(f'{counter}/{len(data)}',end='\r')
# docker run -d -p 3000:3000 staticmaps 