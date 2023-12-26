import pandas as pd
from Model.SelectFrequentItems import SelectFrequentItems
from ast import literal_eval


_selectFrequentItems = SelectFrequentItems()

_elementaryGroupedDf = pd.read_csv("Data/Processed/user_problem_list/user_elementary_problem_list.csv")
_juinorGroupedDf = pd.read_csv("Data/Processed/user_problem_list/user_junior_problem_list.csv")

# 決定最小支持度
_elementaryMinSupport = 0.03
_juinorMinSupport = 0.03

print("elementary min support: ", _elementaryMinSupport)
print("juinor min support: ", _juinorMinSupport)

print(type(_elementaryGroupedDf['ucid'][0]))
_elementaryGroupedDf['ucid'].apply(literal_eval)
_juinorGroupedDf['ucid'].apply(literal_eval)
print(_elementaryGroupedDf['ucid'][0])
# FPTree
_elementaryFrequentItems = _selectFrequentItems.FPTree(_elementaryGroupedDf, minSupport = _elementaryMinSupport)
_juinorFrequentItems = _selectFrequentItems.FPTree(_juinorGroupedDf, minSupport = _juinorMinSupport)

print("true")

_elementaryFrequentItems = _selectFrequentItems.FindMaxSubset(_elementaryFrequentItems)
_juinorFrequentItems = _selectFrequentItems.FindMaxSubset(_juinorFrequentItems)