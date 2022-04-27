import pickle as pkl
import matplotlib.pyplot as plt

dataList = pkl.load(open('GeneticsData.pkl', 'rb'))
plt.plot(dataList[0], dataList[1])
plt.title('Average Scores over Each Generation')
plt.xlabel('Generation')
plt.ylabel('Average Score')
plt.savefig('GeneticScores.png')