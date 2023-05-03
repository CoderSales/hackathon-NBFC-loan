# unsupervised-learning-clustering

## Key elements in this repository

### Setup

1. References
2. `script3.sh` - activates virtual environment (or `source scripy3.sh`)
3. `.bashrc` - for virtual environment
    - in .venv folder
4. Python Select Interpreter
5. pip install ipykernel
6. pip install jupyter
7. sh installer.sh
8. python.exe -m pip install --upgrade pip
9. pip install notebook
10. pip install pandas
11. python -m pip install -U pip
12. python -m pip install -U matplotlib
13. pip install seaborn
14. pip install -U scikit-learn
15. pip install openpyxl
16. pip install nb-black
17. pip install xlwings
18. xlwings addin install
19. pip install natsort
20. pip install imageio

### Save setup

1. pip freeze > requirements.txt

### Load setup

1. pip install -r requirements.txt

### Analysis

1. notebooks/K-Means.ipynb
2. data/technical_support_data-2.csv

### update to .gitignore

```.gitignore
*.json
!spec/*.json
```

adapted to:

`!*/ProcessedData.xlsx`

[git ignore all files of a certain type, except those in a specific subfolder](https://stackoverflow.com/questions/4621072/git-ignore-all-files-of-a-certain-type-except-those-in-a-specific-subfolder)
