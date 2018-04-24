## Read in values

import tkinter
from tkinter.filedialog import askopenfilename
filename = askopenfilename()

F=open(filename,'r')
lines = F.readlines()
F.close()

## Making list of the temperatures

Tlist=[]

location1=[i for i,x in enumerate(lines) if ('Temperature' in x) and ('Kelvin' in x) and ('Pressure' in x) and ('Atm' in x)]

for i in location1:
    foundstring=lines[i]
    value=float(foundstring.split()[1])
    Tlist.append(value)

## Making list of the Gibbs free energies

Glist=[]

location2=[i for i,x in enumerate(lines) if ('Sum of electronic and thermal Free Energies' in x)]

for i in location2:
    foundstring=lines[i]
    value=float(foundstring.split()[7])
    Glist.append(value)

#Relative G
relativelist=[]

minvalue=min(x for x in Glist)

for i in range(len(Glist)):
    j=Glist[i]
    inkcalmol=(j-minvalue)*627.5095
    relativelist.append(inkcalmol)

#transposing the matrix

import pandas as pd

#alldata = [Tlist,Glist,relativelist]

alldata = { 'temperature': Tlist, 'Gfe': Glist, 'rGfe': relativelist }

alldata_df = pd.DataFrame(alldata, columns=['temperature', 'Gfe', 'rGfe'])
#if you do not specify columns, the order of the columns at the moment of writing out might change

#ziptransposed=list(map(list,zip(*alldata)))

#writes everything

import os
cwd=os.getcwd()
newdir=cwd+'/'+'data'
if not os.path.exists(newdir):
    os.makedirs(newdir)
os.chdir(newdir)

#outfile="data_molecule"
#Wf=open(outfile,'w')

alldata_df.to_csv('data_molecule_wdf', sep=' ', float_format='%.3f')

#for x in ziptransposed:
#    Wf.write(' '.join(str(x[i]) for i in range(len(x))))
#    Wf.write('\n')

#Wf.close
