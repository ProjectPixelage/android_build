# Copyright (C) 2023 The Android Open Source Project
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

import os
import pathlib

DEFAULT_REPORT_DIR = "benchmarks"

def get_root():
    top_dir = os.environ.get("ANDROID_BUILD_TOP")
    if top_dir:
        return pathlib.Path(top_dir).resolve()
    d = pathlib.Path.cwd()
    while True:
        if d.joinpath("build", "soong", "soong_ui.bash").exists():
            return d.resolve().absolute()
        d = d.parent
        if d == pathlib.Path("/"):
            return None