import numpy as np
import math
import itertools

class ShannonInequality:
    def __init__(self, nodeNum):
        """
        :param nodeNum: number of storage nodes
        """
        self.nodeNum = nodeNum
        self.storage = {"W"+str(i): 0 for i in range(1, self.nodeNum+1)}
        self.bandwidth = {"S"+str(i)+str(j): 0 for i in range(1, self.nodeNum+1) for j in range(1, nodeNum+1)}
        return
    

if __name__ == "__main__":
    s = ShannonInequality(3)
    print(s.bandwidth)
    print(s.storage)