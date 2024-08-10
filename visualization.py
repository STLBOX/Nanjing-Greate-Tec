import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np

config = {
    "font.family": "SimSun",
    "font.size": 14,
    "mathtext.fontset": "stix",
    "xtick.direction": "in",
    "ytick.direction": "in",
}
rcParams.update(config)
color_list = plt.cm.tab10(np.linspace(0, 1, 12))
linesyle_list = ['-', '-.', '--', ':']

'''
定义画图可视化模版
'''


def plot_curve(data: dict):
    fig, ax = plt.subplots(1, 1, figsize=(5, 4), dpi=160)
    for i in range(len(data["x"])):
        ax.plot(data["x"][i],
                data["y"][i],
                color=color_list[i+1],
                linestyle=linesyle_list[i],
                linewidth=1.2)

    if data.get("ylim"):
        ax.set_ylim(data["ylim"])
    else:
        ax.set_ylim([np.percentile(data["y"][i], 0.5), np.percentile(data["y"][i], 99.5)])
    if data.get("xlim"):
        ax.set_xlim(data["xlim"])
    if data.get("xlabel"):
        ax.set_xlabel(data["xlabel"])
    if data.get("ylabel"):
        ax.set_ylabel(data["ylabel"])
    if data.get("xticks"):
        ax.set_xticks(data["xticks"])
    if data.get("legend"):
        legend_font = {"family": "times new roman", "size": 12}
        fig.legend(data["legend"], frameon=False, bbox_to_anchor=(1.18, 0.85), ncol=2, prop=legend_font)
    plt.show()
