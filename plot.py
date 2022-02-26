from matplotlib import pyplot as plt
from equations import *
from constants import *
from data import X
from neural_network import *

def I_plot(I, F, DPI):
    fig, ax = plt.subplots()
    ax.set_xlabel("X", **{'fontsize': 'x-large'})
    ax.set_ylabel("Y", **{'fontsize': 'x-large'})
    ax.plot(X, I, label="Integration_NN", color="r", ls="--", lw=4)
    ax.plot(X, F, label="Right EQ")
    plt.xticks(X)
    ax.legend()
    plt.savefig("IntegrationPlot.png", dpi=DPI)
    print("Integration plot has been saved")
    #plt.show()

def NN_plot(Y, Z, DPI):
    fig, ax = plt.subplots()
    ax.set_xlabel("X", **{'fontsize': 'x-large'})
    ax.set_ylabel("Result", **{'fontsize': 'x-large'})
    #ax.set(ylim=(0, 2))
    ax.scatter(X, Y, label="Neural nerwork", s=91, facecolors='none', edgecolors='blue', linewidths=1)
    ax.plot(X, Z, label="Correct function", marker="*", markersize=10, c="#e100ff")
    plt.xticks(X)
    ax.legend()
    plt.savefig("NNSolution.png", dpi=DPI)
    print("Neural network plot has been saved")
    #plt.show()

def Err_plot(Y, Z, DPI):
    Y = array(Y)
    Z = array(Z)
    pred_err = list(map(abs, Y-Z))
    fig2, ax2 = plt.subplots()
    ax2.set_xlabel("X", **{'fontsize': 'x-large'})
    ax2.set_ylabel("Error", **{'fontsize': 'x-large'})
    ax2.scatter(X, pred_err, s=49, **{"marker": "o", "fc": "#e100ff", "linewidths": 1})
    ax2.plot(X, pred_err,label="Error", c="#e100ff")
    plt.xticks(X)
    ax2.legend()
    plt.savefig("Error.png", dpi=DPI)
    print("Error plot has been saved")
    #plt.show()