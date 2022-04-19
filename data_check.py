import pandas as pd


def data_check(data):
    df = pd.DataFrame(data, index=[0])
    print(df.isnull().sum(axis=0))
    # 檢查資料是否有遺漏值

    if len(data) == 7:
        #  檢查資料是否短缺
        for i in data.values():
            # 檢查資料格式是否正確
            if type(i) == type('a'):
                continue
            else:
                print(f"{i}:資料有問題")
                break
    else:
        print("資料短缺")
