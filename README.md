# 新闻分类项目 - `People.cn`

## 按任务归档

1. **数据爬取**:
   - `src/01_data_crawling.ipynb`
2. **文本预处理**:
   - `src/02_data_cleaning.ipynb`
   - `src/03_data_preprocessing.ipynb`
   - `src/04_news_columns_generator.ipynb`
3. **数据探索**:
   - `src/05_data_exploration.ipynb`
4. **`SVM` 模型构建**:
   - `src/06_svm.ipynb`
5. **模型评价**:
   - `src/06_svm.ipynb`

## 项目结构:

```
├── README.md
├── data
│   ├── clean
│   │   └── news_dataset.csv
│   ├── labeled
│   │   └── news_labeled.csv
│   ├── preprocessed
│   │   └── news_preprocessed.csv
│   └── raw
│       ├── news_page_1.csv
│      ...
│       └── news_page_75.csv
├── doc
│   └── task.txt
├── main.py
├── models
├── requirements.txt
└── src
    ├── 01_web_scraping.py
    ├── 02_data_cleaning.ipynb
    ├── 03_data_preprocessing.ipynb
    ├── 04_news_columns_generator.ipynb
    ├── 05_data_exploration.ipynb
    └── 06_svm.ipynb
```
