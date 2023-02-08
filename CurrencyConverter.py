# Currency Converter USD/CNY
amount_usd = [1, 1500, 25000]
amount_cny = [1, 1750, 28000]
USD2CNY = 6.74
data = 'Jan 31, 2023'
print(f"{data} : 1 USD = {USD2CNY} CNY / 1 CNY = {round(1/USD2CNY, 3)} USD\n")
for i in amount_usd:
    print(f"Amount {i} USD = {(i * USD2CNY):.2f} CNY")
for j in amount_cny:
    print(f"Amount {j} CNY = {(j / USD2CNY):.2f} USD")
