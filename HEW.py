import cv2
import numpy as np


def pdf(image, histogram):
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            intensity = image[y, x]
            histogram[intensity] += 1


def cdf(histogram, cumulative_histogram):
    cumulative_histogram[0] = histogram[0]

    for i in range(1, 256):
        cumulative_histogram[i] = histogram[i] + cumulative_histogram[i - 1]


def histogram_display(histogram, name):
    histogram_width = 1000
    histogram_height = 300
    bin_width = histogram_width // 256

    histogram_image = 255 * np.ones((histogram_height, histogram_width, 3), dtype=np.uint8)

    maximum_intensity = max(histogram)

    for i in range(256):
        height = int(histogram[i] / maximum_intensity * histogram_height)
        cv2.rectangle(histogram_image, (i * bin_width, histogram_height - height),
                      ((i + 1) * bin_width - 1, histogram_height - 1), (0, 0, 0), -1)

    cv2.imshow(name, histogram_image)
    cv2.waitKey(1)


camera = cv2.VideoCapture(0)

cv2.namedWindow("Original Image")
cv2.namedWindow("Equalized Image")
cv2.namedWindow("Original Histogram")
cv2.namedWindow("Equalized Histogram")

cv2.resizeWindow("Original Image", 640, 480)
cv2.resizeWindow("Equalized Image", 640, 480)
cv2.resizeWindow("Original Histogram", 1000, 300)
cv2.resizeWindow("Equalized Histogram", 1000, 300)

while True:
    ret, rgb_image = camera.read()

    image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2GRAY)

    histogram = [0] * 256
    size = image.shape[0] * image.shape[1]
    alpha = 255.0 / size

    pdf(image, histogram)

    PRk = [0.0] * 256
    for i in range(256):
        PRk[i] = histogram[i] / size

    cumulative_histogram = [0] * 256
    cdf(histogram, cumulative_histogram)

    Sk = [0] * 256
    for i in range(256):
        Sk[i] = int(cumulative_histogram[i] * alpha)

    PSk = [0.0] * 256
    for i in range(256):
        PSk[Sk[i]] += PRk[i]

    final_values = [0] * 256
    for i in range(256):
        final_values[i] = int(PSk[i] * 255)

    final_image = np.zeros((image.shape[0], image.shape[1]), dtype=np.uint8)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            final_image[y, x] = Sk[image[y, x]]

    cv2.imshow("Original Image", image)
    histogram_display(histogram, "Original Histogram")

    cv2.imshow("Equalized Image", final_image)
    histogram_display(final_values, "Equalized Histogram")

    cv2.imwrite("EqualizedImage.jpg", final_image)

    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
        break

camera.release()
cv2.destroyAllWindows()
