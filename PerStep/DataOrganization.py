from Model.SelectFrequentItems import SelectFrequentItems
from MakeFile.FileSaver import FileSaver
from configparser import ConfigParser
import pandas as pd

if __name__ == "__main__":
    _configPath = "PerStep/config.ini"
    _config = ConfigParser()
    _config.read(_configPath)

    # 資料整理
    _selectFrequentItems = SelectFrequentItems()
    _logProblemDf = pd.read_csv(_config["Paths"]["LOG_PROBLEM_PATH"])
    _elementarydfs = pd.read_csv(_config["Paths"]["ELEMENTARY_PROBLEM_CONTENT_PATH"])
    _juniordfs = pd.read_csv(_config["Paths"]["JUNIOR_PROBLEM_CONTENT_PATH"])

    _elementaryGroupedDf = _selectFrequentItems.ReshapeFrame(_logProblemDf, _elementarydfs)
    _juinorGroupedDf = _selectFrequentItems.ReshapeFrame(_logProblemDf, _juniordfs)

    FileSaver.SaveDataframe(_elementaryGroupedDf, _config["Paths"]["ELEMENTARY_LOG_PROBLEM_PATH"])
    FileSaver.SaveDataframe(_juinorGroupedDf, _config["Paths"]["JUNIOR_LOG_PROBLEM_PATH"])