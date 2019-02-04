from datetime import datetime

def timestamp_to_str(timestamp):
    return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
