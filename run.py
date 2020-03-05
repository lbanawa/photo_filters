import os, sys, inspect, getopt

my_location = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
python_sources_root = os.path.join(my_location, 'src')
sys.path.append(python_sources_root)

from process import *


def print_help():
    print("usage:")
    print("  run.py -i <input> -o <output> -f <filter>")
    print("     Input:    image or directory path (default: ./input)")
    print("     Output:   output directory path (default: ./output)")
    print("     Filter:   filter applied to image (gray, sepia)")
    print("                      (default gray)")

def main(argv):


    # default config
    INPUT  = 'input'
    OUTPUT = 'output/'
    FILTER = 'gray'

    # make default output dir if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    try:
        opts, args = getopt.getopt(argv, "hi:o:f:", ["input=","output=","filter="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print_help()
            sys.exit(2)

        elif opt in ("-i", "--input"):
            INPUT = arg

        elif opt in ("-o", "--output"):
            OUTPUT = arg
            shutil.rmtree('output') # using a different dir instead

        elif opt in ("-f", "--filter"):
            FILTER = arg

    run_filter(INPUT, OUTPUT, FILTER)

if __name__ == "__main__":
    main(sys.argv[1:])
