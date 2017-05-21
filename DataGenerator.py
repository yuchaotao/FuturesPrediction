#!/usr/bin/env python3
import os
import json

def gen(fip):
  while True:
    flat = lambda L: sum(list(map(flat,L)),[]) if isinstance(L,list) else [L]
    data = []
    for seq_e in range(params['sequence_length']):
      for tick in range(params['tick_size']):
        l = fip.readline()
        if not l:
          return      
        l = l.strip()
        l = l.split(',')  
        data.append(l)
    data = flat(data)
    yield ','.join(data)

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

