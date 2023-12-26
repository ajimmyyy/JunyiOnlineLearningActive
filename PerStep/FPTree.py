from Model.SelectFrequentItems import SelectFrequentItems
from MakeFile.FileSaver import FileSaver
from configparser import ConfigParser
import pandas as pd

if __name__ == "__main__":
    _configPath = "PerStep/config.ini"
    _config = ConfigParser()
    _config.read(_configPath)

    # 決定最小支持度
    _selectFrequentItems = SelectFrequentItems()
    _elementaryWrongCount = pd.read_csv(_config["Paths"]["ELEMENTARY_WRONG_FREQ_PATH"])
    _juinorWrongCount = pd.read_csv(_config["Paths"]["JUNIOR_WRONG_FREQ_PATH"])
    _elementaryGroupedDf = pd.read_csv(_config["Paths"]["ELEMENTARY_LOG_PROBLEM_PATH"])
    _juinorGroupedDf = pd.read_csv(_config["Paths"]["JUNIOR_LOG_PROBLEM_PATH"])
    
    _elementaryMinSupport = _elementaryWrongCount["wrong_count"].quantile(0.99) / len(_elementaryGroupedDf.index)
    _juinorMinSupport = _juinorWrongCount["wrong_count"].quantile(0.99) / len(_juinorGroupedDf.index)

    print("elementary min support: ", _elementaryMinSupport)
    print("juinor min support: ", _juinorMinSupport)

    # FPTree
    _elementaryFrequentItems = _selectFrequentItems.FPTree(_elementaryGroupedDf, minSupport = _elementaryMinSupport)
    _juinorFrequentItems = _selectFrequentItems.FPTree(_juinorGroupedDf, minSupport = _juinorMinSupport)

    FileSaver.SaveDataframe(_elementaryFrequentItems, _config["Paths"]["ELEMENTARY_FREQUENT_ITEMSET_PATH"])
    FileSaver.SaveDataframe(_juinorFrequentItems, _config["Paths"]["JUNIOR_FREQUENT_ITEMSET_PATH"])