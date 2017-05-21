#!/usr/bin/env python3
import os
import json

feature_col_list = ['Volume', 'LastVolume', 'LastPrice', 'AskPrice1', 'BidPrice1', 'AskPrice1', 'BidPrice1', 'AskVolume1', 'BidVolume1', 'OpenInterest']
price_col_list = ['AskPrice1', 'BidPrice1']
price_ind_list = [feature_col_list.index(x) for x in price_col_list]

def gen(fip):
  last_price = None
  label_list = ['up', 'down']
  data = None
  last_price = 0
  while True:
    label = None
    last_data = data
    flat = lambda L: sum(list(map(flat,L)),[]) if isinstance(L,list) else [L]
    data = []
    for seq_e in range(params['sequence_length']):
      for tick in range(params['tick_size']):
        l = fip.readline()
        if not l:
          return      
        l = l.strip()
        l = l.split(',') 
        price = sum([int(l[i]) for i in price_ind_list])
        if not label and price > last_price:
          label = label_list[0]
        elif not label and price < last_price:
          label = label_list[1] 
        data.append(l)
    data = flat(data)
    last_price = sum([int(data[-(params['feature_size']-i)]) for i in price_ind_list])
    if last_data and label:
      yield label+','+','.join(last_data)

source_data_dir = './data/raw_training_data'
output_data_dir = './data/training_data'

config_file = './config.json'
params = json.load(open(config_file, 'r'))

fon = os.path.join(output_data_dir, 'train')
fop = open(fon, 'w')
for root, dirs, files in os.walk(source_data_dir):
  for f in files:
    fin = os.path.join(root, f)
    fip = open(fin, 'r')
    for data in gen(fip):
      fop.write(data+'\n')

