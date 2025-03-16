# Histogram equalization
To understand this concept you need to know about the following concepts:
1. Histogram
2. CDF plot
## Histogram
Histogram tells the distribution of intensity of the image. Images are plotted in histogram based on two types. 
1. Pixel intensity vs Frequency of pixels in each grey level
2. Pixel intensity vs Probability of occurence of that grey level.
In the histogram equalization we use the 2nd type.
## CDF plot
CDF is abbreviated as Cumulative Distribution Function. It is a probability concept that is used to describe the probability of a random variable X taking a value less than or equal to a certain value. $F(X) = P(X \leq x)$
where $F(X)$ - cumulative sum of all probabilities up to X
$P(X \leq x)$ - probability of `X` takes the value less than or equal to `x`

In the histogram equalization, we need CDF plot to be gradually increased, because if the intensity of the image is equalized then the each pixel is at equal value so if it adds up then it will gradually grow like 1,2,4,6,8,10 etc...

The values provided in this will range from 0 to 1 because we use 2nd type of histogram. To convert it into 0 to 255 greyscale value we use the formula $New_Intensity = \frac{CDF-minCDF}{TotalPixel - MinCDF} * 255$
## Working
1. Calculate the histogram for the image
2. Calculate the CDF of the histogram
3. Intensity mapping
## Resources
1. [OpenCV Python Histogram Equalization and CLAHE| YouTube](https://youtu.be/tn2kmbUVK50?si=DwWgGgz1rrJymOJg)
2. [OpenCV Histogram Equalization | Blog](https://pyimagesearch.com/2021/02/01/opencv-histogram-equalization-and-adaptive-histogram-equalization-clahe/)
3. [CLAHE | OpenCV Docs](https://docs.opencv.org/4.x/d5/daf/tutorial_py_histogram_equalization.html)