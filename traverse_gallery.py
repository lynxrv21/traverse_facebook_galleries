""" Image downloader for Facebook """
# -*- coding: utf-8 -*-
import json
import logging
import timeit
from argparse import ArgumentParser

from lib.files import Files
from lib.gallery_crawler import GalleryCrawler

def main():
    """ Traverse the galleries """
    args = _parse_args()
    try:
        with open(Files.OPTIONS.value) as options_file:
            options = json.load(options_file)
            if args.url:
                options['start_images'] = args.url,
            options['password'] = args.password
            creawler = GalleryCrawler(options)
            creawler.run()
    except FileNotFoundError:
        logging.error(
            "You should create your own %s from %s!",
            Files.OPTIONS.value,
            Files.OPTIONS_TEMPLATE.value
        )

def _parse_args():
    parser = ArgumentParser()
    parser.add_argument('-p', '--password', type=str, help='Facebook password.')
    parser.add_argument('-u', '--url', type=str, help='Start image URL.')
    return parser.parse_args()

if __name__ == "__main__":
    print("[Facebook Gallery Downloader v0.3]")
    START = timeit.default_timer()
    main()
    STOP = timeit.default_timer()
    print("[ Time taken: %ss ]" % str(STOP - START))
    input("Press any key to continue...")
