# Generate CSV file containing filename for Partitioned Nordland Dataset (http://webdiis.unizar.es/~jmfacil/pr-nordland/)
# agtbaskara, 2022-01-18

import os
import glob
import pandas as pd

# generate list for train images
train_df = pd.DataFrame(columns=['section', 'filenumber', 'extension', 'filename'])

train_dir = "Dataset_images/train/spring_images_train"

for filepath in glob.iglob(train_dir + '**/**/**.png', recursive=True):
    print(filepath)
    filenumber = os.path.splitext(os.path.split(filepath)[-1])[0]
    extension = os.path.splitext(os.path.split(filepath)[-1])[-1]
    section = (os.path.split(filepath)[0]).split(os.path.sep)[-1]
    
    train_df = pd.concat([pd.DataFrame([[section, filenumber, extension, '']], columns=train_df.columns), train_df], ignore_index=True)

# sort data
train_df.filenumber = train_df.filenumber.astype(int)
train_df = train_df.sort_values(by=['section', 'filenumber'])
train_df.filenumber = train_df.filenumber.astype(str)
train_df['filename'] = train_df.filenumber.str.cat(train_df.extension)
train_df = train_df.reset_index(drop=True)
train_df = train_df.drop(columns=['filenumber', 'extension'])

# save as csv
train_df.to_csv('train_list.csv', index=False, header=False)

# generate list for test images
test_df = pd.DataFrame(columns=['section', 'filenumber', 'extension', 'filename'])

test_dir = "Dataset_images/test/spring_images_test"

for filepath in glob.iglob(test_dir + '**/**/**.png', recursive=True):
    print(filepath)
    filenumber = os.path.splitext(os.path.split(filepath)[-1])[0]
    extension = os.path.splitext(os.path.split(filepath)[-1])[-1]
    section = (os.path.split(filepath)[0]).split(os.path.sep)[-1]
    
    test_df = pd.concat([pd.DataFrame([[section, filenumber, extension, '']], columns=test_df.columns), test_df], ignore_index=True)

# sort data
test_df.filenumber = test_df.filenumber.astype(int)
test_df = test_df.sort_values(by=['section', 'filenumber'])
test_df.filenumber = test_df.filenumber.astype(str)
test_df['filename'] = test_df.filenumber.str.cat(test_df.extension)
test_df = test_df.reset_index(drop=True)
test_df = test_df.drop(columns=['filenumber', 'extension'])

# save as csv
test_df.to_csv('test_list.csv', index=False, header=False)
print("Finish")
