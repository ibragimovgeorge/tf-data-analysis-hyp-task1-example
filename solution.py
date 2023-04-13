import pandas as pd
import numpy as np


chat_id = 201321241 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    
    return (x_success/x_cnt)>(y_success/y_cnt*1.02) # Ваш ответ, True или False
