import cv2
import numpy as np


def color_filter(image, lower_bound, upper_bound):
    # Convert image to HSV format
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of colors to filter
    lower_color = np.array(lower_bound)
    upper_color = np.array(upper_bound)

    # Create a mask using the specified color range
    mask = cv2.inRange(hsv_image, lower_color, upper_color)

    # Apply the mask to the original image
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    return filtered_image

def color_filter2(image, lower_bound1, upper_bound1, lower_bound2, upper_bound2):
    # Convert image to HSV format
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the range of colors to filter
    lower_color1 = np.array(lower_bound1)
    upper_color1 = np.array(upper_bound1)
    lower_color2 = np.array(lower_bound2)
    upper_color2 = np.array(upper_bound2)

    # Create a mask using the specified color range
    mask1 = cv2.inRange(hsv_image, lower_color1, upper_color1)
    mask2 = cv2.inRange(hsv_image, lower_color2, upper_color2)

    # Combine the masks
    mask = cv2.bitwise_or(mask1, mask2)

    # Apply the mask to the original image
    filtered_image = cv2.bitwise_and(image, image, mask=mask)

    return filtered_image

def main():
    # Load the image
    image = cv2.imread('1.jpg')

    # # Define the lower and upper bounds of the color to filter (in HSV format)
    # lower_bound = [36, 0, 0]  # Example: lower bound for blue color
    # upper_bound = [86, 255, 255]  # Example: upper bound for blue color
    #
    #
    # # Apply the color filter
    # filtered_image = color_filter(image, lower_bound, upper_boundâ
    #
    # # Resize the images
    # image = cv2.resize(image, (600, 600))
    # filtered_image = cv2.resize(filtered_image, (600, 600))


    # Define the lower and upper bounds of the color to filter (in HSV format)
    lower_bound1 = [0, 50, 50]  # Lower bound for red color range 1
    upper_bound1 = [11, 255, 255]  # Upper bound for red color range 1
    lower_bound2 = [175, 50, 50]  # Lower bound for red color range 2
    upper_bound2 = [180, 255, 255]  # Upper bound for red color range 2

    # Apply the color filter
    filtered_image = color_filter2(image, lower_bound1, upper_bound1, lower_bound2, upper_bound2)

    # Resize the images
    image = cv2.resize(image, (600, 600))
    filtered_image = cv2.resize(filtered_image, (600, 600))


    # Create resizable windows
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Filtered Image', cv2.WINDOW_NORMAL)

    # Display the original and filtered images
    cv2.imshow('Original Image', image)
    cv2.imshow('Filtered Image', filtered_image)

    # Resize the windows
    cv2.resizeWindow('Original Image', 600, 600)
    cv2.resizeWindow('Filtered Image', 600, 600)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
