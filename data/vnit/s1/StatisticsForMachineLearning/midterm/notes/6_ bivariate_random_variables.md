# Bivariate Random Variables and Related Concepts

This notebook focuses on the concepts of bivariate random variables, their distributions, and related statistical measures like covariance and correlation, as well as the crucial Central Limit Theorem.

## 1. Bivariate Random Variable

- **Definition:** A pair of random variables $(X, Y)$ considered together, defined on the same sample space. This allows for the study of the joint behavior of two random quantities.

## 2. Sample Space

- **Definition:** The set of all possible outcomes of a random experiment. The bivariate random variable $(X, Y)$ maps these outcomes to pairs of numerical values.

## 3. Joint Cumulative Distribution Function (CDF)

- **Definition:** A function $F_{XY}(x, y) = P(X \le x, Y \le y)$ that gives the probability that the random variable $X$ is less than or equal to $x$ AND the random variable $Y$ is less than or equal to $y$.

## 4. Types of Bivariate Random Variables

- **Discrete Bivariate Random Variable:** A bivariate random variable where both $X$ and $Y$ can only take on a countable number of distinct values.
- **Continuous Bivariate Random Variable:** A bivariate random variable where both $X$ and $Y$ can take on any value within a given range or interval.

## 5. Joint Probability Mass Function (PMF)

- **Applicable to:** Discrete Bivariate Random Variables.
- **Definition:** A function $P_{XY}(x_i, y_j) = P(X = x_i, Y = y_j)$ that gives the probability that the discrete random variable $X$ takes on the value $x_i$ AND the discrete random variable $Y$ takes on the value $y_j$.

## 6. Joint Probability Density Function (PDF)

- **Applicable to:** Continuous Bivariate Random Variables.
- **Definition:** A function $f_{XY}(x, y)$ such that the probability that the continuous random variable $X$ falls in the interval $[a, b]$ AND $Y$ falls in the interval $[c, d]$ is given by the double integral of $f_{XY}(x, y)$ over this rectangular region:
  $$P(a \le X \le b, c \le Y \le d) = \int_{a}^{b} \int_{c}^{d} f_{XY}(x, y) dy dx$$

## 7. Marginal Distribution

- **Definition:** The probability distribution of a single random variable ($X$ or $Y$) when considered in isolation from their joint distribution.
- **Derivation:**
    - For discrete variables: $P_X(x_i) = \sum_j P_{XY}(x_i, y_j)$ and $P_Y(y_j) = \sum_i P_{XY}(x_i, y_j)$.
    - For continuous variables: $f_X(x) = \int_{-\infty}^{\infty} f_{XY}(x, y) dy$ and $f_Y(y) = \int_{-\infty}^{\infty} f_{XY}(x, y) dx$.

## 8. Conditional Distribution

- **Definition:** The probability distribution of one random variable given that the other random variable has taken on a specific value.
- **Formulas:**
    - Discrete: $P_{Y|X}(y|x) = \frac{P_{XY}(x, y)}{P_X(x)}$ (if $P_X(x) > 0$) and $P_{X|Y}(x|y) = \frac{P_{XY}(x, y)}{P_Y(y)}$ (if $P_Y(y) > 0$).
    - Continuous: $f_{Y|X}(y|x) = \frac{f_{XY}(x, y)}{f_X(x)}$ (if $f_X(x) > 0$) and $f_{X|Y}(x|y) = \frac{f_{XY}(x, y)}{f_Y(y)}$ (if $f_Y(y) > 0$).

## 9. Covariance

- **Definition:** A measure of the linear relationship between two random variables, indicating how they change together.
- **Formula:** $Cov(X, Y) = E[XY] - E[X]E[Y]$.
- **Interpretation:**
    - Positive covariance: $X$ and $Y$ tend to increase or decrease together.
    - Negative covariance: $X$ tends to increase when $Y$ decreases (and vice versa).
    - Zero covariance: No linear relationship between $X$ and $Y$.

## 10. Correlation

- **Definition:** A standardized measure of the linear relationship between two random variables, ranging from -1 to +1.
- **Formula:** $Corr(X, Y) = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}$, where $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$, respectively.
- **Interpretation:**
    - +1: Perfect positive linear relationship.
    - -1: Perfect negative linear relationship.
    - 0: No linear relationship.
    - Values between -1 and +1 indicate the strength and direction of the linear relationship.

## 11. Independence (of Random Variables)

- **Definition:** Two random variables $X$ and $Y$ are independent if their joint distribution function can be expressed as the product of their marginal distribution functions:
  - For CDF: $F_{XY}(x, y) = F_X(x)F_Y(y)$ for all $x$ and $y$.
  - For PMF: $P_{XY}(x, y) = P_X(x)P_Y(y)$ for all $x$ and $y$.
  - For PDF: $f_{XY}(x, y) = f_X(x)f_Y(y)$ for all $x$ and $y$.
- **Implication:** The value of one random variable does not provide any information about the value of the other.

## 12. Uncorrelatedness

- **Definition:** Two random variables $X$ and $Y$ are uncorrelated if their covariance is zero ($Cov(X, Y) = 0$).
- **Relationship to Independence:** Independence implies uncorrelatedness, but uncorrelatedness does not necessarily imply independence (unless the variables are jointly Gaussian).

## 13. Gaussian (Normal) Distribution

- **Definition:** A continuous probability distribution characterized by its bell-shaped curve, defined by its mean ($\mu$) and variance ($\sigma^2$). It plays a central role in statistics and probability theory.

## 14. Central Limit Theorem (CLT)

- **Statement:** The distribution of the sum (or mean) of a large number of independent and identically distributed (i.i.d.) random variables approaches a normal distribution, regardless of the original distribution of the individual variables (provided they have finite mean and variance). This is a fundamental theorem in statistics.

## 15. i.i.d.

- **Definition:** An abbreviation for independent and identically distributed, referring to a sequence of random variables where each variable has the same probability distribution as the others and all are mutually independent. This is a common assumption in many statistical analyses and is crucial for the Central Limit Theorem.

# Formulas

# Joint, Conditional Distributions, Covariance, Correlation, and Central Limit Theorem

This notebook summarizes formulas related to joint and conditional distributions of random variables, covariance, correlation, and the Central Limit Theorem as presented in the sources.

## Joint Cumulative Distribution Function (CDF)

- **Definition:**
  $$F_{XY}(x, y) = P(X \le x, Y \le y)$$
  This represents the probability that random variable $X$ is less than or equal to $x$ AND random variable $Y$ is less than or equal to $y$.

- **Relationship to Events:**
  $$F_{XY}(x, y) = P(A \cap B)$$
  where $A$ is the event $\{X \le x\}$ and $B$ is the event $\{Y \le y\}$.

- **Independence:** If $X$ and $Y$ are independent, then:
  $$F_{XY}(x, y) = F_X(x)F_Y(y)$$
  This follows from the independence of events $A$ and $B$, where $P(A \cap B) = P(A)P(B)$.

- **Properties:**
  - $$F_{XY}(-\infty, y) = 0$$
  - $$F_{XY}(x, -\infty) = 0$$
  - $$F_{XY}(\infty, \infty) = 1$$
  - For $x_1 \le x_2$ and $y_1 \le y_2$:
    $$F_{XY}(x_2, y_2) - F_{XY}(x_1, y_2) - F_{XY}(x_2, y_1) + F_{XY}(x_1, y_1) = P(x_1 < X \le x_2, y_1 < Y \le y_2) \ge 0$$

- **Probabilities from Joint CDF:**
  - $$P(x_1 < X \le x_2, Y \le y) = F_{XY}(x_2, y) - F_{XY}(x_1, y)$$
  - $$P(X \le x, y_1 < Y \le y_2) = F_{XY}(x, y_2) - F_{XY}(x, y_1)$$

## Joint Probability Mass Function (PMF)

- **Definition (for discrete random variables):**
  $$P_{XY}(n_i, m_j) = P(X = n_i, Y = m_j)$$
  where $n_i$ and $m_j$ are integer values that $X$ and $Y$ can take.

- **Summation Property:**
  $$\sum_{i} \sum_{j} P_{XY}(n_i, m_j) = 1$$

- **Marginal CDFs from Joint PMF:**
  - $$F_X(x) = \sum_{n_i \le x} \sum_{j} P_{XY}(n_i, m_j)$$
  - $$F_Y(y) = \sum_{i} \sum_{m_j \le y} P_{XY}(n_i, m_j)$$

## Joint Probability Density Function (PDF)

- **Definition (for continuous random variables):**
  $$f_{XY}(x, y) = \frac{\partial^2}{\partial x \partial y} F_{XY}(x, y)$$

- **Integration Property:**
  $$\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{XY}(u, v) du dv = 1$$

- **Non-negativity:**
  $$f_{XY}(x, y) \ge 0$$

- **Marginal PDFs from Joint PDF:**
  - $$f_X(x) = \int_{-\infty}^{\infty} f_{XY}(x, y) dy$$
  - $$f_Y(y) = \int_{-\infty}^{\infty} f_{XY}(x, y) dx$$

## Conditional Probability Distributions

### 1. Conditional Probability Mass Function (PMF)

- $$P_{X|Y}(x|y) = \frac{P_{XY}(x, y)}{P_Y(y)}$$
- $$P_{Y|X}(y|x) = \frac{P_{XY}(x, y)}{P_X(x)}$$

- **Summation Properties:**
  - $$\sum_x P_{X|Y}(x|y) = 1$$
  - $$\sum_y P_{Y|X}(y|x) = 1$$

### 2. Conditional Density Functions

- $$f_{Y|X}(y|x) = \frac{f_{XY}(x, y)}{f_X(x)}$$
- $$f_{X|Y}(x|y) = \frac{f_{XY}(x, y)}{f_Y(y)}$$

- **Integration Properties:**
  - $$\int_{-\infty}^{\infty} f_{Y|X}(y|x) dy = 1$$
  - $$\int_{-\infty}^{\infty} f_{X|Y}(x|y) dx = 1$$

- **Non-negativity:**
  - $$f_{Y|X}(y|x) \ge 0$$
  - $$f_{X|Y}(x|y) \ge 0$$

## Covariance and Correlation

- **Covariance:**
  $$Cov(X, Y) = E[XY] - E[X]E[Y]$$

- **Independence and Expected Value of Product:** If $X$ and $Y$ are independent, then:
  $$E[XY] = E[X]E[Y]$$

- **Independence and Covariance:** For independent $X$ and $Y$:
  $$Cov(X, Y) = 0$$

- **Correlation:**
  $$Corr(X, Y) = \frac{Cov(X, Y)}{\sigma_X \sigma_Y}$$
  where $\sigma_X$ and $\sigma_Y$ are the standard deviations of $X$ and $Y$, respectively.

- **Independence and Correlation:** If $X$ and $Y$ are independent, then:
  $$Corr(X, Y) = 0$$

- **Linear Relationship and Correlation:** If $Y = aX + b$, then:
  $$Corr(X, Y) = \pm 1$$
  The sign depends on the sign of $a$.

## Central Limit Theorem

- For a sequence of $N$ independent and identically distributed (i.i.d.) random variables $X_1, X_2, ..., X_n$, the distribution of the sum $\sum_{i=1}^{N} X_i$ approaches a Gaussian distribution as $N$ becomes large.

- For a sequence of i.i.d. random variables $X_n$ with mean $\mu$ and variance $\sigma^2$, the distribution of the sample mean $\overline{X}_n = \frac{1}{n} \sum_{i=1}^{n} X_i$ approaches a Gaussian distribution with mean $\mu$ and variance $\frac{\sigma^2}{n}$ as $n$ becomes very large.
