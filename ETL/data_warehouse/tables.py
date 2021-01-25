from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from .manager import Base

class FactDemogDWB(Base):
    __tablename__ = 'FACT_DEMOG_DWB'

    ID = Column(Integer, primary_key=True)
    ID_TIME = Column(Integer, ForeignKey('DIM_TIME.ID'))
    ID_GENDER = Column(Integer, ForeignKey('DIM_GENDER.ID'))
    ID_AGE_INTERVAL = Column(Integer, ForeignKey('DIM_AGE_INTERVAL_LVL_1.ID'))

    POP = Column(Integer)
    TOTAL_POP = Column(Integer)

    def add(s, e):
        t = DimTime.get(s, e['Year'])
        g = DimGender.get(s, e['Gender'])
        ai = DimAgeIntervalLVL1.get(s, e['AgeInterval'])
        p = e['Pop']
        tp = e['Total pop']
        s.add(FactDemogDWB(TIME=t, GENDER=g, AGE_INTERVAL=ai, POP=p, TOTAL_POP=tp))


class FactDemogHCP(Base):
    __tablename__ = 'FACT_DEMOG_HCP'

    ID = Column(Integer, primary_key=True)
    ID_TIME = Column(Integer, ForeignKey('DIM_TIME.ID'))
    ID_AREA = Column(Integer, ForeignKey('DIM_AREA.ID'))
    ID_AGE_INTERVAL = Column(Integer, ForeignKey('DIM_AGE_INTERVAL_LVL_1.ID'))
    ID_GENDER = Column(Integer, ForeignKey('DIM_GENDER.ID'))

    POP = Column(Integer)

    def add(s, e):
        t = DimTime.get(s, e['Year'])
        g = DimGender.get(s, e['Gender'])
        ai = DimAgeIntervalLVL1.get(s, e['AgeInterval'])
        a = DimArea.get(s, e['Area'])
        p = e['Pop']
        s.add(FactDemogHCP(TIME=t, GENDER=g, AGE_INTERVAL=ai, AREA=a, POP=p))


class FactEducHCP(Base):
    __tablename__ = 'FACT_EDUC_HCP'

    ID = Column(Integer, primary_key=True)
    ID_TIME = Column(Integer, ForeignKey('DIM_TIME.ID'))
    ID_SECTOR = Column(Integer, ForeignKey('DIM_SECTOR.ID'))
    ID_AGE = Column(Integer, ForeignKey('DIM_AGE.ID'))
    ID_GRADE = Column(Integer, ForeignKey('DIM_GRADE.ID'))
    ID_GENDER = Column(Integer, ForeignKey('DIM_GENDER.ID'))

    NUMBER = Column(Integer)

    def add(s, e):
        t = DimTime.get(s, e['Year'])
        sec = DimSector.get(s, e['Sector'])
        a = DimAge.get(s, e['Age'])
        gr = DimGrade.get(s, e['Grade'])
        g = DimGender.get(s, e['Gender'])
        n = e['Number']
        s.add(FactEducHCP(TIME=t, SECTOR=sec, AGE=a, GRADE=gr, GENDER=g, NUMBER=n))


class FactLiteracy(Base):
    __tablename__ = 'FACT_LITERACY'

    ID = Column(Integer, primary_key=True)
    ID_TIME = Column(Integer, ForeignKey('DIM_TIME.ID'))
    ID_GENDER = Column(Integer, ForeignKey('DIM_GENDER.ID'))

    PERCENTAGE = Column(Float)

    def add(s, e):
        t = DimTime.get(s, e['Year'])
        g = DimGender.get(s, e['Gender'])
        p = e['Percentage']
        s.add(FactLiteracy(TIME=t, GENDER=g, PERCENTAGE=p))


class FactHealthDWB(Base):
    __tablename__ = 'FACT_HEALTH_DWB'

    ID = Column(Integer, primary_key=True)
    ID_TIME = Column(Integer, ForeignKey('DIM_TIME.ID'))
    ID_GENDER = Column(Integer, ForeignKey('DIM_GENDER.ID'))
    ID_CAUSE = Column(Integer, ForeignKey('DIM_CAUSE.ID'))

    PERCENTAGE = Column(Float)

    def add(s, e):
        t = DimTime.get(s, e['Year'])
        g = DimGender.get(s, e['Gender'])
        c = DimCause.get(s, e['Cause'])
        p = e['Percentage']
        s.add(FactHealthDWB(TIME=t, GENDER=g, CAUSE=c, PERCENTAGE=p))


class FactActivityDWB(Base):
    __tablename__ = 'FACT_ACTIVITY_DWB'

    ID = Column(Integer, primary_key=True)
    ID_TIME = Column(Integer, ForeignKey('DIM_TIME.ID'))
    ID_GENDER = Column(Integer, ForeignKey('DIM_GENDER.ID'))

    EMPLOYMENT = Column(Float)
    UNEMPLOYMENT = Column(Float)
    LABOR_FORCE_PARTICIPATION = Column(Float)

    def add(s, e):
        t = DimTime.get(s, e['Year'])
        g = DimGender.get(s, e['Gender'])
        emp = e['Employment percentage']
        unemp = e['Unemployment percentage']
        lfp = e['Labor force participation']
        s.add(FactActivityDWB(TIME=t, GENDER=g, EMPLOYMENT=emp, UNEMPLOYMENT=unemp, LABOR_FORCE_PARTICIPATION=lfp))


class FactActivityHCP(Base):
    __tablename__ = 'FACT_ACTIVITY_HCP'

    ID = Column(Integer, primary_key=True)
    ID_TIME = Column(Integer, ForeignKey('DIM_TIME.ID'))
    ID_GENDER = Column(Integer, ForeignKey('DIM_GENDER.ID'))
    ID_AREA = Column(Integer, ForeignKey('DIM_AREA.ID'))
    ID_AGE_INTERVAL = Column(Integer, ForeignKey('DIM_AGE_INTERVAL_LVL_2.ID'))

    PERCENTAGE = Column(Float)

    def add(s, e):
        t = DimTime.get(s, e['Year'])
        g = DimGender.get(s, e['Gender'])
        a = DimArea.get(s, e['Area'])
        ai = DimAgeIntervalLVL2.get(s, e['AgeInterval'])
        p = e['Percentage']
        s.add(FactActivityHCP(TIME=t, GENDER=g, AGE_INTERVAL=ai, AREA=a, PERCENTAGE=p))


class DimTime(Base):
    __tablename__ = 'DIM_TIME'

    ID = Column(Integer, primary_key=True)
    YEAR = Column(Integer)

    FACT_DEMOG_DWB = relationship('FactDemogDWB', order_by=FactDemogDWB.ID, backref='TIME')
    FACT_DEMOG_HCP = relationship('FactDemogHCP', order_by=FactDemogHCP.ID, backref='TIME')
    FACT_EDUC_HCP = relationship('FactEducHCP', order_by=FactEducHCP.ID, backref='TIME')

    FACT_HEALTH = relationship('FactHealthDWB', order_by=FactHealthDWB.ID, backref='TIME')
    FACT_ACTIVITY_DWB = relationship('FactActivityDWB', order_by=FactActivityDWB.ID, backref='TIME')
    FACT_ACTIVITY_HCP = relationship('FactActivityHCP', order_by=FactActivityHCP.ID, backref='TIME')

    FACT_LITERACY = relationship('FactLiteracy', order_by=FactLiteracy.ID, backref='TIME')

    def get(s, v):
        return s.query(DimTime).filter(DimTime.YEAR == v).first()

    def add(s, e):
        s.add(DimTime(YEAR=e))


class DimGender(Base):
    __tablename__ = 'DIM_GENDER'

    ID = Column(Integer, primary_key=True)
    GENDER = Column(String)

    FACT_DEMOG_DWB = relationship('FactDemogDWB', order_by=FactDemogDWB.ID, backref='GENDER')
    FACT_DEMOG_HCP = relationship('FactDemogHCP', order_by=FactDemogHCP.ID, backref='GENDER')
    FACT_EDUC_HCP = relationship('FactEducHCP', order_by=FactEducHCP.ID, backref='GENDER')

    FACT_HEALTH = relationship('FactHealthDWB', order_by=FactHealthDWB.ID, backref='GENDER')
    FACT_ACTIVITY_DWB = relationship('FactActivityDWB', order_by=FactActivityDWB.ID, backref='GENDER')
    FACT_ACTIVITY_HCP = relationship('FactActivityHCP', order_by=FactActivityHCP.ID, backref='GENDER')

    FACT_LITERACY = relationship('FactLiteracy', order_by=FactLiteracy.ID, backref='GENDER')

    def get(s, v):
        return s.query(DimGender).filter(DimGender.GENDER == v).first()

    def add(s, e):
        s.add(DimGender(GENDER=e))


class DimAge(Base):
    __tablename__ = 'DIM_AGE'

    ID = Column(Integer, primary_key=True)
    ID_AGE_INTERVAL_LVL_1 = Column(Integer, ForeignKey('DIM_AGE_INTERVAL_LVL_1.ID'))

    AGE = Column(Integer)

    FACT_EDUC_HCP = relationship('FactEducHCP', order_by=FactEducHCP.ID, backref='AGE')

    def get(s, v):
        return s.query(DimAge).filter(DimAge.AGE == v).first()

    def intervalResolver(a):
        if a in range(15, 20):
            return '15-19'
        elif a in range(20, 25):
            return '20-24'
        elif a in range(25, 30):
            return '25-29'
        elif a in range(30, 35):
            return '30-34'

    def add(s, e):
        ai = DimAgeIntervalLVL1.get(s, DimAge.intervalResolver(e))
        s.add(DimAge(AGE_INTERVAL_LVL_1=ai, AGE=e))


class DimAgeIntervalLVL1(Base):
    __tablename__ = 'DIM_AGE_INTERVAL_LVL_1'

    ID = Column(Integer, primary_key=True)
    ID_AGE_INTERVAL_LVL_2 = Column(Integer, ForeignKey('DIM_AGE_INTERVAL_LVL_2.ID'))

    AGE_INTERVAL = Column(String)

    FACT_DEMOG_DWB = relationship('FactDemogDWB', order_by=FactDemogDWB.ID, backref='AGE_INTERVAL')
    FACT_DEMOG_HCP = relationship('FactDemogHCP', order_by=FactDemogHCP.ID, backref='AGE_INTERVAL')
    AGES = relationship('DimAge', order_by=DimAge.ID, backref='AGE_INTERVAL_LVL_1')

    def get(s, v):
        return s.query(DimAgeIntervalLVL1).filter(DimAgeIntervalLVL1.AGE_INTERVAL == v).first()

    def intervalResolver(a):
        if a == '15-19' or a == '20-24':
            return '15-24'
        elif a == '25-29' or a == '30-34':
            return '25-34'

    def add(s, e):
        ai = DimAgeIntervalLVL2.get(s, DimAgeIntervalLVL1.intervalResolver(e))
        s.add(DimAgeIntervalLVL1(AGE_INTERVAL_LVL_2=ai, AGE_INTERVAL=e))


class DimAgeIntervalLVL2(Base):
    __tablename__ = 'DIM_AGE_INTERVAL_LVL_2'

    ID = Column(Integer, primary_key=True)
    ID_AGE_INTERVAL_LVL_3 = Column(Integer, ForeignKey('DIM_AGE_INTERVAL_LVL_3.ID'))

    AGE_INTERVAL = Column(String)

    FACT_ACTIVITY_HCP = relationship('FactActivityHCP', order_by=FactActivityHCP.ID, backref='AGE_INTERVAL')
    AGE_INTERVAL_LVL_1 = relationship('DimAgeIntervalLVL1', order_by=DimAgeIntervalLVL1.ID,
                                      backref='AGE_INTERVAL_LVL_2')

    def get(s, v):
        return s.query(DimAgeIntervalLVL2).filter(DimAgeIntervalLVL2.AGE_INTERVAL == v).first()

    def intervalResolver(a):
        return '15-34'

    def add(s, e):
        ai = DimAgeIntervalLVL3.get(s, DimAgeIntervalLVL2.intervalResolver(e))
        s.add(DimAgeIntervalLVL2(AGE_INTERVAL_LVL_3=ai, AGE_INTERVAL=e))


class DimAgeIntervalLVL3(Base):
    __tablename__ = 'DIM_AGE_INTERVAL_LVL_3'

    ID = Column(Integer, primary_key=True)
    AGE_INTERVAL = Column(String)

    AGE_INTERVAL_LVL_2 = relationship('DimAgeIntervalLVL2', order_by=DimAgeIntervalLVL2.ID,
                                      backref='AGE_INTERVAL_LVL_3')

    def get(s, v):
        return s.query(DimAgeIntervalLVL3).filter(DimAgeIntervalLVL3.AGE_INTERVAL == v).first()

    def add(s, e):
        s.add(DimAgeIntervalLVL3(AGE_INTERVAL=e))


class DimCause(Base):
    __tablename__ = 'DIM_CAUSE'

    ID = Column(Integer, primary_key=True)
    CAUSE = Column(String)

    FACT_HEALTH = relationship('FactHealthDWB', order_by=FactHealthDWB.ID, backref='CAUSE')

    def get(s, v):
        return s.query(DimCause).filter(DimCause.CAUSE == v).first()

    def add(s, e):
        s.add(DimCause(CAUSE=e))


class DimArea(Base):
    __tablename__ = 'DIM_AREA'

    ID = Column(Integer, primary_key=True)
    AREA = Column(String)

    FACT_DEMOG_HCP = relationship('FactDemogHCP', order_by=FactDemogHCP.ID, backref='AREA')
    FACT_ACTIVITY_HCP = relationship('FactActivityHCP', order_by=FactActivityHCP.ID, backref='AREA')

    def get(s, v):
        return s.query(DimArea).filter(DimArea.AREA == v).first()

    def add(s, e):
        s.add(DimArea(AREA=e))


class DimSector(Base):
    __tablename__ = 'DIM_SECTOR'

    ID = Column(Integer, primary_key=True)
    SECTOR = Column(String)

    FACT_EDUC_HCP = relationship('FactEducHCP', order_by=FactEducHCP.ID, backref='SECTOR')

    def get(s, v):
        return s.query(DimSector).filter(DimSector.SECTOR == v).first()

    def add(s, e):
        s.add(DimSector(SECTOR=e))


class DimGrade(Base):
    __tablename__ = 'DIM_GRADE'

    ID = Column(Integer, primary_key=True)
    ID_CYCLE = Column(Integer, ForeignKey('DIM_CYCLE.ID'))

    GRADE = Column(String)

    FACT_EDUC_HCP = relationship('FactEducHCP', order_by=FactEducHCP.ID, backref='GRADE')

    def cycleResolver(g):
        if g in ['C1', 'C2', 'C3']:
            return 'COL'
        elif g in ['L1', 'L2', 'L3']:
            return 'LYC'

    def get(s, v):
        return s.query(DimGrade).filter(DimGrade.GRADE == v).first()

    def add(s, e):
        c = DimGrade.cycleResolver(e)
        s.add(DimGrade(GRADE=e, CYCLE=DimCycle.get(s, c)))


class DimCycle(Base):
    __tablename__ = 'DIM_CYCLE'

    ID = Column(Integer, primary_key=True)
    CYCLE = Column(String)

    GRADE = relationship('DimGrade', order_by=DimGrade.ID, backref='CYCLE')

    def get(s, v):
        return s.query(DimCycle).filter(DimCycle.CYCLE == v).first()

    def add(s, e):
        s.add(DimCycle(CYCLE=e))

