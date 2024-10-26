from pathlib import Path
from tkinter import filedialog

from ttkthemes import ThemedTk


class FileExplorer:
    """File and directory exploration using Tkinter."""

    def __init__(
            self
            ):
        self.root = ThemedTk(theme="plastik")
        dpi = self.root.winfo_fpixels('1i')
        self.root.geometry(f"400x300+{dpi}+{dpi}")
        self.root.withdraw()

    def __enter__(
            self
            ):
        # Perform any actions necessary for setup
        return self  # Return the instance itself

    def __exit__(
            self,
            exc_type,
            exc_val,
            exc_tb
            ):
        # Perform cleanup tasks, such as destroying the Tkinter root window
        self.root.destroy()

    @staticmethod
    def file_explorer(
            initialdir=".",
            types=()
            ):
        """Opens a file browser dialog and returns the selected file path."""
        file_path = filedialog.askopenfilename(
                initialdir=initialdir,
                title="Select a File",
                filetypes=types
        )

        if file_path:
            return str(Path(file_path).resolve())
        else:
            return None

    @staticmethod
    def files_explorer(
            initialdir=".",
            types=()
            ):
        """Opens a file browser dialog and returns the selected file path."""
        file_paths = filedialog.askopenfilenames(
                initialdir=initialdir,
                title="Select Files",
                filetypes=types
        )

        if file_paths:
            return [str(Path(path).resolve()) for path in file_paths]
        else:
            return None

    @staticmethod
    def directory_explorer(
            initialdir="."
            ):
        """Opens a directory browser dialog and returns the selected
           directory path."""
        directory_path = filedialog.askdirectory(
                initialdir=initialdir,
                title="Select a Directory"
        )

        if directory_path:
            return Path(directory_path).resolve()
        else:
            return None
