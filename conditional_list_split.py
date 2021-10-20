import glob
import os
import argparse
from PIL import Image
import cv2
import matplotlib.pyplot as plt
import numpy
import re
import pandas as pd


def conditional_list_split(lbl, path):
    lbls = lbl.split(',')
    df = pd.read_table(path, sep=' ', encoding='utf-8',header=None)

    df.columns = ['data', 'label']
    df_slct = df.where(df['label'].isin(lbls)).dropna(how='all')
    df_no_slct = df.where(~df['label'].isin(lbls)).dropna(how='all')

    df_slct['label'] = df_slct['label'].astype('int64')
    df_no_slct['label'] = df_no_slct['label'].astype('int64')
    dirname = os.path.dirname(path)
    slct_path = dirname + '\\' + os.path.splitext(os.path.basename(path))[0] + '_target.txt'
    no_slct_path = dirname + '\\' + os.path.splitext(os.path.basename(path))[0] + '_no_target.txt'
    df_slct.to_csv(slct_path, header=False, index=False, sep=' ', encoding='utf-8')
    df_no_slct.to_csv(no_slct_path, header=False, index=False, sep=' ', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description='conditional_list_split')
    parser.add_argument('--conditions', required=True, default=None)
    parser.add_argument('--datas', help='Path to label list file')
    args = parser.parse_args()
    labels = args.conditions
    conditional_list_split(labels, args.datas)


if __name__ == '__main__':
    main()