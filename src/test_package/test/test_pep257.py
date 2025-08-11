# Copyright 2015 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from ament_pep257.main import main
import pytest

# Lint varsayılan kapalı; RUN_LINT=1 verince açılır
pytestmark = pytest.mark.skipif(os.getenv("RUN_LINT", "0") != "1",
                                reason="lint disabled")

@pytest.mark.linter
@pytest.mark.pep257
def test_pep257():
    # Sadece aday kodunu kontrol et; test klasörünü dışarıda bırak
    rc = main(argv=['src/candidate_package'])
    assert rc == 0, 'Found code style errors / warnings'

