import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import sys
import argparse
from dropbox_file_uploader import DropboxUploader

parser = argparse.ArgumentParser(description='Sync ~/Downloads to Dropbox')
parser.add_argument('dropbox_folder', nargs='?', default='Downloads',
                    help='Folder name in your Dropbox')
parser.add_argument('local_folder', nargs='?', default='~/Downloads',
                    help='Local directory to upload')
parser.add_argument('--token', help='Access token '
                                    '(see https://www.dropbox.com/developers/apps)')


class DropboxEventhandler(FileSystemEventHandler):
    def __init__(self, dropbox_uploader: DropboxUploader):
        self.dropbox_uploader = dropbox_uploader

    def on_created(self, event):
        self.dropbox_uploader.sync()

    def on_modified(self, event):
        self.dropbox_uploader.sync()


def main():
    args = parser.parse_args()
    local_folder = args.local_folder
    dropbox_folder = args.dropbox_folder
    token = args.token
    print("starting")

    if not args.token:
        print('--token is mandatory')
        sys.exit(2)

    dropbox_uploader = DropboxUploader(token, dropbox_folder, local_folder)

    event_handler = DropboxEventhandler(dropbox_uploader)
    observer = Observer()
    observer.schedule(event_handler, local_folder, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    return 0


if __name__ == '__main__':
    main()
