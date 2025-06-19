# JPEG Compression Standard: Summary of Lec_11_JPEG.pdf

## 1. Introduction and Standardisation

* JPEG (Joint Photographic Experts Group) standard is a result of collaboration between:
    * International Telecommunication Union (ITU)
    * International Organization for Standardization (ISO)
    * International Electrotechnical Commission (IEC)
* Formal designations:
    * ISO/IEC 10918-1 Digital compression and coding of continuous-tone still image
    * ITU-T Recommendation T.81
* Highlights widespread acceptance and application.

## 2. Modes of Operation

* **Lossless mode:** Exact recovery of original image data after decompression (no data loss). Crucial for applications where data integrity is paramount.
* **Sequential mode:** Single-pass compression (left to right, top to bottom). Most common and straightforward mode.
* **Progressive mode:** Multi-scan compression. Low-quality preview displayed quickly, quality improves with more data.
* **Hierarchical mode:** Compression at multiple resolutions. Lower-resolution versions accessible without full decompression.

## 3. Encoder Steps (Lossy Compression Focus)

* Primarily focuses on lossy JPEG compression.
* **Discrete Cosine Transform (DCT):**
    * Input image divided into **8x8 pixel blocks**.
    * **Forward DCT** applied to each block: "The input data is first divided into 8x8 blocks and then each block is given as input to the Forward DCT block."
    * Transforms each 8x8 block into **64 DCT coefficients** representing different spatial frequencies: "Output of the DCT block will be 8x8 (=64) Each contains one of the 64 unique 2D spatial frequencies which comprise the input signal spectrum."
    * **DC component (F(0,0)):** Average intensity. "The first coefficient F(0,0) is the DC component". "1st DCT coefficient has no frequency component it is pure DC component."
    * **AC components (63):** Represent variations in intensity. "Other 63 coefficients are AC component."
* **Quantisation:**
    * **Lossy step**.
    * Uses an **8x8 quantisation matrix** with 64 integer step-size parameters (1-255): "The 64 quantization step-size parameters for uniform quantization of the 64 DCT coefficients form an 8x8 quantization matrix. Each element in the quantization matrix is an integer between 1 and 255."
    * Each DCT coefficient $F(u,v)$ is divided by the corresponding quantiser step-size $Q(u,v)$ and rounded: "[Equation involving division and rounding]".
    * The **quantisation table used during encoding is required for decoding**: "For Encoding purpose we require the Quantization table used at the transmitter end and its specifications are required Sample quantization table for Quality=50 (Q50)".
* **Zig-Zag Ordering:**
    * The 64 quantised DCT coefficients in the 8x8 block are reordered into a **1D sequence** using a zig-zag pattern: "After Zig-Zag ordering the 2D image data is converted to 1D data."
    * Groups low-frequency coefficients (higher energy) at the beginning and high-frequency coefficients (often zero/near-zero after quantisation) at the end.
* **Entropy Coding:**
    * Lossless compression applied to the 1D sequence.
    * JPEG uses **Huffman coding**: "Entropy coding used in JPEG is HUFFMAN coding."
    * **Run-Length Encoding (RLE)** is applied before Huffman coding to efficiently represent sequences of zeros: "Before Going to the Huffman Coding we will apply run length coding on to the 1D data so as to decrease the number of bits."
    * RLE represents data by its value and run length (e.g., "1110011111" $\implies$ Value: "1 0 1", Run Lengths: "3 2 5").

## 4. Decoder Steps

* Reverses the encoding process.
* **Inverse Huffman and Run-Length Decoding:** Reconstructs the 1D sequence of quantised DCT coefficients.
* **Inverse Zig-Zag Ordering:** Rearranges the 1D sequence back into an 8x8 block.
* **Dequantisation:** Multiplies the quantised DCT coefficients by the corresponding values in the encoding quantisation matrix: "For Decoding purpose we require the Quantization table used at the transmitter end and its specifications are required Sample quantization table for Quality=50 (Q50)".
* **Inverse DCT (IDCT):** Applied to each 8x8 block to reconstruct the original pixel values: "Inverse DCT equation".

## 5. Performance Metrics

* **Compression Ratio (CR):** Ratio of original data size to compressed data size: "image raw in the bits ofNumber string compressed in the used bitsofNumber = CR".
* **Peak Signal to Noise Ratio (PSNR):** Measures the quality of the reconstructed image compared to the original (higher PSNR $\implies$ better quality). Involves Mean Squared Error (MSE) and maximum pixel value ($I_{max}$).

## 6. Disadvantages

* **Blocking Artefacts:** Visible block boundaries in the reconstructed image, especially at high compression ratios: "Blocking Artefacts Disadvantage of JPEG".

## 7. YCbCr Colour Space

* Often used in JPEG compression.
* MATLAB function for RGB to YCbCr conversion: `YCBCR = rgb2ycbcr(RGB)`.
* Separates RGB into:
    * Y (luminance - brightness)
    * Cb (blue-difference chrominance)
    * Cr (red-difference chrominance)
* JPEG often applies more aggressive compression to chrominance components due to lower human sensitivity to colour details.

This briefing document summarises the core concepts of JPEG compression, including standardisation, modes, encoding/decoding steps (lossy DCT focus), performance metrics, disadvantages, and the use of YCbCr colour space.

# Formulas

# JPEG Compression Formulas (Explicitly Stated)

This section details the formulas explicitly provided in the lecture excerpts for JPEG compression performance metrics. It also notes the mentioned equations for DCT and quantisation, although their full mathematical forms are not given.

## 1. Compression Ratio (CR)

* **Formula:**
    $\qquad CR = \frac{\text{Size of original (uncompressed) data}}{\text{Size of compressed data}}$
* **Source:** Mentioned as "image raw in the bits ofNumber string compressed in the used bitsofNumber = CR".

## 2. Peak Signal to Noise Ratio (PSNR)

* **Formula:**
    $\qquad PSNR = 10 \cdot \log_{10} \left( \frac{I_{max}^2}{MSE} \right)$
* **Description:** A measure of the quality of the reconstructed image compared to the original. Higher PSNR indicates better quality.

## 3. Mean Squared Error (MSE)

* **Formula:**
    $\qquad MSE = \frac{1}{M \cdot N} \sum_{i=0}^{M-1} \sum_{j=0}^{N-1} [I(i, j) - \hat{I}(i, j)]^2$
* **Where:**
    * $I$ is the original image.
    * $\hat{I}$ is the reconstructed image.
    * $M \cdot N$ is the total number of pixels in the image.

## 4. Forward DCT Equation

* **Mention:** Stated as being "use in the JPEG compression" and applied to 8x8 blocks.
* **Formula:** The specific mathematical formula is **not provided** in the excerpts. However, the general form of the 2D DCT for an $M \times N$ matrix $A$ is typically given by:
    $$B_{pq} = \alpha_p \alpha_q \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} A_{mn} \cos\left(\frac{\pi (2m+1)p}{2M}\right) \cos\left(\frac{\pi (2n+1)q}{2N}\right)$$
    where $\alpha_p$ and $\alpha_q$ are scaling factors. For JPEG (8x8 blocks, $M=N=8$), this becomes:
    $$F(u,v) = \frac{1}{4} C(u) C(v) \sum_{x=0}^{7} \sum_{y=0}^{7} f(x,y) \cos\left(\frac{(2x+1)u\pi}{16}\right) \cos\left(\frac{(2y+1)v\pi}{16}\right)$$
    where $C(u), C(v) = 1/\sqrt{2}$ for $u, v = 0$ and $1$ otherwise.

## 5. Quantisation

* **Description:** Each DCT coefficient $F(u,v)$ is divided by the corresponding quantiser step-size parameter $Q(u,v)$ from the quantisation matrix, and the result is rounded to the nearest integer.
* **Formula (Conceptual):**
    $\qquad F_q(u,v) = \text{round} \left( \frac{F(u,v)}{Q(u,v)} \right)$
* **Note:** The specific values within the quantisation matrix $Q(u,v)$ are not defined by a single formula in the JPEG standard but are typically provided by standard or custom tables.

## 6. Inverse DCT Equation

* **Mention:** Used in the decoder to reconstruct pixel values from the DCT coefficients.
* **Formula:** The specific mathematical formula is **not present** in the provided excerpts. However, the general form of the 2D Inverse DCT for an $M \times N$ matrix $B$ of DCT coefficients is:
    $$A_{mn} = \sum_{p=0}^{M-1} \sum_{q=0}^{N-1} \alpha_p \alpha_q B_{pq} \cos\left(\frac{\pi (2m+1)p}{2M}\right) \cos\left(\frac{\pi (2n+1)q}{2N}\right)$$
    For JPEG (8x8 blocks):
    $$f(x,y) = \frac{1}{4} \sum_{u=0}^{7} \sum_{v=0}^{7} C(u) C(v) F(u,v) \cos\left(\frac{(2x+1)u\pi}{16}\right) \cos\left(\frac{(2y+1)v\pi}{16}\right)$$
    where $C(u), C(v) = 1/\sqrt{2}$ for $u, v = 0$ and $1$ otherwise.

This compilation provides the explicitly stated formulas and context for other important equations used in JPEG compression as mentioned in the lecture notes.