# Image Filtering in Computer Vision

## 1. Introduction to Image Filtering

* **Definition:** The process of replacing a pixel with a value based on some operations or functions (filters/masks/kernels/templates/windows).
* **Primary Uses in Digital Image Processing (DIP):**
    * **Noise removal:** Suppressing unwanted variations in pixel intensity.
    * **Suppressing high frequencies:** Leading to image smoothing (blurring).
    * **Suppressing low frequencies:** Resulting in image enhancement or edge detection (sharpening).
* **Applications:**
    * Noise removal
    * Edge detection
    * Image Sharpening
    * Feature extraction
* **Categorization:**
    * **Spatial domain filtering:** Filters operate directly on the pixels of the image plane.
    * **Frequency domain filtering:** Filters operate by modifying the Fourier transform (FT) of an image.

## 2. Spatial Domain Filtering

* Involves directly operating on the pixels and their neighboring pixels.
* **General Process:**
    $\qquad g(x,y) = T[f(x,y)]$
    where $f(x,y)$ is the input image, $g(x,y)$ is the processed image, and $T$ is an operator on $f$ defined over a neighborhood of $(x,y)$.
* **Neighborhood:** Typically a subimage area centered at $(x,y)$ (e.g., 3x3 square).

### 2.1 Linear Spatial Filters

* The result at a point $(x,y)$, $R$, is a weighted sum of the pixel values in the neighborhood.
* Weights are determined by the **mask coefficients** $w(i,j)$.
* **Example (3x3 mask):**
    $\qquad R = w(-1,-1)f(x-1,y-1) + ... + w(0,0)f(x,y) + ... + w(1,1)f(x+1,y+1)$
* **Convolution:** The general process of linear spatial filtering.
    $\qquad g(x,y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t)f(x+s, y+t)$
    where the mask size is $m \times n$ ($m = 2a+1, n = 2b+1$).

#### 2.1.1 Smoothing Filters

* Used for blurring and noise reduction by reducing sharp transitions.
* **Mean Filter (Average Filter):** All coefficients in the mask are equal.
    * Example (3x3):
        $\qquad \frac{1}{9} \begin{bmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{bmatrix}$
* **Weighted Average Filters:** Different pixels in the neighborhood are given different weights.
    * Example:
        $\qquad \frac{1}{16} \begin{bmatrix} 1 & 2 & 1 \\ 2 & 4 & 2 \\ 1 & 2 & 1 \end{bmatrix}$
    * **General Expression:**
        $\qquad g(x,y) = \frac{\sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t)f(x+s, y+t)}{\sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t)} = \frac{1}{w'} \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t)f(x+s, y+t)$

### 2.2 Nonlinear Spatial Filters

* Based on operations other than linear combinations of pixel values.
* **Order-Statistic Filters:** Work by ordering or ranking pixel values in the neighborhood.
* **Median Filter:** Replaces a pixel value with the median of its neighboring pixel values.
    * Effective in **salt & pepper noise** removal.
* **Other Nonlinear Filters:**
    * **Max Filters:** Replace the center pixel with the maximum value in the neighborhood (finding brightest points).
    * **Min Filters:** Replace the center pixel with the minimum value in the neighborhood (finding darkest points).

### 2.3 Spatial Filters - Sharpening

* **Objectives:**
    * Highlight fine detail in an image.
    * Enhance detail that has been blurred.
* Achieved through **spatial differentiation**.
* **First Order Derivative (1D):**
    $\qquad \frac{\partial f}{\partial x} \approx f(x+1) - f(x)$
* **Second Order Derivative (1D):**
    $\qquad \frac{\partial^2 f}{\partial x^2} \approx f(x+1) - 2f(x) + f(x-1)$
* **Laplacian (2D - Second Order Derivative):**
    $\qquad \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = [f(x+1,y)+f(x-1,y)+f(x,y+1)+f(x,y-1)] - 4f(x,y)$
* **Laplacian Masks (Examples):**
    $\qquad \begin{bmatrix} 0 & 1 & 0 \\ 1 & -4 & 1 \\ 0 & 1 & 0 \end{bmatrix}, \quad \begin{bmatrix} 1 & 1 & 1 \\ 1 & -8 & 1 \\ 1 & 1 & 1 \end{bmatrix}, \quad \begin{bmatrix} -1 & 2 & -1 \\ 2 & -4 & 2 \\ -1 & 2 & -1 \end{bmatrix}$

## 3. Frequency Domain Filtering

* Involves manipulating the **Fourier Transform (FT)** of an image.
* **Fourier Transform (FT):** Decomposes an image into its sine and cosine components, transforming real space to frequency space. Each point in frequency space represents a particular frequency.
* **Discrete Fourier Transform (DFT):**
    $\qquad F(u,v) = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j2\pi(ux/M + vy/N)}$
* **Inverse Discrete Fourier Transform (IDFT):**
    $\qquad f(x,y) = \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{j2\pi(ux/M + vy/N)}$
* **Basic Steps:**
    1. Compute the DFT of the input image: $F(u,v)$.
    2. Multiply the DFT by the filter transfer function $H(u,v)$: $G(u,v) = H(u,v)F(u,v)$.
    3. Compute the Inverse DFT of the result: $g(x,y)$.
* **Frequencies in an Image:**
    * **High frequencies:** Rapid changes in gray level values (edges, noise).
    * **Low frequencies:** Slow changes in gray level values (smooth regions).

### 3.1 Types of Frequency Filters

* **Lowpass Filters:** Attenuate high frequencies, pass low frequencies $\implies$ Smoothing (blurring).
    * **Ideal Lowpass Filter (ILPF):**
        $\qquad H(u,v) = \begin{cases} 1 & \text{if } D(u,v) \leq D_0 \\ 0 & \text{if } D(u,v) > D_0 \end{cases}$
        where $D(u,v)$ is the distance from the origin in the frequency domain, and $D_0$ is the cutoff frequency.
    * **Butterworth Lowpass Filter (BLPF):**
        $\qquad H(u,v) = \frac{1}{1 + (D(u,v)/D_0)^{2n}}$
    * **Gaussian Lowpass Filter (GLPF):**
        $\qquad H(u,v) = e^{-D^2(u,v) / 2\sigma^2}$
* **Highpass Filters:** Attenuate low frequencies, pass high frequencies $\implies$ Sharpening, edge detection.
    * $H_{hp}(u,v) = 1 - H_{lp}(u,v)$
    * Ideal Highpass Filter (IHPF), Butterworth Highpass Filter (BHPF), Gaussian Highpass Filter (GHPF).
* **Bandpass Filters:** Attenuate very low and very high frequencies, pass a range of intermediate frequencies $\implies$ Enhancing specific frequency components (e.g., certain textures or edges while reducing noise).
    * $H_{bp}(u,v) = H_{lp}(u,v) \cdot H_{hp}(u,v)$

## 4. Relationship and Comparison with Spatial Filters

* **Convolution Theorem:**
    * Spatial domain convolution $\iff$ Frequency domain multiplication
    * $\qquad g(x,y) = f(x,y) * h(x,y) \iff G(u,v) = F(u,v)H(u,v)$
* **Comparison:**
    * **Frequency filtering:** More computationally efficient for larger filter kernels (due to FFT).
    * **Spatial filtering:** More intuitive to understand and implement directly for smaller kernels.

## 5. Other Masks Used During Segmentation

* **Averaging Filters:** Used before or after segmentation to smooth out effects of noise, sampling, or quantization.
    * Can be of various odd sizes (3x3, 5x5, 7x7, etc.). Larger sizes lead to more blurring.
* **Gaussian Smoothing Operation:** Provides a smoother blurring effect compared to simple averaging.
    * Kernel size and standard deviation ($\sigma$) control the degree of smoothing. Example with $\sigma = 2.0$ for 3x3, 5x5, 7x7 kernels.

## 6. References

* Digital Image Processing, 3rd Edition, R. C. Gonzalez and R. E. Woods, Pearson Education.
* www.imageprocessingplace.com

## 7. Summary

* **Filtering:** Applying a transform on an image to enhance it.
* **Subdivided into:**
    * **Spatial domain filtering:** Direct pixel manipulation.
    * **Frequency domain filtering:** Modification of the Fourier transform.

# Important Formulas

# Key Formulas for Image Filtering

This section summarizes the key mathematical expressions related to image filtering, covering both spatial and frequency domain techniques.

## 1. General Spatial Filtering

* **Formula:**
    $\qquad g(x,y) = T[f(x,y)]$
* **Description:** This general expression denotes spatial filtering, where the processed image $g(x,y)$ is the result of applying an operator $T$ to the input image $f(x,y)$ over some neighborhood of the pixel $(x,y)$.

## 2. Linear Spatial Filtering (Convolution)

* **Result at a Point (3x3 Mask):**
    $\qquad R = w(-1,-1)f(x-1,y-1) + w(0,-1)f(x,y-1) + ... + w(0,0)f(x,y) + ... + w(0,1)f(x,y+1) + w(1,1)f(x+1,y+1)$
* **General Formula:**
    $\qquad g(x,y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t)f(x+s,y+t)$
    * $f(x,y)$: Input image of size $M \times N$.
    * $w(s,t)$: Filter mask of size $m \times n$, where $m = 2a+1$ and $n = 2b+1$.

## 3. Weighted Average Filters

* **Formula:**
    $\qquad g(x,y) = \frac{1}{w'} \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t)f(x+s,y+t)$
    * $w' = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t)$: The sum of the weights in the filter mask.

## 4. Derivatives for Sharpening (1D)

* **First Order Derivative:**
    $\qquad \frac{\partial f}{\partial x} = f(x+1) - f(x)$
* **Second Order Derivative:**
    $\qquad \frac{\partial^2 f}{\partial x^2} = f(x+1) + f(x-1) - 2f(x)$

## 5. Laplacian Operator (2D - Second Order Derivative)

* **Formula:**
    $\qquad \nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = [f(x+1,y) + f(x-1,y) + f(x,y+1) + f(x,y-1)] - 4f(x,y)$

## 6. Frequency Domain Filtering

* **Discrete Fourier Transform (DFT):**
    $\qquad F(u,v) = \frac{1}{MN} \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y)e^{-j2\pi(ux/M + vy/N)}$
* **Inverse Discrete Fourier Transform (IDFT):**
    $\qquad f(x,y) = \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v)e^{j2\pi(ux/M + vy/N)}$

## 7. Ideal Lowpass Filter (ILPF)

* **Formula:**
    $\qquad H(u,v) = \begin{cases} 1 & \text{if } D(u,v) \leq D_0 \\ 0 & \text{if } D(u,v) > D_0 \end{cases}$
    * $D(u,v)$: Distance from the origin in the frequency domain.
    * $D_0$: Cutoff frequency.

## 8. Butterworth Lowpass Filter (BLPF)

* **Formula:**
    $\qquad H(u,v) = \frac{1}{1 + (D(u,v)/D_0)^{2n}}$
    * $n$: Order of the filter.

## 9. Gaussian Lowpass Filter (GLPF)

* **Formula:**
    $\qquad H(u,v) = e^{-D^2(u,v) / 2\sigma^2}$
    * $\sigma$: Standard deviation controlling the width of the Gaussian.

## 10. Relationship between Lowpass and Highpass Filters

* **Formula:**
    $\qquad H_{hp}(u,v) = 1 - H_{lp}(u,v)$

## 11. Bandpass Filter

* **Formula:**
    $\qquad H_{bp}(u,v) = H_{lp}(u,v) \times H_{hp}(u,v)$

## 12. Convolution Theorem (Spatial vs. Frequency)

* **Formula:**
    $\qquad g(x,y) = f(x,y) * h(x,y) \iff G(u,v) = H(u,v)F(u,v)$
    * $*$ denotes convolution.
    * $\iff$ denotes the Fourier transform pair.