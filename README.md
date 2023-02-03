# Random Forest Classifier (Non-GPU)
#### Omar Halawa (ohalawa@ucsd.edu) of the GenePattern Team @ Mesirov Lab - UCSD
\
The following repository is a GenePattern module written in Python 3, using the following [Docker image](https://hub.docker.com/layers/genepattern/notebook-python39/22.04/images/sha256-1182e33d0a4d944e676003b2d4a410ec3a197db13847292cedca441a0541513d?context=explore). 
\
It serves as a foundation for implementing the cuML-based GPU Random Forest Classifier.

It takes in two files, one for classifier feature data (.gct), and one for classifier target data (.cls). Then, it processes them into DataFrames and performs random forest classification on them using Scikit-learn's RandomForestClassifier, generating an accuracy score and a target prediction done on the feature dataset, outputting a results (.pred.odf) file. Created for module usage through optional arguments for classifier parameters. Designed for smooth implementation of other file type inputs and future features.

Documentation on usage and implementation is found [here](https://github.com/omarhalawa3301/randomforest/blob/main/docs/tutorial.md).
All source files, including iris ([.gct](https://github.com/omarhalawa3301/randomforest/blob/main/data/iris.gct), [.cls](https://github.com/omarhalawa3301/randomforest/blob/main/data/iris.cls)) and all_aml ([.gct](https://github.com/omarhalawa3301/randomforest/blob/main/data/all_aml_train.gct), [.cls](https://github.com/omarhalawa3301/randomforest/blob/main/data/all_aml_train.cls)) test datasets with [output examples](https://github.com/omarhalawa3301/randomforest/blob/main/data/example_output) ("examples," as the classifier utilizes randomness, so each run varies) are available for better reproducibility and portability. 
