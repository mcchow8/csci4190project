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
snap.PrintInfo(G, "Python type PNGraph", "info-pngraph.txt", False)

# initialize lists
for NI in G.Nodes():
    #print("node id %d with degree %d" % ( NI.GetId(), NI.GetOutDeg()))
    nodestatusList.append('B')
    nodedegreeList.append(NI.GetOutDeg())
    nodeaffectList.append(0)
    nodeinitialList.append(0)

#print "Updated List : ", nodedegreeList

for NI in G.Nodes():
    nid = NI.GetId() 
    print len(list(NI.GetOutEdges()))
    break

degreefile = open("degree_list.txt", "w")
# Undirected - Plot degree distribution and data
DegToCntV = snap.TIntPrV()
snap.GetInDegCnt(G, DegToCntV)
for p in DegToCntV:
    degreefile.write("%d %d\r\n" % (p.GetVal1(), p.GetVal2()))
in_degrees = [(item.GetVal2(), item.GetVal1()) for item in DegToCntV]
snap.PlotInDegDistr(G, "project_degree", "Undirected graph - degree Distribution", False, True)

#Initialize
for i in range(35000):
    randomID = random.randint(1, 82168)
    while(nodestatusList[randomID]=="A"):
        randomID = random.randint(1, 82168)
    nodestatusList[randomID]='A'
    nodeinitialList[randomID]=1


#print "Updated List : ", nodestatusList
thersold = random.uniform(0, 1)
print ("Thersold: %.2f") % (thersold)

for i in range(10):

    # traverse the edges
    for NI in G.Nodes():
        nodeaffectList[NI.GetId()] = 0

    for EAI in G.Edges():
        if(nodestatusList[EAI.GetSrcNId()]=="A"):
            nodeaffectList[EAI.GetDstNId()] = nodeaffectList[EAI.GetDstNId()] + 1
            #print("edge (%d, %d)" % (EI.GetSrcNId(), EI.GetDstNId()))

    count_check = 0

    for EI in G.Edges():
        p = nodeaffectList[EI.GetDstNId()]/ nodedegreeList[EI.GetDstNId()]
        if(nodestatusList[EI.GetSrcNId()]=="A" and p>=thersold and nodestatusList[EI.GetDstNId()]=="B"):
            nodestatusList[EI.GetDstNId()]="A"
            count_check = count_check + 1
    
    print "The number of affected nodes after this loop: %d"%(count_check)

total=0
for i in nodestatusList:
    if(i=="A"):
        total = total + 1
print("Total affected numbers: %d") % (total)
        
