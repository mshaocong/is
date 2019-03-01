This is an extension of a simulation course project. A general frame for importance sampling is implemented here. It will contains the following part: 

1. Sampling a stochastic process (under the realistic measure). 

2. Change of measure - usually we want to sample the stochastic process from a different measure (given the Radon-Nikodym density).

3. Siegmund algorithm.

4. I will write a note about its application in simulation.

# A brief introduction to importance sampling

[Importance sampling](https://en.wikipedia.org/wiki/Importance_sampling) is well-known variance reduction technique. It has been used in many fields including finance and machine learning. The general idea is, when estimate something, instead of sampling under the original measure $\mathbb{P}$, we sample under a better measure such that the variance of our estimator is much smaller.   

# Sampling
In `mc_generator.py`, a usual method used to simulate a Markov processes is implemented.  

# Importance Sampling Notebook
Consider several cases of rare event. Use IS to estimate the probability.
