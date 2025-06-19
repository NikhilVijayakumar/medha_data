# Colour Image Processing

## 1. Introduction

This briefing document summarizes the key themes and important ideas from the lecture notes on colour image processing. It covers the rationale for using colour, colour fundamentals, colour models, pseudo-colour processing, and basic full-colour image processing techniques (transformations, smoothing, sharpening).

## 2. Why Use Colour in Image Processing?

* **Enhanced Object Identification and Extraction:** Colour aids in distinguishing and isolating objects (e.g., "Face detection using skin colors").
* **Increased Discernibility for Humans:** Humans can differentiate far more colours than grey shades ("Humans can discern thousands of color shades and intensities" vs. "Human discern only two dozen shades of grays").

## 3. Categories of Colour Image Processing

* **Full Colour Processing:** Images acquired with full colour information.
* **Pseudo-colour Processing:** Assigns colours to different ranges of monochrome intensities for human visualisation, especially when "color sensors and processing hardware are not available" (historically).

## 4. Colour Fundamentals

* **Physical Phenomenon:** Colour is a physical property related to the electromagnetic spectrum ("400 to 700 nm" for chromatic light).
* **Physio-psychological Phenomenon:** Colour perception is influenced by brain interpretation ("How human brain perceive and interpret color?").
* **Light Reflection:** Perceived colour is the light reflected by an object. "The color that human perceive in an object = the light reflected from the object."
* **Physical Quantities of Chromatic Light:**
    * **Radiance:** Total energy flow (watts).
    * **Luminance:** Energy perceived by observer (lumens) ("Far infrared light: high radiance, but 0 luminance").
    * **Brightness:** Subjective descriptor similar to achromatic light intensity.
* **Human Eye's Light Sensing:** "6~7M Cones" with three principal sensing categories: "Red light 65%, green light 33%, and blue light 2%."
* **Primary and Secondary Colours:**
    * **Primary (CIE 1931):** B = 435.8 nm, G = 546.1 nm, R = 700 nm.
    * **Secondary:** G+B=Cyan, R+G=Yellow, R+B=Magenta.
* **Mixture of Light vs. Pigments:** Additive mixing (light - colour TV) differs from subtractive mixing (pigments - printing). Pigments absorb a primary colour of light and reflect/transmit the other two.
* **CIE XYZ Model:** Standard colour representation derived from RGB via linear transformation. Uses normalized tristimulus values (x, y, z) where "x+y+z=1. Thus, x, y (chromaticity coordinate) is enough to describe all colors."
* **Chromaticity Diagram:** Illustrates the colour gamut reproducible by a set of primaries. "By additivity of colors: Any color inside the triangle can be produced by combinations of the three initial colors."

## 5. Colour Models

* Standard ways to specify colours within a coordinate system (also called colour spaces or colour systems).
* **RGB Model:** Hardware-oriented (monitors). "Full-color image: 24-bit RGB color image" (8 bits/component). "Safe RGB colors (safe Web colors, safe browser colors)" are a subset.
* **CMY and CMYK Models:** CMY (Cyan, Magenta, Yellow) are secondary colours of light/primary of pigments, used for "hardcopy output."
    * Conversion from RGB to CMY:
        $\begin{bmatrix} C \\ M \\ Y \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \begin{bmatrix} R \\ G \\ B \end{bmatrix}$
    * CMYK adds black (K) for better dark colour reproduction.
* **HSI Model:** Hue, Saturation, Intensity - more intuitive for human colour description.
    * **Hue:** Colour attribute.
    * **Saturation:** Colour purity (0=white, 1=pure).
    * **Intensity:** Brightness (achromatic component).

## 6. Pseudo-Colour Image Processing

* Assigns colours to grey values for enhanced visualisation.
* **Purpose:** "For human visualization and interpretation of gray-scale events."
* **Methods:**
    * **Intensity Slicing:** Divides intensity range into slices, assigns different colours.
    * **Gray Level to Colour Transformations:** Functions map grey levels to colours (piecewise linear or more general).
* **Applications:** Radiation test patterns, X-ray welds, rainfall statistics, combining multi-spectral images (assigning bands to colour channels).

## 7. Basics of Full-Colour Image Processing

* Processing techniques applied directly to colour images.
* **Colour Pixel Representation:** Pixel at (x,y) is a vector in colour space (e.g., $\mathbf{c}(x,y) = \begin{bmatrix} R(x,y) \\ G(x,y) \\ B(x,y) \end{bmatrix}$ in RGB) vs. grey-scale $f(x,y) = I(x,y)$.
* **Approaches to Colour Vector Processing:**
    * **Per-colour-component processing:** Process each colour channel independently.
    * **Vector-based processing:** Process the entire colour vector as a unit.
* **Equivalence of Methods:** Equivalent when "Operation on each component of a vector must be independent of the other component."
* **Spatial Processing Categories:** "Pixel-wise processing" and "Neighborhood processing" (similar to grey-scale).

## 8. Colour Transformations

* Modify colour values of pixels.
* **General Form:** $\mathbf{g}(x,y) = T[\mathbf{f}(x,y)]$, where $\mathbf{f}$ is input and $\mathbf{g}$ is transformed image. Can be represented as $s_i = T_i(r_1, r_2, ..., r_n)$, for components $i=1$ to $n$.
* **Colour Model Selection:** "Practically, some operations are better suited to specific color model" (though theoretically possible in any: RGB, CMY(K), HSI).
* **Example: Modifying Intensity:** Decreasing by factor $k$ ($0 < k < 1$).
    * **HSI:** $s_3 = k r_3$ (modifies Intensity).
    * **RGB:** $s_i = k r_i$ (applied to each component).
    * **CMY:** $s_i = k r_i + (1-k)$.
    * HSI often preferred for intensity modification due to direct access to the intensity component, though RGB is simpler to implement.
* **Problem with Hue Component:** Can be "dis-continuous" and "Un-defined over gray axis," requiring careful handling.
* **Colour Slicing:** Selecting a colour region of interest by defining a "prototype color" and a region around it (e.g., "Sphere region" or "Cube region" in colour space).

## 9. Colour Image Smoothing

* Neighbourhood processing to reduce noise.
* **Averaging Mask:** Similar to grey-scale, averages colour values of surrounding pixels. For neighbourhood $S_{xy}$ with $K$ pixels, smoothed colour vector $\mathbf{c}(x,y)$ using per-component processing:
    * $R(x,y) = \frac{1}{K} \sum_{(s,t) \in S_{xy}} R(s,t)$
    * $G(x,y) = \frac{1}{K} \sum_{(s,t) \in S_{xy}} G(s,t)$
    * $B(x,y) = \frac{1}{K} \sum_{(s,t) \in S_{xy}} B(s,t)$
* Equivalent to vector processing if averaging is applied to the colour vector. Example of a "5x5 smoothing mask." Smoothing Intensity in HSI can differ from smoothing RGB.

## 10. Conclusion

The lecture provides a foundational understanding of colour image processing, covering colour theory, models, pseudo-colouring, and basic full-colour manipulation (transformations, smoothing). Emphasises the importance of colour model choice based on the processing task.

# Formula

# Colour Image Processing Formulas

This section compiles the formulas explicitly presented in the provided sources related to colour image processing.

## 1. Normalized Tristimulus Values (CIE XYZ)

* **Formulas:**
    $\qquad x = \frac{X}{X+Y+Z}$
    $\qquad y = \frac{Y}{X+Y+Z}$
    $\qquad z = \frac{Z}{X+Y+Z}$
* **RGB to XYZ Conversion Matrix:**
    $\qquad \begin{bmatrix} X \\ Y \\ Z \end{bmatrix} = \begin{bmatrix} 0.431 & 0.342 & 0.178 \\ 0.222 & 0.707 & 0.071 \\ 0.020 & 0.130 & 0.939 \end{bmatrix} \begin{bmatrix} R \\ G \\ B \end{bmatrix}$

## 2. CMY Model (+Black = CMYK)

* **Conversion from RGB:**
    $\qquad \begin{bmatrix} C \\ M \\ Y \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix} - \begin{bmatrix} R \\ G \\ B \end{bmatrix}$

## 3. Colour Pixel in RGB Colour Space

* **Vector Representation:**
    $\qquad \mathbf{c}(x,y) = \begin{bmatrix} R(x,y) \\ G(x,y) \\ B(x,y) \end{bmatrix}$

## 4. Colour Transformation

* **General Form:**
    $\qquad \mathbf{g}(x,y) = T[\mathbf{f}(x,y)]$
* **Component-wise Transformation:**
    $\qquad s_i = T_i(f_1(x,y), f_2(x,y), ..., f_n(x,y)), \quad i = 1, 2, ..., n$

## 5. Example: Modify Intensity of a Colour Image

### 5.1. HSI Colour Space

* **Formula:**
    $\qquad s_3 = k r_3$
    * Where $s_3$ and $r_3$ represent the intensity component of the output and input pixels, respectively, and $k$ is a scaling factor.

### 5.2. RGB Colour Space

* **Formula:**
    $\qquad s_i = k r_i$
    * Where $s_i$ and $r_i$ represent the $i$-th colour component (R, G, or B) of the output and input pixels, respectively, and $k$ is a scaling factor.

### 5.3. CMY Colour Space

* **Formula:**
    $\qquad s_i = k r_i + (1-k)$
    * Where $s_i$ and $r_i$ represent the $i$-th colour component (C, M, or Y) of the output and input pixels, respectively, and $k$ is a scaling factor.

## 6. Colour Image Smoothing: Averaging Mask

* **Vector Averaging:**
    $\qquad \mathbf{c}(x,y) = \frac{1}{K} \sum_{(s,t) \in S_{xy}} \mathbf{c}(s,t)$
* **Component-wise Averaging:**
    $\qquad R(x,y) = \frac{1}{K} \sum_{(s,t) \in S_{xy}} R(s,t)$
    $\qquad G(x,y) = \frac{1}{K} \sum_{(s,t) \in S_{xy}} G(s,t)$
    $\qquad B(x,y) = \frac{1}{K} \sum_{(s,t) \in S_{xy}} B(s,t)$
    * Where $K$ is the number of pixels in the averaging mask $S_{xy}$ centred at $(x,y)$.
