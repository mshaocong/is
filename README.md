This is an extension of a simulation course project I have taken in the past. A general frame for importance sampling is implemented here. This branch will contains the following part: 

1. Sampling a stochastic process (under the objective measure). 

2. Change of measure - usually we want to sample the stochastic process from a different measure (given the Radon-Nikodym density).

3. Siegmund algorithm.

4. I will write a note about its application in simulation; and I plan to test it on a real financial dataset.

# A brief introduction to importance sampling

[Importance sampling](https://en.wikipedia.org/wiki/Importance_sampling) is a well-known variance reduction technique. It has been used in many fields including simulation, finance, and machine learning. The general idea is, for example, when we want to estimate an expectation of a random variable, instead of sampling it under the objective measure, we sample it under a better measure such that the variance of our estimator is much smaller.   

# Sampling a Markov process and Application of Simulation in Finance

## Sampling a Markov process
In `mc_generator.py`, a usual method used to simulate a Markov processes is implemented. In `Markov process.ipynb` notebook, several examples are introduced, including the following part

* Sample some classical processes such as Brownian motion or Poisson process.

* Sample an Ito diffusion such as [CIR diffusion](https://en.wikipedia.org/wiki/Cox%E2%80%93Ingersoll%E2%80%93Ross_model)

* Sample a couting process given its intensity. **Its intensity may depend on the process itself**.

## Application of Simulation in Finance
In 'Finance Example.ipynb' notebook, I record a classical model of pricing the defaultable bond; in this model, we can compute the price explicitly. However, generally when the interest rate and the defautable time are more complicated, it is impossible to find the theoritical solution. Then we have to use some numerical method to find the approximated price. 

# Why we need importance sampling?
When we want to estimate the probability of some rare events (for example, the rare event could be the number of defaults being large than a given threshold), the Monte Carlo method will give a extremly high relative error. It will influence our strategy. 

We have two methods to reduce the errors. First, obviously we can increase the number of trails; but this method will consume a lot of computing resource. Second, we can apply the importance sampling method. It will have the same comlexity but a lower estimation variance; sometimes, it will have a vanishing or bounded relative error.  

# Importance Sampling
Consider several cases of rare event. Use IS to estimate the probability. To be completed.
