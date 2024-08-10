"""
定义滤波器 filter
"""


# 中值滤波
import numpy as np

class MedianFilter:
    def __init__(self, kernel_size=3):
        self.kernel_size = kernel_size

    def apply(self, data):
        if len(data.shape) == 1:
            return self._apply_1d(data)
        else:
            raise ValueError("Input data must be a 1D array.")

    def _apply_1d(self, data):
        """
        在线中值滤波的形式得到滤波结果，与真正在线运行时算法保持一致，会存在迟延
        :param data:
        :return:
        """
        filtered_data = np.zeros_like(data)
        medianWindows = [data[0] for i in range(self.kernel_size)]
        for i in range(data.shape[0]):
            medianWindows.append(data[i])
            medianWindows.pop(0)
            filtered_data[i] = sum(medianWindows) / self.kernel_size
        return filtered_data


class DataValid:
    """
    为防止噪声干扰，
    限制数据在合理范围内，超限保持为上一时刻值不变，
    限制数据变数速率，
    """
    def __init__(self, min_value, max_value, step_limit, step_value):
        self.min_value = min_value
        self.max_value = max_value
        self.step_limit = step_limit
        self.step_value = step_value

    def apply(self, data):
        dataWindows = data[0]
        for i in range(len(data)):
            if data[i] < self.min_value:
                data[i] = self.min_value
            elif data[i] > self.max_value:
                data[i] = self.max_value
            data_step = data[i] - dataWindows
            if data_step < -self.step_limit:
                data[i] = dataWindows - self.step_value
            elif data_step > self.step_limit:
                data[i] = dataWindows + self.step_value
            dataWindows = data[i]
        return data