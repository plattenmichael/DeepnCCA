# DeepCC
This is a tool that extracts the intracranial and corpus callosum area as a biomarker, normalized corpus callosum, for neurodegeneration in multiple sclerosis.

In the required.txt file you will find the versions of the tools used to run the model. It is important that you are using the correct environment, otherwise you may receive errors.

#Instructions:

#Pre-processing

The first step is to extract the middle slice from your T2-weighted MRI sequence. For this you will apply the script "Preprocessing.py". This script will extract the middle slice, pre-process and reshape the target slice and make it compatible with the DeepCC model. You have to make sure to fill in your source path (where your MRIs are located) as well as the destination path (where you want the output). Below is an example of the paths:

    img_path = '/Users/yourcomputer/MRI/where_you_have_your_MRI'
    dest_path = '/Users/yourcomputer/output'

After this, we highly recommend you control your data as to make sure that the middle slice actually represents something close to the anatomical middle. Structures that speak for an anatomical middle are: the cerebral aqueduct, fornix, superior/inferior colliculus, a well-defined corpus callosum.


#The Model

You are now ready to apply the model on your data. In the file "Main" you will enter the path to where your pre-processed images are. You will also add the path to the two models (corpus callosum and brain). The predictor will combine these two models and output the segmentation along with the normalized corpus callosum value.

    data_path_b, data_path_cc, image_path = '/path_to_images_to_be_segmented/*.jpeg'
    model_corpus_callosum = '/path_to_the_saved_model_corpus_callosum/model/'
    model_brain = '/path_to_the_saved_model_brain/model/'

Download the two models here: 
https://ki.box.com/s/r3og7cjrpxqtfd2u185jo9od5wn5rh4i
https://ki.box.com/s/o3eanuvv86d1hkyn1axchejbwbhjqd1m

