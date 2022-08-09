def quoteFilter(quote,stock,date):
    parts = quote.strip().split(' ')
    carryList = list(filter(''.__ne__, parts))

    for item in list(carryList):
        try:
            flItem = float(item)
        except ValueError:
            carryList.remove(item)

    for i in range(0, len(carryList)):
        item = carryList[i]
        carryList[i] = "{:,}".format(float(item))
    return (f"""```lua
{stock.upper()} -- [{date}]
Recent: ${carryList[5]}

====================
Open: ${carryList[2]}
High: ${carryList[0]}
Low: ${carryList[1]}
Close: ${carryList[3]}
Trade Volume: {carryList[4]}
```""")
