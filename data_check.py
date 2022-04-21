import pandas as pd


def data_check(data):
    #  檢查資料是否短缺
    if len(data) == 7:
        for i in data.values():
            # 檢查資料格式是否正確
            if type(i) == type('a'):
                continue
            else:
                return "資料格式錯誤"

    else:
        return "資料短缺"


def data_check_null(data):
    # 檢查資料是否遺漏
    df = pd.DataFrame(data, index=[0])
    print(df.isnull().sum(axis=0))
