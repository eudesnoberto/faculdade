import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
import seaborn as sns
import random

dados_one = random.sample(range(100), k=20)
dados_two = random.sample(range(100), k=20)

plt.plot(dados_one, dados_two )
plt.show()

#df = sns.load_dataset("titanic")
#sns.countplot(x=df["class"])
#sns.scatterplot(data=765, x=675, y=5673)
