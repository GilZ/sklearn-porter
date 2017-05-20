# -*- coding: utf-8 -*-

from unittest import TestCase
import numpy as np
import random

from sklearn.svm.classes import SVC

from ..Classifier import Classifier
from ...language.PHP import PHP


class SVCPHPTest(PHP, Classifier, TestCase):

    def setUp(self):
        super(SVCPHPTest, self).setUp()
        mdl = SVC(C=1., kernel='rbf',
                  gamma=0.001,
                  random_state=0)
        self._port_model(mdl)

    def tearDown(self):
        super(SVCPHPTest, self).tearDown()

    def test_rbf_kernel_w_binary_data(self):
        self.load_binary_data()
        clf = SVC(C=1., kernel='rbf',
                  gamma=0.001,
                  random_state=0)
        self._port_model(clf)
        Y, Y_py = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.N_RANDOM_TESTS):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            Y.append(self.make_pred_in_custom(x))
            Y_py.append(self.make_pred_in_py(x))
        self.assertListEqual(Y, Y_py)

    def test_linear_kernel(self):
        clf = SVC(C=1., kernel='linear',
                  gamma=0.001,
                  random_state=0)
        self._port_model(clf)
        Y, Y_py = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.N_RANDOM_TESTS):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            Y.append(self.make_pred_in_custom(x))
            Y_py.append(self.make_pred_in_py(x))
        self.assertListEqual(Y, Y_py)

    def test_linear_kernel_w_binary_data(self):
        self.load_binary_data()
        clf = SVC(C=1., kernel='linear',
                  gamma=0.001,
                  random_state=0)
        self._port_model(clf)
        Y, Y_py = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.N_RANDOM_TESTS):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            Y.append(self.make_pred_in_custom(x))
            Y_py.append(self.make_pred_in_py(x))
        self.assertListEqual(Y, Y_py)

    def test_poly_kernel(self):
        clf = SVC(C=1., kernel='poly',
                  gamma=0.001,
                  random_state=0)
        self._port_model(clf)
        Y, Y_py = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.N_RANDOM_TESTS):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            Y.append(self.make_pred_in_custom(x))
            Y_py.append(self.make_pred_in_py(x))
        self.assertListEqual(Y, Y_py)

    def test_poly_kernel_w_binary_data(self):
        self.load_binary_data()
        clf = SVC(C=1., kernel='poly',
                  gamma=0.001,
                  random_state=0)
        self._port_model(clf)
        Y, Y_py = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.N_RANDOM_TESTS):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            Y.append(self.make_pred_in_custom(x))
            Y_py.append(self.make_pred_in_py(x))
        self.assertListEqual(Y, Y_py)

    def test_sigmoid_kernel(self):
        clf = SVC(C=1., kernel='sigmoid',
                  gamma=0.001,
                  random_state=0)
        self._port_model(clf)
        Y, Y_py = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.N_RANDOM_TESTS):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            Y.append(self.make_pred_in_custom(x))
            Y_py.append(self.make_pred_in_py(x))
        self.assertListEqual(Y, Y_py)

    def test_sigmoid_kernel_w_binary_data(self):
        self.load_binary_data()
        clf = SVC(C=1., kernel='sigmoid',
                  gamma=0.001,
                  random_state=0)
        self._port_model(clf)
        Y, Y_py = [], []
        min_vals = np.amin(self.X, axis=0)
        max_vals = np.amax(self.X, axis=0)
        for n in range(self.N_RANDOM_TESTS):
            x = [random.uniform(min_vals[f], max_vals[f]) for f in
                 range(self.n_features)]
            Y.append(self.make_pred_in_custom(x))
            Y_py.append(self.make_pred_in_py(x))
        self.assertListEqual(Y, Y_py)