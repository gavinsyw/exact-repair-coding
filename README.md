# Exact-repair-coding

## Simple Introduction

This is a program for redoing the 4,3,3-exact repair coding technique. This program aims to find the boundary and the proof for the boundary by computer, or more specifically, by linear optimization.

## Boundary Calculation

* The set-growth program reduces the number of joint entropies according to exact repair conditions and symmetry. 
* The optimization program conducts all the Shannon inequalities, i.e., the constraints for the boundary, and then put them into an linear optimization program to get the actual boundary.
* The present program can only get the numerical relationship between storage covering $\alpha$ and bandwidth covering $\beta$, with one of them given.

## Computer-aided Proof

* Computer-aided proof approach is also based on linear optimization. We use Lagrange Dual to determine the weight of each inequality we are going to use to prove the boundary.


