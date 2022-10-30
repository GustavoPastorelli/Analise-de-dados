import zipfile
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 14,6



#esse comando funciona melhor no spyder ou vs code
fantasy_zip = zipfile.ZipFile('BaseCompleta__.zip')
fantasy_zip.extractall()
fantasy_zip.close()


#pega base ses_seguros

ses_seguros = pd.read_csv('ses_seguros.csv' , sep=';')
ses_seguros.head()


ses_seguros['coenti'].astype('int64')


ses_seguros = ses_seguros.astype({'coenti':'int64', 'coenti':'int64'})
ses_seguros.info()



#pega grupos economicos
ses_grupos_economicos = pd.read_csv('Ses_grupos_economicos.csv', sep=';', encoding='latin-1')
ses_grupos_economicos = ses_grupos_economicos.drop('damesano', axis=1)

ses_grupos_economicos = ses_grupos_economicos.drop_duplicates(subset='coenti')
ses_grupos_economicos.info()

#faz join nas bases - left jon - merge
ses_seguros2 = ses_seguros.set_index('coenti').join(ses_grupos_economicos.set_index('coenti'), how='left', lsuffix='left')


#pega base ramos

ses_ramos = pd.read_csv('Ses_ramos.csv' , sep=';', encoding='latin-1')
ses_ramos.head()
ses_ramos.info()

ses_ramos['coramo'].astype('float64')



#ses_seguros2 = ses_seguros2.astype({'coramo':'int64', 'coramo':'int64'})
#ses_ramos.info()

ses_ramos.drop_duplicates(subset='coramo')


#join
ses_seguros3 = ses_seguros2.set_index('coramo').join(ses_ramos.set_index('coramo'), how='left', lsuffix='left')
ses_seguros3.info()


ses_seguros3 = ses_seguros3.loc[(ses_seguros3['damesano'] >= 200001)]
ses_seguros3['damesano'].values


ses_seguros3.to_csv('ses_seguros_filtrada.csv')
