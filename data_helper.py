import os
import re
import time
import logging
import numpy as np

logging.getLogger().setLevel(logging.INFO)

def batch_iter(data, batch_size, num_epochs, shuffle=True):
  data = np.array(data)
  data_size = len(data)
  num_batches_per_epoch = int(data_size / batch_size) + 1

  for epoch in range(num_epochs):
    if shuffle:
      shuffle_indices = np.random.permutation(np.arange(data_size))
      shuffled_data = data[shuffle_indices]
    else:
      shuffled_data = data

    for batch_num in range(num_batches_per_epoch):
      start_index = batch_num * batch_size
      end_index = min((batch_num + 1) * batch_size, data_size)
      yield shuffled_data[start_index:end_index]

def load_data(filename):
  time_start = time.time()
  print('loading')
  f = open(filename, 'r')
  label_dict = {'up':np.array([1,0]), 'down':np.array([0,1])}

  import json
  params = json.load(open('config.json', 'r'))

  cnt = 0
 
  x = []
  y = []
  while True:
    l = f.readline()
    if not l:
      break
    cnt += 1
    #if cnt > 100000 :break
    l = l.strip()
    data = l.split(',')
    x.append(np.array(data[1:], dtype=np.float32).reshape([params['sequence_length'], params['tick_size']*params['feature_size']]))
    y.append(label_dict[data[0]])
  x = np.array(x, dtype=np.float32)
  y = np.array(y, dtype=np.float32)
  print('loading took {0}s'.format(time.time()-time_start))
  return x, y

if __name__ == "__main__":
  train_file = './data/training_data/train'
  x,y = load_data(train_file)
  print(y[0], x[0])
