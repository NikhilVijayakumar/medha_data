# Histogram Equalisation for Image Enhancement

## Core Concept

Histogram equalisation is a technique to enhance image contrast by redistributing intensity values to achieve a more uniform distribution across the available grey levels. The goal is to transform the input image so its output histogram approximates a uniform distribution.

## Key Definitions and Principles

* **Histogram of a digital image:** A discrete function $p(r_k) = \frac{n_k}{n}$, where $r_k$ is the grey value, $n_k$ is the number of pixels with that grey value, and $n$ is the total number of pixels.
    * "The histogram of a digital image with gray values $(r_0, r_1, ..., r_{L-1})$ is the discrete function $(p(r_k) = \frac{n_k}{n})$."
    * "Histogram provides a global description of the appearance of the image."
    * "$(p(r_k) \approx P(R = r_k))$" - Histogram approximates the probability density.
* **Contrast Enhancement:** The histogram's shape indicates contrast characteristics (dark, bright, low/high contrast).
* **Transformation Function (T(r)):** A function $s = T(r)$ that maps input grey values $r$ to new output grey values $s$ in the range $[0, 1]$ (for normalised values).
    * **Conditions for $T(r)$:**
        * Monotonically increasing for $0 \leq r \leq 1$ (preserves grey value order).
        * Maps $[0, 1]$ into $[0, 1]$ (preserves the range).
    * The inverse transformation $r = T^{-1}(s)$ is also assumed to satisfy these conditions.
* **Probability Density Functions:** Input $p_{in}(r)$ and output $p_{out}(s)$ images have probability density functions related by:
    * "$(p_{out}(s) = p_{in}(r) \left| \frac{dr}{ds} \right|_{r = T^{-1}(s)})$"
* **Uniform Distribution Goal:** Design $T(r)$ so that output grey values are uniformly distributed in $[0, 1]$, meaning $p_{out}(s) = 1$ for $0 \leq s \leq 1$.
    * "The histogram equalization is an approach to enhance a given image. The approach is to design a transformation $T(.)$ such that the gray values in the output is uniformly distributed in $[0, 1]$."
    * "In terms of histograms, the output image will have all gray values in “equal proportion” ."

## Mathematical Formulation

* **Continuous Grey Values:** The transformation function for a uniform output histogram is the Cumulative Distribution Function (CDF) of the input grey values:
    * "$(s = T(r) = \int_{0}^{r} p_{in}(w) dw)$"
    * Differentiating with respect to $r$: " $(\frac{ds}{dr} = p_{in}(r))$"
    * Substituting into the PDF relationship confirms $p_{out}(s) = 1$.

## Discrete Implementation Steps

For digital images with discrete grey values (0 to $L-1$):

1.  **Compute the probability of occurrence of each grey level:**
    * "$(p_{in}(r_k) = \frac{n_k}{n}), (0 \leq k \leq L-1)$"
2.  **Compute the discrete version of the transformation function (CDF):**
    * "$(s_k = T(r_k) = \sum_{j=0}^{k} p_{in}(r_j) = \sum_{j=0}^{k} \frac{n_j}{n}), (0 \leq k \leq L-1)$"
3.  Scale the resulting $s_k$ values back to the original grey level range (e.g., multiply by $(L-1)$ and round to the nearest integer).
    * Example table illustrates: "rk nk P(rk)=nk/n CDF CDF*(L-1) Rounding"

## Illustrative Example

* A detailed example with an 8-level (L=8) 64x64 image demonstrates the calculation of probability of occurrence, CDF, and rounded output grey levels, showing mapping of input to a smaller set of distinct output levels.
* Visual comparison of histograms before and after equalisation shows the output histogram is approximately uniform.

## Results and Comments

* "Note that the histogram of output image is only approximately, and not exactly, uniform. This should not be surprising, since there is no result that claims uniformity in the discrete case."

## Limitations

* May not always produce desirable results, especially with very narrow input histograms.
* Can introduce false edges and regions.
* Can increase image "graininess" and "patchiness."

# Formulas

# Histogram Equalisation Formulas

This section compiles the key formulas related to histogram equalisation presented in the provided sources.

## 1. Probability of a Gray Value

* **Formula:**
    $\qquad p(r_k) = \frac{n_k}{n}$
* **Description:** Defines the probability of occurrence of a specific gray value $r_k$ in an image, where $n_k$ is the number of pixels with that gray value, and $n$ is the total number of pixels in the image.

## 2. Histogram as Probability Density Approximation

* **Approximation:**
    $\qquad p(R = r_k) \approx p(r_k)$
* **Description:** Indicates that the image histogram $p(r_k)$ provides an approximation of the probability density of the random variable $R$, which represents the gray values in the image.

## 3. Gray Value Transformation

* **Transformation Function:**
    $\qquad s = T(r)$
* **Description:** Represents a transformation where an input gray value $r$ is mapped to a new output gray value $s$ using a transformation function $T$.

## 4. Inverse Transformation

* **Inverse Function:**
    $\qquad r = T^{-1}(s)$
* **Description:** Denotes the inverse of the transformation function $T(r)$, allowing the mapping back from the output gray value $s$ to the original input gray value $r$.

## 5. Relationship between Input and Output Probability Density Functions (Continuous)

* **Formula:**
    $\qquad p_{out}(s) \left| \frac{ds}{dr} \right| = p_{in}(r)$
* **Alternative Forms:**
    $\qquad p_{out}(s) = p_{in}(r) \left| \frac{dr}{ds} \right|$
    $\qquad p_{out}(s) = p_{in}(T^{-1}(s)) \left| \frac{dT^{-1}(s)}{ds} \right|$
    $\qquad p_{out}(s) = \frac{p_{in}(T^{-1}(s))}{\left| T'(r) \right|}$
* **Description:** This formula from probability theory establishes the relationship between the probability density function of the output image $p_{out}(s)$ and the probability density function of the input image $p_{in}(r)$ through the transformation function $T(r)$ and its derivative.

## 6. Desired Uniform Output Probability Density Function (Continuous)

* **Uniform PDF:**
    $\qquad p_{out}(s) = 1, \quad \text{for } 0 \leq s \leq 1$
* **Description:** Defines the target uniform probability density function for the output image after histogram equalisation in the continuous gray value domain.

## 7. Transformation Function using CDF (Continuous)

* **Formula:**
    $\qquad T(r) = \int_{0}^{r} p_{in}(w) dw, \quad \text{for } 0 \leq r \leq 1$
* **Description:** This formula defines the transformation function $T(r)$ for continuous gray values as the cumulative distribution function (CDF) of the input gray values $p_{in}(r)$.

## 8. Derivative of the Transformation Function

* **Derivative:**
    $\qquad \frac{ds}{dr} = p_{in}(r)$
* **Description:** This is derived from the previous equation using the fundamental theorem of calculus, showing that the derivative of the transformation function is equal to the probability density function of the input gray values.

## 9. Proof of Uniform Output PDF using CDF Transformation

* **Derivation:**
    $\qquad p_{out}(s) = p_{in}(T^{-1}(s)) \left| \frac{dT^{-1}(s)}{ds} \right| = p_{in}(r) \left| \frac{1}{ds/dr} \right| = p_{in}(r) \left| \frac{1}{p_{in}(r)} \right| = 1, \quad \text{for } 0 \leq s \leq 1$
* **Description:** This demonstrates how using the CDF as the transformation function $T(r)$ results in a uniform output probability density function $p_{out}(s)$.

## 10. Discrete Histogram Equalisation Transformation

* **Formula:**
    $\qquad s_k = T(r_k) = \sum_{j=0}^{k} p_{in}(r_j) = \sum_{j=0}^{k} \frac{n_j}{n}, \quad \text{for } 0 \leq k \leq L-1$
* **Description:** This is the discrete version of the histogram equalisation transformation. The output gray level $s_k$ for an input gray level $r_k$ is calculated as the cumulative sum of the probabilities of all input gray levels from 0 up to $r_k$.

## 11. Reiterated Discrete Transformation Formula

* **Formula:**
    $\qquad s_k = \sum_{j=0}^{k} p_{in}(r_j)$
* **Description:** A reiterated, more concise form of the discrete histogram equalisation transformation formula.