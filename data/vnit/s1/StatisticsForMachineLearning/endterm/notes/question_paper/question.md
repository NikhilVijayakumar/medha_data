## Visvesvaraya National Institute of Technology, Nagpur
## Department of Electronics and Communication Engineering
### M.Tech. (AAI) Sem-1, Cohort 2
### End-Sem, Dec 2024
### Statistics for Machine Learning

**Time:** 03 Hours
**Marks:** 50

**Important Instructions:**
* For any queries, feel free to contact the instructor/invigilator immediately.
* Appropriate credits would be given for precision, and elaborate explanation.
* Assume suitable data wherever necessary.
* Each question carries equal marks.

---

**1.** A company runs two independent recommendation systems to suggest movies to users.[4, 5] The first system ($S_1$) suggests action movies, while the second system ($S_2$) suggests comedies. Each system tracks whether a user engages with its recommendations (e.g., watches a recommended movie).[6] The engagement probability for $S_1$ is $p_1 = 0.6$ and for $S_2$ is $p_2 = 0.7$.[7] Over the course of a day:
    * $S_1$ makes $n_1 = 4$ recommendations to a user.
    * $S_2$ makes $n_2 = 3$ recommendations to the same user.

Let X denote the number of engagements with $S_1$ recommendations and Y denote the number of engagements with $S_2$ recommendations.
1.  What is the joint probability $P(X=2, Y=1)$, representing the likelihood that the user engages with 2 recommendations from $S_1$ and 1 from $S_2$?
2.  Compute the expected number of engagements $E[X]$ and $E[Y]$ for $S_1$ and $S_2$.
3.  Determine whether the number of engagements with $S_1$ and $S_2$ recommendations (X and Y) are independent.
4.  If the total user engagement across both systems is $Z=X+Y$, what are the expected total engagements $E[Z]$ and the variance Var(Z)?

---

**2.** A machine learning engineer is analyzing the daily sales of a product $(X_t)$ over time t. The sales data is modeled as:
    $X_t = 10 + Y_t + N_t$
    where:
    * 10 is the baseline average daily sales
    * $Y_t = 3 \cos(2\pi f_0 t)$ models the seasonality component with frequency $f_0 = \frac{1}{7}$ (weekly pattern) and amplitude 3.
    * $\{N_t\}$ represents i.i.d. Gaussian noise with mean 0 and variance $\sigma^2 = 2$.

1.  Is the process $\{X_t\}$ stationary in the strict or wide-sense?
2.  Compute the mean and autocovariance function of $\{X_t\}$.
3.  What do you mean by the power spectral density (PSD)? If the noise sequence $N_t$ is i.i.d. and independent of $Y_t$, compute the PSD of $\{X_t\}$.

---

**3.** A data scientist is working on predicting the average daily sales $(\mu)$ of a product for a machine learning model. The daily sales data is assumed to follow a normal distribution. The data scientist collects a sample of $n=10$ days of sales data, which are independent and identically distributed (i.i.d.) with $X_i \sim N(\mu, \sigma^2=4)$.[18] The observed sales data is:
    $X = \{5.2, 4.8, 5.4, 4.9, 5.1, 5.0, 4.7, 5.3, 5.0, 4.9\}$.

1.  Compute the sample mean $\overline{X}$, which serves as an estimate of the average daily sales ($\mu$).
2.  Calculate the mean squared error (MSE) of $\overline{X}$ as an estimator of $\mu$.
3.  Explain why $\overline{X}$ is a consistent estimator of $\mu$.
4.  Construct a 95% confidence interval for the average daily sales ($\mu$) using the sample data.

---

**4.** A machine learning engineer is working with two feature vectors:
    $v_1 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ $v_2 = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$

These vectors are not orthogonal.[20] To preprocess the feature set for a machine learning model, the engineer performs the following steps:
1.  Apply Gram-Schmidt orthogonalization to the feature vectors to obtain orthogonal vectors $u_1$ and $u_2$.
2.  Normalize the orthogonal vectors to create an orthonormal basis.
3.  Represent the original vectors $v_1$ and $v_2$ in terms of the orthonormal basis.
4.  Compute the determinant of the transformation matrix from the original feature set to the orthonormal basis.
5.  Discuss the significance of the orthonormal basis and determinant in the context of linear independence, basis transformation, and feature engineering in machine learning.

---

**5.** A data analyst is working with a $2 \times 2$ covariance matrix:
    $A = \begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}$

The analyst needs to perform eigenvalue decomposition to understand the matrix's properties and apply it to data transformation.
1.  Find the eigenvalues of the matrix A.
2.  Find the eigenvectors corresponding to the eigenvalues.
3.  Perform eigenvalue decomposition: represent A in the form $A = Q\Lambda Q^\top$ where:
    * $\Lambda$ is the diagonal matrix of eigenvalues.
    * Q is the orthogonal matrix of eigenvectors.
4.  Explain how eigenvalue decomposition can be used for dimensionality reduction in machine learning.

**End of exam**