import numpy as np
import snap
import matplotlib.pyplot as plt
import random

payoff_a = 2
payoff_b = 3
thersold = payoff_a/(payoff_a+payoff_b)
nodestatusList = []
nodedegreeList = []
nodeaffectList = []
nodeinitialList = []
G = snap.LoadEdgeList(snap.PUNGraph, "data/soc-Slashdot0902.txt", 0, 1, '\t')
snap.PlotClustCf(G, "project_cluster_coeff", "Undirected graph - clustering coefficient")

DegToCCfV = snap.TFltPrV()
result = snap.GetClustCfAll(G, DegToCCfV)
for item in DegToCCfV:
    print("degree: %d, clustering coefficient: %f" % (item.GetVal1(), item.GetVal2()))
print("average clustering coefficient", result[0])

clusterfile = open("clustering_list.txt", "w")
NIdCCfH = snap.TIntFltH()
snap.GetNodeClustCf(G, NIdCCfH)
for item in NIdCCfH:
    clusterfile.write("%d %d\r\n" % (item, NIdCCfH[item]))
