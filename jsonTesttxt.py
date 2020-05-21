from pykrx import stock 
import json, sqlite3

# stockJSON = {
# "skhynix":{
#     "price":9000,
#     "rank":1
# },
# "kisa":{
#     "price":8900,
#     "rank":2
# },
# "samsun" :{
#     "price":8800,
#     "rank":3
# }
# }

# with open('stocklist.json','w') as JSON:
#     json.dump(stockJSON,JSON)

# with open('stocklist.json','r') as JSON:
#     json_data = json.load(JSON)

# print(json_data)

# with open("stocklist.json","r") as JSON:
#     myJSON = json.load(JSON)

# mySort = []
# for k in myJSON.keys():
#     mySort.append([k,myJSON[k]["rank"]])

# mySort.sort(key=lambda x: x[1])
# print(mySort)

# conn = sqlite3.connect("db.sqlite3")
# cur = conn.cursor()
# res = cur.execute("SELECT * FROM User").fetchall()

# print(res)

tickers = stock.get_market_ticker_list()
# print(tickers)
myJSON = {}
for ticker in tickers:
    myJSON[ticker]=stock.get_market_ticker_name(ticker)

with open("tickerList.json","w") as JSON:
    json.dump(myJSON,JSON,ensure_ascii=False)

with open("tickerList.json","r") as JSON:
    myJson=json.load(JSON)

print(myJson)