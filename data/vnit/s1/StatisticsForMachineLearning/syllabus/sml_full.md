# Fundamentals of Probability and Statistics Course Documentation

## Table of Contents
- [Module 1: Fundamentals of Probability and Statistics](#module-1-fundamentals-of-probability-and-statistics)
- [Module 2: Random Processes - Convergence, Markov Chains and Applications](#module-2-random-processes---convergence-markov-chains-and-applications)
- [Module 3: Frequentist Statistics, Regression, Bayesian Statistics and Hypothesis Testing](#module-3-frequentist-statistics-regression-bayesian-statistics-and-hypothesis-testing)
- [Module 4: Linear Algebra](#module-4-linear-algebra)
- [Module 5: Optimization Techniques](#module-5-optimization-techniques)

---

## Module 1: Fundamentals of Probability and Statistics

### Key Topics
**Probability spaces**: Sample space, events, probability axioms.  
**Conditional probability**: Definition, Bayes' Theorem.  
**Independence**: Independent events and random variables.  

#### Random Variables
- **Discrete random variables**: Probability mass function (PMF), examples like Bernoulli, Binomial.
- **Continuous random variables**: Probability density function (PDF), examples like Uniform, Normal.

**Expectation Operator**:  
- Definition: $ E[X] = \sum x P(X=x) $ for discrete, $ E[X] = \int x f(x) dx $ for continuous.  
- Properties: Linearity, expectation of functions.

#### Functions of Random Variables
- Transformations of random variables (e.g., $ Y = g(X) $).  
- Generating random variables via inversion method or rejection sampling.

#### Multivariate Random Variables
**Joint distributions**: Discrete joint PMF and continuous joint PDF.  
**Functions of several random variables**: Convolution, transformation techniques.  

**Joint Moments**: Covariance, correlation coefficient.  
**Generating multivariate random variables**: Copulas, multivariate normal distribution.

---

## Module 2: Random Processes - Convergence, Markov Chains and Applications

### Key Topics
**Random Processes**: Definition, stationarity (strict and wide-sense), mean, autocovariance functions.  

#### Special Cases of Random Processes
- **Independent Identically Distributed (IID) Sequences**: Properties and applications.
- **Gaussian Process**: Multivariate normal distribution, properties.
- **Poisson Process**: Counting process, interarrival times, memoryless property.
- **Random Walk**: Discrete-time stochastic process with independent increments.

#### Convergence of Random Processes
**Types of convergence**:  
- Almost sure convergence.  
- Convergence in probability.  
- Convergence in distribution.  

**Law of Large Numbers (LLN)**: Weak and strong forms.  
**Central Limit Theorem (CLT)**: Distribution of sample means tends to Gaussian.

#### Markov Chains
**Time-homogeneous discrete-time Markov chains**: Transition matrices, recurrence, periodicity.  
**Markov Chain Monte Carlo (MCMC)**: Gibbs sampling, Metropolis-Hastings algorithm.  

**Descriptive Statistics**: Histograms, sample mean and variance, order statistics.  
**Sample Covariance and Covariance Matrix**: Estimation from data.

---

## Module 3: Frequentist Statistics, Regression, Bayesian Statistics and Hypothesis Testing

### Key Topics
#### **Frequentist Statistics**
- **Independent Identically Distributed (IID) Sampling**: Properties of estimators.
- **Mean Square Error (MSE)**: Trade-off between bias and variance.  
- **Consistency**: Asymptotic properties of estimators.

**Confidence Intervals**:  
- Constructing intervals for population mean, proportion, etc.  
- Nonparametric vs parametric methods.

#### **Regression Models**
- **Linear Regression**: Model form $ y = X\beta + \epsilon $.  
- **Least-Squares Estimation**: Normal equation $ \hat{\beta} = (X^T X)^{-1} X^T y $.  
- **Overfitting**: Regularization techniques (Lasso, Ridge).

#### **Bayesian Statistics**
- **Parametric Models**: Prior and posterior distributions.  
- **Conjugate Priors**: Beta-Gamma, Normal-Normal families.  
- **Bayesian Estimators**: Maximum a Posteriori (MAP), Minimum Mean Square Error (MMSE).

#### **Hypothesis Testing**
**Framework**: Null vs alternative hypotheses, p-values, significance levels.  
**Parametric Tests**: t-test, ANOVA, chi-squared test.  
**Nonparametric Tests**: Permutation tests, Wilcoxon rank-sum test.  
**Multiple Testing**: Bonferroni correction, False Discovery Rate (FDR).

---

## Module 4: Linear Algebra

### Key Topics
- **Vector Spaces**: Subspaces, basis, dimensionality.  
- **Norms and Inner Products**: Euclidean norm, Frobenius norm, Cauchy-Schwarz inequality.

**Linear Mappings**:  
- Range (column space), null space (kernel).  
- Rank-nullity theorem.

**Matrix Operations**:  
- Matrix multiplication, transpose, inverse.  
- Properties of matrix norms and operations.

---

## Module 5: Optimization Techniques

### Key Topics
#### **Basic Concepts**
- **Normal Equation**: Closed-form solution for linear regression.  

#### **Gradient-Based Methods**
- **Steepest Descent**: Iterative method with gradient direction.  
- **Conjugate Gradient**: Accelerated descent using conjugate directions.  

**Optimality Conditions**:  
- First-order (gradient zero) and second-order (Hessian positive definite).  

#### **Local Quadratic Models**
- Newton's Method: Uses quadratic approximation for faster convergence.  
- Line Search Methods: Ensuring sufficient decrease in objective function.

---

## Conclusion
This documentation provides a structured overview of probability, statistics, random processes, linear algebra, and optimization techniques essential for data science, machine learning, and engineering applications. It serves as a foundational reference for students and researchers exploring statistical modeling and computational methods.