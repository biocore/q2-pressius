# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
from setuptools import setup, find_packages


setup(
    name="q2-pressius",
    version="2018.4.0.dev0",
    packages=find_packages(),
    author="Kumar Thurimella",
    author_email="kthurimella@gmail.com",
    description="Benchmarking 16s genome matching",
    entry_points={
        "qiime2.plugins":
        ["q2-pressius=q2_pressius.plugin_setup:plugin"]
    },
    license='BSD-3-Clause',
    package_data={
        'q2_pressius.tests': ['data/*']}
)
