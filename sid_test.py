import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--cuda_device', type=str, help="CUDA Device?", default="cuda:0")
parser.add_option('--img_to_load', type=int, help="Image to load?", default=-1)
parser.add_option('--img_size', type=int, default=(256, 256))

def main(argv):
    (opts, args) = parser.parse_args(argv)
    print(opts)
    print("Test script")

if __name__ == "__main__":
    main(sys.argv)