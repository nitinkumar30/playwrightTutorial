import os
import pathlib

PIPE = "│"
ELBOW = "└──"
TEE = "├──"
PIPE_PREFIX = "│   "
SPACE_PREFIX = "    "


class DirectoryTreeGenerator:
    def __init__(self, root_dir, exclude_folders=None):
        self._generator = _TreeGenerator(root_dir, exclude_folders, os.path.basename(__file__))

    def generate(self):
        tree = self._generator.build_tree()
        for entry in tree:
            print(entry)


class _TreeGenerator:
    def __init__(self, root_dir, exclude_folders=None, current_file_name=None):
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []
        self._exclude_folders = exclude_folders if exclude_folders else []
        self._current_file_name = current_file_name

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _tree_head(self):
        self._tree.append(f"{self._root_dir}{os.sep}")
        self._tree.append(PIPE)

    def _tree_body(self, directory, prefix=""):
        entries = directory.iterdir()
        entries = sorted(entries, key=lambda entry: entry.is_file())
        entries_count = len(entries)
        for index, entry in enumerate(entries):
            connector = ELBOW if index == entries_count - 1 else TEE
            if entry.is_dir() and entry.name not in self._exclude_folders:
                self._add_directory(
                    entry, index, entries_count, prefix, connector
                )
            elif entry.is_file() and entry.name != self._current_file_name:
                self._add_file(entry, prefix, connector)

    def _add_directory(self, directory, index, entries_count, prefix, connector):
        self._tree.append(f"{prefix}{connector} {directory.name}{os.sep}")
        if index != entries_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX
        self._tree_body(
            directory=directory,
            prefix=prefix,
        )
        self._tree.append(prefix.rstrip())

    def _add_file(self, file, prefix, connector):
        self._tree.append(f"{prefix}{connector} {file.name}")


# Example usage:
exclude_folders = [".venv", "node_modules", ".git"]  # List of folder names to exclude dynamically

tree = DirectoryTreeGenerator("./", exclude_folders=exclude_folders)
tree.generate()
