import sys
import json
from shrinkwrap2yarn.parser import ShrinkwrapParser

def main(file_path):
    parser = ShrinkwrapParser()
    parsed = parser.parse(file_path)
    # print(json.dumps(parsed, indent=2))
    parser.print_yarn(parsed)


if __name__ == '__main__':
    main(sys.argv[1])
