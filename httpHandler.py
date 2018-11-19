import requests as reqs
import alchItems

r = reqs.get('http://localhost:3000/grabprices')
itemData = r.json()
targetItems = list(filter(lambda item : item['alchProfit'] >=50,itemData))
print(targetItems)
if len(targetItems)>0:
    alchItems.itemList = targetItems


