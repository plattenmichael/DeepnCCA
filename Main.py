
from DataLoader import DataLoader
from load_model_and_predict import Predictor


#Dataloader was also used in the training of the algorithm, and thus had several functions. For predicting with the model, the below pathways are not being called.

data_path_b = data_path_cc = image_path = '/path_to_images_to_be_segmented/*.jpeg'
model_corpus_callosum = '/path_to_the_saved_model_corpus_callosum/model/'
model_brain = '/path_to_the_saved_model_brain/model/'

dl_b = DataLoader(data_path_b, im_size=(256, 256))
dl_c = DataLoader(data_path_cc, im_size=(256, 256))


#This calls the model predictor.

prd = Predictor(dl_c, image_path)
prd.load_and_predict_both_models(model_paths=[model_corpus_callosum,
                                model_brain])
