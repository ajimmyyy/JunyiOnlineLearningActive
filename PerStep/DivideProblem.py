from Model.SelectFrequentItems import SelectFrequentItems
from MakeFile.FileSaver import FileSaver
from configparser import ConfigParser
import pandas as pd

if __name__ == "__main__":
    _configPath = "PerStep/config.ini"
    _config = ConfigParser()
    _config.read(_configPath)

    # 區分初階與進階題目
    _selectFrequentItems = SelectFrequentItems()
    _contentDf = pd.read_csv(_config["Paths"]["PROBLEM_CONTENT_PATH"])

    _dfsDict = _selectFrequentItems.DivideDataFrame(_contentDf)

    FileSaver.SaveDataframe(_dfsDict["elementary"], _config["Paths"]["ELEMENTARY_PROBLEM_CONTENT_PATH"])
    FileSaver.SaveDataframe(_dfsDict["junior"], _config["Paths"]["JUNIOR_PROBLEM_CONTENT_PATH"])