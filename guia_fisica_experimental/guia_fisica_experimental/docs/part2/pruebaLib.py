import numpy as np
import matplotlib.pyplot as plt



def func1(N):

    ################
    sigma = 0.1
    dt = 0.05
    ################
    data = sigma*np.random.randn(1,N) + 0.6398 + dt

    fig , ax1 = plt.subplots(figsize=(8,3))
    eje = np.zeros(len(data))
    ax1.set_title('La linea vertical discontinua corresponde al valor aceptado')
    ax1.plot(data,eje,'r|',ms= 10)
    ax1.vlines(0.6398,-0.1,0.2,'k',linestyle='--')
    ax1.set(yticklabels=[])  # remove the tick labels
    ax1.tick_params(left=False)  # remove the ticks
    ax1.set_xlabel('tiempo/s',fontsize=18)
    ax1.set_xlim(0.1,1.1)
    ax1.set_ylim(-1,1)
    # use set_position
    ax1.spines['top'].set_color('none')
    ax1.spines['left'].set_color('none')
    ax1.spines['right'].set_color('none')
    ax1.spines['bottom'].set_position('zero')
