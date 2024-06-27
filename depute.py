import pandas as pd 

data = pd.read_csv("deputes-historique.csv")
data_txt = pd.read_csv("test.csv")

merge = pd.merge(data_txt, data, on="id")

merge.to_csv("merged_XV_XVI.csv")
print(merge.columns)
