from dwb_utils import *
from dwb_crawler import extract_data

extract_data()
dfs = {}

dfs['demog'] = process_demog()
dfs['activity'] = process_activity()
dfs['literacy'] = process_literacy()
dfs['cod'] = process_cod()

for name,df in dfs.items():
    df.to_csv('./data/dwb/dwb_{}.csv'.format(name), index = False)