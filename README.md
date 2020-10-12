# DeepCC
This is a tool that extracts the intracranial and corpus callosum area as a biomarker, normalized corpus callosum, for neurodegeneration in multiple sclerosis.

#Instructions:
The first step is to extract the middle slice from your T2-weighted MRI sequence. For this you will apply the script "convert_nii_to_jpeg_no_label.py". What this script does is that it will extract the middle slice, pre-process and reshape the target slice and make it compatible with the DeepCC model.
