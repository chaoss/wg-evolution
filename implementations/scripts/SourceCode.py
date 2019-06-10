class SourceCode:

    def __init__(self, source_code_exclude_list=None, method="naive"):
        """
        A SourceCode object is used to help define source code.
        :param source_code_exclude_list: a list of either
            file extensions or directories to exclude
        :param method: a string which can be "naive",
            "folder_exclude" or "extension_exclude"
        For example,
        source_code_exclude_list = ["py", "other", "gitignore"]
        or source_code_exclude_list = ["tests/", "bin/", "drivers/base/"]
        """
        self.source_code_exclude_list = source_code_exclude_list
        self.method = method

    def is_source_code(self, commit):
        """
        Given a commit structure, which is a dictionary returned
        by the _summary function, and given a list of files to exclude
        using source_code_exclude_list while instantiating an object,
        decide whether all the files in a commit are to be excluded or not.

        :param commit: a commit structure, returned by the _summary method.
        """
        options_dict = {
            "naive": self._naive_implementation,
            "folder_exclude": self._folder_exclude_implementation,
            "extension_exclude": self._extension_exclude_implementation
        }

        return options_dict[self.method](commit)

    def _naive_implementation(self, commit):
        """
        This implementation is naive, meaning that is assumes that
        all the files a commit deal with are part of the source code,
        irrespective of how the source code is defined.

        :param commit: a commit structure, returned by the _summary method.
        """
        return True

    def _folder_exclude_implementation(self, commit):
        """
        This implementation is based on the directory a file
        is present in, like "tests/" or "bin/".
        If all the files affected by a commit are present
        in directories which are mentioned source_code_exclude_list,
        that commit will not be considered for analysis.

        :param commit: a commit structure, returned by the _summary method.
        """
        if self.source_code_exclude_list is None:
            return True

        for file in commit['files']:
            if not any(file['file'].startswith(path)
                       for path in self.source_code_exclude_list):
                return True
        return False

    def _extension_exclude_implementation(self, commit):
        """
        This implementation is based on the extensions of the files involved
        in a commit, like "py", "json", etc.
        If all the files affected by a commit have extensions which are
        present in the source_code_exclude_list parameter, that commit will
        not be considered for the analysis.

        :param commit: a commit structure, returned by the _clean_commit method
            of Commit class.
        """
        extension_set = set()
        for file in commit['files']:
            extension_set.add(SourceCode._get_extension(file))

        if self.source_code_exclude_list is None    \
                or len(extension_set
                       .difference(self.source_code_exclude_list)) > 0:
            return True
        return False

    @staticmethod
    def _get_extension(file):
        """
        Given a file structure, which is a dictionary and an element
        of commit['files'], return the extension of that file.
        For files without a standard ".xyz" extension, like LICENCE or AUTHORS,
        the "others" extension is used.

        :param file: a file structure which is a dictionary, an element
        of commit["files"]
        """

        file_name = file['file']
        if '.' in file_name:
            file_extension = file_name.split('.')[1]
        else:
            file_extension = "other"
        return file_extension
