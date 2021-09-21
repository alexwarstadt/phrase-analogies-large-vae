import pandas as pd
import argparse
from numpy.random import choice


def make_quadruples(df_pairs, args):
    """
    :param df_pairs: a pandas dataframe of sentence pairs with (at least) columns "a" and "b"
    :param args: the parser arguments
    :return: a pandas dataframe of sentence quadruples
    """
    df_pairs = df_pairs[["a", "b"]]
    x = [i for i in range(len(df_pairs))]
    y = [(a, b) for a in x for b in x if a != b]
    sample = choice(range(len(y)), min(args.max_quadruples, len(y)), replace=False)
    quadruples = []
    for s in sample:
        i, j = y[s]
        quadruples.append(pd.concat([df_pairs.iloc[i].rename({"a": "a", "b": "b"}),
                                     df_pairs.iloc[j].rename({"a": "c", "b": "d"})]))
    quadruples = pd.concat(quadruples, axis=1).transpose()
    return quadruples


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_path", help="Path to input .csv file containing sentence pairs")
    parser.add_argument("--output_path", help="Path output .csv file containing sentence quadruples")
    parser.add_argument("--max_quadruples", type=int, default=1000, help="Maximum number of quadruples to sample")
    args = parser.parse_args()
    df_pairs = pd.read_csv(args.input_path, header=0)
    df_quadruples = make_quadruples(df_pairs, args)
    df_quadruples.to_csv(args.output_path, index=False)


if __name__ == "__main__":
    main()



