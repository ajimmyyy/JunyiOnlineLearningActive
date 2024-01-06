from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from ast import literal_eval
from tqdm import tqdm
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict

class SelectFrequentItems:
    def DivideDataFrame(self, dataFrame, selectionRow = "learning_stage"):
        groupedDf = dataFrame.groupby(selectionRow)
        return {group: df for group, df in groupedDf}

    def ReshapeFrame(self, dataFrame, selectDf, superclass = "uuid", subclass = "ucid"):
        filteredDf = dataFrame[dataFrame["is_correct"] == False]

        tqdm.pandas(desc="filting...")
        df = filteredDf.groupby(superclass)[subclass].progress_apply(list).reset_index()

        tqdm.pandas(desc="Reshape...")
        df[subclass] = df[subclass].progress_apply(self.__FilterList, args = (selectDf, subclass,))

        df = df[df[subclass].apply(len) > 0]
        return df
    
    def StatisticsFrequent(self, dataFrame, frequentClass = "ucid"):        
        uniqueWrongQuestions = defaultdict(int)
        for sublist in dataFrame[frequentClass]:
            for qid in set(sublist):
                uniqueWrongQuestions[qid] += 1

        df = pd.DataFrame(list(uniqueWrongQuestions.items()), columns=['ucid', 'wrong_count'])
        return df
    
    def FPTree(self, dataFrame, frequentClass = "ucid", minSupport = 0.2):        
        te = TransactionEncoder()
        teAry = te.fit(dataFrame[frequentClass]).transform(dataFrame[frequentClass])

        fpDf = pd.DataFrame(teAry, columns=te.columns_)
        frequentItemsets = fpgrowth(fpDf, min_support = minSupport, use_colnames = True)

        frequentItemsets['itemsets'] = frequentItemsets['itemsets'].apply(lambda x: list(x))
        return frequentItemsets
    
    def DrawBarPlot(self, dataFrame, x, y, title):
        df = dataFrame.sort_values(by = y)

        fig = plt.figure(figsize=(32,25))
        plt.bar(df[x], df[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.title(title)

        return fig
    
    def FindMaxSubset(self, dataFrame):
        remove = []
        for i, row in dataFrame.iterrows():
            for j, otherRow in dataFrame.iterrows():
                if i != j and set(row['itemsets']).issubset(set(otherRow['itemsets'])):
                    remove.append(i)
        filteredDf = dataFrame.drop(index=remove).reset_index(drop=True)
        return filteredDf
    
    def MapIdsToNames(self, dataFrame, problemDf, idCol = 'ucid', nameCol = 'content_pretty_name'):
        dataFrame['itemsets'] = dataFrame['itemsets'].apply(self.__mapRowIdToName, args = (problemDf, idCol, nameCol,))
        return dataFrame
        
    def __mapRowIdToName(self, itemset, problemDf, idCol, nameCol):
        return frozenset(problemDf[nameCol][problemDf[idCol].isin(itemset)])

    def __FilterList(self, row, selectDf, subclass):
        return [x for x in row if x in selectDf[subclass].tolist()]