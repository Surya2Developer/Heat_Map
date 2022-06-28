#
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
flights1 = sns.load_dataset("flights")
flights1 = flights1.pivot("month", "year", "passengers")

ax = sns.heatmap(flights1, annot=True, fmt='d', linewidth=.1)
plt.title("Heatmap Flight Data")
plt.show()



