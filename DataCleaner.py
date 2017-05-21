#!/usr/bin/env python3

source_data_dir = './data/extracted/DBExport'
raw_training_data_dir = './data/raw_training_data'

col_list = ['InstrumentID','TradingDay','UpdateTime','UpdateMillisec','LastPrice','Volume','LastVolume','Turnover','LastTurnover','AskPrice5','AskPrice4','AskPrice3','AskPrice2','AskPrice1','BidPrice1','BidPrice2','BidPrice3','BidPrice4','BidPrice5','AskVolume5','AskVolume4','AskVolume3','AskVolume2','AskVolume1','BidVolume1','BidVolume2','BidVolume3','BidVolume4','BidVolume5','OpenInterest','UpperLimitPrice','LowerLimitPrice']

feature_col_list = ['Volume', 'LastVolume', 'LastPrice', 'AskPrice1', 'BidPrice1', 'AskPrice1', 'BidPrice1', 'AskVolume1', 'BidVolume1', 'OpenInterest']

feature_col_index_list = [col_list.index(x) for x in feature_col_list]

import os
for root, dirs, files in os.walk(source_data_dir):
  for f in files:
    fin = os.path.join(root,f)
    fip = open(fin, 'r')
    fon = os.path.join(raw_training_data_dir, f.replace('csv', 'dat'))
    fop = open(fon, 'w')

    fip.readline()
    while True:
      l = fip.readline()
      if not l:
        break
      val_l = l.split(',')
      data = [str(int(eval(val_l[x]))) for x in feature_col_index_list]
      fop.write(','.join(data)+'\n')
