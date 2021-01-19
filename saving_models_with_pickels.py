""" This works with the concept of picking.. That is saving a processed data from the memory to a file to be used later """

import pickle

models_filename = ""


# Saving to the Pickle file
with open(models_filename, 'wb') as f:
    pickle.dump(clf, f)


# Using the saved model
pickle_model_in = open(models_filename, 'rb')

clf = pickle.load(pickle_model_in)









pickle_model_in.close()