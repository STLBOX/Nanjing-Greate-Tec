import pandas as pd
import numpy as np
import torch
from visualization import plot_curve
from filter import *


def dataFrameAppend(data: pd.DataFrame, columns:dict, file_name: str):
    for key,value in columns.items():
        data[key] = value
    data.to_excel(file_name, index=False)


def print_distribution(data, points=[0.5,1,2,3,97,98,99,99.5]):
    for point in points:
        print(f"分位数{point}:",np.percentile(data, point))
    data_inc = (np.roll(data, -1) - data)[:-1]
    for point in points:
        print(f"增量分位数{point}:",np.percentile(data_inc, point))


def CalculateThermalEfficiency(CO, Cfh, O2, Etem, INtem):
    """
    计算锅炉热效率
    :param CO:
    :param Cfh:
    :param O2:
    :param Etem:
    :param INtem:
    :return:
    """
    Mar = 7.6/100  # 收到基水分 Mt
    Mad = 2.58/100  # 空气干燥基水分 Mad
    Aar = 27.16/100  # 收到基灰分 Aar
    Qnet=20.9*1000  # 低位发热量 Qnet
    Xar2ad=(1-Mar)/(1-Mad)  # 收到基-空气干燥基转换系数
    c = Xar2ad*49.35/100
    h = Xar2ad*3.20/100
    n = Xar2ad*0.90/100
    s = Xar2ad*0.78/100
    o = 1-c-h-n-s-Mar-Aar
    ALPHA=21/(21-O2)  # 过量空气系数
    Vgk0=100*(0.089*(c+0.375*s)+0.265*h-0.0333*o)  # 理论干空气量 m^3
    Vgy0=1.866*(c+0.375*s)+0.79*Vgk0+0.8*n  # 理论干烟气量
    Vgy=Vgy0+(ALPHA-1)*Vgk0  # 每千克燃料生成的干烟气量
    Cpy=0.8967+0.0013*(Etem)-0.000003*(Etem)*(Etem)   # 干烟气平均定压比热容 kJ/ (kg·K)
    Q2gy = Vgy*Cpy*(Etem-INtem)/Qnet  # 干烟气热损失
    V_H2O = 1.24*((9*h+Mar)+1.293*ALPHA*Vgk0*0.001)  # 烟气中水蒸气的体积
    Q_H2O = V_H2O*1.5093*(Etem-INtem)  # 干烟气热损失中水蒸气显热
    Q2H2O = Q_H2O/Qnet  # 水分热损失
    Q3 = Vgy*126.36*CO*10e-6*100/Qnet
    Q4 = 33730*Aar/Qnet*Cfh/(100-Cfh) # 飞灰含碳热损失
    Q5 = 0.035
    eff = 1 - Q2H2O - Q2gy - Q3 - Q4 - Q5# 锅炉效率
    return eff


if __name__ == "__main__":
    data = pd.read_excel(r'model_data\东华\datafortest.xlsx', sheet_name='select', header=0)
    nox = data["#1炉SCR反应器A脱硝前烟气NOx含量"]
    nox_data_valider = DataValid(min_value=70, max_value=500, step_limit=1)
    nox_data_filter = MedianFilter(kernel_size=5)
    nox_valid = nox_data_valider.apply(np.array(nox))
    nox_filter = nox_data_filter.apply(nox)