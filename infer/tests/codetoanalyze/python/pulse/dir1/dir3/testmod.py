# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

import random
import taint

tainted_global3 = taint.source()
untainted_global3 = random.random()
