import pandas as pd

def parse_dimensions(json_data):
    periods = json_data['periodes']
    dimensions = {}
    for d in json_data['dimensions']:
        dimensions[len(json_data['dimensions']) - d['rang'] + 1] = \
        {'name' : d['libelle'] , \
         'sub-values' : {m['rang'] - 1 : m['libelle'] for m in d['modalites']}}
    return dimensions

def loop_over_dimensions(l, json_data, dimensions, ndim, dims_values = []):
    '''
        l : list where to store extracted data
        data : part of the json file containing data
        dimensions : dict with infos about the dimensions
        ndim : actual dimension
        dims_values : values of past dimensions
    '''
    
    if ndim == 0:
        for row in json_data:
            values = list(row.values())
            values.reverse()
            l.append(dims_values + values)
    elif ndim == 1:
        for i, row in enumerate(json_data):
            tmp_dims_values = dims_values.copy()
            tmp_dims_values.append(dimensions[ndim]['sub-values'][i])
            if row['serie']: #if there is no data row['serie'] will be None
                loop_over_dimensions(l, row['serie']['data'], dimensions, ndim - 1, tmp_dims_values)
    else:
        for i, row in enumerate(json_data):
            tmp_dims_values = dims_values.copy()
            tmp_dims_values.append(dimensions[ndim]['sub-values'][i])
            loop_over_dimensions(l, row['sub-levels'], dimensions, ndim - 1, tmp_dims_values)

def format_cols_and_values(df, meta_data):
    df.loc[:] = df.apply(lambda x: x.str.strip())
    for dim, meta_inf in meta_data.items():
        df.rename(columns={dim: meta_inf['name']}, inplace=True)
        if 'values' in meta_inf.keys():
            df[meta_inf['name']].replace(to_replace=meta_inf['values'], inplace=True)
        if meta_inf['dtype'] == 'float32':
            df[meta_inf['name']] = df[meta_inf['name']].str.replace(',', '.').astype(meta_inf['dtype'])
        else:
            df[meta_inf['name']] = df[meta_inf['name']].astype({meta_inf['name']: meta_inf['dtype']})
    df.loc[:, meta_data['Valeur']['name']] = df[meta_data['Valeur']['name']].apply(meta_data['Valeur']['transform'])

def process_chom_data(df):
    select_criteria = ((df['AgeInterval'] == '15-24') | \
                       (df['AgeInterval'] == '25-34')) &\
                      (df['Gender'] != 'TOT') & \
                      (df['Area'] != 'National') & \
                      (df['Percentage'] != 0)
    df.drop(df[~select_criteria].index, axis = 0, inplace = True)
    df.reset_index(drop = True, inplace = True)


def process_demog_data(df):
    select_criteria = ((df['AgeInterval'] == '15-19') | \
                       (df['AgeInterval'] == '20-24') | \
                       (df['AgeInterval'] == '25-29') | \
                       (df['AgeInterval'] == '30-34')) & \
                      (df['Gender'] != 'TOT') & \
                      (df['Area'] != 'National') & \
                      (df['Pop'] != 0) & \
                      (df['Year'] < 2021)
    df.drop(df[~select_criteria].index, axis = 0, inplace = True)
    df.reset_index(drop=True, inplace=True)


def process_edu_col_pub(df):
    df.drop(df[df['Age'] == 'TOT'].index, axis = 0, inplace = True)
    df['Age'] = df['Age'].astype('int32')
    selection_criteria = (df['Age'] >= 15) & \
                         (df['Grade'] != 'TOT') & \
                         (df['Area'] == 'National')

    df.drop(df[~selection_criteria].index, axis = 0, inplace = True)
    df.drop(['Area'], axis=1, inplace=True)
    df.sort_values(['Year', 'Age', 'Grade', 'Gender'], inplace = True)

    df['Sector'] = 'PUB'

    df.reset_index(drop=True, inplace=True)

    df.loc[df['Gender'] == 'TOT', 'Number'] = df.groupby(['Year', 'Sector', 'Age', 'Grade'], as_index=False)['Number'].diff()
    df['Number'] = df['Number'].astype('int32')
    df.replace({'TOT' : 'MA'}, inplace = True)

    cols = ['Age', 'Grade', 'Year', 'Sector']
    errors_loc = df.loc[df.Number < 0, cols]
    for err in errors_loc.values:
        errors_idxs = df[pd.concat([df[col] == value for col, value in zip(cols, err)], axis=1).all(axis=1)].index
        df.drop(errors_idxs, axis=0, inplace=True)

def process_edu_lyc_pub(df):
    df.drop(df[(df['Age'] == 'TOT') | (df['Age'] == '24+')].index, axis = 0, inplace = True)
    df['Age'] = df['Age'].astype('int32')
    selection_criteria = (df['Age'] >= 15) & \
                         (df['Grade'] != 'TOT') & \
                         (df['Area'] == 'National')

    df.drop(df[~selection_criteria].index, axis = 0, inplace = True)
    df.drop(['Area'], axis=1, inplace=True)
    df.sort_values(['Year', 'Age', 'Grade', 'Gender'], inplace = True)

    df['Sector'] = 'PUB'

    df.reset_index(drop=True, inplace=True)

    df.loc[df['Gender'] == 'TOT', 'Number'] = df.groupby(['Year', 'Sector', 'Age', 'Grade'], as_index=False)['Number'].diff()
    df['Number'] = df['Number'].astype('int32')
    df.replace({'TOT' : 'MA'}, inplace = True)

    cols = ['Age', 'Grade', 'Year', 'Sector']
    errors_loc = df.loc[df.Number < 0, cols]
    for err in errors_loc.values:
        errors_idxs = df[pd.concat([df[col] == value for col, value in zip(cols, err)], axis=1).all(axis=1)].index
        df.drop(errors_idxs, axis=0, inplace=True)

def process_edu_lyc_prv(df):
    selection_criteria = (df['Grade'] != 'TOT')
    df.drop(df[~selection_criteria].index, axis=0, inplace=True)
    df['Age'] = [16 if g == 'L1' else (17 if g == 'L2' else 18) for g in df['Grade']]

    df.sort_values(['Year', 'Age', 'Grade', 'Gender'], inplace=True)
    df['Sector'] = 'PRV'

    df.reset_index(drop=True, inplace=True)

    df.loc[df['Gender'] == 'TOT', 'Number'] = df.groupby(['Year', 'Sector', 'Age', 'Grade'], as_index=False)['Number'].diff()
    df.dropna(inplace=True)
    df['Number'] = df['Number'].astype('int32')
    df.replace({'TOT': 'MA'}, inplace=True)

