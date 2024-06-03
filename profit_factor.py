import pandas as pd

trades = [
    {
        "type": "trade",
        "orderno": "16440352066",
        "secid": "12208",
        "union": "677477RGJZB",
        "ticker": "MCT/MS",
        "client": "7EV2W/7EV2W",
        "buysell": "S",
        "value": 97.19,
        "price": 97.19,
        "quantity": 1,
        "time": "2024-05-31 14:31:10",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47595455965",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 456,
        "price": 228,
        "quantity": 2,
        "time": "2024-05-29 23:31:33",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47595438845",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 455.58,
        "price": 227.79,
        "quantity": 2,
        "time": "2024-05-29 23:30:48",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47595259326",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 455.6,
        "price": 227.8,
        "quantity": 2,
        "time": "2024-05-29 23:25:21",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47595123968",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 455.5,
        "price": 227.75,
        "quantity": 2,
        "time": "2024-05-29 23:22:41",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47595105082",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 455.58,
        "price": 227.79,
        "quantity": 2,
        "time": "2024-05-29 23:21:19",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47594999309",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 227.92,
        "price": 227.92,
        "quantity": 1,
        "time": "2024-05-29 23:16:50",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47594970959",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 455.98,
        "price": 227.99,
        "quantity": 2,
        "time": "2024-05-29 23:15:45",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47594941541",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 455.72,
        "price": 227.86,
        "quantity": 2,
        "time": "2024-05-29 23:14:36",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47594884991",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 454.84,
        "price": 227.42,
        "quantity": 2,
        "time": "2024-05-29 23:11:04",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47594853733",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 454.56,
        "price": 227.28,
        "quantity": 2,
        "time": "2024-05-29 23:09:36",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47594597589",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 454.16,
        "price": 227.08,
        "quantity": 2,
        "time": "2024-05-29 23:01:46",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47594434126",
        "secid": "4688",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 453.9,
        "price": 226.95,
        "quantity": 2,
        "time": "2024-05-29 23:00:25",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47518271536",
        "secid": "4663",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 439.42,
        "price": 219.71,
        "quantity": 2,
        "time": "2024-05-28 19:59:59",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47518250494",
        "secid": "4663",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 439.58,
        "price": 219.79,
        "quantity": 2,
        "time": "2024-05-28 19:59:38",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47517995351",
        "secid": "4663",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 439.84,
        "price": 219.92,
        "quantity": 2,
        "time": "2024-05-28 19:55:03",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47517976347",
        "secid": "4663",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 439.82,
        "price": 219.91,
        "quantity": 2,
        "time": "2024-05-28 19:54:55",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47517967821",
        "secid": "4663",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 659.76,
        "price": 219.92,
        "quantity": 3,
        "time": "2024-05-28 19:54:47",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47517442431",
        "secid": "4663",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "S",
        "value": 220.19,
        "price": 220.19,
        "quantity": 1,
        "time": "2024-05-28 19:46:35",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47483809951",
        "secid": "4613",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 442.3,
        "price": 221.15,
        "quantity": 2,
        "time": "2024-05-28 15:22:02",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47483809951",
        "secid": "4613",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 442.3,
        "price": 221.15,
        "quantity": 2,
        "time": "2024-05-28 13:22:02",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "47483809951",
        "secid": "4613",
        "union": "677477RFCY9",
        "ticker": "TQBR/MTLR",
        "client": "6WWKY/6WWKY",
        "buysell": "B",
        "value": 442.3,
        "price": 221.15,
        "quantity": 2,
        "time": "2024-05-28 13:21:03",
        "status": None
    },
    {
        "type": "trade",
        "orderno": "16440352066",
        "secid": "12208",
        "union": "677477RGJZB",
        "ticker": "MCT/MS",
        "client": "7EV2W/7EV2W",
        "buysell": "B",
        "value": 98.19,
        "price": 98.19,
        "quantity": 2,
        "time": "2024-05-28 13:21:05",
        "status": None
    },
]


def get_profit(df):
    def get_same_quantities_buy_sell(df):
        def drop_started_sell_ending_buy(df):
            tickers = df['ticker'].unique().tolist()
            for ticker in tickers:
                for index, row in df.iterrows():
                    if row['buysell'] == 'B' and row['ticker'] == ticker:
                        df = df.drop(index)
                    else:
                        break
                # Сброс индексов таблицы начиная с 0
                df = df.reset_index(drop=True)

                # Перебор DataFrame в обратном порядке
                for index in range(len(df) - 1, -1, -1):
                    if df.loc[index, 'buysell'] == 'S' and df.loc[index, 'ticker'] == ticker:
                        df = df.drop(index)
                    else:
                        break
                # Сброс индексов таблицы начиная с 0
                df = df.reset_index(drop=True)

            return df

        def get_difference(df, ticker):
            # Просуммировать все строки 'quantity', где 'buysell' == 'S'
            total_quantity_buy = df.loc[(df['buysell'] == 'B') & (df['ticker'] == ticker), 'quantity'].sum()
            # Просуммировать все строки 'quantity', где 'buysell' == 'S'
            total_quantity_sell = df.loc[(df['buysell'] == 'S') & (df['ticker'] == ticker), 'quantity'].sum()

            return total_quantity_buy - total_quantity_sell

        # Убираем поздние строки с покупкой и ранние с продажей
        df = drop_started_sell_ending_buy(df)
        tickers = df['ticker'].unique().tolist()
        for ticker in tickers:
            difference = get_difference(df, ticker)
            # print(ticker, difference)
            if difference > 0:
                # Перебор DataFrame в обратном порядке
                for index in range(len(df) - 1, -1, -1):
                    if difference != 0:
                        if df.loc[index, 'buysell'] == 'B' and df.loc[index, 'ticker'] == ticker:
                            if df.loc[index, 'quantity'] <= difference:
                                difference -= df.loc[index, 'quantity']
                                df = df.drop(index)
                            elif df.loc[index, 'quantity'] > difference:
                                df.loc[index, 'quantity'] -= difference
                                df.loc[index, 'value'] = df.loc[index, 'quantity'] * df.loc[index, 'price']
                                difference = 0
                    else:
                        break
            elif difference < 0:
                difference = abs(difference)
                # Перебор DataFrame
                for index, row in df.iterrows():
                    if difference != 0:
                        if row['buysell'] == 'S' and row['ticker'] == ticker:
                            if row['quantity'] <= difference:
                                difference -= row['quantity']
                                df = df.drop(index)
                            elif row['quantity'] > difference:
                                df.loc[index, 'quantity'] -= difference
                                df.loc[index, 'value'] = row['quantity'] * row['price']
                                difference = 0
                    else:
                        break

            # Сброс индексов таблицы начиная с 0
            df = df.reset_index(drop=True)
        return df

    # Оставляем равное количество проданного и купленного
    df = get_same_quantities_buy_sell(df)
    tickers = df['ticker'].unique().tolist()
    # print(df[['ticker', 'buysell', 'value', 'price', 'quantity', 'time']])

    # Инициализировать переменные для хранения промежуточных сумм и доходности
    sum_quantities_B = 0
    sum_quantities_S = 0
    sum_values_B = 0
    sum_values_S = 0
    cur_qs_b = 0
    cur_qs_s = 0
    differences = {
        'profit': 0,
        'loose': 0
    }

    for ticker in tickers:
        # Собираем доходы и убытки
        for index, row in df.iterrows():
            if row['ticker'] == ticker:
                if row['buysell'] == 'B':
                    if sum_quantities_B + row['quantity'] > sum_quantities_S > sum_quantities_B:
                        cur_qs_b = sum_quantities_S - sum_quantities_B
                        sum_quantities_B += cur_qs_b
                        sum_values_B += row['price'] * cur_qs_b
                    else:
                        sum_quantities_B += row['quantity']
                        sum_values_B += row['value']
                elif row['buysell'] == 'S':
                    if sum_quantities_S + row['quantity'] > sum_quantities_B > sum_quantities_S:
                        cur_qs_s = sum_quantities_B - sum_quantities_S
                        sum_quantities_S += cur_qs_s
                        sum_values_S += row['price'] * cur_qs_s
                    else:
                        sum_quantities_S += row['quantity']
                        sum_values_S += row['value']

                if sum_quantities_B == sum_quantities_S:
                    profit = sum_values_B - sum_values_S
                    if profit >= 0:
                        differences['profit'] += profit
                    else:
                        differences['loose'] += profit
                    # print(index, sum_quantities_B, sum_quantities_S, differences)
                    sum_quantities_B = row['quantity'] - cur_qs_b if cur_qs_b > 0 else 0
                    sum_values_B = row['price'] * sum_quantities_B if cur_qs_b > 0 else 0
                    cur_qs_b = 0
                    sum_quantities_S = row['quantity'] - cur_qs_s if cur_qs_s > 0 else 0
                    sum_values_S = row['price'] * sum_quantities_S if cur_qs_s > 0 else 0
                    cur_qs_s = 0
        print('dif', ticker, differences)

    profit_factor = abs(differences['profit']/differences['loose'])
    return round(profit_factor*100)/100


# Создаем DataFrame из списка словарей
df = pd.DataFrame(trades)
profit_factor = get_profit(df)
print(profit_factor)