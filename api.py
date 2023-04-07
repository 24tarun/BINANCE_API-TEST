from binance import Client
import pandas as pd

api_key='FlA5fSAYb1HHk5ozWNDaljsIot0p0mVlxRgWtOF5kmvJmzt5gRZ1mePKbskadY6U'
api_secret='spD9RxuIgl6NTwUFFED7jjXgLIMap1s1akywuUgEWFien7LjkmhF7Fr37lRVNlxj'
client = Client(api_key, api_secret)
client.get_account()