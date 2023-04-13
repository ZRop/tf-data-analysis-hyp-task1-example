import numpy as np
import plotly.graph_objects as go
import pandas as pd
from scipy.stats import norm
from scipy.stats import ttest_ind
from statsmodels.stats.weightstats import ztest
import random

chat_id = 672508499 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, #покупка
             x_cnt: int, #Заявка
             y_success: int, 
             y_cnt: int) -> bool:

    data1 = [0]*int(x_cnt)
    data2 = [0]*int(y_cnt)

    for i in range(x_success):
        idx = random.randint(0, x_cnt-1)
        while data1[idx] == 1:
            idx = random.randint(0, x_cnt-1)
        data1[idx] = 1

    for i in range(y_success):
        idx = random.randint(0, y_cnt-1)
        while data2[idx] == 1:
            idx = random.randint(0, y_cnt-1)
        data2[idx] = 1

    ttest1 = ztest(data1,data2)
    print(ttest1[1])

    if ttest1[1] < 0.1:
        return True
    else:
        return False
    
    
