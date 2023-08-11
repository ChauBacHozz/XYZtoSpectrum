import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def xyz2spec(xyz_bar, xyz_color, D65):
    wl = xyz_bar[:, 0]
    A = xyz_bar[:, 1:]
    s1 = np.dot(A[:, 1].T, D65)
    c1 = s1 * xyz_color
    E = np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)
    f1 = np.dot(c1, E)
    return wl, f1.T

# DEMO
D65 = pd.read_csv("CIE-D65-5nm.csv").values
D65 = D65[:, 1:]
xyz_color = np.atleast_2d([30.64, 19.812, 8.203])
xyz_bar = pd.read_csv("CIE_xyz_bar_5nm_array.csv")
wl, spec = xyz2spec(xyz_bar.values, xyz_color, D65)
plt.plot(wl, spec)
plt.show()

    


