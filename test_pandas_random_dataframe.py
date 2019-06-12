import pandas.util.testing as tm
tm.N, tm.K = 15, 3

import numpy as np
np.random.seed(1)

df = tm.makeDataFrame()
print(df.head())

print([i for i in dir(tm) if i.startswith("make")])

"""
RESULT: random columns and values
                   A         B         C
LRmijlfpaq  1.923832  0.572392 -0.774052
bmhT8gzYuL  0.991091  0.759955  0.610019
sul8QCDoYe  0.380611  0.735682 -1.547081
xxPX3EGwnP -0.747766  1.013892 -0.204768
jh9w5ba8ri -1.317678 -0.738431 -1.468292
['makeBoolIndex', 'makeCategoricalIndex', 'makeCustomDataframe', 'makeCustomIndex', 'makeDataFrame', 'makeDateIndex', 'makeFloatIndex', 'makeFloatSeries', 'makeIntIndex', 'makeIntervalIndex', 'makeMissingCustomDataframe', 'makeMissingDataframe', 'makeMixedDataFrame', 'makeMultiIndex', 'makeObjectSeries', 'makePanel', 'makePeriodFrame', 'makePeriodIndex', 'makePeriodPanel', 'makePeriodSeries', 'makeRangeIndex', 'makeStringIndex', 'makeStringSeries', 'makeTimeDataFrame', 'makeTimeSeries', 'makeTimedeltaIndex', 'makeUIntIndex', 'makeUnicodeIndex']
"""
