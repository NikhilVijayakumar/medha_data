# Random Variables and Common Probability Distributions

This notebook provides definitions of different types of random variables, their associated probability functions, and some common probability distributions along with their defining parameters.

## 1. Random Variables (RV)

- **Definition:** A variable whose value is a numerical outcome of a random phenomenon.

## 2. Types of Random Variables

- **Discrete Random Variable:** A random variable that can only take on a finite or countably infinite number of distinct values (e.g., the number of heads in 10 coin flips, the number of customers arriving at a store in an hour).

- **Continuous Random Variable:** A random variable that can take on any value within a given interval or range (e.g., height of a person, temperature of a room, time taken to complete a task).

## 3. Probability Functions

- **Probability Mass Function (PMF):**
  - **Applicable to:** Discrete Random Variables.
  - **Definition:** A function that gives the probability that the discrete random variable is exactly equal to a specific value.
  - Notation: Typically denoted as $P(X=x)$ or $p_X(x)$.

- **Probability Density Function (PDF):**
  - **Applicable to:** Continuous Random Variables.
  - **Definition:** A function that describes the likelihood of a continuous random variable taking on a given value within a certain range. The area under the PDF over an interval represents the probability that the random variable falls within that interval.
  - Notation: Typically denoted as $f_X(x)$.
  - Note: The value of the PDF at a single point does not directly represent probability for a continuous random variable.

## 4. Common Probability Distributions

### 4.1. Discrete Distributions

- **Binomial Distribution:**
  - **Description:** Models the number of successes in a fixed number ($n$) of independent Bernoulli trials, each with the same probability of success ($p$).
  - **Parameters:** $n$ (number of trials), $p$ (probability of success).

- **Poisson Distribution:**
  - **Description:** Models the number of events occurring in a fixed interval of time or space, given a known average rate ($\lambda$) and independence of events.
  - **Parameter:** $\lambda$ (average rate of events).

- **Bernoulli Distribution:**
  - **Description:** Models a single trial of a random experiment with only two possible outcomes, typically labelled success (1) and failure (0). It's a special case of the Binomial distribution with $n=1$.
  - **Parameter:** $p$ (probability of success).

### 4.2. Continuous Distributions

- **Uniform Distribution:**
  - **Description:** All values within a specified interval $[a, b]$ are equally likely.
  - **Parameters:** $a$ (lower bound), $b$ (upper bound).

- **Normal (Gaussian) Distribution:**
  - **Description:** Characterized by its bell-shaped curve, symmetric around the mean ($\mu$). The spread of the distribution is determined by the variance ($\sigma^2$) or standard deviation ($\sigma$).
  - **Parameters:** $\mu$ (mean), $\sigma^2$ (variance) or $\sigma$ (standard deviation).

## 5. Measures of Central Tendency and Dispersion

- **Mean (Expected Value):**
  - **Definition:** The average value of a random variable over many repetitions of the experiment.
  - **Discrete RV:** $E[X] = \sum x P(X=x)$ (sum over all possible values $x$).

- **Variance:**
  - **Definition:** A measure of the spread or dispersion of the possible values of a random variable around its mean. It is the expected value of the squared difference from the mean: $Var(X) = E[(X - E[X])^2]$.

- **Standard Deviation:**
  - **Definition:** The square root of the variance ($\sigma = \sqrt{Var(X)}$). It provides a measure of the typical deviation of values from the mean in the same units as the random variable.

## 6. Parameter

- **Definition:** A numerical characteristic of a population or a probability distribution that helps define its shape and location.
- **Examples:**
  - Binomial: $n$ (number of trials), $p$ (probability of success).
  - Poisson: $\lambda$ (average rate).
  - Normal: $\mu$ (mean), $\sigma^2$ (variance).
  - Bernoulli: $p$ (probability of success).

# Formulas

# Probability Distributions and Their Properties

This notebook summarizes common probability distributions and their key formulas as presented in the source. Note that the source contains several typos and unclear expressions, which have been corrected or clarified where possible.

## Discrete Probability Distributions

### 1. Binomial Distribution

- **Probability Mass Function (PMF):**
  $$P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$$
  where:
    - $n$ is the number of trials
    - $k$ is the number of successful trials
    - $p$ is the probability of success on a single trial

  *Note: The source had a typo in the PMF formula.*

### 2. Poisson Distribution

- **Probability Mass Function (PMF):**
  $$P(X=r) = e^{-\lambda} \frac{\lambda^r}{r!}$$
  where:
    - $\lambda$ is the average rate of events
    - $r$ is the number of events

  *Note: The source had a typo ('é' instead of 'e').*

- **Example Probability Calculation:**
  $$P(X=10) = e^{-5} \frac{5^{10}}{10!}$$
  (Probability of 10 events occurring when the average rate is 5)

### 3. Bernoulli Distribution

- **Probability Mass Function (PMF):**
  $$P(X=k) = p^k (1-p)^{1-k} \quad \text{for } k \in \{0, 1\}$$
  where:
    - $p$ is the probability of success (k=1)
    - $1-p$ is the probability of failure (k=0)

- **Mean:**
  $$E[X] = p$$

- **Variance:**
  $$Var(X) = p(1-p)$$

- **Calculated Example (Mean):**
  If $p = 0.8$, then $E[X] = (0.8 \times 1) + (0.2 \times 0) = 0.8$

- **Calculated Example (Variance):**
  If $p = 0.8$, then $Var(X) = (1 - 0.8)^2 \times 0.8 + (0 - 0.8)^2 \times 0.2 = 0.16$

## Continuous Probability Distributions

### 1. Uniform Distribution

- **Probability Density Function (PDF):**
  $$f(x) = \frac{1}{b-a} \quad \text{for } a \le x \le b$$
  $$f(x) = 0 \quad \text{otherwise}$$
  where $a$ is the lower bound and $b$ is the upper bound of the interval.

- **Mean:**
  $$E[X] = \frac{a+b}{2}$$
  *Note: The source had an unclear expression for the mean.*

- **Variance:**
  $$Var(X) = \frac{(b-a)^2}{12}$$
  *Note: The source had an unclear expression for the variance.*

- **Probability for an interval $[c, d]$ within $[a, b]$:**
  $$P(c \le X \le d) = \int_{c}^{d} f(x) dx = \int_{c}^{d} \frac{1}{b-a} dx = \frac{d-c}{b-a}$$
  *Note: The source had an unclear expression related to the integral.*

### 2. Normal (Gaussian) Distribution

- **Probability Density Function (PDF):**
  $$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2} (\frac{x-\mu}{\sigma})^2}$$
  where:
    - $\mu$ is the mean
    - $\sigma$ is the standard deviation
    - $\sigma^2$ is the variance

- **Notation:** A Normal distribution with mean $\mu$ and variance $\sigma^2$ is denoted as $X \sim N(\mu, \sigma^2)$.
  - Example from the source: $X \sim N(5, 2)$ (mean = 5, variance = 2)

### 3. Standard Normal Distribution

- A special case of the Normal distribution with mean $\mu = 0$ and variance $\sigma^2 = 1$.
- **Notation:** $Z \sim N(0, 1)$

### 4. Chi-squared Distribution

- Denoted as $X^2 \sim N(0.5)$ in the source, which likely refers to a Chi-squared distribution with a specific degrees of freedom parameter not clearly stated. The standard notation is $X^2 \sim \chi^2(k)$, where $k$ is the degrees of freedom.

## Cumulative Distribution Function (CDF)

- **Definition:**
  $$F_X(w) = P(X \le w)$$
  This gives the probability that the random variable $X$ takes on a value less than or equal to $w$.

- **Probability in terms of CDF:**
  $$P(X \le w) = F_X(w)$$

## Properties of Random Variables

### 1. Expected Value (Mean)

- **Discrete Random Variable:**
  $$E[X] = \sum x P(x)$$
  *Note: The source had an unclear representation.*

- **Discrete Distribution (Alternative Notation):**
  $$E[X] = \sum p_i x_i$$

- **nth Central Moment:**
  $$E[(X - \mu_X)^n]$$
  For $n=2$, this gives the variance.

### 2. Variance

- **Definition:**
  $$Var(X) = E[(X - E[X])^2]$$
- **Alternative Formula:**
  $$Var(X) = E[X^2] - (E[X])^2$$
  *Note: The source had several unclear representations of variance.*

- **Discrete Distribution:**
  $$Var(X) = \sum (x_i - \mu_X)^2 P(x_i)$$

### 3. Standard Deviation

- **Definition:**
  $$\sigma_X = \sqrt{Var(X)}$$

### 4. Linear Transformation of a Normal Random Variable

- If $X \sim N(\mu_X, \sigma_X^2)$ and $Y = aX + b$, then:
  $$Y \sim N(a\mu_X + b, a^2\sigma_X^2)$$
  *Note: The source had a very convoluted and unclear representation of this property.*