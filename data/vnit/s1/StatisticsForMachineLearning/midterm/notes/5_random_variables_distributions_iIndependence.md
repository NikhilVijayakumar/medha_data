# Random Variables, Distributions, Independence, and Correlation

This notebook elaborates on the concepts of random variables, their distributions, the notions of independence and identical distribution, joint and marginal distributions, and the relationship between independence and correlation.

## 1. Random Variable (RV)

- **Definition:** A variable whose value is a numerical outcome of a random phenomenon.

## 2. Distribution of a Random Variable

- **Definition:** Describes the probabilities of all possible values that the random variable can take.
- **Representation:**
    - **Probability Density Function (PDF):** Used for continuous random variables.
    - **Probability Mass Function (PMF):** Used for discrete random variables.

## 3. Parameters of a Distribution

- **Definition:** Values that define the specific form of a probability distribution.
- **Examples:**
    - Gaussian distribution: mean ($\mu$) and variance ($\sigma^2$).
    - Poisson distribution: rate parameter ($\lambda$).

## 4. Identically Distributed

- **Definition:** Two or more random variables have the same probability distribution (same PDF or PMF) and the same parameter values.
- **Implication:** Their statistical properties (mean, variance, etc.) are the same, although their actual values in a specific instance can differ.

## 5. Independent Events

- **Definition:** Two events A and B are independent if the probability of both occurring is the product of their individual probabilities:
  $$P(A \cap B) = P(A) \times P(B)$$
- **Key Characteristic:** The outcome of one event does not influence the outcome of the other.

## 6. Independent Random Variables

- **Definition:** Two random variables X and Y are independent if their joint probability distribution (joint PDF or PMF) is the product of their individual (marginal) distributions:
    - Continuous: $f_{XY}(x, y) = f_X(x) \times f_Y(y)$
    - Discrete: $P_{XY}(x, y) = P_X(x) \times P_Y(y)$
- **Extension to Collections:** For a collection of random variables to be independent, this condition must hold for any subset of the collection.

## 7. Independent and Identically Distributed (i.i.d.)

- **Definition:** A collection of random variables is i.i.d. if each random variable:
    - Has the same probability distribution as the others (identically distributed).
    - Is mutually independent of each other (independent).

## 8. Joint Distribution (Joint PDF/PMF)

- **Definition:** The probability distribution of two or more random variables considered together.
- **Purpose:** Specifies the probabilities of all possible combinations of values of these variables.

## 9. Marginal Distribution (Marginal PDF/PMF)

- **Definition:** The probability distribution of a single random variable when considered in isolation from a joint distribution.
- **Derivation:** Obtained by summing (for discrete) or integrating (for continuous) the joint distribution over all possible values of the other variables.

## 10. Uncorrelated Random Variables

- **Definition:** Two random variables X and Y are uncorrelated if their covariance is zero:
  $$Cov(X, Y) = E[XY] - E[X]E[Y] = 0$$
- **Interpretation:** Indicates no linear relationship between the variables.

## 11. Covariance

- **Definition:** A measure of how two random variables change together.
- **Interpretation:**
    - Positive covariance: Variables tend to increase or decrease together.
    - Negative covariance: One variable tends to increase when the other decreases.
    - Zero covariance: No linear relationship.

## 12. Relation Between Independence and Uncorrelatedness

- **Key Principle:** If two random variables are independent, then they are always uncorrelated.
- **Important Note:** The converse is not necessarily true; uncorrelated random variables are not always independent. There might be non-linear relationships between them.

## 13. Mutual Exclusiveness

- **Definition:** Two events are mutually exclusive if they cannot occur at the same time.
- **Probability:** If events A and B are mutually exclusive, then $P(A \cap B) = 0$.
- **Distinction from Independence:** Independence and mutual exclusiveness are generally distinct concepts, except in trivial cases where one of the probabilities is zero. Mutually exclusive events cannot be independent unless one of their probabilities is zero. If $P(A) > 0$ and $P(B) > 0$ and they are mutually exclusive ($P(A \cap B) = 0$), then $P(A \cap B) \neq P(A)P(B)$, violating the condition for independence.

# Formualas

# Independence, Correlation, and Covariance of Random Variables and Events

This notebook summarizes the concepts of independence, correlation, and covariance for both events and random variables, as presented in the sources.

## Independence

### 1. Independent Events

- For two independent events A and B, the probability of both occurring is the product of their individual probabilities:
  $$P(A \cap B) = P(A) P(B)$$

### 2. Independent Random Variables

- Two random variables X and Y are independent if their joint probability density function (PDF) is the product of their individual PDFs:
  $$f_{XY}(x, y) = f_X(x) f_Y(y)$$

- For a vector $\mathbf{X} = (X_1, X_2, ..., X_N)$ of $N$ independent and identically distributed (i.i.d.) components, the joint PDF is the product of the individual PDFs:
  $$f(x_1, x_2, ..., x_N) = \prod_{i=1}^{N} f(x_i)$$

## Correlation and Covariance

### 1. Uncorrelated Random Variables

- Two random variables X and Y are uncorrelated if their covariance is zero:
  $$Cov(X, Y) = 0$$

### 2. Covariance Formula

- The formula for covariance between two random variables X and Y is:
  $$Cov(X, Y) = E[XY] - E[X]E[Y]$$

- The covariance can also be expressed using integrals of the PDFs:
  $$Cov(X, Y) = \int \int xy f_{XY}(x, y) dx dy - \int x f_X(x) dx \int y f_Y(y) dy$$

- The covariance of a random variable with itself is its variance:
  $$Cov(X, X) = E[X^2] - (E[X])^2 = Var(X)$$

## Mutually Exclusive Events

- For two mutually exclusive events A and B, the probability of both occurring is zero:
  $$P(A \cap B) = 0$$

## Relationship between Independence and Uncorrelation

- If two random variables X and Y are independent, then they are uncorrelated. This can be shown as follows:
  If X and Y are independent, then $f_{XY}(x, y) = f_X(x) f_Y(y)$. Substituting this into the covariance formula yields:
  $$Cov(X, Y) = \int \int xy f_X(x) f_Y(y) dx dy - \int x f_X(x) dx \int y f_Y(y) dy$$
  $$Cov(X, Y) = \left(\int x f_X(x) dx\right)\left(\int y f_Y(y) dy\right) - \left(\int x f_X(x) dx\right)\left(\int y f_Y(y) dy\right)$$
  $$Cov(X, Y) = E[X]E[Y] - E[X]E[Y] = 0$$
  Therefore, independence implies uncorrelation. However, the converse is not always true. Uncorrelated random variables are not necessarily independent.