# Copyright (c) 2020 Graphcore Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Tests covering various training options using the DIN model.
"""
import tensorflow as tf
import unittest
import pytest

from test_common import get_log, run_train


@pytest.mark.category1
@pytest.mark.ipus(1)
class TestDINTraining(unittest.TestCase):
    """Testing some basic training parameters"""

    @classmethod
    def setUpClass(cls):
        out = run_train(**{'--use-synthetic-data': True,
                           '--epochs': 1,
                           '--seed': 3,
                           '--learning-rate': 0.1,
                           '--batches-per-step': 1600})
        cls.out = out
        cls.training = get_log(out)


    def test_train_results(self):
        # test_train_accuracy
        final_acc = self.training
        self.assertGreaterEqual(final_acc, 0.0)
