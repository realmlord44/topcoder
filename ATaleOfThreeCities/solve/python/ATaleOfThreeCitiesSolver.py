#! /usr/bin/env python
import os, sys
import ATaleOfThreeCities

def init():
    default_path = os.path.join(os.getenv("HOME"), ".gettc")
    gettc_home = os.path.abspath(os.getenv("GETTC_HOME", default_path))
    include_dir = os.path.join(gettc_home, "include/python")
    sys.path.append(include_dir)

def main():
    import topcoder as tc
    with open(sys.argv[1], "r") as fi:
        input = fi.read()
        reader = tc.Reader(input)

        ax = reader.next("int[]")
        reader.next()
        ay = reader.next("int[]")
        reader.next()
        bx = reader.next("int[]")
        reader.next()
        by = reader.next("int[]")
        reader.next()
        cx = reader.next("int[]")
        reader.next()
        cy = reader.next("int[]")

    result = ATaleOfThreeCities.connect(ax, ay, bx, by, cx, cy)
    with open(sys.argv[2], "w") as fo:
        fo.write(tc.write(result, "double"))

if __name__ == "__main__":
    init()
    main()
