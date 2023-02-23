# !pip install mlxtend
import os
import pickle
# import warnings
# warnings.filterwarnings('ignore')
import ssl
from datetime import datetime

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules, fpgrowth
from mlxtend.preprocessing import TransactionEncoder

ssl._create_default_https_context = ssl._create_unverified_context
data = pd.read_csv(
    os.environ['DATA'])

transactions = [list(i[1]["track_name"]) for i in data.groupby(["name"])]
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)
rules = apriori(df, min_support=0.01, use_colnames=True)
rules["num"] = rules["itemsets"].apply(lambda x: len(x))
rules = association_rules(rules, metric="confidence", min_threshold=0.7)
time = str(datetime.now())
rules = [rules, time]

binary_data = pickle.dumps(rules)

# 将序列化的数据保存到文件
with open('/data/rules', 'wb') as f:
    f.write(binary_data)
# # 从文件中读取数据并反序列化为 Python 对象
# with open('rules', 'rb') as f:
#     restored_data = pickle.load(f)

# display(restored_data[0])
