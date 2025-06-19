# Probability and Statistics Summary

---

## I. Sample Space and Events

- **Sample Space:**  
  The set of all possible outcomes of an experiment, denoted as:  
  $$
  S = \{ s_1, s_2, ..., s_n \}
  $$

- **Event:**  
  A subset of the sample space.  
  If \( A \subseteq S \), then A is an event.

---

## II. Probability of an Event

- **Classical Definition (Equally Likely Outcomes):**  
  $$
  P(A) = \frac{n(A)}{n(S)}
  $$

- **Axioms of Probability:**  
  1. \( 0 \leq P(A) \leq 1 \)  
  2. \( P(S) = 1 \)  
  3. If \( A_1, A_2, ..., A_n \) are mutually exclusive:  
     $$
     P\left( \bigcup_{i=1}^{n} A_i \right) = \sum_{i=1}^{n} P(A_i)
     $$

---

## III. Conditional Probability

- **Definition:**  
  $$
  P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad \text{if } P(B) > 0
  $$

- **Multiplication Rule:**  
  $$
  P(A \cap B) = P(A|B) \cdot P(B)
  $$

---

## IV. Independence of Events

- Events A and B are **independent** if:  
  $$
  P(A \cap B) = P(A) \cdot P(B)
  $$

---

## V. Bayes' Theorem

- **Formula:**  
  $$
  P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}
  $$

- **Total Probability Theorem (For mutually exclusive \( A_i \)'s):**  
  $$
  P(B) = \sum_{i=1}^{n} P(B|A_i) \cdot P(A_i)
  $$

---

## VI. Random Variables

- **Discrete Random Variable:** Takes a finite or countable set of values.  
- **Continuous Random Variable:** Takes an uncountable number of possible values.

---

## VII. Probability Distribution

- **Discrete Random Variable X:**  
  Probability Mass Function (PMF):  
  $$
  p(x) = P(X = x)
  $$

- **Continuous Random Variable X:**  
  Probability Density Function (PDF):  
  $$
  f(x), \quad \text{such that } P(a \leq X \leq b) = \int_a^b f(x) \, dx
  $$

---

## VIII. Cumulative Distribution Function (CDF)

- **For a random variable X:**  
  $$
  F(x) = P(X \leq x)
  $$

- **Relationship with PDF (for continuous X):**  
  $$
  F(x) = \int_{-\infty}^{x} f(t) \, dt
  $$

---

## IX. Expectation and Variance

- **Expectation (Mean):**  
  - Discrete:  
    $$
    E[X] = \sum_x x \cdot p(x)
    $$  
  - Continuous:  
    $$
    E[X] = \int_{-\infty}^{\infty} x \cdot f(x) \, dx
    $$

- **Variance:**  
  $$
  \text{Var}(X) = E[(X - \mu)^2] = E[X^2] - (E[X])^2
  $$

- **Standard Deviation:**  
  $$
  \sigma = \sqrt{\text{Var}(X)}
  $$

---

## X. Common Distributions

### 1. **Bernoulli Distribution**

- PMF:  
  $$
  P(X = x) = p^x (1 - p)^{1 - x}, \quad x \in \{0, 1\}
  $$
- Mean:  
  $$
  \mu = p
  $$
- Variance:  
  $$
  \sigma^2 = p(1 - p)
  $$

---

### 2. **Binomial Distribution**

- PMF:  
  $$
  P(X = k) = \binom{n}{k} p^k (1 - p)^{n - k}, \quad k = 0, 1, ..., n
  $$
- Mean:  
  $$
  \mu = np
  $$
- Variance:  
  $$
  \sigma^2 = np(1 - p)
  $$

---

### 3. **Poisson Distribution**

- PMF:  
  $$
  P(X = k) = \frac{\lambda^k e^{-\lambda}}{k!}, \quad k = 0, 1, 2, ...
  $$
- Mean:  
  $$
  \mu = \lambda
  $$
- Variance:  
  $$
  \sigma^2 = \lambda
  $$

---

### 4. **Uniform Distribution (Continuous)**

- PDF:  
  $$
  f(x) = \frac{1}{b - a}, \quad a \leq x \leq b
  $$
- Mean:  
  $$
  \mu = \frac{a + b}{2}
  $$
- Variance:  
  $$
  \sigma^2 = \frac{(b - a)^2}{12}
  $$

---

### 5. **Normal Distribution**

- PDF:  
  $$
  f(x) = \frac{1}{\sqrt{2 \pi \sigma^2}} \, \exp\left( -\frac{(x - \mu)^2}{2 \sigma^2} \right)
  $$
- Standard Normal Variable:  
  $$
  Z = \frac{X - \mu}{\sigma}
  $$

---

### 6. **Exponential Distribution**

- PDF:  
  $$
  f(x) = \lambda e^{-\lambda x}, \quad x \geq 0
  $$
- Mean:  
  $$
  \mu = \frac{1}{\lambda}
  $$
- Variance:  
  $$
  \sigma^2 = \frac{1}{\lambda^2}
  $$

---

## XI. Covariance and Correlation

- Covariance:  
  $$
  \text{Cov}(X, Y) = E[(X - \mu_X)(Y - \mu_Y)] = E[XY] - E[X]E[Y]
  $$

- Correlation Coefficient:  
  $$
  \rho_{XY} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}
  $$

- Range:  
  $$
  -1 \leq \rho_{XY} \leq 1
  $$

---

## XII. Law of Large Numbers & Central Limit Theorem

- **Law of Large Numbers (LLN):**  
  As \( n \to \infty \), the sample mean converges to the population mean.

- **Central Limit Theorem (CLT):**  
  For large \( n \), the distribution of the sample mean \( \bar{X} \) tends to:  
  $$
  \bar{X} \sim N\left( \mu, \frac{\sigma^2}{n} \right)
  $$

---

## XIII. Hypothesis Testing

- **Null Hypothesis**: \( H_0 \)  
- **Alternative Hypothesis**: \( H_1 \)  
- Use a test statistic and compare with critical values or compute p-value.  
- **Significance Level**:  
  $$
  \alpha = P(\text{Type I error})
  $$

---

## XIV. Confidence Intervals

- **Known \( \sigma \):**  
  $$
  \bar{X} \pm Z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}
  $$

- **Unknown \( \sigma \):**  
  $$
  \bar{X} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}
  $$

---

## XV. Moment Generating Function (MGF)

- Definition:  
  $$
  M_X(t) = E[e^{tX}]
  $$

- Moments:  
  - First Moment (mean):  
    $$
    M'_X(0) = E[X]
    $$
  - Second Moment:  
    $$
    M''_X(0) = E[X^2]
    $$

---

## XVI. Chebyshev's Inequality

- For any \( k > 0 \):  
  $$
  P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}
  $$

---

