from sklearn.externals import joblib

# Saving a model
file_name = "my_model.sklearn"
joblib.dump(clf, file_name)

# Opening the model your have saved in the same dir
clf = joblib.load(file_name)