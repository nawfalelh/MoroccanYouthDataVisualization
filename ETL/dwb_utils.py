import pandas as pd
import json

def process_demog():
    path = './lake/dwb/data_SP.POP.{}.{}.5Y.json'
    gender = ['MA', 'FE']
    ages = [{'name': '1519', 'value': '15-19'},
            {'name': '2024', 'value': '20-24'},
            {'name': '2529', 'value': '25-29'},
            {'name': '3034', 'value': '30-34'}, ]

    l = [['Year', 'Gender', 'AgeInterval', 'Percentage'], ]

    for a in ages:
        for g in gender:
            with open(path.format(a['name'], g)) as json_data:
                data = json.load(json_data)
                for e in data[1]:
                    l.append([e['date'], g, a['value'], e['value']])
    df_ages = pd.DataFrame(l, columns=l[0])[1:]
    df_ages = df_ages.dropna().sort_values(by=['Year', 'Gender', 'AgeInterval'])

    df_ages['Percentage'] = df_ages['Percentage'].astype('float32') / 100
    df_ages.reset_index(drop = True, inplace = True)

    l = [['Year', 'Gender', 'Total pop'], ]
    path = './lake/dwb/data_SP.POP.TOTL.{}.IN.json'
    for g in gender:
        with open(path.format(g)) as json_data:
            data = json.load(json_data)
            for e in data[1]:
                l.append([e['date'], g, e['value']])
    df_tot = pd.DataFrame(l, columns=l[0])[1:]
    df_tot = df_tot.dropna().sort_values(by=['Year', 'Gender'])
    df_tot.reset_index(drop=True, inplace=True)


    df = pd.merge(df_ages, df_tot, left_on=['Year', 'Gender'], right_on=['Year', 'Gender'])
    df['Percentage'] = df['Percentage'].round(5)
    df['Percentage'] = (df['Total pop'] * df['Percentage']).astype('int')
    df.rename(columns={'Percentage': 'Pop'}, inplace=True)
    df.reset_index(drop = True, inplace = True)
    return df

def process_activity():
    gender = ['MA', 'FE']

    l = [['Year', 'Gender', 'Employment percentage'], ]
    path = './lake/dwb/data_SL.EMP.1524.SP.{}.ZS.json'
    for g in gender:
        with open(path.format(g)) as json_data:
            data = json.load(json_data)
            for e in data[1]:
                l.append([e['date'], g, e['value']])
    df_emp = pd.DataFrame(l, columns=l[0])[1:]
    df_emp = df_emp.dropna().sort_values(by=['Year', 'Gender', 'Employment percentage'])

    l = [['Year', 'Gender', 'Unemployment percentage'], ]
    path = './lake/dwb/data_SL.UEM.1524.{}.ZS.json'

    for g in gender:
        with open(path.format(g)) as json_data:
            data = json.load(json_data)
            for e in data[1]:
                l.append([e['date'], g, e['value']])
    df_unemp = pd.DataFrame(l, columns=l[0])[1:]
    df_unemp = df_unemp.dropna().sort_values(by=['Year', 'Gender', 'Unemployment percentage'])

    l = [['Year', 'Gender', 'Labor force participation'], ]
    path = './lake/dwb/data_SL.TLF.ACTI.1524.{}.ZS.json'

    for g in gender:
        with open(path.format(g)) as json_data:
            data = json.load(json_data)
            for e in data[1]:
                l.append([e['date'], g, e['value']])
    df_lfp = pd.DataFrame(l, columns=l[0])[1:]
    df_lfp = df_lfp.dropna().sort_values(by=['Year', 'Gender', 'Labor force participation'])

    df = pd.merge(df_lfp, df_emp, left_on=['Year', 'Gender'], right_on=['Year', 'Gender'])
    df = pd.merge(df, df_unemp, left_on=['Year', 'Gender'], right_on=['Year', 'Gender'])

    df['Labor force participation'] = (df['Labor force participation'] / 100).astype('float32').round(5)
    df['Employment percentage'] = (df['Employment percentage'] / 100).astype('float32').round(5)
    df['Unemployment percentage'] = (df['Unemployment percentage'] / 100).astype('float32').round(5)

    df.reset_index(drop=True, inplace=True)
    return df

def process_literacy():
    gender = ['MA', 'FE']

    l = [['Year', 'Gender', 'Percentage'], ]
    path = './lake/dwb/data_SE.ADT.1524.LT.{}.ZS.json'

    for g in gender:
        with open(path.format(g)) as json_data:
            data = json.load(json_data)
            for e in data[1]:
                l.append([e['date'], g, e['value']])
    df = pd.DataFrame(l, columns=l[0])[1:]
    df = df.dropna().sort_values(by=['Year', 'Gender', 'Percentage'])

    df['Percentage'] = (df['Percentage'].astype('float32') / 100).round(5)

    df.reset_index(drop=True, inplace=True)
    return df

def process_cod():
    cause = ['COMM', 'NCOM', 'INJR']
    gender = ['MA', 'FE']

    l = [['Year', 'Gender', 'Cause', 'Percentage'], ]
    path = './lake/dwb/data_SH.DTH.{}.1534.{}.ZS.json'

    for c in cause:
        for g in gender:
            with open(path.format(c, g)) as json_data:
                data = json.load(json_data)
                for e in data[1]:
                    l.append([e['date'], g, c, e['value']])

    df = pd.DataFrame(l, columns=l[0])[1:]
    df = df.dropna().sort_values(by=['Year', 'Gender', 'Cause'])
    df['Percentage'] = df['Percentage'].astype('float32') / 100

    df.reset_index(drop=True, inplace=True)
    return df

