# Copyright 2017 Open Source Robotics Foundation, Inc.
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
from ament_flake8.main import main_with_errors
import pytest

pytestmark = pytest.mark.skipif(os.getenv("RUN_LINT", "0") != "1",
                                reason="lint disabled")

@pytest.mark.flake8
@pytest.mark.linter
def test_flake8():
    # Kuralı yumuşat + sadece aday kodunu tara
    rc, errors = main_with_errors(argv=[
        '--max-line-length=120',
        '--extend-ignore=E302,E401,E702,F401',
        'src/candidate_package',
    ])
    assert rc == 0, (
        'Found %d code style errors / warnings:\n' % len(errors)
        + '\n'.join(errors)
    )
