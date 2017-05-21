This project is forked from https://github.com/jiegzhan/multi-class-text-classification-cnn-rnn

Usage
---

First you have to download the data. If you are enrolled in this course, you will get this from a ftp endpoint. Extract your csv files to the data/ folder, and rewrite the path in these python files inside this project.

Next run DataClearner.py to clean the data. It will extract data of the feature columns and normalize by the max value of the according set.

Next run DataGenerator.py to generate the data which the train.py can use to train. It will add the label to the data.

Finally run train.py to train. The usage of this train.py should be referred from the source of this forked project.
