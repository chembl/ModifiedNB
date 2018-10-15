# ModifiedNB Model

Scikit-learn based implementation of Laplace corrected Naïve Bayes algorithm as described in:

    Prediction of Biological Targets for Compounds Using Multiple-Category Bayesian Models Trained on Chemogenomics Databases
    Nidhi,†, Meir Glick,‡, John W. Davies,‡ and, and Jeremy L. Jenkins*,‡
    Journal of Chemical Information and Modeling 2006 46 (3), 1124-1133
    DOI: 10.1021/ci060003g

## Installation

    python setup.py install

## Usage

Works exactly like any other Scikit-learn model.

    import numpy as np
    X = np.random.randint(5, size=(6, 100))
    y = np.array([1, 2, 3, 4, 5, 6])
    
    from ModifiedNB import ModifiedNB
    clf = ModifiedNB()
    clf.fit(X, y)
    print(clf.predict(X[2:3]))
