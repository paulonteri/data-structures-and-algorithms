import glob
import os
import shutil
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile


class UpdateNotes:

    def __init__(self, notes_zip_url, notes_dir='./notes/', notes_index_file='index.md', ):
        self.notes_zip_url = notes_zip_url
        self.notes_dir = notes_dir
        self.notes_index_file = notes_index_file

    def replace_old_notes_with_new(self):
        """
        Updates notes.
        """
        self._delete_all_notes()
        self._download_and_extract_notes_zip()

    def _delete_all_notes(self):
        """
        Delete all notes in the notes directory.
        """
        for path in glob.glob(self.notes_dir+"*"):
            if path.endswith(self.notes_index_file):
                continue

            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)

    def _download_and_extract_notes_zip(self):
        """
        Download notes zip file and extract it into the notes_dir
        """

        http_response = urlopen(self.notes_zip_url)

        zipfile = ZipFile(BytesIO(http_response.read()))
        zipfile.extractall(path=self.notes_dir)


if __name__ == "__main__":
    notes_zip_url = os.environ.get('NOTES_ZIP_URL')
    if not notes_zip_url:
        raise Exception(
            "Please set the NOTES_ZIP_URL environment variable to the url of the notes zip file.")

    print(notes_zip_url)

    update_notes = UpdateNotes(notes_zip_url)
    update_notes.replace_old_notes_with_new()
