import numpy as np
import pandas as pd
import os
import csv

import numpy as np
import matplotlib.pyplot as plt

mygsid = input("Input desired GSID:  ")

plt.rcParams.update({'font.size': 7})

CORval=[]
allCOR=[]

dataset = pd.read_csv('data/'+str(mygsid)+'.csv')

Gscore = np.array(dataset[['growthScore']])
FRscore = np.array(dataset[['financialReturnsScore']])
Mscore = np.array(dataset[['multipleScore']])
Iscore = np.array(dataset[['integratedScore']])
dateb = np.array(dataset[['date']])
y = np.array(dataset['close'])

date= []
for i in range(len(Gscore)):
	date.append(dateb[i][0])

Growth = []
for i in range(len(Gscore)):
	Growth.append(Gscore[i][0])


FinancialRet = []
for i in range(len(FRscore)):
	FinancialRet.append(FRscore[i][0])


Multiple= []
for i in range(len(Mscore)):
	Multiple.append(Mscore[i][0])

IntFactor = []
for i in range(len(Iscore)):
	IntFactor.append(Iscore[i][0])
'''
price = []
for i in range(len(Iscore)):
	price.append(y[i][0])
'''


#CORval.append(files[:-4])
G=np.corrcoef(Growth, y)[0][1]
F=np.corrcoef(FinancialRet, y)[0][1]
M=np.corrcoef(Multiple, y)[0][1]
I=np.corrcoef(IntFactor, y)[0][1]




f, (ax1, ax2, ax3, ax4,ax5) = plt.subplots(5, sharex=True, sharey=False)
ax1.plot(date,y , 'r',label="Price")
ax2.plot(date,Growth , 'b',label="Growth r="+str(G)[:5])
ax3.plot(date,FinancialRet , 'g',label="FinancialRet  r="+str(F)[:5])
ax4.plot(date,Multiple , 'c',label="Multiple r="+str(M)[:5])
ax5.plot(date,IntFactor , 'm',label="IntFactor. r="+str(I)[:5])
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.xticks([1,100,200,300,380,460])
plt.xlabel('Date', fontsize=8, color='black')
ax1.legend()
ax2.legend()
ax3.legend()
ax4.legend()
ax5.legend()

plt.show()






