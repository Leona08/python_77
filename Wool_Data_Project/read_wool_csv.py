import pandas as pd
data = pd.read_csv(r'C:\Users\WFM\python\wool_data_analysis\merge_2.csv')
data.head(200).to_csv('sample_200.csv')
