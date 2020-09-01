'''
Created on 07 mag 2018

@author: GianpieroF
'''
import pyodbc
class DbPoweri():
     
    def __init__(self):
        super(DbPoweri, self).__init__()

    def connection(self):
        connection = pyodbc.connect(driver='{iSeries Access ODBC Driver}',
                        system='172.18.0.43',uid='QPGMR',pwd='QPGMR')
        self.c1 = connection.cursor()
         
    def selectMgesi(self,c1 ):
         
        stringa=("select  cdarme, dsarma, umbama, decimal(giatme,9,2) "  
                 " from scp90DAT.mgesi00f   " +
                 "   inner join scp90dat.mgart00f on cddtme=cddtma and cdarme=cdarma "   
                 " where giatme<>0 "  
                   " order by cdarme")
         
        print (stringa)
        c1.execute(stringa) 
        
        row = c1.fetchall()
        return row