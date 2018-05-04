# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------
import qiime2.plugin

#TODO: Use these types to find some conversion
from q2_types.feature_data import (FeatureData, SampleData)

import q2_pressius as q2p

plugin = qiime2.plugin.Plugin(
    name='pressius',
    version=q2p.__version__,
    website='https://github.com/biocore/q2-pressius',
    short_description='Plugin for benchmarking 16s genome data.',
    package='q2_pressius',
    user_support_text=('https://github.com/biocore/'
                       'pressius/issues')
)
