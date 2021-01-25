from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class DWManager():

    def __init__(self, DWName):
        self.conString = 'mssql+pyodbc://localhost/{}?driver=SQL+Server+Native+Client+11.0'
        self.DWName = DWName

    def createDW(self):
        eng = create_engine(self.conString.format('master'), echo=False, connect_args={'autocommit': True})
        try:
            eng.execute('CREATE DATABASE %s;' % (self.DWName))
        except:
            print('Unable to create Database %s' % (self.DWName))

    def dropDW(self):
        eng = create_engine(self.conString.format('master'), echo=False, connect_args={'autocommit': True})
        try:
            eng.execute('DROP DATABASE %s;' % (self.DWName))
        except:
            print('Unable to drop Database %s' % (self.DWName))

    def createBase(self):
        return declarative_base()

    def createTables(self):
        eng = create_engine(self.conString.format(self.DWName), echo=False)
        Base.metadata.create_all(eng)

    def createSession(self):
        eng = create_engine(self.conString.format(self.DWName), echo=False)
        Session = sessionmaker(bind=eng)
        return Session()

DWM = DWManager('YouthDataWarehouse')
DWM.dropDW()
DWM.createDW()
Base = DWM.createBase()
