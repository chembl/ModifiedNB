from sklearn.naive_bayes import BaseDiscreteNB
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.utils.validation import check_is_fitted
from sklearn.utils import check_array
from scipy.sparse import issparse
import numpy as np


class ModifiedNB(BaseDiscreteNB):
    """
    References
    ----------
    Xiaoyang Xia, Edward G. Maliski, Paul Gallant and David Rogers (2004)
    Classification of Kinase Inhibitors Using a Bayesian Model. 
    J. Med. Chem. 2004, 47, 4463 - 4470
    ----------
    Nidhi, Meir Glick, John W. Davies and Jeremy L. Jenkins (2006)
    Prediction of Biological Targets for Compounds Using Multiple-Category 
    Bayesian Models Trained on Chemogenomics Databases
    J. Chem. Inf. Model. 2006, 46, 1124 - 1133
    """
    def __init__(self, alpha=1.0, fit_prior=False, class_prior=None):
        self.alpha = alpha
        self.fit_prior = fit_prior
        self.class_prior = class_prior

    def _count(self, X, Y):
        """Count and smooth feature occurrences."""
        if np.any((X.data if issparse(X) else X) < 0):
            raise ValueError("Input X must be non-negative")
        self.feature_count_ += safe_sparse_dot(Y.T, X)
        self.class_count_ += Y.sum(axis=0)

    def _update_feature_log_prob(self, alpha):
        """Apply smoothing to raw counts and recompute log probabilities"""
        total_samples = self.class_count_.sum(axis=0)
        at = self.class_count_ / total_samples
        denom = self.feature_count_.sum(axis=0) * at.reshape(-1, 1)
        self.feature_log_prob_ = np.log((self.feature_count_ + alpha) / (denom + alpha))

    def _joint_log_likelihood(self, X):
        """Calculate the posterior log probability of the samples X"""
        check_is_fitted(self, "classes_")
        X = check_array(X, accept_sparse='csr')
        return (safe_sparse_dot(X, self.feature_log_prob_.T) + self.class_log_prior_)
