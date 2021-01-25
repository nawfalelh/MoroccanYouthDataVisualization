from data_warehouse import *
import pandas as pd

exec(open("./hcp_etl_job.py").read())
exec(open("./dwb_etl_job.py").read())


DWM.createTables()

df_demog_hcp = pd.read_csv('./data/hcp/hcp_demog.csv')
df_edu_hcp = pd.read_csv('./data/hcp/hcp_edu.csv')
df_act_hcp = pd.read_csv('./data/hcp/hcp_chom.csv')
df_demog_dwb = pd.read_csv('./data/dwb/dwb_demog.csv')
df_act_dwb = pd.read_csv('./data/dwb/dwb_activity.csv')
df_lt = pd.read_csv('./data/dwb/dwb_literacy.csv')
df_cod_dwb = pd.read_csv('./data/dwb/dwb_cod.csv')

s = DWM.createSession()

years = set(list(df_demog_dwb['Year']) + list(df_cod_dwb['Year']) + list(df_demog_hcp['Year']))
genders = set(df_demog_dwb['Gender'])
ages = set(df_edu_hcp['Age'])
ageslvl1 = set(df_demog_dwb['AgeInterval'])
ageslvl2 = set(['15-24', '25-34'])
ageslvl3 = set(['15-34'])
causes = set(df_cod_dwb['Cause'])
areas = set(df_demog_hcp['Area'])
grades = set(df_edu_hcp['Grade'])
cycles = set(['COL', 'LYC'])
sectors = set(df_edu_hcp['Sector'])

for y in years:
    DimTime.add(s, y)

for g in genders:
    DimGender.add(s, g)

for a in ageslvl3:
    DimAgeIntervalLVL3.add(s, a)

for a in ageslvl2:
    DimAgeIntervalLVL2.add(s, a)

for a in ageslvl1:
    DimAgeIntervalLVL1.add(s, a)

for a in ages:
    DimAge.add(s, a)

for c in causes:
    DimCause.add(s, c)

for a in areas:
    DimArea.add(s, a)

for c in sectors:
    DimSector.add(s, c)

for c in cycles:
    DimCycle.add(s, c)

for g in grades:
    DimGrade.add(s, g)

for i, r in df_demog_dwb.iterrows():
    FactDemogDWB.add(s, r)

for i, r in df_act_dwb.iterrows():
    FactActivityDWB.add(s, r)

for i, r in df_cod_dwb.iterrows():
    FactHealthDWB.add(s, r)

for i, r in df_demog_hcp.iterrows():
    FactDemogHCP.add(s, r)

for i, r in df_edu_hcp.iterrows():
    FactEducHCP.add(s, r)

for i, r in df_act_hcp.iterrows():
    FactActivityHCP.add(s, r)

for i, r in df_lt.iterrows():
    FactLiteracy.add(s, r)

s.commit()
s.close()