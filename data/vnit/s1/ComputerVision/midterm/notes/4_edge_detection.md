# Edge Detection in Computer Vision

## 1. What are Edges?

* Edges are locations in an image where a significant and abrupt change in brightness occurs.
* They correspond to **object boundaries**.
* Edges are defined by pixels where **image brightness changes abruptly**.
* An edge is not a single pixel property but is determined by the **image function behavior in a neighborhood of the pixel**.
* It's a **vector variable** possessing both:
    * **Magnitude (strength):** Often related to the gradient.
    * **Direction (orientation):**
* **Core Principle:** Analyzing the relationship between a pixel and its surrounding neighbors.
    * Similar grey levels in the neighborhood $\implies$ less likely to be an edge.
    * Widely varying grey levels in the neighborhood $\implies$ potential edge point.

## 2. Edge Detection Methods and Operators

* Many methods rely on:
    * **Convolution masks**.
    * **Discrete approximations to differential operators**.
* Differential operations aim to **measure the rate of change in the image brightness function**.
* Some operators provide **orientation** information, while others only indicate the **existence** of an edge.

### 2.1. Roberts Operator

* Designed to **mark edge points only**.
* Provides **no information about edge orientation**.
* Works best with **binary images**.
* **High sensitivity to noise** due to using **few pixels** to approximate the gradient.
* **Masks ($h_1$ and $h_2$):**
    $\qquad h_1 = \begin{bmatrix} -1 & 0 \\ 0 & 1 \end{bmatrix}, \quad h_2 = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$
* **Edge Strength Formula:**
    $\qquad |I(r, c) - I(r-1, c-1)| + |I(r-1, c) - I(r, c-1)|$

### 2.2. Sobel Operator

* Aims to find edges in both **horizontal and vertical directions**.
* Combines this information into a single metric (magnitude) and also provides **direction**.
* **Masks ($h_x$ and $h_y$):**
    $\qquad h_x = \begin{bmatrix} -1 & 0 & 1 \\ -2 & 0 & 2 \\ -1 & 0 & 1 \end{bmatrix}, \quad h_y = \begin{bmatrix} -1 & -2 & -1 \\ 0 & 0 & 0 \\ 1 & 2 & 1 \end{bmatrix}$
* **Edge Magnitude Formula:**
    $\qquad \text{Edge Magnitude} = \sqrt{G_x^2 + G_y^2}$
* **Edge Direction Formula:**
    $\qquad \text{Edge Direction} = \operatorname{atan2}\left(\frac{G_y}{G_x}\right)$

### 2.3. Prewitt Operator

* Similar to the Sobel operator, looks for **horizontal and vertical edges** using convolution masks.
* Key difference lies in the **different mask coefficients**.
* **Masks ($h_x$ and $h_y$):**
    $\qquad h_x = \begin{bmatrix} -1 & 0 & 1 \\ -1 & 0 & 1 \\ -1 & 0 & 1 \end{bmatrix}, \quad h_y = \begin{bmatrix} -1 & -1 & -1 \\ 0 & 0 & 0 \\ 1 & 1 & 1 \end{bmatrix}$
* **Edge Magnitude Formula:**
    $\qquad \text{Edge Magnitude} = \sqrt{G_x^2 + G_y^2}$
* **Edge Direction Formula:**
    $\qquad \text{Edge Direction} = \operatorname{atan2}\left(\frac{G_y}{G_x}\right)$

### 2.4. Laplacian Operators

* Approximate edge magnitude using a **convolution sum**.
* Based on **2nd-order derivatives**.
* The **sign of the result (+ or -) from two adjacent pixels provides edge orientation and tells us which side of the edge is brighter**.
* **Examples of Masks:**
    * 4-neighbourhood: $\begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}$
    * 8-neighbourhood: $\begin{bmatrix} 1 & 1 & 1 \\ 1 & -8 & 1 \\ 1 & 1 & 1 \end{bmatrix}$
    * Variations: $\begin{bmatrix} 1 & 2 & 1 \\ 2 & -4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$, $\begin{bmatrix} 2 & 1 & 2 \\ 1 & -4 & 1 \\ 2 & 1 & 2 \end{bmatrix}$

## 3. Detection of Discontinuities

* Three basic types of grey level discontinuities:
    * **Points**
    * **Lines**
    * **Edges**
* Typically detected using **masks and correlation**.

### 3.1. Point Detection

* Achieved using a specific mask (conceptually: central positive weight, surrounding negative weights).
* Followed by **thresholding** the filtered image.
* Points are detected where the filtered response exceeds the threshold.

### 3.2. Line Detection

* More complex than point detection.
* Aims to identify **lines that are one pixel thick and running in a particular direction**.
* Uses specific masks to extract lines at different orientations (e.g., -45° line detector).
* Typically involves **thresholding** the filter result.

## 4. Edges and Derivatives

* Derivatives are used to find discontinuities.
* **1st derivative** indicates where an edge is (magnitude of change).
* **2nd derivative** can be used to show edge direction (sign of the change).
* **Caution:** Derivative-based edge detectors are **extremely sensitive to noise**.

## 5. Common Edge Detectors (Generalized Mask)

* A generalized 3x3 mask representation exists as a basis for common edge detection filters.
* Specific operators (Sobel, Prewitt) are instantiations of this general form with different weight values.

## 6. Edge Detection Problems and Solutions

* Common issue: **too much detail**, leading to the detection of unwanted edges (e.g., texture).
* Solution: **smooth images prior to edge detection** to reduce noise and fine details.

## 7. Laplacian Edge Detection and Laplacian of Gaussian (LoG)

* Laplacian filter is a **2nd-order derivative based** operator.
* **Not typically used by itself** as it is **too sensitive to noise**.
* **Laplacian of Gaussian (LoG):**
    * Combines **Gaussian smoothing (noise removal)** with **Laplacian (edge detection)**.
    * Also known as the "**Mexican hat**" filter due to its impulse response shape.

## Key Takeaways

* Edges are crucial image features representing boundaries with significant brightness changes.
* Edge detection often uses convolution masks approximating image derivatives.
* Different operators (Roberts, Sobel, Prewitt, Laplacian) have varying characteristics (noise sensitivity, orientation info, complexity).
* First derivatives indicate edge presence; second derivatives can indicate edge direction.
* Noise is a significant challenge; pre-smoothing is often used.
* Laplacian of Gaussian (LoG) is a common technique combining noise reduction and edge detection.
* Beyond edges, points and lines are other grey level discontinuities detectable with masks.