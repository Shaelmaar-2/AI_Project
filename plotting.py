import pickle as pkl
import matplotlib.pyplot as plt

d = pkl.load(open('Defaults.pkl', 'rb'))
dataList = d['data']
fig, axs = plt.subplots(2,sharex=True)
fig.suptitle('Average Winrates and Scores over each Generation (Cr Prob = 0.15)')
axs[0].plot(dataList[0],dataList[1])
axs[1].plot(dataList[0],dataList[2])
axs[1].set(xlabel='Generation',ylabel='Average Winrate')
axs[0].set(ylabel='Average Score')
plt.savefig('Defaults.png')

"""dataList = pkl.load(open('ApproxQLearning.pkl', 'rb'))
plt.plot(dataList[0],dataList[1],label='Windowed Average')
plt.plot(dataList[0],dataList[2],label='Total Average')
plt.xlabel('Training Episodes Complete')
plt.ylabel('Average Score')
plt.title('Average Score over Training for Approximate Q-Learning')
plt.legend()
plt.savefig('ApproxQLearning.png')"""