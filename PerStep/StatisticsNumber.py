from Model.SelectFrequentItems import SelectFrequentItems
from MakeFile.FileSaver import FileSaver
from configparser import ConfigParser
from ast import literal_eval
import pandas as pd

if __name__ == "__main__":
    _configPath = "PerStep/config.ini"
    _config = ConfigParser()
    _config.read(_configPath)

    # 統計題目出現次數
    _selectFrequentItems = SelectFrequentItems()
    _elementaryGroupedDf = pd.read_csv(_config["Paths"]["ELEMENTARY_LOG_PROBLEM_PATH"])
    _juinorGroupedDf = pd.read_csv(_config["Paths"]["JUNIOR_LOG_PROBLEM_PATH"])

    _elementaryGroupedDf['ucid'] = _elementaryGroupedDf['ucid'].apply(literal_eval)
    _juinorGroupedDf['ucid'] = _juinorGroupedDf['ucid'].apply(literal_eval)

    _elementaryWrongCount = _selectFrequentItems.StatisticsFrequent(_elementaryGroupedDf)
    _juinorWrongCount = _selectFrequentItems.StatisticsFrequent(_juinorGroupedDf)

    _elementaryFig = _selectFrequentItems.DrawBarPlot(_elementaryWrongCount, "ucid", "wrong_count", "wrong frequency")
    _juinorFig = _selectFrequentItems.DrawBarPlot(_juinorWrongCount, "ucid", "wrong_count", "wrong frequency")
    FileSaver.SavePlot(_elementaryFig, _config["Paths"]["ELEMENTARY_WRONG_FREQ_PATH"])
    FileSaver.SavePlot(_juinorFig, _config["Paths"]["JUNIOR_WRONG_FREQ_PATH"])