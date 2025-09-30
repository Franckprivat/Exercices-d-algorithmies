from typing import List

def get_top_stocks(stocks: List[str], prices: List[List[float]]) -> List[str]:
    
    averages = []
    
    for i in range(len(stocks)):
        
        total = sum(prices[day][i] for day in range(len(prices)))
        avg = total / len(prices)
        averages.append((avg, stocks[i]))  

    averages.sort(reverse=True, key=lambda x: x[0])
    
    return [stock for _, stock in averages[:3]]


stocks = ["AMZN", "CACC", "EQIX", "GOOG", "ORLY", "ULTA"]
prices = [
    [12.81, 11.09, 12.11, 10.93, 9.83, 8.14],
    [10.34, 10.56, 10.14, 12.17, 13.1, 11.22],
    [11.53, 10.67, 10.42, 11.88, 11.77, 10.21]
]

top_3 = get_top_stocks(stocks, prices)

print(top_3)