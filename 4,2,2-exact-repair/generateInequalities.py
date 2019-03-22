#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import scipy


class Entropy:
    def __init__(str entropy):
        this.entropy = entropy;
        this.attribute = (entropy[0] == "W")?0: 1
        if this.attribute == 0:
            this.nodes = [int(entropy[1])]
        else:
            this.nodes = [int(entropy[1]), int(entropy[2])]
        return;


