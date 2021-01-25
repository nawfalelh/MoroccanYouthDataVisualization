from hcp_crawler import extract_data
from hcp_meta_data import meta_data, sources
from hcp_utils import *

import pandas as pd
import json

extract_data()
dfs = {}

for s in sources:
    with open('./lake/hcp/hcp_data_{}.json'.format(s['name'])) as json_file:
        json_data = json.load(json_file)

    dimensions = parse_dimensions(json_data)

    l = []
    loop_over_dimensions(l, json_data['levels'], dimensions, len(dimensions))

    df = pd.DataFrame(l, columns=[d['name'] for d in dimensions.values()] + ['Annee', 'Valeur'])
    df.dropna(inplace=True)
    df.reset_index(drop = True, inplace=True)
    format_cols_and_values(df, meta_data[s['name']])

    dfs[s['name']] = df

process_chom_data(dfs['chom'])
process_demog_data(dfs['demog'])
process_edu_col_pub(dfs['edu_col_pub'])
process_edu_lyc_pub(dfs['edu_lyc_pub'])
process_edu_lyc_prv(dfs['edu_lyc_prv'])

dfs['edu'] = pd.concat([dfs['edu_col_pub'], dfs['edu_lyc_pub'], dfs['edu_lyc_prv']])
dfs['edu'].reset_index(drop = True, inplace = True)

del dfs['edu_col_pub']
del dfs['edu_lyc_pub']
del dfs['edu_lyc_prv']

for name,df in dfs.items():
    df.to_csv('./data/hcp/hcp_{}.csv'.format(name), index = False)
