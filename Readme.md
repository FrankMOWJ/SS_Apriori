# Readme

## Requirement

If you want to verify your result with the result from the library `mlxtend`, please install 

```shell
pip install mlxtend
```



## File Structure 

- `\dataset`: contain the original dataset(.csv) and its pre-processed version(.txt). There are three datasets used in this experiment.
  - MovieLens: https://grouplens.org/datasets/movielens/
  - Groceries: https://www.kaggle.com/datasets/irfanasrullah/groceries
  - UNIX_usage: adapted from https://github.com/RITCHIEHuang/AssociateMining/tree/master/dataset/UNIX_usage
- `L1_SS_Apriori.py`: SS_Apriori method using $L_1$ item-transaction table to prune the search area
- `L2_SS_Apriori.py`: SS_Apriori method using $L_2$ item-transaction table to prune the search area
- `test.py`: using `mlxtend` to check whether the code and the result is correct



## How to Run

- Run original Apriori method

  By default， the `min support` is set to 0.01

```
python L1_SS_Apriori.py -f DATASET_PATH -s MIN_SUPPORT -m apriori
```

- Run L1_SS_Apriori

```
python L1_SS_Apriori.py -f DATASET_PATH -s MIN_SUPPORT 
```

- Run  L2_SS_Apriori

```
python L2_SS_Apriori.py -f DATASET_PATH -s MIN_SUPPORT 
```



## Acknowledgment

The code is modified from code https://github.com/AshishSinha5/apriori

