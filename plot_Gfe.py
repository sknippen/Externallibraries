import pandas as pd
import matplotlib.pyplot as plt

tb = pd.read_csv('data/data_molecule_wdf', sep=' ')

tb.plot(title='relative Gfe', x='temperature', y='rGfe')

plt.savefig('rGfe.png', dpi=400)

