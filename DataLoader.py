import glob

import matplotlib.pyplot as plt
import tensorflow as tf




class DataLoader():
    '''

    DataLoader takes a path to folder with both training and testing images. It will load, normalize, augment and parse
    these images into a Tensorflow Dataset-structure to be fed into the training and testing of the network

    '''

    def __init__(self, image_path, im_size=(512, 512), batch_size=1):
        '''

        Init function for class DataLoader

        :param image_path: Path to folder containing both training and testing images and labels
        :param im_size: Desired image size in tensorflow dataset
        :param images_as_jpeg: Indicates whether image_path contains .jpeg-images or .nii-images
        :param jpeg_path: Optional parameter to specify where to save jpeg-images to
        '''

        self.image_path = image_path
        self.im_size = im_size
        self.batch_size = batch_size

    def single_parser(self, filename):
        '''
        Function that parses image and corresponding mask from filename and mask_filename

        :param self: instance of DataLoader-class
        :param filename: the path to the image
        :return: image, mask
        '''

        image = tf.read_file(filename)
        image = tf.image.decode_jpeg(image, channels=1) # JPEG-images
        image = tf.image.flip_up_down(image)

        # Resize image and mask
        image = tf.image.resize_images(image, self.im_size)

        # Normalize image and mask
        image = tf.divide(image, tf.reduce_max(image))

        image = tf.cast(image, tf.float32)

        return image


    def parser(self, filename, mask_filename):
        '''
        Function that parses image and corresponding mask from filename and mask_filename

        :param self: instance of DataLoader-class
        :param filename: the path to the image
        :param mask_filename: the path to the corresponding image mask
        :return: image, mask
        '''

        image = tf.read_file(filename)
        image = tf.image.decode_image(image, channels=1) # JPEG-images
        image = tf.image.flip_up_down(image)

        mask = tf.read_file(mask_filename)
        mask = tf.image.decode_image(mask, channels=1)
        mask = tf.image.flip_up_down(mask)

        # Resize image and mask
        image = tf.image.resize_images(image, self.im_size)
        mask = tf.image.resize_images(mask, self.im_size)
        mask = tf.reshape(mask, [mask.shape[0], mask.shape[1]])  # Drop the third dimension

        # Normalize image and mask
        image = tf.divide(image, tf.reduce_max(image))
        mask = tf.divide(mask, tf.reduce_max(mask))

        image = tf.cast(image, tf.float32)
        mask = tf.cast(mask, tf.uint8)

        return image, mask


    def load_images(self, custom_image_path):
        '''
                If custom path is given, load from that folder and return iterable dataset

                :return: Tensorflow dataset of the images in path
                '''
        image_addrs = glob.glob(custom_image_path)
        images = []
        image_names = []

        print(image_addrs)

        for addr in image_addrs:
            images.append(addr)
            image_names.append(addr[len(custom_image_path)-6:-5])

        for img in images:
            print(img)

        # First create the training data from the splitted array
        dataset = tf.data.Dataset.from_tensor_slices(images)
        dataset = dataset.map(self.single_parser, num_parallel_calls=4)
        dataset = dataset.batch(batch_size=self.batch_size)
        dataset = dataset.prefetch(1)

        return image_names, dataset



















