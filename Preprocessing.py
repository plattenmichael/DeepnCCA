import SimpleITK as sitk
import glob
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image
import os
import errno

'''
#This file contains a script to convert all .nii files in image_path into one-channel jpeg images and save them in another file
#The img_path should lead to a folder that contains all your .nii files. 
'''

img_path = '/Users/yourcomputer/MRI/where_you_have_your_MRI/*'
dest_path = '/Users/yourcomputer/output/'

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

def histogram_normalization(image):

    w, h = image.shape
    unique_pixels = len(np.unique(image))
    image_histogram = np.histogram(image, bins=unique_pixels)

    total_pixels = np.sum(image_histogram[0])

    first_sum = 0
    second_sum = 0

    for i in range(len(image_histogram[0])):
        first_sum += image_histogram[0][i]
        if (first_sum / total_pixels) > 0.05:
            first_map_pixel = image_histogram[1][i]
            break

    for i in range(len(image_histogram[0]) - 1, 0, -1):
        second_sum += image_histogram[0][i]
        if (second_sum / total_pixels) > 0.05:
            second_map_pixel = image_histogram[1][i]
            break

    flat_image = image.flatten()

    # Map the pixels outside of our range to the min/max value(first_map_pixel, second_map_pixel)
    for i in range(len(flat_image)):
        if flat_image[i] < first_map_pixel:
            flat_image[i] = first_map_pixel
        if flat_image[i] > second_map_pixel:
            flat_image[i] = second_map_pixel

    # Then map the existing range (first_map_pixel, second_map_pixel) into the range (0, 1000)
    for i in range(len(flat_image)):
        flat_image[i] = translate(flat_image[i], first_map_pixel, second_map_pixel, 0, 1000)

    image = np.reshape(flat_image, (w, h))

    '''
    plt.hist(image, bins="auto")  # arguments are passed to np.histogram
    plt.title("Histogram with 'auto' bins")
    plt.show()
    '''

    return image

if __name__ == '__main__':

    #image_path = 'This is where you have your T2-weighted images'
    #dest_path_all = 'This is where you want the output'

    image_path = img_path
    dest_path_all = dest_path

    image_addrs = glob.glob(image_path)

    print(image_addrs)

    images = []
    image_names = []

    # Create lists where each row corresponds to the right image and label
    for addr in image_addrs:
        images.append(addr)

    for idx, image_addr in enumerate(images):

        print('Processing image {}'.format(image_addr))
        image_names.append(image_addr[len(image_path):-7])

        # Read and get numpy array from image/label
        image = sitk.GetArrayFromImage(sitk.ReadImage(image_addr))

        print(image.shape)
        mask_slice_idx = int(image.shape[0] // 2)
        #mask_variable = 0

        image = image[mask_slice_idx, :, :]  # Get the corresponding slice in the image

        # Normalize image
        norm_image = histogram_normalization(image)

        images[idx] = norm_image

    for image in images:
        print(image.shape)

    # Save the both-label-images
    for image_name, image in zip(image_names, images):
        plt.figure()
        plt.imshow(image)
        plt.show()
        plt.imsave(dest_path_all + image_name + '.jpeg', image, cmap='gray')
