import argparse

from lib import whismur as wh

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default=None)
    parser.add_argument('--classifier', default="knn")
    parser.add_argument('--trim_silence', default=False)
    parser.add_argument('--bpm', default=False)
    args = vars(parser.parse_args())
    print args
    whismur = wh.Whismur(args['file'], args['classifier'], args['trim_silence'], args['bpm'])
