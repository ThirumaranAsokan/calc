import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
from datetime import datetime, timedelta
cg = CoinGeckoAPI()

st.image('', use_column_width=True)
#st.write('''## Choose Crypto Currency''')
Stocks = st.selectbox('Select Crypto Currency', ['bitcoin','dogecoin','ethereum','binancecoin','tether','cardano','litecoin','shiba-inu','wazirx','polygon','bnb','xrp','dai','avalanche','stellar','cronos','ftx','uniswap','polkadot'])
st.write('Choice',Stocks)
choice= Stocks
st.write('Date')
today = datetime.utcnow().date()
past = today - timedelta(days=1)
date = st.date_input("Date: ", value=past, min_value=datetime(2015,1,1), max_value=past)
st.write(date)
currency = st.selectbox('Currency Type', ['GBP'])
Purchase = st.number_input(currency +" purchase: ", min_value=0, max_value=999999999)
crypto_current = cg.get_price(choice, vs_currencies= currency)[id][currency]

#Reformat Historical Date for next function
Date = date.strftime("%d-%m-%Y")
Years = datetime.strptime(Date,"%d-%m-%Y")
value = cg.value(choice, vs_currencies=selected_currency_type, date=selected_historical_date_reformat)['market_data']['current_price'][selected_currency_type]
value = float(value)

# Display Results - Historical Value
st.write('''# Results''')
st.write('''## Historic Analysis''')

if selected_crypto_currency_historic == 0:
    st.write("YOU  PURCHASED: 0",selected_crypto_currency)
else:
    st.write("YOU  PURCHASED: ", round((selected_amount/selected_crypto_currency_historic),5),selected_crypto_currency)

st.write("At A PRICE $", selected_crypto_currency_historic,' per',selected_crypto_currency)


st.write('''## Today Prices''')
if selected_crypto_currency_historic == 0:
    total_coins = 0
else:
    total_coins = selected_amount/selected_crypto_currency_historic

current_selected_currency_type = total_coins * crypto_current
perc_change = (current_selected_currency_type - selected_amount)/(selected_amount)*100
selected_currency_type_diff = current_selected_currency_type - selected_amount

st.write("CURRENCY VALUE: $", round(current_selected_currency_type,2))
st.write(" VALUE IN PERCENTAGE ", round(perc_change, 2), "%")

if selected_currency_type_diff == 0:
   st.write('''# You were lucky with profit''')
elif selected_currency_type_diff <= 0:
   st.write('''# You got Loss''')
else:
   st.write('''# You lost Out On''')
st.write('$', abs(round(selected_currency_type_diff,2)),"!!!")

now = datetime.now()
historical_prices = cg.get_coin_market_chart_range_by_id(id, vs_currency=selected_currency_type, from_timestamp=selected_historical_date_datetime.timestamp(), to_timestamp=now.timestamp())['prices']

dates = []
prices = []

for x,y in historical_prices:
  dates.append(x)
  prices.append(y)

dictionary = {"Prices":prices, "Dates":dates}
df = pd.DataFrame(dictionary)
df['Dates'] = pd.to_datetime(df['Dates'],unit='ms',origin='unix')

st.line_chart(df.rename(columns={"Dates":"index"}).set_index("index"))