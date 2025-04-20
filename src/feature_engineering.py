import pandas as pd

def compute_spread(df):
    """
    Compute the bid-ask spread: ask_1_price - bid_1_price
    """
    df['spread'] = df['AskPriceL1'] - df['BidPriceL1']
    return df

def compute_orderbook_imbalance(df):
    """
    Compute imbalance at level 1: (bid_qty - ask_qty) / (bid_qty + ask_qty)
    """
    bid_qty = df['BidQtyL1']
    ask_qty = df['AskQtyL1']
    df['imbalance'] = (bid_qty - ask_qty) / (bid_qty + ask_qty)
    return df

def compute_microprice(df):
    """
    Compute microprice: (bid_price * ask_qty + ask_price * bid_qty) / (bid_qty + ask_qty)
    """
    bid_price = df['BidPriceL1']
    ask_price = df['AskPriceL1']
    bid_qty = df['BidQtyL1']
    ask_qty = df['AskQtyL1']
    
    df['microprice'] = (bid_price * ask_qty + ask_price * bid_qty) / (bid_qty + ask_qty)
    return df

def add_depth_features(df):
    """
    Apply all basic depth-related features.
    """
    df = compute_spread(df)
    df = compute_orderbook_imbalance(df)
    df = compute_microprice(df)
    return df
def compute_cumulative_depth(df):
    """
    Compute cumulative bid and ask quantity from L1 to L20
    """
    bid_cols = [f'BidQtyL{i}' for i in range(1, 21)]
    ask_cols = [f'AskQtyL{i}' for i in range(1, 21)]

    df['cum_bid_qty'] = df[bid_cols].sum(axis=1)
    df['cum_ask_qty'] = df[ask_cols].sum(axis=1)
    return df

def compute_midprice(df):
    """
    Compute mid-price: average of top bid and ask
    """
    df['midprice'] = (df['BidPriceL1'] + df['AskPriceL1']) / 2
    return df

def compute_rolling_volatility(df, window=10):
    """
    Compute rolling standard deviation of mid-price returns over N rows
    """
    df = compute_midprice(df)
    df['mid_return'] = df['midprice'].pct_change()
    df['volatility'] = df['mid_return'].rolling(window=window).std()
    return df

def add_advanced_depth_features(df):
    """
    Add cumulative depth and volatility features
    """
    df = compute_cumulative_depth(df)
    df = compute_rolling_volatility(df)
    return df

def compute_volume_features(trades_df, window='10s'):
    """
    Adds rolling buy/sell volume and volume imbalance to the aggTrade data.
    """
    trades_df = trades_df.copy()
    
    # Categorize direction based on market maker
    trades_df['buy_volume'] = trades_df.apply(lambda row: 0 if row['IsMarketMaker'] else row['Quantity'], axis=1)
    trades_df['sell_volume'] = trades_df.apply(lambda row: row['Quantity'] if row['IsMarketMaker'] else 0, axis=1)

    # Set Time as index
    trades_df = trades_df.set_index('Time')

    # Rolling volumes
    trades_df['buy_vol_rolling'] = trades_df['buy_volume'].rolling(window).sum()
    trades_df['sell_vol_rolling'] = trades_df['sell_volume'].rolling(window).sum()

    # Volume imbalance
    trades_df['volume_imbalance'] = (
        trades_df['buy_vol_rolling'] - trades_df['sell_vol_rolling']
    ) / (
        trades_df['buy_vol_rolling'] + trades_df['sell_vol_rolling'] + 1e-6  # prevent divide by zero
    )

    # Reset index
    trades_df = trades_df.reset_index()

    return trades_df

def merge_orderbook_trades(depth_df, trades_df):
    """
    Merges order book and trade features on nearest timestamp using pandas merge_asof.
    """
    # Make sure both are sorted by time
    depth_df = depth_df.sort_values('Time')
    trades_df = trades_df.sort_values('Time')

    # Merge on nearest past trade for each order book snapshot
    merged_df = pd.merge_asof(depth_df, trades_df, on='Time', direction='backward', tolerance=pd.Timedelta('1s'))

    return merged_df
