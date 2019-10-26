import os
import logging
import program
import sys
import argparse
import traceback

from watchFaceParser.config import Config

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--gtr', action='store_true', help='force GTR watchface')
    parser.add_argument('--miband', action='store_true', help='force MiBand watchface')
    parser.add_argument('filename', nargs='+', help='''watchface.bin - unpacks watchface images and config
    watchface.json - packs config and referenced images to bin file''')
    args = parser.parse_args()

    if args.gtr:
        Config.enableGtrMode()
    elif args.miband:
        Config.enableMibandMode()

    for inputFileName in args.filename:
        isDirectory = os.path.isdir(inputFileName)
        isFile = os.path.isfile(inputFileName)
        if not isDirectory and not isFile:
            print("File or direcotry %s doesn't exists." % (inputFileName, ))
            continue
        if isDirectory:
            print("Not supported yet.")
            sys.exit(1)
        _, inputFileExtension = os.path.splitext(inputFileName)
        try:
            if inputFileExtension == '.bin':
                program.Parser.unpackWatchFace(inputFileName)
            elif inputFileExtension == '.json':
                program.Parser.packWatchFace(inputFileName)
            else:
                print("The app doesn't support file with extension %s." % (inputFileExtension, ))
            print("Done")
        except Exception as e:
            print('[Fatal] %s' % (e, ))
            traceback.print_stack()
            logging.exception(e)

