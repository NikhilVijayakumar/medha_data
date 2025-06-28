Here's the well-formatted Markdown document, with LaTeX for mathematical formulas, based on the provided "Solution to Mid Sem Exam Apr 2025.pdf" content.

---

# Solution to Mid-Semester Exam - April 2025

This document presents the solutions to the mid-semester examination questions from April 2025.

---

## Question 1

Given the probability density function (PDF):
[cite_start]$f_x(x) = \frac{C}{x^2+1}$, for $-\infty < x < \infty$ [cite: 1]

### a) To find the value of $C$

We use the property that the integral of a PDF over its entire domain must equal 1:
[cite_start]$$\int_{-\infty}^{\infty} f_x(x)dx = 1$$ [cite: 1]
Substituting the given PDF:
[cite_start]$$\int_{-\infty}^{\infty} \frac{C}{x^2+1}dx = 1$$ [cite: 1]
Integrating, we get:
[cite_start]$$C \left[ \tan^{-1}x \right]_{-\infty}^{\infty} = 1$$[cite: 1][cite_start]$$C \left[ \tan^{-1}(\infty) - \tan^{-1}(-\infty) \right] = 1$$[cite: 1][cite_start]$$C \left[ \frac{\pi}{2} - \left(-\frac{\pi}{2}\right) \right] = C\pi = 1$$ [cite: 1]
Therefore, the value of $C$ is:
[cite_start]$$C = \frac{1}{\pi}$$ [cite: 1]

### b) To find $P_r \left\{ \frac{1}{3} < X^2 < 1 \right\}$

[cite_start]We need to calculate $P_r \left\{ \frac{1}{3} \le X^2 \le 1 \right\}$[cite: 2]. This implies:
[cite_start]$$P_r \left\{ \frac{1}{\sqrt{3}} \le X \le 1 \right\} \quad \text{OR} \quad P_r \left\{ -1 \le X \le -\frac{1}{\sqrt{3}} \right\}$$ [cite: 2]
This can be written as the sum of two integrals:
[cite_start]$$P_r \left\{ \frac{1}{\sqrt{3}} \le X \le 1 \right\} + P_r \left\{ -1 \le X \le -\frac{1}{\sqrt{3}} \right\}$$[cite: 2][cite_start]$$= \frac{1}{\pi} \int_{1/\sqrt{3}}^{1} \frac{1}{x^2+1}dx + \frac{1}{\pi} \int_{-1}^{-1/\sqrt{3}} \frac{1}{x^2+1}dx$$ [cite: 2]
Due to the symmetry of the integrand, this simplifies to:
[cite_start]$$= \frac{2}{\pi} \left[ \tan^{-1}x \right]_{1/\sqrt{3}}^{1}$$[cite: 2][cite_start]$$= \frac{2}{\pi} \left[ \tan^{-1}(1) - \tan^{-1}\left(\frac{1}{\sqrt{3}}\right) \right]$$[cite: 2][cite_start]$$= \frac{2}{\pi} \left[ \frac{\pi}{4} - \frac{\pi}{6} \right]$$[cite: 2][cite_start]$$= \frac{2}{\pi} \left[ \frac{3\pi - 2\pi}{12} \right] = \frac{2}{\pi} \left[ \frac{\pi}{12} \right] = \frac{1}{6}$$ [cite: 2]

---

## Question 2

Given the PDF:
[cite_start]$f_x(x) = \frac{x}{C}$, for $0 < x < C$ [cite: 3]

### a) To find the value of $C$

Using the property that the integral of a PDF over its domain is 1:
[cite_start]$$\int_{0}^{C} \frac{x}{C}dx = 1$$[cite: 3][cite_start]$$\frac{1}{C} \int_{0}^{C} x dx = 1$$[cite: 3][cite_start]$$\frac{1}{C} \left[ \frac{x^2}{2} \right]_{0}^{C} = 1$$[cite: 3][cite_start]$$\frac{1}{C} \left( \frac{C^2}{2} - 0 \right) = 1$$[cite: 3][cite_start]$$\frac{C^2}{2C} = \frac{C}{2} = 1$$ [cite: 3]
[cite_start]Therefore, $C = 2$[cite: 3].

### b) To find $E[X]$

The expected value $E[X]$ is calculated as:
[cite_start]$$E[X] = \int_{0}^{C} x \cdot f_x(x)dx$$ [cite: 3]
Substitute $C=2$ and $f_x(x) = \frac{x}{2}$:
[cite_start]$$E[X] = \int_{0}^{2} x \cdot \frac{x}{2}dx$$[cite: 3][cite_start]$$E[X] = \int_{0}^{2} \frac{x^2}{2}dx$$[cite: 3][cite_start]$$E[X] = \frac{1}{2} \left[ \frac{x^3}{3} \right]_{0}^{2}$$[cite: 3][cite_start]$$E[X] = \frac{1}{2} \cdot \frac{2^3}{3} = \frac{1}{2} \cdot \frac{8}{3} = \frac{4}{3}$$ [cite: 3]

---

## Question 3

[cite_start]Consider two bags of balls[cite: 4]:
* [cite_start]**Bag 1:** 3 White (W), 2 Black (B) (Total 5 balls) [cite: 4]
* [cite_start]**Bag 2:** 4 White (W), 2 Black (B) (Total 6 balls) [cite: 4]

[cite_start]Let $W_1$ be the event of drawing a white ball from the first bag. [cite: 5]
[cite_start]Let $W_2$ be the event of drawing a white ball from the second bag. [cite: 5]

### a) Probability that both balls are white

[cite_start]$P(\text{Both are white}) = P(W_1 \cap W_2) = P(W_2|W_1)P(W_1)$ [cite: 5]
[cite_start]$P(W_1) = \frac{3}{5}$ (from Bag 1) [cite: 5]
[cite_start]$P(W_2) = \frac{4}{6}$ (from Bag 2) [cite: 5]
Since the draws are independent from two separate bags:
$P(W_1 \cap W_2) = P(W_1) \cdot P(W_2) = \frac{3}{5} \cdot \frac{4}{6} = \frac{12}{30} = \frac{2}{5}$

[cite_start]The provided solution has $P(W_2|W_1)P(W_1) = (\frac{3}{8})(\frac{4}{6}) = \frac{1}{4}$[cite: 5], which seems to use different numbers for the bags. Based on the given bag compositions:
$P(\text{Both are white}) = P(\text{White from Bag 1}) \times P(\text{White from Bag 2})$
$P(\text{Both are white}) = \frac{3}{5} \times \frac{4}{6} = \frac{12}{30} = \frac{2}{5}$

Let's use the probabilities given in the calculation if they are meant to override the initial stated bag contents:
[cite_start]$P(W_1) = \frac{4}{6}$ [cite: 5]
[cite_start]$P(W_2) = \frac{3}{8}$ [cite: 5]
$P(\text{Both are white}) = P(W_1 \cap W_2) = P(W_1) \cdot P(W_2)$ (Assuming independent draws from two bags)
[cite_start]$= (\frac{3}{8})(\frac{4}{6}) = \frac{1}{4}$ [cite: 5]

### b) Probability that one ball is white and one is black

First, calculate the probability that both are black:
$P(\text{Both are Black}) = P(B_1) \cdot P(B_2)$
[cite_start]Using probabilities from the calculation section: $P(B_1) = \frac{2}{6}$ and $P(B_2) = \frac{5}{8}$ [cite: 5]
[cite_start]$P(\text{Both are Black}) = (\frac{2}{6})(\frac{5}{8}) = \frac{10}{48} = \frac{5}{24}$ [cite: 5]

The probability that one is white and one is black is $1 - P(\text{Both are white}) - P(\text{Both are black})$:
[cite_start]$P(\text{One W & One B}) = 1 - \left( P(\text{Both are white}) + P(\text{Both are black}) \right)$ [cite: 5]
[cite_start]$P(\text{One W & One B}) = 1 - \left( \frac{1}{4} + \frac{5}{24} \right)$ [cite: 5]
[cite_start]$P(\text{One W & One B}) = 1 - \left( \frac{6}{24} + \frac{5}{24} \right) = 1 - \frac{11}{24} = \frac{13}{24}$ [cite: 5]

---

## Question 4

[cite_start]Given that 20% of items are defective. [cite: 6]
[cite_start]This means the probability of a defective item, $p = 0.2$. [cite: 6]
[cite_start]The probability of a non-defective item is $1-p = 0.8$. [cite: 6]
[cite_start]We are considering 4 items, so $n=4$. [cite: 6] This is a binomial distribution.

### a) Probability that exactly 1 item is defective

Using the binomial probability formula $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$:
[cite_start]$P(X=1) = \binom{4}{1} (0.2)^1 (0.8)^{4-1}$ [cite: 6]
[cite_start]$P(X=1) = 4 \times (0.2) \times (0.8)^3$ [cite: 6]
[cite_start]$P(X=1) = 4 \times 0.2 \times 0.512 = 0.4096$ [cite: 6]

### b) Probability that exactly 0 items are defective

[cite_start]$P(X=0) = \binom{4}{0} (0.2)^0 (0.8)^{4-0}$ [cite: 6]
[cite_start]$P(X=0) = 1 \times 1 \times (0.8)^4$ [cite: 6]
[cite_start]$P(X=0) = 0.4096$ [cite: 6]

### c) Probability that less than 2 items are defective

[cite_start]$P(X < 2) = P(X=1) + P(X=0)$ [cite: 7]
[cite_start]$P(X < 2) = 0.4096 + 0.4096$ [cite: 7]
[cite_start]$P(X < 2) = 0.8192$ [cite: 7]

---

## Question 5 (Implied from the structure)

[cite_start]Given $X \sim N(3.5, \sqrt{12})$[cite: 7]. This notation usually means $\mu = 3.5$ and $\sigma = \sqrt{12}$. However, the standard notation for variance is $\sigma^2$. The solution then uses $3\sqrt{12}$ in the denominator of the exponential, implying $\sigma^2 = 3\sqrt{12}$ or a confusion between $\sigma$ and $\sigma^2$. Let's assume the question meant $X \sim N(3.5, 12)$ where $\sigma^2 = 12$, so $\sigma = \sqrt{12}$. The subsequent calculation uses $\sqrt{3}X$.

[cite_start]Let $Y = \sqrt{3}X$[cite: 7].
For a linear transformation $Y = aX+b$, if $X \sim N(\mu, \sigma^2)$, then $Y \sim N(a\mu+b, a^2\sigma^2)$.
Here $a = \sqrt{3}$ and $b = 0$.
[cite_start]So, $Y \sim N(\sqrt{3} \times 3.5, (\sqrt{3})^2 \times 12)$ [cite: 7]
[cite_start]$Y \sim N(3.5\sqrt{3}, 3 \times 12)$ [cite: 7]
[cite_start]$Y \sim N(3.5\sqrt{3}, 36)$ [cite: 7]

The PDF of a normal distribution $Y \sim N(\mu_Y, \sigma_Y^2)$ is:
$f_Y(y) = \frac{1}{\sqrt{2\pi\sigma_Y^2}} \exp\left(-\frac{(y-\mu_Y)^2}{2\sigma_Y^2}\right)$
Substituting $\mu_Y = 3.5\sqrt{3}$ and $\sigma_Y^2 = 36$:
$f_Y(y) = \frac{1}{\sqrt{2\pi \cdot 36}} \exp\left(-\frac{(y-3.5\sqrt{3})^2}{2 \cdot 36}\right)$
$f_Y(y) = \frac{1}{\sqrt{72\pi}} \exp\left(-\frac{(y-3.5\sqrt{3})^2}{72}\right)$

[cite_start]The solution provided states $CN(\sqrt{3},3\sqrt{12})$ and $CN(\sqrt{3}\times3.5,3\sqrt{12})$[cite: 7]. There appears to be a mix-up or a specific context for the variance calculation, as it uses $3\sqrt{12}$ instead of $3 \times 12 = 36$ for variance. Assuming the notation $N(\mu, \sigma^2)$ is standard and the provided solution's variance calculation is as written:
[cite_start]$Y \sim N(\sqrt{3} \times 3.5, 3\sqrt{12})$ [cite: 7] (This implies $\sigma_Y^2 = 3\sqrt{12}$)
The PDF would then be:
[cite_start]$f_Y(y) = \frac{1}{\sqrt{2\pi (3\sqrt{12})}} \exp\left(-\frac{(y - 3.5\sqrt{3})^2}{2(3\sqrt{12})}\right)$ [cite: 7]
[cite_start]$f_Y(y) = \frac{1}{\sqrt{6\pi\sqrt{12}}} \exp\left(-\frac{(y - 3.5\sqrt{3})^2}{6\sqrt{12}}\right)$ [cite: 7]