
import gymnasium as gym
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np 
import time

def mostraMov(env,randomAction):
    print("SSSSSSSSSSs")
    periodo_tempo = 1000 
    inicio = time.time()
   # while time.time() - inicio < periodo_tempo:
    # Seu código aqui
    #print("Executando...")
    env.render()
        #print(env.observation_space)#dimencoes do espaco saida discreta pode assumir valores 0 a 15 
        #print(env.action_space)#possiveis acoes left 0, dow 1 right 2 , up 3 
        #randomAction=env.action_space.sample()#movimnetacao aleatoria 
        #print(randomAction)
    temp=env.step(randomAction)
    if temp[2]:
        env.reset()
        #print(returnValue)#(0, 0.0, False, False, {'prob': 0.3333333333333333}) pirmiro argumento estado apos aplicar a acao = observation
                    #segundo argumento e a recompensa = reward
                    #terceira argumento confere se esta terminado 
                    #probabilidade de executar a acao desejada 

        # Aguardar um breve intervalo de tempo entre as iterações
    time.sleep(0.5) 





env=gym.make('FrozenLake-v1', render_mode="human")
env.reset()
discountFactor=0.9#omega
valueFunctionVector=np.zeros(env.observation_space.n)#varores para cada estado 
#print(len(valueFunctionVector))
#print(np.linalg.norm(valueFunctionVector,2))
maxNumberIterations=1000#numero maximo de interacoes K

convergenceTolerance=10**(-6)
convergenceTrack=[]

for iterations in range(maxNumberIterations):
    convergenceTrack.append(np.linalg.norm(valueFunctionVector,2))#norma = sqrt(valueFunctionVector[0]^2 + valueFunctionVector[1]^2 + ... + valueFunctionVector[n-1]^2)
    valueFunctionVectorNextIteration=np.zeros(env.observation_space.n)
    for state in env.P:
        outerSum=0
        for action in env.P[state]:
            innerSum=0
            for probability,nexState,reward,isTerminalState in env.P[state][action]:
                innerSum =innerSum+probability*(reward+discountFactor*valueFunctionVector[nexState])
            outerSum=outerSum+0.25*innerSum
           
            print(action)
            mostraMov(env,action)
        valueFunctionVectorNextIteration[state]=outerSum
        
        #print(np.argmax(valueFunctionVectorNextIteration[state]))
        #print(np.argmax(valueFunctionVectorNextIteration))
    #3mostraMov(env,np.argmax(valueFunctionVectorNextIteration))
       # mostraMov(env,action)
    if(np.max(np.abs(valueFunctionVectorNextIteration-valueFunctionVector))<convergenceTolerance):
        valueFunctionVector=valueFunctionVectorNextIteration
        print('Converged!')
        break
    valueFunctionVector=valueFunctionVectorNextIteration 
#print(convergenceTrack)

# visualize the state values
def grid_print(valueFunction,reshapeDim):
    ax = sns.heatmap(valueFunction.reshape(4,4),
                     annot=True, square=True,
                     cbar=False, cmap='Blues',
                     xticklabels=False, yticklabels=False)
    plt.savefig('valueFunctionGrid.png',dpi=600)
    plt.show()
     
#grid_print(valueFunctionVector,4)
 
#plt.plot(convergenceTrack)
#plt.xlabel('steps')
#plt.ylabel('Norm of the value function vector')
#plt.savefig('convergence.png',dpi=600)
#plt.show()