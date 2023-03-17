ArrayNodes = [[0 for X in range(3)] for Y in range(20)] #of INTEGER
RootPointer = -1
FreeNode = 0

def AddNode(ArrayNodes, RootPointer, FreeNode):
    NodeData = int(input("Input data to add: "))
    if FreeNode <= 19:
        ArrayNodes[FreeNode][0] = -1
        ArrayNodes[FreeNode][1] = NodeData
        ArrayNodes[FreeNode][2] = -1

        if RootPointer == -1:
            RootPointer = 0
        else:
            Placed = False
            CurrentNode = RootPointer
            while Placed == False:
                if NodeData < ArrayNodes[CurrentNode][1]:
                    if ArrayNodes[CurrentNode][0] == -1:
                        ArrayNodes[CurrentNode][0] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][0]
                else:
                    if ArrayNodes[CurrentNode][2] == -1:
                        ArrayNodes[CurrentNode][2] = FreeNode
                        Placed = True
                    else:
                        CurrentNode = ArrayNodes[CurrentNode][2]
        FreeNode = FreeNode + 1
    else:
        print("Tree is full")
    return ArrayNodes, RootPointer, FreeNode

def InOrder(ArrayNodes, RootPointer):
    if ArrayNodes[RootPointer][0] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootPointer][0])
    print(str(ArrayNodes[RootPointer][1]))
    if ArrayNodes[RootPointer][2] != -1:
        InOrder(ArrayNodes, ArrayNodes[RootPointer][2])

def PrintAll(ArrayNodes):
    for i in range(20):
        print(str(ArrayNodes[i][0]), " ", str(ArrayNodes[i][1]), " ", str(ArrayNodes[i][2]))

for i in range(10):
    ArrayNodes, RootPointer, FreeNode = AddNode(ArrayNodes, RootPointer, FreeNode)

InOrder(ArrayNodes, RootPointer)
PrintAll(ArrayNodes)