#!/usr/bin/env python3

source_data_dir = './data/extracted/DBExport'
raw_training_data_dir = './data/raw_training_data'

col_list = ['InstrumentID','TradingDay','UpdateTime','UpdateMillisec','LastPrice','Volume','LastVolume','Turnover','LastTurnover','AskPrice5','AskPrice4','AskPrice3','AskPrice2','AskPrice1','BidPrice1','BidPrice2','BidPrice3','BidPrice4','BidPrice5','AskVolume5','AskVolume4','AskVolume3','AskVolume2','AskVolume1','BidVolume1','BidVolume2','BidVolume3','BidVolume4','BidVolume5','OpenInterest','UpperLimitPrice','LowerLimitPrice']

feature_col_list = ['Volume', 'LastVolume', 'LastPrice', 'AskPrice1', 'BidPrice1', 'AskVolume1', 'BidVolume1', 'OpenInterest']
max_col_list = [['Volume', 'LastVolume', 'AskVolume1', 'BidVolume1', 'OpenInterest'], ['LastPrice', 'AskPrice1', 'BidPrice1']]

import os
import re
import time
import pickle

time_start = time.time()

lines = []
for root, dirs, files in os.walk(source_data_dir):
  for f in files:
    fin = os.path.join(root,f)
    fip = open(fin, 'r')
    
    fip.readline()
    lines += fip.readlines()
    fip.close()

max_values = max([[int(re.sub(r'\.0*', '', l.strip().split(',')[col_list.index(fe)])) for fe in feature_col_list] for l in lines])
max_values = [max([max_values[feature_col_list.index(fe)] for fe in max_set]) for feature in feature_col_list for max_set in max_col_list if feature in max_set]
print(max_values)
print('elaspsed: {}s'.format(time.time()-time_start))
time_start = time.time()

for root, dirs, files in os.walk(source_data_dir):
  for f in files:
    fin = os.path.join(root,f)
    fip = open(fin, 'r')
    fon = os.path.join(raw_training_data_dir, f.replace('csv', 'dat'))
    fop = open(fon, 'wb')

    fip.readline()
    data = []
    while True:
      l = fip.readline()
      if not l:
        break
      l = l.strip()
      val_l = l.split(',')
      data.append([int(re.sub(r'\.0*', '', val_l[col_list.index(fe)]))*1.0/max_values[feature_col_list.index(fe)] for fe in feature_col_list])
    pickle.dump(data, fop, -1)
    fop.close() 
    fip.close()
print('elaspsed: {}s'.format(time.time()-time_start))
