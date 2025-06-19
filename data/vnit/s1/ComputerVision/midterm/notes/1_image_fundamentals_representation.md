# Fundamentals of Digital Image Processing

This notebook introduces fundamental concepts and terminology used in the field of Digital Image Processing (DIP).

## 1. Digital Image Processing (DIP)

- **Definition:** The use of computer algorithms to perform image processing tasks on digital images.

## 2. Core Image Elements

- **Pixel:** The smallest addressable element in a digital image. Each pixel represents a single point and contains information about its intensity or colour.
- **Intensity:** The brightness value of a pixel. It is typically represented by a numerical value within a specific range.
    - **Example (8-bit Grey Scale):** Intensity values range from 0 (black) to 255 (white), with intermediate values representing shades of grey.
- **Spatial Coordinates:** The location of a pixel within the image, usually defined by its row and column number, often denoted as $(x, y)$ or $(m, n)$.

## 3. Signal Types

- **Analog Signal:** A continuous signal where a time-varying feature represents another time-varying quantity.
- **Digital Signal:** A signal that represents data as a sequence of discrete values. Digital images are a form of digital signal representing spatial information.

## 4. Image Acquisition

- **Definition:** The process of capturing or creating a digital image. This often involves sensors that convert physical stimuli (like light) into digital data.

## 5. Digitization Processes

- **Sampling:** The process of discretizing the spatial coordinates of a continuous image. This divides the continuous image into a grid of discrete points, which become the pixels of the digital image.
- **Quantization:** The process of discretizing the intensity values of the sampled image. This assigns a finite number of levels to the continuous range of intensity values. The number of bits used for quantization determines the number of distinct intensity levels (e.g., 8 bits allow for $2^8 = 256$ levels).

## 6. Types of Digital Images

- **Binary Image:** A digital image where each pixel has only two possible intensity values, typically representing black and white (e.g., 0 and 1).
- **Grey Scale Image:** A digital image where each pixel has an intensity value representing a shade of grey. These values typically fall within a range, such as 0-255 for an 8-bit image.
- **RGB Colour Image:** A digital image where each pixel's colour is represented by three components: red (R), green (G), and blue (B). Each component is typically represented by 8 bits, allowing for $256 \times 256 \times 256$ possible colours.

## 7. Pixel Neighborhoods

- **4-Neighbors:** The pixels directly adjacent to a central pixel, horizontally (left and right) and vertically (above and below). For a pixel at $(x, y)$, its 4-neighbors are $(x-1, y), (x+1, y), (x, y-1), (x, y+1)$.
- **Diagonal Neighbors:** The pixels diagonally adjacent to a central pixel. For a pixel at $(x, y)$, its diagonal neighbors are $(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)$.
- **8-Neighbors:** The combination of the 4-neighbors and the diagonal neighbors of a central pixel.

## 8. Basic Image Operations

- **Arithmetic Operations:** Basic mathematical operations (addition, subtraction, multiplication, division) performed on the pixel values of one or more images. These operations can be used for tasks like image enhancement, noise reduction, or combining information from multiple images.
- **Logic Operations:** Boolean operations (AND, OR, NOT, XOR) performed on the binary representations of pixel values. These are often used in binary image processing for tasks like object detection and shape analysis.

# Important Formula

# Basic Arithmetic Operations on Digital Images

This notebook outlines fundamental arithmetic operations that can be performed on the pixel values of digital images.

## 1. Image Inversion (Negative)

- **Purpose:** To create the negative image, where dark areas appear light and vice versa.
- **Formula (for an 8-bit grayscale image):**
  $$c = 255 - a$$
  where:
    - $a$ is the intensity value of a pixel in the original image.
    - $c$ is the intensity value of the corresponding pixel in the inverted image.
    - 255 is the maximum intensity value for an 8-bit image ($2^8 - 1$).

- **Generalized Formula (for a B-bit representation):**
  $$c = (2^B - 1) - a$$
  where $B$ is the number of bits used to represent each pixel's intensity.

## 2. Image Addition

- **Purpose:** Can be used for various effects, such as brightening images or combining information from multiple images (e.g., noise reduction by averaging).
- **Formula (for two images A(m,n) and B(m,n)):**
  $$Z(x, y) = A(m,n) + B(m,n)$$
  where:
    - $A(m,n)$ is the intensity of the pixel at coordinates $(m, n)$ in image A.
    - $B(m,n)$ is the intensity of the pixel at coordinates $(m, n)$ in image B.
    - $Z(x, y)$ is the intensity of the corresponding pixel at coordinates $(x, y)$ in the resulting image Z. Note that $(x, y)$ corresponds to $(m, n)$ assuming the images have the same dimensions.

## 3. Image Subtraction

- **Purpose:** Useful for tasks like detecting differences between images (e.g., motion detection or change detection).
- **Formula (for two images A(m,n) and B(m,n)):**
  $$Z(m,n) = A(m,n) - B(m,n)$$
  where the variables are defined similarly to image addition. The result can be positive or negative, and may need to be scaled or offset for display.

## 4. Image Multiplication

- **Purpose:** Can be used for masking parts of an image or for scaling intensity values in a non-linear way.
- **Formula (for two images A(m,n) and B(m,n)):**
  $$Z(m,n) = A(m,n) \times B(m,n)$$
  where the variables are defined similarly to image addition. The resulting intensity values can be outside the original range and may need to be normalized.

## 5. Image Division

- **Purpose:** Can be used for tasks like correcting for uneven illumination or for ratio imaging.
- **Formula (for two images A(m,n) and B(m,n)):**
  $$Z(m,n) = A(m,n) / B(m,n)$$
  where the variables are defined similarly to image addition. Division by zero needs to be handled carefully, and the resulting values may need scaling.