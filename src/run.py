from process import *
import sys, getopt

def print_help():
    print("usage:")
    print("  run.py -i <input> -o <output> -f <filter>")
    print("     Input:    image or directory path (default: ./input/)")
    print("     Output:   output directory path (default: ./output/)")
    print("     Filter:   filter applied to image (gray, sepia)")
    print("                      (default gray)")

def main(argv):
    # default config
    INPUT  = 'input'
    OUTPUT = 'output'
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
        exit = False
        if opt == '-h':
            exit = True

        elif opt in ("-i", "--input"):
            INPUT = arg

        elif opt in ("-o", "--output"):
            OUTPUT = arg
            shutil.rmtree('output') # using a different dir instead

        elif opt in ("-f", "--filter"):
            FILTER = arg

    if exit:
        print_help()
        sys.exit(2)


    run_filter(INPUT, OUTPUT, FILTER)


if __name__ == "__main__":
    main(sys.argv[1:])
