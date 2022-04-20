from data_check import data_check


def test_data_check_type():
    a = {"ad_network": "FOO",
         "date": "2019-06-05",
         "app_name": "LINETV",
         "unit_id": "55665201314",
         "request": 100,
         "revenue": "0.00365325",
         "imp": "23"}

    assert data_check(a) == "資料格式錯誤"


def test_data_check_len():
    a = {"ad_network": "FOO",
         "date": "2019-06-05",
         "app_name": "LINETV",
         "unit_id": "55665201314",
         "revenue": "0.00365325",
         "imp": "23"}

    assert data_check(a) == "資料短缺"
