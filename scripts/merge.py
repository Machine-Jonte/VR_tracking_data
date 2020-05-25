import numpy as np
import pandas as pd
import os
import sys



if __name__ == "__main__":
    file_name_left = sys.argv[1]
    file_name_right = sys.argv[2]
    print("Merging: " + file_name_left + " + " + file_name_right)

    arm_row = []
    names = ["left", "right"]
    for name in names:
        one_arm = [
            name + ": target position x",
            name + ": target position y",
            name + ": target position x",
            name + ": current position x",
            name + ": current position y",
            name + ": current position z"
        ]
        arm_row += one_arm

    header = ["time"] + arm_row

    df_left = pd.read_csv(str(file_name_left))
    df_right = pd.read_csv(str(file_name_right))
    df_right = df_right.drop(columns=["Time"])

    
    result = pd.concat([df_left, df_right], axis=1, sort=False)
    result.columns = header

    result.to_csv("merged.csv", index=False)



    