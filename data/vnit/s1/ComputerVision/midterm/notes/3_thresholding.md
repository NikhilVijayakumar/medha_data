# Thresholding in Computer Vision: A Foundational Segmentation Technique

## 1. Introduction

This document provides a briefing on the topic of thresholding in computer vision, a foundational technique and often one of the initial steps in **image segmentation**. Thresholding converts a grayscale image into a binary (or multi-level) image by comparing pixel intensities against one or more threshold values. This process helps to isolate objects or regions of interest from the background.

## 2. Main Themes and Important Ideas

### 2.1. Definition and Basic Concept of Thresholding

**Thresholding** is an image segmentation technique that converts a grayscale image $f(x,y)$ into a binary image $g(x,y)$ (or an image with discrete levels for multiple thresholds) by comparing each pixel's intensity value against one or more threshold values ($T$).

The basic mathematical representation of **single-value (global) thresholding** is:

$\qquad g(x,y) = \begin{cases}
1 \text{ (e.g., white)} & \text{if } f(x,y) > T \\
0 \text{ (e.g., black)} & \text{if } f(x,y) \leq T
\end{cases}$

The lecture illustrates the application of thresholding with the example of a poker-playing robot needing to interpret cards, where separating the card features from the background is crucial.

### 2.2. Importance and Potential Pitfalls

Thresholding is typically among the "first few steps of any segmentation approach" due to its simplicity and computational efficiency. It's a crucial preprocessing step for many computer vision tasks, including object detection, pattern recognition, and image analysis.

However, the selection of an appropriate **threshold value ($T$) is critical**. As emphasized, "If you get the threshold wrong the results can be disastrous." Examples demonstrate how setting the threshold too low can lead to the object and background being merged, while setting it too high can cause parts of the object to be lost. The examples of thresholding an image at $T=127, 50, 10, 200,$ and $225$ clearly illustrate the sensitivity of the results to the chosen threshold.

### 2.3. Issues in Thresholding

Several key challenges are associated with thresholding:

* **Selection of threshold value ($T$):** Determining the optimal threshold that effectively separates the desired regions is a fundamental problem.
* **Multiple thresholds:** Images containing more than one object or distinct regions with varying intensity levels may require the use of multiple thresholds to achieve proper segmentation.
* **Global vs. Local (Adaptive) Thresholding:**
    * **Global thresholding:** Uses a single or a fixed set of threshold values for the entire image. It is computationally efficient but sensitive to variations in illumination and image content.
    * **Local (Adaptive) thresholding:** Employs different threshold values for different local regions (neighborhoods) of the image. The threshold for each pixel is determined based on the intensity characteristics of its surrounding pixels. This approach is more robust to illumination variations and complex scenes.
* **Complex environment - illumination:** Varying or uneven illumination across an image can significantly alter pixel intensity values for the same object or background, making it challenging for a fixed global threshold to produce satisfactory results.

### 2.4. Multiple Thresholding

When dealing with images containing "more than one object or regions" with distinct intensity ranges, **multiple thresholds** can be used to segment the image into more than two sets of pixels (i.e., multiple intensity levels).

Mathematically, this can be represented as a piecewise function:

$\qquad g(x,y) =
\begin{cases}
\text{level}_1 & \text{if } f(x,y) > T_1 \\
\text{level}_2 & \text{if } T_2 < f(x,y) \leq T_1 \\
\vdots & \vdots \\
\text{level}_n & \text{if } f(x,y) \leq T_{n-1}
\end{cases}$

The example with $T_1 = 150$ and $T_2 = 100$ shows how different pixel intensity ranges can be assigned different output values (e.g., 255, 50, 10), effectively segmenting the image into three distinct regions based on intensity. The visual demonstrations with different $T_1$ and $T_2$ values (250 & 10, 225 & 75) further highlight the flexibility of multiple thresholding.

### 2.5. Automatic Selection of Threshold ($T$)

Manually selecting an optimal threshold can be time-consuming and subjective. Several algorithms exist for automatically determining a suitable threshold value. The lecture outlines a basic **iterative algorithm** for automatic global threshold selection:

1.  **Select an initial threshold value $T_0$.** A common initial estimate is the average gray level of the image or the mean of the minimum and maximum gray levels.
2.  **Segment the image using $T_k$** into two groups:
    * $G_1$: Pixels with gray levels $> T_k$ (considered foreground).
    * $G_2$: Pixels with gray levels $\leq T_k$ (considered background).
3.  **Calculate the mean gray level of each group:**
    * $m_1$: Mean of gray levels in $G_1$.
    * $m_2$: Mean of gray levels in $G_2$.
4.  **Compute a new threshold value $T_{k+1} = 0.5(m_1 + m_2)$.**
5.  **Repeat steps 2-4 until the difference between successive threshold values ($|T_{k+1} - T_k|$) is below a predefined limit ($\epsilon$).** This indicates convergence to a stable threshold.

The example of applying this to a fingerprint image, starting with a gray level mean, illustrates the iterative process converging to a threshold of $T = 125.4$ after 3 iterations.

### 2.6. Effects of Illumination

The lecture emphasizes the impact of illumination on image intensity, described by the **image formation model**:

$\qquad f(x,y) = i(x,y) \cdot r(x,y)$

where $i(x,y)$ represents the **illumination** component (the amount of light falling on the scene) and $r(x,y)$ represents the **reflectance** component (the intrinsic property of the object's surface).

Changes in illumination can significantly affect the pixel intensity values $f(x,y)$ for the same object or background regions across an image or between different images. This makes it difficult for a fixed global threshold to segment the image effectively under non-uniform lighting conditions.

The examples of a "Dull image of cameraman" and an "overexposed cameraman image" both demonstrate the failure of a single global threshold ($T = 127$) to produce meaningful segmentation due to variations in illumination.

The issue is further explained by considering the logarithmic transformation, which converts the multiplicative components into additive ones:

$\qquad z(x,y) = \ln f(x,y) = \ln i(x,y) + \ln r(x,y)$

When illumination and reflectance are treated as independent random variables, their histograms convolve in the logarithmic domain.

"Multiple objects or bad illumination" can lead to histograms where the gray levels of the object and background are mixed, making it hard to find a clear separation point for thresholding. The example of a histogram with gray levels around 60, 70, and 77 due to illumination effects illustrates how this can result in multiple unintended regions after applying a single threshold.

### 2.7. Basic Global Thresholding Algorithm (Detailed)

The lecture provides a more formal algorithm for basic global thresholding:

1.  **Select an initial estimate for the threshold $T_0$** (typically the average gray level in the image).
2.  **Segment the image using $T_k$** to produce two groups of pixels:
    * $G_1$: Pixels with gray levels $> T_k$.
    * $G_2$: Pixels with gray levels $\leq T_k$.
3.  **Compute the average gray levels of pixels in each group:**
    * $\mu_1 = \text{mean}(G_1)$
    * $\mu_2 = \text{mean}(G_2)$
4.  **Compute a new threshold value:** $T_{k+1} = (\mu_1 + \mu_2) / 2$.
5.  **Repeat steps 2-4 until the difference in $T$ in successive iterations ($|T_{k+1} - T_k|$) is less than a predefined convergence limit $T_\infty$ ($\epsilon$).**

It is noted that "This algorithm works very well for finding thresholds when the histogram is suitable," specifically for images with **bimodal histograms** where the intensity distributions of the foreground and background are well-separated.

Examples of successful global thresholding are shown with corresponding original images and their bimodal histograms, demonstrating clear valleys that the algorithm can effectively identify as the threshold.

### 2.8. Problems with Single Value Thresholding (Reiterated)

* **"Single value thresholding only works for bimodal histograms."** When the histogram has multiple peaks (multimodal) or broad, overlapping distributions, a single threshold will likely fail to segment the image accurately, resulting in either merging distinct objects or breaking a single object into multiple parts.
* **"Images with other kinds of histograms need more than a single threshold"** (i.e., multiple thresholding techniques).
* **Uneven illumination** is again highlighted as a major limitation for single-valued thresholding. Examples show poor segmentation results in the presence of shadows or varying light intensity compared to results obtained under uniform illumination.

The example of bottles is used to illustrate a likely **multimodal histogram** where a single threshold would be insufficient to isolate the contents of each bottle from the background and potentially from each other.

### 2.9. Basic Adaptive Thresholding

To overcome the limitations of global thresholding, especially with uneven illumination or complex objects, **adaptive thresholding** techniques are employed. The core idea is to:

* **Divide the image into smaller, overlapping or non-overlapping sub-images (local regions).**
* **Calculate a threshold value for each local region independently**, based on the intensity characteristics within that region (e.g., mean, median, local histogram).
* **Apply the calculated threshold to the pixels within that local region.**

Because "the threshold for each pixel depends on its location within an image, this technique is said to be adaptive." Common adaptive thresholding methods include:

* **Mean Adaptive Thresholding:** The threshold for each pixel is the mean intensity of its surrounding neighborhood.
* **Gaussian Adaptive Thresholding:** Similar to mean thresholding, but the neighboring pixels are weighted using a Gaussian function, giving more importance to closer pixels.
* **Median Adaptive Thresholding:** The threshold is the median intensity of the neighborhood.
* **Local Binary Pattern (LBP) based thresholding:** Uses local texture information to determine the threshold.
* **Niblack's method, Sauvola's method, and others:** More sophisticated techniques that consider local statistics (mean, standard deviation) to determine the threshold.

An example shows an image where global thresholding failed due to uneven illumination, and adaptive thresholding applied to sub-images yielded mixed success initially. Further subdivision of "troublesome sub-images" into even smaller regions led to more successful thresholding, demonstrating the principle of adapting the threshold locally to account for intensity variations.

### 2.10. Sample Program (Illustrative - MATLAB-like)

A basic MATLAB-like code snippet demonstrates simple global thresholding:

```matlab
img = imread('cameraman.jpg');
T = input('Enter the value of Threshold   =  ');
[m, n] = size(img); % Get image dimensions
for i = 1:m
  for j = 1:n
    if (img(i,j) > T)
      img(i,j) = 255; % Set pixel to white (foreground)
    else
      img(i,j) = 0;   % Set pixel to black (background)
    end
  end
end
imshow(img); % Display the thresholded image
```
## 3. Key Takeaways

* **Thresholding is a fundamental image segmentation technique** used to create binary or multi-level images by comparing pixel intensities to one or more threshold values.
* The choice of **threshold value(s) is crucial** for the success of thresholding; incorrect values can lead to poor segmentation.
* **Global thresholding**, using a single threshold for the entire image, is computationally efficient but **works best for images with bimodal histograms and relatively uniform illumination.**
* **Automatic threshold selection algorithms** can help determine a suitable global threshold based on image statistics, especially for bimodal distributions.
* **Uneven illumination and complex image content pose significant challenges for global thresholding**, often leading to unsatisfactory results.
* **Adaptive thresholding**, where different thresholds are applied to local regions of the image, **can be more effective in handling variations in illumination and complex scenes.** The threshold is calculated based on the local intensity characteristics.
* Further subdivision of image regions in adaptive thresholding can improve the accuracy of segmentation in areas with significant local variations.

## 4. Further Considerations

* The lecture primarily focuses on basic thresholding techniques. **More advanced methods exist**, such as **Otsu's method** for automatic global thresholding (which finds the threshold that minimizes the intra-class variance of the thresholded black and white pixels) and various sophisticated adaptive thresholding algorithms (e.g., Niblack, Sauvola, Bradley-Roth).
* The choice between global and adaptive thresholding **depends heavily on the specific characteristics of the image** (e.g., histogram shape, illumination uniformity) and the **segmentation goals.**
* Understanding the **impact of illumination on image intensity** is essential for selecting and applying appropriate thresholding techniques. Preprocessing steps to correct for uneven illumination might be necessary before applying thresholding.
* **Hybrid approaches** that combine global and local thresholding or integrate thresholding with other segmentation techniques can also be effective in certain scenarios.

# Important Formulas
## Thresholding Formulas and Models from Lecture Excerpts

This section consolidates the specific formulas and models related to thresholding discussed in the lecture excerpts.

### 1. Basic Single Value Thresholding

* **Formula:**
    $\qquad g(x,y) = \begin{cases} 1 & \text{if } f(x,y) > T \\ 0 & \text{if } f(x,y) \leq T \end{cases}$

* **Details:** This formula defines the fundamental process of binary thresholding. For each pixel at coordinates $(x, y)$ in the original grayscale image $f(x,y)$, its corresponding pixel in the binary (thresholded) image $g(x,y)$ is set to one of two values (typically 1 for foreground/object and 0 for background) based on whether its intensity is greater than or less than or equal to a single threshold value $T$.

### 2. General Multiple Thresholding

* **Formula:** (Implicitly described, general form shown previously)
    The output pixel value $g(x,y)$ depends on which range defined by the multiple threshold values $T_1, T_2, ..., T_n$ the original pixel intensity $f(x,y)$ falls into.

* **Details:** Multiple thresholding extends the basic concept to segment an image into more than two distinct regions or intensity levels. It uses a series of ordered threshold values. If a pixel's intensity lies between two consecutive thresholds, it is assigned a specific output value corresponding to that range.

### 3. Example of Multiple Thresholding

* **Specific Examples:**
    * $T_1 = 150, T_2 = 100$ (with corresponding output values illustrated visually in the source).
    * $T_1 = 250, T_2 = 10$ (visual example).
    * $T_1 = 225, T_2 = 75$ (visual example).

* **Details:** These examples provide concrete illustrations of how multiple thresholds segment an image. By setting two threshold values, the intensity range is divided into three intervals, and pixels within each interval are mapped to a specific output intensity, resulting in a three-level segmented image. The visual presentations in the source likely demonstrate the effect of different threshold combinations on the resulting segmentation.

### 4. Formula for Automatic Threshold Selection (New Threshold)

* **Formula:**
    $\qquad T_{new} = 0.5(m_1 + m_2) \quad \text{or} \quad T = \frac{m_1 + m_2}{2}$

* **Details:** This formula is a key step in an iterative algorithm used to automatically determine a global threshold $T$.
    * $m_1$ represents the mean gray level of all pixels in the original image whose intensity is *greater* than the current threshold.
    * $m_2$ represents the mean gray level of all pixels whose intensity is *less than or equal to* the current threshold.
    The calculated $T_{new}$ (or $T$) becomes the threshold for the next iteration of the algorithm. The algorithm starts with an initial estimate for $T$ (e.g., the average gray level of the image or the mean of the minimum and maximum gray levels) and iteratively refines it until the change in $T$ between successive iterations falls below a predefined small value (convergence criterion).

### 5. Illumination-Reflectance Model

* **Formula:**
    $\qquad f(x,y) = i(x,y) \cdot r(x,y)$

* **Details:** This fundamental model in image processing describes the observed intensity $f(x,y)$ of a pixel at coordinates $(x, y)$ as a product of two components:
    * $i(x,y)$: The **illumination** component, representing the amount of light incident on the scene at that point.
    * $r(x,y)$: The **reflectance** component, representing the intrinsic ability of the object surface at that point to reflect light. This model highlights how changes in illumination can significantly affect the perceived intensity of objects in an image, posing challenges for thresholding techniques that rely solely on intensity values.

### 6. Logarithmic Transformation of Illumination-Reflectance Model

* **Formula:**
    $\qquad \ln f(x,y) = \ln i(x,y) + \ln r(x,y)$

* **Details:** By applying the natural logarithm to the illumination-reflectance model, the multiplicative relationship between illumination and reflectance is transformed into an additive one. This transformation is particularly useful in scenarios where the illumination and reflectance components can be considered statistically independent. In such cases, operations in the logarithmic domain can simplify the analysis and potentially the separation of these components, which can be beneficial when dealing with issues caused by non-uniform illumination in thresholding and other image processing tasks.