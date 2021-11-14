import os
import urllib.parse

IGNORED_FILES = {"index.md", }


class AddFooterToNotes:

    def __init__(self, notes_directory: str = "notes"):
        self.notes_directory = notes_directory

    def find_markdown_files_and_add_footers(self):
        """
        Finds all markdown files in the notes_directory and adds a footer to the end of each file.
        """
        for subdir, _, files in os.walk(self.notes_directory):
            for file in files:
                if not file.endswith(".md") or file in IGNORED_FILES:
                    continue

                file_path = subdir + os.sep + file
                print("add_footer_to_file: ", file_path)
                try:
                    self.add_footer_to_file(file_path)
                except Exception as e:
                    print("Failed!")
                    print(e)
                else:
                    print("Completed successfully!")
                print("add_footer_to_file done \n ---------------------------------")

    @staticmethod
    def add_footer_to_file(file_path: str):
        """
        Adds the footer to the end of the file.
        """
        file_name = file_path.split("/")[-1]
        url_path = urllib.parse.quote(file_name[:-3])

        with open(file_path, "a") as file_object:
            footer = (
                "\n\n\n\n"
                "--- \n --- \n\n"
                "Find the original version of this page (with additional content) on Notion"
                f" [here](https://paulonteri.notion.site/{url_path}). \n\n"
                "--- \n"
            )
            file_object.write(footer)


if __name__ == "__main__":
    add_footer_to_notes = AddFooterToNotes()
    add_footer_to_notes.find_markdown_files_and_add_footers()
