Here's the well-formatted Markdown documentation with LaTeX for mathematical formulas, based on the provided "SML-Formulas.pdf" content.

---

# SML - Essential Formulas and Concepts

This document summarizes key formulas and concepts in probability, statistics, and linear algebra, primarily focusing on topics relevant to machine learning.

---

## 1. Probability Distributions

### 1.1 Density Function
For a continuous probability distribution, the integral of the probability density function (PDF) $f(x)$ over its entire domain must equal 1:
[cite_start]$$\int_{-\infty}^{\infty}f(x)dx=1$$ [cite: 1]

### 1.2 Binomial Probability Formula
The probability mass function (PMF) for a binomial distribution, where $k$ is the number of successes in $n$ trials, $p$ is the probability of success, and $q = (1-p)$ is the probability of failure, is given by:
[cite_start]$$P(x=k) = nC_{k} \cdot p^{k} \cdot q^{n-k}$$ [cite: 1]
Alternatively, using binomial coefficient notation:
[cite_start]$$P(X=k) = \binom{n}{k}p^{k}(1-p)^{n-k}$$ [cite: 8]
[cite_start]where $n$ is the number of samples, and $k$ is the number of classifications[cite: 9]. The binomial coefficient is defined as:
[cite_start]$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$ [cite: 8]

### 1.3 Gaussian (Normal) Distribution
For a Gaussian random variable $X$:
[cite_start]$$X \sim N(\mu_{x}, \sigma_{x}^{2})$$ [cite: 1]
[cite_start]Here, $\mu_x$ represents the mean and $\sigma_x^2$ represents the variance[cite: 1].

#### Linear Transformation of a Gaussian Variable
If $Y = aX + b$ (a linear transformation), and $X \sim N(\mu_x, \sigma_x^2)$, then $Y$ also follows a normal distribution:
[cite_start]$$Y \sim N(a\mu_{x}+b, a^{2}\sigma_{x}^{2})$$ [cite: 1]
For independent random variables $X \sim N(\mu_x, \sigma_x^2)$ and $Y \sim N(\mu_y, \sigma_y^2)$, their sum $Z = X+Y$ is also normally distributed:
[cite_start]$$Z \sim N((\mu_x+\mu_y), \sigma_x^2 + \sigma_y^2)$$ [cite: 6]

### 1.4 PDF of Exponential Distribution
For $\lambda > 0$, the probability density function (PDF) of an exponential distribution is:
[cite_start]$$f_{x}(x) = \begin{cases} \lambda e^{-\lambda x}, & x \ge 0 \\ 0, & x < 0 \end{cases}$$ [cite: 3]

### 1.5 Poisson Distribution
For a Poisson random variable $X$ with parameter $\lambda$ ($X \sim \text{Poisson}(\lambda)$):
[cite_start]$$P(X=k) = \frac{e^{-\lambda}\lambda^{k}}{k!}$$ [cite: 12]
The expectation and variance are both equal to $\lambda$:
[cite_start]$$E[X] = \lambda$$ [cite: 12]
[cite_start]$$Var(X) = \lambda$$ [cite: 12]

---

## 2. Probability Concepts

### 2.1 Conditional Probability
The conditional probability of event $A$ given event $B$ is:
[cite_start]$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$ [cite: 2]

### 2.2 Bayes' Theorem
Bayes' Theorem relates conditional probabilities:
[cite_start]$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$ [cite: 2]

### 2.3 Law of Total Probability
The Law of Total Probability states that for an event $A$ and its complement $\overline{B}$:
[cite_start]$$P(A) = P(A|B) \cdot P(B) + P(A|\overline{B}) \cdot P(\overline{B})$$ [cite: 2]

### 2.4 Independent Events
Two events $A$ and $B$ are independent if and only if the probability of their intersection is the product of their individual probabilities:
[cite_start]$$P(A \cap B) = P(A) \cdot P(B)$$ [cite: 3]

---

## 3. Random Variables and Expectation/Variance

### 3.1 Discrete and Continuous Random Variables
* [cite_start]**Discrete:** Takes countable values and is associated with a Probability Mass Function (PMF), $P(X=x)$[cite: 3].
* [cite_start]**Continuous:** Takes interval values and is associated with a Probability Density Function (PDF), $f_x(u)$[cite: 3].

### 3.2 Expectation (Mean)
* **For a discrete random variable $X$:**
    [cite_start]$$E(X) = \sum_{x} x P(X=x)$$ [cite: 3]
* **For a continuous random variable $X$:**
    [cite_start]$$E(X) = \int x f(x)dx$$ [cite: 3]
* **For a Bernoulli random variable $X \sim \text{Bernoulli}(p)$:**
    [cite_start]$$E[X] = p$$ [cite: 7]
* **For a Binomial random variable $X \sim \text{Binoulli}(n, p)$:**
    [cite_start]$$E[X] = n \cdot p$$ [cite: 7]

### 3.3 Variance
The variance of a random variable $X$ is given by:
[cite_start]$$Var(X) = E[X^2] - (E[X])^2$$ [cite: 3]
* **For a Bernoulli random variable $X \sim \text{Bernoulli}(p)$:**
    [cite_start]$$Var(X) = p(1-p)$$ [cite: 7]
* **For a Binomial random variable $X \sim \text{Bernoulli}(n, p)$:**
    [cite_start]$$Var(X) = n \cdot p(1-p)$$ [cite: 7]

---

## 4. Statistical Inference

### 4.1 Z-Standardization Formula
The Z-score for a value $x$ from a distribution with mean $\mu$ and standard deviation $\sigma$ is:
[cite_start]$$z = \frac{x-\mu}{\sigma}$$ [cite: 6]

### 4.2 Z-table Values
A table provides Z-score to probability mappings:
| Z-Value | Probability |
| :------ | :---------- |
| -2      | 0.0228      |
| -1      | 0.1587      |
| 0       | 0.5000      |
| 1       | 0.8413      |
| 1.5     | 0.9332      |
| 2       | [cite_start]0.9772      | [cite: 5]

### 4.3 Maximum Likelihood Estimate (MLE)
[cite_start]The MLE of $p$ (probability of success) for Bernoulli/Binomial models is simply the observed proportion of successes[cite: 9].

### 4.4 Confidence Interval for Binomial Proportion
* **Standard Error (SE):**
    [cite_start]$$SE = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$ [cite: 10]
* **Margin of Error (ME):**
    [cite_start]$$ME = \text{Critical Value} \times SE$$ [cite: 10]
* **Confidence Interval (CI):**
    [cite_start]$$CI = \hat{p} \pm ME$$ [cite: 10]

#### Critical Values for Confidence Intervals:
| Confidence % | Critical Value |
| :----------- | :------------- |
| 90%          | 1.645          |
| 95%          | 1.96           |
| 99%          | [cite_start]2.576          | [cite: 11]

---

## 5. Linear Algebra

### 5.1 Determinant
The characteristic equation used to find eigenvalues ($\lambda$) of a matrix $\bar{A}$ is:
[cite_start]$$[\bar{A} - \lambda I] = 0$$ [cite: 13]
For a 3x3 matrix, the expanded form of the characteristic equation is:
$$\lambda^3 - P\lambda^2 + Q\lambda - |\bar{A}| [cite_start]= 0$$ [cite: 13]
Where:
* [cite_start]$P$ = sum of diagonals of $A$ (Trace) [cite: 14]
* [cite_start]$Q$ = sum of minors of diagonals [cite: 14]
* [cite_start]$|\bar{A}|$ = Determinant of $A$ [cite: 14]

### 5.2 Gram-Schmidt Orthogonalization
[cite_start]Given a set of linearly independent vectors $v_1, v_2, v_3, \ldots, v_n$ [cite: 15][cite_start], the Gram-Schmidt process produces an orthogonal set of vectors $u_1, u_2, u_3, \ldots, u_n$ such that $u_i$ are orthogonal[cite: 15].
The steps are:
* [cite_start]$u_1 = v_1$ [cite: 16]
* [cite_start]$u_2 = v_2 - \text{proj}_{u_1}(v_2)$ [cite: 16]
    where the projection of $v_2$ onto $u_1$ is given by:
    [cite_start]$$\text{proj}_{u_1}(v_2) = \frac{v_2 \cdot u_1}{||u_1||^2} u_1$$ [cite: 16]

### 5.3 Null Space of a Matrix
The null space of a matrix $A$ consists of all vectors $\bar{x}$ that satisfy the condition:
[cite_start]$$A\bar{x} = 0$$ [cite: 17]

### 5.4 Eigenvalue Decomposition (EVD)
For any Hermitian Symmetric Matrix $\bar{A}$, its Eigenvalue Decomposition is:
[cite_start]$$\bar{A} = \bar{V} \bar{\Lambda} \bar{V}^{H}$$ [cite: 18]
Where:
* [cite_start]$\bar{A}$ is a Hermitian Symmetric Matrix [cite: 18]
* [cite_start]$\bar{V}$ is a matrix of eigenvectors [cite: 18]
* [cite_start]$\bar{\Lambda}$ is a diagonal matrix of eigenvalues [cite: 18]
* [cite_start]$\bar{V}^{H}$ is the Hermitian (conjugate) transpose of $\bar{V}$ [cite: 18]

---

## 6. Covariance and Correlation

### 6.1 Covariance
The covariance between two random variables $X$ and $Y$ is defined as:
[cite_start]$$Cov(X,Y) = E[(X-\mu_{X})(Y-\mu_{Y})]$$ [cite: 19]
Alternatively, it can be calculated as:
[cite_start]$$Cov(X,Y) = E[XY] - E[X] \cdot E[Y]$$ [cite: 19]
[cite_start]If $X$ and $Y$ are independent, then $E[XY] = E[X] \cdot E[Y]$[cite: 19]. Therefore, for independent $X$ and $Y$:
[cite_start]$$Cov(X,Y) = 0$$ [cite: 20]

If $X$ and $Y$ are not independent:
[cite_start]$$E[XY] = Cov(X,Y) + E[X] \cdot E[Y]$$ [cite: 20]

### 6.2 Correlation
The correlation between two random variables $X$ and $Y$ is:
[cite_start]$$Corr(X,Y) = \frac{Cov(X,Y)}{\sqrt{Var(X) \cdot Var(Y)}}$$ [cite: 19]