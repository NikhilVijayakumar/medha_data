
# Sampling

## 1. Sample Mean ($\bar{x}$)

The **sample mean** ($\bar{x}$) is a statistic that represents the average of the values within a specific sample.

* **Definition:** The sample mean ($\bar{x}$) is calculated by summing all the values in a sample ($X_i$) and dividing by the sample size ($n$).
* **Formula:**
    $$\bar{x} = \frac{1}{n} \sum X_i$$
    For a particular sample with values $x_1, x_2, \ldots, x_n$, the sample mean is calculated as:
    $$\bar{x} = \frac{x_1 + x_2 + \ldots + x_n}{n}$$
* **Example:** For a sample of size $5$ with values $9, 1, 1, 6, 2$, the sample mean is:
    $$\bar{x} = \frac{(9 + 1 + 1 + 6 + 2)}{5} = \frac{19}{5} = 3.8$$

---

## 2. Population Mean ($\mu$)

The **population mean** ($\mu$) is the true average of all values within an entire population.

* **Definition:** The population mean ($\mu$) is calculated by summing all members ($x$) of the population and dividing by the total number of members in the population ($N$).
* **Formula:**
    $$\mu = \frac{\sum x}{N}$$
* **Example:** For a population consisting of five members $\{2, 3, 6, 8, 11\}$, the population mean is:
    $$\mu = \frac{(2 + 3 + 6 + 8 + 11)}{5} = \frac{30}{5} = 6$$

---

## 3. Standard Deviation of Population ($\sigma$)

The **standard deviation of the population** ($\sigma$) measures the dispersion or spread of values within an entire population around the population mean.

* **Definition:** The standard deviation of the population ($\sigma$) measures the dispersion of values around the population mean.
* **Formula:**
    $$\sigma = \sqrt{\frac{\sum(x - \mu)^2}{N}}$$
* **Example:** For the population $\{2, 3, 6, 8, 11\}$ with a population mean ($\mu$) of $6$, the standard deviation is calculated as:
    $$\sigma = \sqrt{\frac{(2-6)^2 + (3-6)^2 + (6-6)^2 + (8-6)^2 + (11-6)^2}{5}}$$
    $$\sigma = \sqrt{\frac{(-4)^2 + (-3)^2 + (0)^2 + (2)^2 + (5)^2}{5}}$$
    $$\sigma = \sqrt{\frac{(16 + 9 + 0 + 4 + 25)}{5}}$$
    $$\sigma = \sqrt{\frac{54}{5}} = \sqrt{10.8} \approx 3.286$$

---

## 4. Mean of Sampling Distribution of Means ($\mu_{\bar{x}}$)

The **mean of the sampling distribution of means** ($\mu_{\bar{x}}$) describes the average of all possible sample means that could be drawn from a population.

* **Relationship:** The mean of the sampling distribution of means ($\mu_{\bar{x}}$) is equal to the population mean ($\mu$).
* **Formula:**
    $$\mu_{\bar{x}} = \mu$$

---

# Optimization


## 1. Linear Combination for a Line Segment (Defining Convex Sets)

This formula represents any point on the straight line segment between two given points in N-dimensional space. It is fundamental to the definition of convex sets.

* **Formula:** For two N-dimensional vectors (points) $\bar{x}_1$ and $\bar{x}_2$, a point $\bar{x}$ on the line segment joining them can be represented by:
    $$\bar{x} = \theta \bar{x}_1 + (1-\theta) \bar{x}_2$$
* **Parameter $\theta$:** In this formula, $\theta$ (theta) is a scalar value constrained to the range:
    $$0 \leq \theta \leq 1$$
* **Interpretation:** This constraint on $\theta$ ensures that $\bar{x}$ lies specifically between $\bar{x}_1$ and $\bar{x}_2$.
    * If $\theta = 0$, then $\bar{x} = \bar{x}_2$.
    * If $\theta = 1$, then $\bar{x} = \bar{x}_1$.
    * For any value of $\theta$ strictly between $0$ and $1$, $\bar{x}$ is a point strictly between $\bar{x}_1$ and $\bar{x}_2$.
* **Relevance to Convex Sets:** A set $S$ is defined as a **Convex Set** if, for any two points $\bar{x}_1$ and $\bar{x}_2$ within the set (i.e., $\bar{x}_1 \in S$ and $\bar{x}_2 \in S$), the entire line segment joining them (as represented by the formula above) also belongs to the set $S$.

---

## 2. Convex Combination of Multiple Points (Defining Convex Hull)

This is a generalization of the linear combination for a line segment, extended to multiple points. It is the basis for defining the convex hull.

* **Formula:** For a general case involving $k$ points in N-dimensional space ($\bar{x}_1, \bar{x}_2, \ldots, \bar{x}_k$), a convex combination $\bar{x}$ is given by:
    $$\bar{x} = \sum_{i=1}^{k} \theta_i \bar{x}_i \quad \text{or} \quad \bar{x} = \theta_1 \bar{x}_1 + \theta_2 \bar{x}_2 + \ldots + \theta_k \bar{x}_k$$
* **Conditions for Coefficients $\theta_i$:** The coefficients $\theta_i$ (theta\_i) must satisfy two crucial conditions:
    * **Sum to One:** The sum of all coefficients must equal $1$:
        $$\sum_{i=1}^{k} \theta_i = 1$$
    * **Non-negativity:** Each coefficient must be non-negative:
        $$\theta_i \geq 0 \quad \text{for all } i$$
* **Convex Hull:** The "Convex Hull" of a set of points is defined as the set of all possible such convex combinations of those points. It is the smallest convex set containing all the given points.

---

## 3. Linear Combination for a Line (Defining Affine Sets)

This formula describes any point on the entire infinite line passing through two given points in N-dimensional space. It is fundamental to the definition of affine sets.

* **Formula:** For two N-dimensional points $\bar{x}_1$ and $\bar{x}_2$, a point $\bar{x}$ on the infinite line passing through them is given by:
    $$\bar{x} = \theta \bar{x}_1 + (1-\theta) \bar{x}_2$$
* **Parameter $\theta$:** The key difference from the line segment formula is that $\theta$ (theta) can be any real number:
    $$\theta \in \mathbb{R}$$
* **Relevance to Affine Sets:** An **Affine Set** $S$ is defined such that if any two points $\bar{x}_1$ and $\bar{x}_2$ lie in $S$ (i.e., $\bar{x}_1 \in S$ and $\bar{x}_2 \in S$), then the entire infinite line passing through them (as described by the formula above for all $\theta \in \mathbb{R}$) is also contained in the set $S$.

---

## 4. Equation of a Hyperplane (Defining Half-spaces)

A hyperplane is a fundamental geometric object in N-dimensional space that serves as the boundary for half-spaces.

* **Formula:** In N-dimensional space, the equation that represents a **hyperplane** is given by:
    $$a^T \bar{x} = b$$
* **Components:**
    * $\mathbf{a}$: A non-zero N-dimensional vector (representing the normal vector to the hyperplane).
    * $\bar{x}$: An N-dimensional vector representing any point on the hyperplane.
    * $b$: A scalar constant.
* **Role in Defining Half-spaces:** This equation defines the boundary for **half-spaces**, which are regions formed by dividing the entire N-dimensional space. A half-space itself is defined by a linear inequality, such as $a^T \bar{x} \leq b$ or $a^T \bar{x} \geq b$. While half-spaces are always convex, they are generally not affine.

---

#Extra Linear algebra

Here's the well-formatted Markdown documentation for the provided Linear Algebra formulas, with mathematical expressions rendered using LaTeX:

---

# Essential Linear Algebra Formulas

This document compiles key formulas from linear algebra, covering vector projections, norms, orthogonality, the null space, matrix trace, Hermitian matrix properties, and Eigenvalue Decomposition.

---

## 1. Projection and Component of Vectors

These formulas describe how to find the extent to which one vector aligns with another.

* **Component of a vector $\bar{v}$ on a vector $\bar{w}$ (Scalar Projection):** This formula gives the scalar length of the projection of $\bar{v}$ onto $\bar{w}$, indicating how much of $\bar{v}$ lies in the direction of $\bar{w}$.
    $$\text{component} = \frac{\bar{v}^T \bar{w}}{||\bar{w}||}$$
    This can also be written as $\frac{\bar{v} \cdot \bar{w}}{||\bar{w}||}$.

* **Projection of $\bar{v}$ on $\bar{w}$ (Vector Projection):** This formula gives the vector component of $\bar{v}$ that lies along the direction of $\bar{w}$.
    $$\text{projection} = \left(\frac{\bar{v}^T \bar{w}}{||\bar{w}||^2}\right) \bar{w}$$
    Alternatively, if $\bar{w}$ is a unit vector ($||\bar{w}|| = 1$), the projection simplifies to:
    $$\text{projection} = (\bar{v}^T \bar{w}) \bar{w}$$

---

## 2. Norm of a Vector

The norm (or magnitude) of a vector represents its length in N-dimensional space.

* **Formula:** For a vector $\bar{w} = [w_1, w_2, \ldots, w_n]^T$, its norm $||\bar{w}||$ is calculated as the square root of the sum of the squares of its components:
    $$||\bar{w}|| = \sqrt{w_1^2 + w_2^2 + \ldots + w_n^2}$$
* **Examples:**
    * For $\bar{w} = [2, 4, 2]^T$:
        $$||\bar{w}|| = \sqrt{2^2 + 4^2 + 2^2} = \sqrt{4 + 16 + 4} = \sqrt{24}$$
    * For $\bar{w} = [5, 1, 9]^T$:
        $$||\bar{w}|| = \sqrt{5^2 + 1^2 + 9^2} = \sqrt{25 + 1 + 81} = \sqrt{107}$$
* **Unit Norm Vector:** A vector is a **unit norm vector** if its norm is equal to $1$. Unit norm vectors are often obtained by normalizing other vectors, for example, by dividing eigenvectors by their norm.

---

## 3. Orthogonal Vectors

Orthogonal vectors are vectors that are perpendicular to each other.

* **Condition for Orthogonality:** Two vectors $\bar{w}_1$ and $\bar{w}_2$ are orthogonal to each other if their **dot product** is zero:
    $$\bar{w}_1^T \bar{w}_2 = 0 \quad \text{or} \quad \bar{w}_1 \cdot \bar{w}_2 = 0$$
* **Unit Norm and Orthogonal:** If $\bar{w}_1$ and $\bar{w}_2$ are both unit norm and orthogonal, then their dot product is still zero, as per the definition.

---

## 4. Null Space of a Matrix ($N(A)$)

The null space of a matrix consists of all vectors that are mapped to the zero vector by the matrix transformation.

* **Defining Condition:** The null space of a matrix $A$, denoted as $N(A)$, comprises all vectors $\bar{x}$ such that when multiplied by $A$, they result in the zero vector:
    $$A \bar{x} = \mathbf{0}$$
    where $\mathbf{0}$ is the zero vector.
* **Property:** If $\bar{x} \in N(A)$, then any linear combination of vectors in $N(A)$ will also belong to $N(A)$, meaning the null space is a vector subspace.
* **Example Calculation for $A = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$:** To find $\bar{x} = \begin{pmatrix} x_1 \\ x_2 \end{pmatrix}$ such that $A\bar{x} = \mathbf{0}$:
    $$\begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
    This leads to the condition $x_1 + 2x_2 = 0$ (after row reduction).

---

## 5. Trace of a Matrix

The trace is a property of square matrices that is the sum of its diagonal elements.

* **Definition:** The trace of a square matrix $A$, denoted as $\text{Tr}(A)$, is the sum of its diagonal elements:
    $$\text{Tr}(A) = \sum_{i=1}^{n} A_{ii}$$
* **Property:** For two conformable matrices $A$ and $B$, the trace of their product is commutative:
    $$\text{Tr}(AB) = \text{Tr}(BA)$$

---

## 6. Hermitian Symmetric Matrix Properties

Hermitian symmetric matrices (which are real symmetric matrices in the context of real numbers) possess crucial properties related to their eigenvalues and eigenvectors.

* **Definition:** A matrix $A$ is **Hermitian symmetric** if it is equal to its own conjugate transpose ($A = A^*$). For real matrices, this simplifies to being symmetric ($A = A^T$).
* **Eigenvalue Property:** Eigenvalues of a Hermitian matrix are always **real numbers**.
* **Eigenvector Property:** Eigenvectors of a Hermitian symmetric matrix corresponding to **distinct eigenvalues** are **orthogonal** to each other.

---

## 7. Eigenvalue Decomposition (EVD)

EVD is a factorization of a square matrix into a set of its eigenvectors and eigenvalues, providing insights into the matrix's behavior.

* **Defining Equation for Eigenvectors and Eigenvalues:** The relationship between a matrix $A$, its eigenvector $\bar{v}$, and corresponding eigenvalue $\lambda$ is:
    $$A \bar{v} = \lambda \bar{v}$$
* **EVD Formula for a Hermitian Symmetric Matrix $A \in \mathbb{R}^{n \times n}$:**
    $$A = V \Lambda V^T$$
    Here:
    * $V$: Is a matrix whose columns are the **eigenvectors** of $A$. If these eigenvectors are normalized to unit length, then $V$ is an **orthogonal matrix** (meaning $V^T V = I$, where $I$ is the identity matrix, and thus $V^{-1} = V^T$).
    * $\Lambda$: Is a **diagonal matrix** whose diagonal elements are the corresponding **eigenvalues** of $A$. The form is:
        $$\Lambda = \begin{pmatrix} \lambda_1 & 0 & \ldots & 0 \\ 0 & \lambda_2 & \ldots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ldots & \lambda_n \end{pmatrix}$$
* **Derivation (Demonstration):** The EVD can be demonstrated by starting from the eigenvalue definition for multiple eigenvectors arranged as columns in $V$:
    $$A V = V \Lambda$$
    Multiplying both sides by $V^T$ (from the right, utilizing $V^T V = I$ for orthogonal $V$):
    $$A V V^T = V \Lambda V^T$$   $$A I = V \Lambda V^T$$   $$A = V \Lambda V^T$$
    This representation is specifically valid and particularly useful for Hermitian (or real symmetric) matrices due to their orthogonal eigenvectors.

---

# Matrices and Linear Algebra

Here's the well-formatted Markdown documentation for the provided Linear Algebra concepts, with mathematical expressions rendered using LaTeX:

---

# Core Concepts in Matrices and Linear Algebra

This document outlines fundamental definitions, properties, and relationships within matrix algebra and linear algebra.

---

## 1. Matrix Dimensions and Equality

These foundational concepts define the size and conditions for identity between matrices.

* **Matrix Dimensions/Order:** If a matrix $A$ has $m$ rows and $n$ columns, its dimensions, size, or order is given by $m \times n$.
    * **Notation:** $A_{m \times n}$

* **Matrix Equality:** Two matrices, $A$ and $B$, are equal if and only if $a_{ij} = b_{ij}$ for all $i$ and $j$, and they must have the same dimensions ($m \times n$).

---

## 2. Matrix Multiplication Conditions

Matrix multiplication has specific rules regarding the dimensions of the matrices involved.

* **Condition for Matrix Multiplication:** For two matrices $A_{m \times n}$ and $B_{n \times p}$, their multiplication $AB$ is possible only if the number of columns of $A$ ($n$) equals the number of rows of $B$ ($n$). The resulting matrix $C$ will have dimensions $m \times p$.

---

## 3. Properties of Matrix Transpose

The transpose operation provides a way to transform a matrix by interchanging its rows and columns.

* **Properties:**
    * $(A^T)^T = A$
    * $(kA)^T = kA^T$ (where $k$ is a scalar)
    * $(A + B)^T = A^T + B^T$
    * $(AB)^T = B^T A^T$

---

## 4. Definitions of Special Matrices

Certain matrices possess unique structures and properties that give them special roles in linear algebra.

* **Symmetric Matrix:** A square matrix $A$ is **symmetric** if $A = A^T$.
* **Skew-Symmetric Matrix:** A square matrix $A$ is **skew-symmetric** if $A^T = -A$. Diagonal elements of a skew-symmetric matrix are always zero.
* **Inverse of a Matrix:** A square matrix $A$ is said to have an **inverse matrix** $B$ (denoted $A^{-1}$) if their product yields the identity matrix, such that $AB = I$ and $BA = I$. The inverse, if it exists, is unique.

---

## 5. Property of Matrix Inverse

The inverse operation also follows specific rules for products of matrices.

* **Property of Matrix Inverse:**
    * $(AB)^{-1} = B^{-1}A^{-1}$

---

## 6. N-Dimensional Vector Representation and Norm

Vectors are fundamental elements in linear algebra, representing points or directions in space, and their "length" is defined by their norm.

* **N-Dimensional Vector Representation:** An $n$-dimensional vector $\bar{x}$ can be represented as a column matrix:
    $$\bar{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$$
* **Norm (Magnitude or Length) of a Vector:** For an $n$-dimensional vector $\bar{x} = [x_1, x_2, \ldots, x_n]^T$, its norm, denoted as $||\bar{x}||$, is calculated as:
    $$||\bar{x}|| = \sqrt{x_1^2 + x_2^2 + \ldots + x_n^2}$$
    This can also be written using summation notation:
    $$||\bar{x}|| = \sqrt{\sum_{i=1}^{n} x_i^2}$$
    * The square of the norm is:
        $$||\bar{x}||^2 = x_1^2 + x_2^2 + \ldots + x_n^2$$
    * A **unit norm vector** is a vector $\bar{x}$ for which $||\bar{x}|| = 1$.
    * **Example 1:** For $\bar{x} = [2, 3, 1]^T$, its norm is:
        $$||\bar{x}|| = \sqrt{2^2 + 3^2 + 1^2} = \sqrt{4 + 9 + 1} = \sqrt{14}$$
    * **Example 2:** For an $n$-dimensional vector with all elements being $1$ (e.g., $\bar{x} = [1, 1, \ldots, 1]^T$), its norm is:
        $$||\bar{x}|| = \sqrt{1^2 + 1^2 + \ldots + 1^2} = \sqrt{n}$$
        Its unit norm vector would be $\frac{1}{\sqrt{n}}\bar{x}$.

---

## 7. Linear Independence and Dependence of Vectors

These concepts define whether a set of vectors contains redundant information in terms of direction.

* **Linearly Independent Vectors:** A set of $m$ vectors $\bar{w}_1, \bar{w}_2, \ldots, \bar{w}_m$ are **linearly independent** if their linear combination summing to the zero vector implies that all coefficients must be zero:
    $$\text{If } c_1\bar{w}_1 + c_2\bar{w}_2 + \ldots + c_m\bar{w}_m = \mathbf{0}, \text{ then } c_1 = c_2 = \ldots = c_m = 0$$
* **Linearly Dependent Vectors:** A set of $m$ vectors $\bar{w}_1, \bar{w}_2, \ldots, \bar{w}_m$ are **linearly dependent** if their linear combination can sum to the zero vector for which not all coefficients $c_i$ are zero.
    * **Example:** For $\bar{w}_1 = [1, 2]^T$ and $\bar{w}_2 = [-2, -4]^T$, the linear combination $2\bar{w}_1 + 1\bar{w}_2 = 2\begin{pmatrix} 1 \\ 2 \end{pmatrix} + 1\begin{pmatrix} -2 \\ -4 \end{pmatrix} = \begin{pmatrix} 2 \\ 4 \end{pmatrix} + \begin{pmatrix} -2 \\ -4 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$. Since coefficients $c_1=2$ and $c_2=1$ are not all zero, these vectors are linearly dependent.

---

## 8. Rank of a Matrix

The rank of a matrix quantifies the effective dimensionality of the space spanned by its rows or columns.

* **Definition:** The **rank** of any matrix $A$ is defined as the maximum number of linearly independent rows or columns in $A$.
* **Property:** For an $m \times n$ matrix, the rank is always less than or equal to the minimum of $m$ or $n$:
    $$\text{Rank}(A) \leq \min(m, n)$$

---

## 9. Eigenvalue and Eigenvector Definition

Eigenvalues and eigenvectors are crucial for understanding how a linear transformation scales and preserves the direction of certain vectors.

* **Definition:** For a square matrix $A$, a non-zero vector $\bar{x}$ is an **eigenvector** and $\lambda$ (lambda) is its corresponding **eigenvalue** if:
    $$A \bar{x} = \lambda \bar{x}$$
    Here, $\lambda$ is a scalar constant representing the eigenvalue, which indicates how much the eigenvector $\bar{x}$ is scaled by the transformation $A$.

---

## 10. Characteristic Equation (for finding Eigenvalues)

The characteristic equation is the key to calculating a matrix's eigenvalues.

* **Derivation:** To find the eigenvalues $\lambda$, the eigenvalue equation $A \bar{x} = \lambda \bar{x}$ is rearranged as $A \bar{x} - \lambda \bar{x} = \mathbf{0}$, which can be written as $(A - \lambda I) \bar{x} = \mathbf{0}$ (where $I$ is the identity matrix).
* **Condition for Non-Zero Eigenvector:** For a non-zero eigenvector $\bar{x}$ to exist, the determinant of the matrix $(A - \lambda I)$ must be zero:
    $$\text{det}(A - \lambda I) = 0$$
    Solving this polynomial equation for $\lambda$ yields the eigenvalues.
* **Singular Matrix:** A square matrix $A$ is called a **singular matrix** if its determinant is zero ($\text{det}(A) = 0$). Singular matrices do not have an inverse.

---

## 11. Properties of Symmetric Matrices

Symmetric matrices have specific, powerful properties related to their eigenvalues and eigenvectors.

* **Eigenvalue Property:** Eigenvalues of symmetric matrices (including Hermitian matrices for real entries) are always **REAL**.
* **Eigenvector Property:** Eigenvectors corresponding to **distinct eigenvalues** of a symmetric matrix are **ORTHOGONAL**.
    * **Example:** For $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, which is symmetric, its eigenvalues are $\lambda_1 = 3$ and $\lambda_2 = 1$ (both real). The corresponding eigenvectors $\bar{v}_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$ and $\bar{v}_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$ are orthogonal, as their dot product is $(1)(1) + (1)(-1) = 1 - 1 = 0$.

---

# Matrices and Linear Algebra 2

Here's a well-formatted Markdown document, complete with LaTeX for mathematical notation, summarizing the provided concepts in linear algebra and multivariate Gaussian distributions.

---

# Comprehensive Guide to Matrix and Vector Properties

This document provides a concise overview of fundamental concepts in matrix algebra, vector properties, and their applications, particularly in the context of multivariate Gaussian distributions.

---

## 1. Matrix Properties and Definitions

Understanding matrix structure and basic operations is foundational to linear algebra.

* **Matrix Dimensions/Order:** If a matrix $A$ has $m$ rows and $n$ columns, its dimensions, size, or order is given by $m \times n$.
    * **Notation:** $A_{m \times n}$

* **Matrix Equality:** Two matrices, $A$ and $B$, are equal if and only if their corresponding elements are identical ($a_{ij} = b_{ij}$ for all $i$ and $j$), and they must have the same dimensions ($m \times n$).

* **Matrix Multiplication Condition:** For two matrices $A_{m \times n}$ and $B_{n \times p}$, their product $AB$ is possible only if the number of columns of $A$ ($n$) equals the number of rows of $B$ ($n$). The resulting matrix $C$ will have dimensions $m \times p$.

* **Properties of Matrix Transpose:** The transpose of a matrix $A$, denoted $A^T$, is formed by interchanging its rows and columns.
    * $(A^T)^T = A$
    * $(kA)^T = kA^T$ (where $k$ is a scalar)
    * $(A + B)^T = A^T + B^T$
    * $(AB)^T = B^T A^T$

* **Definitions of Special Matrices:**
    * **Symmetric Matrix:** A square matrix $A$ is **symmetric** if $A = A^T$.
    * **Skew-Symmetric Matrix:** A square matrix $A$ is **skew-symmetric** if $A^T = -A$. The diagonal elements of a skew-symmetric matrix are always zero.
    * **Inverse of a Matrix:** A square matrix $A$ has an **inverse matrix** $B$ (denoted $A^{-1}$) if their product yields the identity matrix, such that $AB = I$ and $BA = I$. The inverse, if it exists, is unique.

* **Property of Matrix Inverse:**
    * $(AB)^{-1} = B^{-1}A^{-1}$

* **Trace of a Matrix:** The **trace** of a square matrix $A$ ($\text{Tr}(A)$) is the sum of its diagonal elements.
    * For two matrices $A$ and $B$, the property $\text{Tr}(AB) = \text{Tr}(BA)$ holds.

---

## 2. Positive Definite (PD) and Positive Semidefinite (PSD) Matrices

These properties are crucial in optimization, stability analysis, and probability.

* **Positive Semidefinite (PSD) Matrix:** A real square matrix $A$ is called a **PSD matrix** if $x^T A x \ge 0$ for all real vectors $x$.
    * **Condition based on eigenvalues:** If a symmetric matrix $A$ has eigenvalues $\lambda_i$ such that $\lambda_i(A) \ge 0$, then $A$ is PSD.

* **Positive Definite (PD) Matrix:** A real square matrix $A$ is called a **PD matrix** if $x^T A x > 0$ for all non-zero real vectors $x$.
    * **Condition based on eigenvalues:** If a symmetric matrix $A$ has eigenvalues $\lambda_i$ such that $\lambda_i(A) > 0$, then $A$ is PD.

---

## 3. Vector Properties and Operations

Vectors are fundamental for representing points, directions, and data in multi-dimensional spaces.

* **N-Dimensional Vector Representation:** An $n$-dimensional vector $\bar{x}$ can be represented as a column matrix:
    $$\bar{x} = \begin{bmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{bmatrix}$$

* **Norm (Magnitude or Length) of a Vector:** For an $n$-dimensional vector $\bar{x} = [x_1, x_2, \ldots, x_n]^T$, its norm, denoted as $||\bar{x}||$, is calculated as:
    $$||\bar{x}|| = \sqrt{x_1^2 + x_2^2 + \ldots + x_n^2}$$
    This can also be written as $||\bar{x}|| = \sqrt{\sum x_i^2}$.
    * The square of the norm is $||\bar{x}||^2 = x_1^2 + x_2^2 + \ldots + x_n^2$.
    * A **unit norm vector** is a vector $\bar{x}$ for which $||\bar{x}|| = 1$.

* **Properties of Norm:**
    * $||\mathbf{0}|| = 0$
    * $||\bar{w}|| = 0$ only if $\bar{w} = \mathbf{0}$
    * $||c \bar{w}|| = |c| ||\bar{w}||$ (where $c$ is a scalar)
    * **Triangle Inequality:** $||\bar{v} + \bar{w}|| \le ||\bar{v}|| + ||\bar{w}||$

* **Component of a Vector:** The component of a vector $\bar{v}$ along a vector $\bar{w}$ is given by:
    $$\text{component} = \frac{\bar{v}^T\bar{w}}{||\bar{w}||}$$

* **Projection of a Vector:** The projection of $\bar{v}$ onto $\bar{w}$ is:
    $$\text{projection} = \left(\frac{\bar{v}^T\bar{w}}{||\bar{w}||^2}\right) \bar{w}$$
    If $\bar{w}$ is a unit vector, the projection simplifies to $(\bar{v}^T\bar{w}) \bar{w}$.

* **Orthogonal Vectors:** Two vectors $\bar{w}_1$ and $\bar{w}_2$ are **orthogonal** to each other if their dot product (standard inner product) is zero: $\bar{w}_1^T\bar{w}_2 = 0$. If $\bar{w}_1$ and $\bar{w}_2$ are unit norm and orthogonal, then $\bar{w}_1^T\bar{w}_2 = 0$.
    * For unit vectors $\mathbf{i}, \mathbf{j}, \mathbf{k}$ in $x, y,$ and $z$ dimensions respectively, their dot products are: $\mathbf{i} \cdot \mathbf{j} = 0$, $\mathbf{i} \cdot \mathbf{k} = 0$, $\mathbf{j} \cdot \mathbf{k} = 0$.

* **Linear Combination for a Line Segment (Defining Convex Sets):** For two $N$-dimensional vectors (points) $\bar{x}_1$ and $\bar{x}_2$, a point $\bar{x}$ on the line segment joining them can be represented by the formula:
    $$\bar{x} = \theta\bar{x}_1 + (1-\theta)\bar{x}_2$$
    Here, $0 \le \theta \le 1$.

* **Convex Combination of Multiple Points (Defining Convex Hull):** For $k$ points ($\bar{x}_1, \bar{x}_2, \ldots, \bar{x}_k$), a **convex combination** is given by:
    $$\bar{x} = \sum_{i=1}^{k} (\theta_i \bar{x}_i) = \theta_1\bar{x}_1 + \theta_2\bar{x}_2 + \ldots + \theta_k\bar{x}_k$$
    Here, the coefficients $\theta_i$ must satisfy:
    * $\sum_{i=1}^{k} \theta_i = 1$
    * $\theta_i \ge 0$ for all $i$.

* **Linear Combination for a Line (Defining Affine Sets):** The linear combination of two $N$-dimensional points $\bar{x}_1$ and $\bar{x}_2$ defines the entire infinite line passing through them:
    $$\bar{x} = \theta\bar{x}_1 + (1-\theta)\bar{x}_2$$
    The key difference here is that $\theta \in \mathbb{R}$ (theta can be any real number).

* **Equation of a Hyperplane (Defining Half-spaces):** In $N$-dimensional space, the equation that represents a **hyperplane** is given by:
    $$\mathbf{a}^T\mathbf{x} = b$$
    Where $\mathbf{a}$ is a non-zero $N$-dimensional normal vector, $\mathbf{x}$ is an $N$-dimensional vector representing a point on the hyperplane, and $b$ is a scalar.

---

## 4. Inner Product

The inner product extends the concept of dot product to more general vector spaces, allowing for definitions of angle and length.

* **Properties of Inner Product:** For vectors $\bar{u}, \bar{v}, \bar{w}$ and scalars $a, b$:
    * **Linearity:** $\langle a \bar{u} + b \bar{v}, \bar{w} \rangle = a\langle \bar{u}, \bar{w} \rangle + b\langle \bar{v}, \bar{w} \rangle$
    * **Symmetry:** $\langle \bar{u}, \bar{v} \rangle = \langle \bar{v}, \bar{u} \rangle$ (for real vector spaces; for complex, it's conjugate symmetry)
    * **Positive Definiteness:** $\langle \bar{w}, \bar{w} \rangle \ge 0$ for any $\bar{w}$, and $\langle \bar{w}, \bar{w} \rangle = 0$ if and only if $\bar{w} = \mathbf{0}$.

* **Standard Dot Product (Standard Inner Product):** The standard dot product of two vectors $\bar{u}$ and $\bar{w}$ is defined as: $\bar{u}^T\bar{w}$. When applied to a vector with itself, it is $\bar{w}^T\bar{w} = ||\bar{w}||^2$. This standard dot product satisfies all three properties of an inner product.

* **General Valid Inner Product Assignment:** An assignment of the following type on $\mathbb{R}^n$ can be a valid inner product: $\langle \bar{x}, \bar{y} \rangle = \bar{x}^T A \bar{y}$. For this to be a valid inner product, matrix $A$ must be a **symmetric positive definite (SPD) matrix**.

---

## 5. Linear Independence and Rank

These concepts describe the inherent structure and dimensionality of vector spaces and matrices.

* **Linearly Independent Vectors:** A set of $m$ vectors $\bar{w}_1, \bar{w}_2, \ldots, \bar{w}_m$ are **linearly independent** if their linear combination summing to the zero vector implies that all coefficients must be zero: If $c_1\bar{w}_1 + c_2\bar{w}_2 + \ldots + c_m\bar{w}_m = \mathbf{0}$, then $c_1 = c_2 = \ldots = c_m = 0$.

* **Linearly Dependent Vectors:** A set of $m$ vectors $\bar{w}_1, \bar{w}_2, \ldots, \bar{w}_m$ are **linearly dependent** if their linear combination can sum to the zero vector for which not all coefficients $c_i$ are zero.

* **Rank of a Matrix:** The **rank** of any matrix $A$ is defined as the maximum number of linearly independent rows or columns in $A$. For an $m \times n$ matrix, the rank is always less than or equal to the minimum of $m$ or $n$: $\text{Rank}(A) \le \min(m, n)$.

---

## 6. Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors reveal the intrinsic scaling and directional properties of linear transformations.

* **Eigenvalue and Eigenvector Definition:** For a square matrix $A$, a non-zero vector $\bar{x}$ is an **eigenvector** and $\lambda$ (lambda) is its corresponding **eigenvalue** if:
    $$A \bar{x} = \lambda \bar{x}$$

* **Characteristic Equation (for finding Eigenvalues):** To find the eigenvalues $\lambda$, the characteristic equation is:
    $$\text{det}(A - \lambda I) = 0$$

* **Properties of Symmetric Matrices related to Eigenvalues/Eigenvectors:**
    * Eigenvalues of symmetric matrices are **REAL**.
    * Eigenvectors of a Hermitian symmetric matrix (or just symmetric for real matrices) corresponding to distinct eigenvalues are **ORTHOGONAL**.

* **Eigenvalue Decomposition (EVD):** For a symmetric matrix $A \in \mathbb{R}^{n \times n}$ (an $n \times n$ real symmetric matrix), its eigenvalue decomposition is given by:
    $$A = V \Lambda V^T$$
    Here, $V$ is a matrix whose columns are the eigenvectors of $A$, and $\Lambda$ (Lambda) is a diagonal matrix whose diagonal elements are the corresponding eigenvalues of $A$:
    $$\Lambda = \begin{pmatrix} \lambda_1 & 0 & \ldots & 0 \\ 0 & \lambda_2 & \ldots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ldots & \lambda_n \end{pmatrix}$$

---

## 7. Null Space of a Matrix

The null space helps understand the set of vectors that are mapped to the zero vector by a linear transformation.

* **Null Space of a Matrix ($\mathcal{N}(A)$):** The null space of a matrix $A$ comprises all vectors $\bar{x}$ such that when multiplied by $A$, they result in the zero vector. The defining condition for a vector $\bar{x}$ to be in the null space of $A$ is:
    $$A \bar{x} = \mathbf{0}$$

---

## 8. Multivariate Gaussian Random Variable and Covariance Matrix

These concepts are fundamental in probability and statistics for modeling multi-dimensional random phenomena.

* **Covariance Matrix Element ($\sigma_{ij}$):** For a multivariate Gaussian random variable $\bar{x}$, the elements of its covariance matrix $\Sigma$ are denoted by $\sigma_{ij}$.

* **Diagonal of Covariance Matrix:** The diagonal elements of the covariance matrix ($\sigma_{ii}$ or $\sigma_i^2$) are the **variances** of individual elements in the random vector.

* **Determinant of a Diagonal Covariance Matrix:** For a diagonal covariance matrix $R$ (where off-diagonal elements are zero, e.g., for independent components), its determinant is the product of its diagonal elements (variances):
    $$\text{det}(R) = \sigma_1^2 \sigma_2^2 \ldots \sigma_n^2 = \prod_{i=1}^{n} \sigma_i^2$$
    This implies $\text{det}(R) \neq 0$ for a non-singular diagonal matrix.

* **Inverse of a Diagonal Matrix:** The inverse of a diagonal matrix $R$ is given by replacing the main diagonal elements with their reciprocals. If $R = \text{diag}(\sigma_1^2, \sigma_2^2, \ldots, \sigma_n^2)$, then $R^{-1} = \text{diag}(1/\sigma_1^2, 1/\sigma_2^2, \ldots, 1/\sigma_n^2)$.
    $$\text{If } R = \begin{pmatrix} \sigma_1^2 & 0 & \ldots & 0 \\ 0 & \sigma_2^2 & \ldots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ldots & \sigma_n^2 \end{pmatrix} \text{ then } R^{-1} = \begin{pmatrix} 1/\sigma_1^2 & 0 & \ldots & 0 \\ 0 & 1/\sigma_2^2 & \ldots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \ldots & 1/\sigma_n^2 \end{pmatrix}$$

* **Probability Density Function (PDF) of an n-dimensional Multivariate Gaussian Random Variable:** For an $n$-dimensional vector $\bar{x}$ that is a multivariate Gaussian Random Variable with mean vector ${\mu}$ and covariance matrix $\Sigma$, its PDF is given by:
    $$f(\bar{x}) = \frac{1}{\sqrt{(2\pi)^n \text{det}(\Sigma)}} \exp\left(-\frac{1}{2}(\bar{x} - {\mu})^T \Sigma^{-1} (\bar{x} - {\mu})\right)$$
    * In a specific case where the mean ${\mu} = \mathbf{0}$ (zero vector) and $\Sigma = R$ (a diagonal covariance matrix), the PDF simplifies to:
        $$f(\bar{x}) = \frac{1}{\sqrt{(2\pi)^n \text{det}(R)}} \exp\left(-\frac{1}{2} \bar{x}^T R^{-1} \bar{x}\right)$$

---

# Matrix and Linear Algebra- Gram Schmidt

Here's the well-formatted Markdown document, with LaTeX for mathematical notation, summarizing the provided concepts related to vector norms, components, and orthogonality.

---

# Vector Properties and Orthogonality: A Briefing

This document outlines key concepts and operations related to vector norms, components, and the condition for orthogonality, as referenced in the provided source material.

---

## 1. Vector Norm and Unit Norm Vector

* **Norm of a vector:** This refers to calculating the magnitude or length of a vector, typically denoted as $||\bar{w}||$. While the source notation "YIFER" is unclear, the concept is about quantifying a vector's size.
* **Unit norm vector:** This refers to the process of **normalizing** a vector. A unit norm vector (or unit vector) is a vector divided by its norm. For a vector $\bar{w}$, its unit norm vector, often denoted $\hat{w}$, is calculated as:
    $$\hat{w} = \frac{\bar{w}}{||\bar{w}||}$$
* The condition for a unit norm vector is that its magnitude is equal to 1, implying $||\bar{w}|| = 1$.

---

## 2. Vector Component and Projection

* **Calculating the component of one vector in the direction of another:** This process involves determining how much of one vector lies along the direction of another. In the context of a vector $\bar{v}_A$ and a unit vector $\hat{v}_B$ (representing the direction of $\bar{v}_B$), the scalar component of $\bar{v}_A$ in the direction of $\hat{v}_B$ is given by their dot product: $\bar{v}_A \cdot \hat{v}_B$.
    The vector **projection** of $\bar{v}_A$ onto $\bar{v}_B$ is the vector component of $\bar{v}_A$ that lies along $\bar{v}_B$. If $\hat{v}_B$ is the unit vector in the direction of $\bar{v}_B$, the projection is:
    $$\text{proj}_{\bar{v}_B} \bar{v}_A = (\bar{v}_A \cdot \hat{v}_B)\hat{v}_B = \left(\frac{\bar{v}_A \cdot \bar{v}_B}{||\bar{v}_B||^2}\right) \bar{v}_B$$
    The source's corrupted notations like "w̅ w̅ w̅" and "$52^T \bar{w} \bar{w}$" likely refer to variations of dot products or scalar components in this context.

---

## 3. Obtaining a New Orthogonal Vector

* **Removing components:** This is a core step in processes like Gram-Schmidt orthogonalization. To obtain a new vector that is orthogonal to a reference vector, one must subtract the projection of the new vector onto the reference vector.
    For example, to find a vector $\bar{v}_{\text{new}}$ orthogonal to $\bar{w}$, given an original vector $\bar{v}$, you would subtract the projection of $\bar{v}$ onto $\bar{w}$ from $\bar{v}$:
    $$\bar{v}_{\text{new}} = \bar{v} - \text{proj}_{\bar{w}} \bar{v} = \bar{v} - \left(\frac{\bar{v} \cdot \bar{w}}{||\bar{w}||^2}\right) \bar{w}$$
    The source's references to "removing this component from the Step21 vector" and "Remove from 3 i vector its components" directly refer to this procedure.

---

## 4. Orthogonality Condition (Dot Product)

* The fundamental condition for two vectors to be **orthogonal** (or perpendicular) is that their **dot product is zero**.
    * $\bar{v}_2 \cdot \bar{w} = 0$
    * If $\bar{w}_1, \bar{w}_2, \bar{w}_3$ are orthogonal to each other, then $\bar{w}_1 \cdot \bar{w}_2 = 0$, $\bar{w}_1 \cdot \bar{w}_3 = 0$, and $\bar{w}_2 \cdot \bar{w}_3 = 0$.
    * For standard Cartesian unit vectors, $\mathbf{i} \cdot \mathbf{j} = 0$.

---

