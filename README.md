# DeepCC
This is a tool that extracts the intracranial and corpus callosum area as a biomarker, normalized corpus callosum, for neurodegeneration in multiple sclerosis.

#Instructions:

#Pre-processing

The first step is to extract the middle slice from your T2-weighted MRI sequence. For this you will apply the script "convert_nii_to_jpeg_no_label.py". This script will extract the middle slice, pre-process and reshape the target slice and make it compatible with the DeepCC model. You have to make sure to fill in your source path (where your MRIs are located) as well as the destination path (where you want the output). After this, we highly recommend you control your data as to make sure that the middle slice actually represents something close to the anatomical middle.


#The Model

You are now ready to apply the model on your data. In the file "Main" you will enter the path to where your pre-processed images are. You will also add the path to the two models (corpus callosum and brain). The predictor will combine these two models and output the segmentation along with the normalized corpus callosum value. 
