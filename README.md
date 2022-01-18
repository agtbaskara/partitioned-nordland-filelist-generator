# partitioned-nordland-filelist-generator
Generate CSV file containing filename for Partitioned Nordland Dataset (http://webdiis.unizar.es/~jmfacil/pr-nordland/)

# How to use:
- Put `generate_csv.py` inside `Partitioned_Nordland_Dataset` or `Partitioned_Nordland_Dataset_lowres` folder.
- Run `generate_csv.py`, then `test_list.csv` and `train_list.csv` will be generated.

# CSV Formatting:

| section  | filename |
| -------- |:--------:|
| section1 | 0.png    |
| section1 | 1.png    |
| ...      | ...      |
| ...      | ...      |
| section3 | 3448.png |
| section3 | 3449.png |

`section` is folder name, `filename` is the image filename.
For example to load `0.png` concatenate `section1` to the path so it become like `.../section1/0.png`

Notes:
- The list is generated based only on spring images because all of the seasons have the same filename and directory structure.
- fullpath of an images is `Dataset_images/[train or test]/[seasons]_images_[tran or test]/[section]/[filename]` for example `Dataset_images/train/spring_images_train/section1/0.png`
