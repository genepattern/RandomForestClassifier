#!/usr/bin/env python3

# Importing necessary functions for Classifier processing
from rnd_forest_functions import *

# Importing modules
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

"""
    Name:          Omar Halawa
    Email:         ohalawa@ucsd.edu
    File name:     Classifier.py
    Project:       RandomForest (Non-GPU)
    Description:   Class file that contains the attributes and logic
                   of the Random Forest Classifier's data classifying process.
                   Future implementation: contain methods of Classifier object. 
    References:    scholarworks.utep.edu/cs_techrep/1209/
                   datacamp.com/tutorial/random-forests-classifier-python
                   tiny.cc/7cl2vz
"""


# Initializing Classifier class 
class Classifier:

    # Creating class constructor for initialization
    # Contains self, feature, target, and Random Forest Classifier arguments
    def __init__(self, feature, target):

        """ Classifier class initializer/constructor
        Arguments:
            self:    For self-reference
            feature: Processed DataFrame of feature data file
            target:  Processed DataFrame of target data file
        Returns:     Nothing, class initializer
        """

        # Assigning feature and target to parsed arguments in initializer
        self.feature = feature
        self.target = target

        # Obtaining debugging boolean and test/training float split 
        debug_value = get_debug()
        test_value=get_test_size()

        # Assigning Random Forest Classifier arguments using getter methods
        # Descriptions available in rnd_forest_params.py
        bootstrap_value = get_bootstrap()
        ccp_value = get_ccp()
        weight_value = get_class_weight()
        criteria_value = get_criterion()
        depth_value = get_max_depth()
        feature_value = get_max_features()
        node_value = get_max_nodes()
        sample_value = get_max_samples()
        impurity_value = get_impurity()
        leaf_value = get_min_samples_leaf()
        split_value = get_split()
        fraction_value = get_min_weight_fraction()
        estimator_value = get_estimators()
        job_value = get_jobs()
        oob_value = get_oob()
        random_value = get_random()
        verbose_value = get_verbose()
        warm_value = get_warm()

        # Creating instance of Random Forest Classifier with arguments parsed
        clf = RandomForestClassifier(bootstrap=bootstrap_value,
        ccp_alpha=ccp_value, class_weight=weight_value, 
        criterion=criteria_value, max_depth=depth_value,
        max_features=feature_value, max_leaf_nodes=node_value,
        max_samples=sample_value, min_impurity_decrease=impurity_value,
        min_samples_leaf=leaf_value, min_samples_split=split_value,
        min_weight_fraction_leaf=fraction_value, n_estimators=estimator_value,
        n_jobs=job_value, oob_score=oob_value, random_state=random_value,
        verbose=verbose_value, warm_start=warm_value)

        # Printing list of passed-in values if verbosity is on (value greater than 0)
        print("Test/Training Split is: ", test_value * 100, "/", (1-test_value) * 100)
        print()
        print("Classifier parameter values: ")
        print(clf.get_params(True))
        print()

        # Setting values to test and training feature and target dataframes
        # For 30/70 Test/Training split default, see first source
        X_train, X_test, y_train, y_test = train_test_split(self.feature.T,
                                        self.target.T, test_size=test_value)

        # Training the model with training sets of X and y
        # Raveling y_train's values for data classification format, see last reference
        clf.fit(X_train, y_train.values.ravel())

        # Predicting using test features
        y_pred=clf.predict(X_test)

        # Classifier accuracy check
        accuracy = accuracy_score(y_test, y_pred) * 100
        print(f"Accuracy score: " + "{0:.2f}%".format(accuracy))
        print()
    
        # Printing prediction of feature training set
        print("Prediction on feature training set: ")
        print(clf.predict(X_train))

    # TODO, implement prediction of other user-input feature data
    # def predict(self, df):
    #     """ Function of Classifier class that parses input argument df to
    #         Scikit Random Forest Classifier's predict method

    #     Argument:
    #         self:     For self-reference
    #         df:       DataFrame to predict withobject's classification
    #     Returns:
    #         Classifier.clf.predict(df):  Prediction output data to ease printing
    #     """

    #     return Classifier.clf.predict(df)