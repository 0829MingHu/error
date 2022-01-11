import re
from pathlib import Path
import os
import pandas as pd
pattern = re.compile(r'\.f\d+\.')
def get_information():
    root_path = './animal_video'
    df = pd.read_csv('1.csv')
    vedio_cnt = len(df)
    print(vedio_cnt)
    oldpath = Path(root_path)

    for i in range(vedio_cnt):
        path = Path(root_path) / df['family'][i].strip() / df['genus'][i].strip() / df['keyword'][i].strip() / df['action'][i].strip()
        if oldpath != path:
            oldpath = path
            # print(path)
            filelist = []
            filenames = [f for f in os.listdir(path)]
            filenames = sorted(filenames, key=lambda i: len(i), reverse=False)
            for filename in filenames:
                if re.search(pattern, filename):
                    newname = re.sub(pattern, ".", filename)
                    if newname not in filelist:
                        os.rename(os.path.join(path, filename), os.path.join(path,newname))
                        filelist.append(filename)
                        print("rename success")
                    else:
                        os.remove(os.path.join(path, filename))
                        print("del success")
                else:
                    filelist.append(filename)
get_information()
