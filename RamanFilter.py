import numpy as np
from matplotlib import pyplot as plt


class RamanFilter:
    def __init__(self, filepath, filename, muscleName):
        fn = filepath + filename
        data_load = np.genfromtxt(fn, delimiter=",")
        self.name = muscleName
        self.x = data_load[:, 0]
        self.y = data_load[:, 1]
        self.mPoly = np.zeros(np.size(self.x))
        self.iPoly = np.zeros(np.size(self.x))
        self.zhangFit = np.zeros(np.size(self.x))
        self.signal = {"Lipids": 1305, "Tphan": 1350, "Phospholipids": 1450, "Tryptophan": 1550, "Phenyalanine": 1590,
                     "Helix": 1650}

    def plot_original(self):
        plt.title(self.name)
        plt.ylabel("Absorbance (a.u.)")
        plt.xlabel("Raman Shift")
        plt.plot(self.x, self.y)
        plt.show()

    def plot_filtered(self):
        plt.title(self.name)
        plt.ylabel("Absorbance (a.u.)")
        plt.xlabel("Raman Shift")
        plt.plot(self.x, self.mPoly, label = "mPoly")
        plt.plot(self.x, self.iPoly, label="iPoly")
        plt.plot(self.x, self.zhangFit, label="Zhang Fit")
        plt.legend()
        plt.show()

    def plot_zhang_fit(self):
        plt.title('Zhang Fit of ' + self.name)
        plt.ylabel("Absorbance (a.u.)")
        plt.xlabel("Raman Shift")
        plt.plot(self.x, self.zhangFit)
        plt.show()

    def zoom_zhang_fit(self, start, stop):
        plt.xlim(start, stop)
        plt.title('Zhang Fit of ' + self.name)
        plt.ylabel("Absorbance (a.u.)")
        plt.xlabel("Raman Shift")
        plt.plot(self.x, self.zhangFit)
        #locs, labels = plt.xticks()  # Get the current locations and labels
        #plt.xticks = np.arange(start, stop, step=50)
        for xloc in self.signal.values():
            plt.vlines(xloc, -20, 100, 'red', linestyles='dotted', label='My Label')
        plt.show()
