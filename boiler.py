import numpy as np


class Boiler:
    def __init__(self):
        self.ctrl_o2 = None
        self.ctrl_coal = None
        self.ctrl_sec = None
        self.ctrl_sofa = None

        self.state_all = None
        self.target_etem = None
        self.target_rtem = None
        self.target_co = None
        self.target_nox = None

        self.ctrl_o2_limit = None
        self.ctrl_coal_limit = None
        self.ctrl_sec_limit = None
        self.ctrl_sofa_limit = None
        self.state_all_limit = None
        self.target_etem_limit = None
        self.target_co_limit = None
        self.target_nox_limit = None
        self.target_rtem_limit = None

    def init_data(self, model_data:dict, data_limit:dict):
        if model_data.get("ctrl_o2"):
            self.ctrl_o2 = np.array(model_data["ctrl_o2"])
            self.ctrl_o2_limit = np.array(data_limit["ctrl_o2"])
        if model_data.get("ctrl_coal"):
            self.ctrl_coal = np.array(model_data["ctrl_coal"])
        if model_data.get("ctrl_o2"):
            self.ctrl_o2 = np.array(model_data["ctrl_o2"])
        if model_data.get("ctrl_o2"):
            self.ctrl_o2 = np.array(model_data["ctrl_o2"])
        if model_data.get("ctrl_o2"):
            self.ctrl_o2 = np.array(model_data["ctrl_o2"])
        if model_data.get("ctrl_o2"):
            self.ctrl_o2 = np.array(model_data["ctrl_o2"])

    def normalize(self):
        pass

