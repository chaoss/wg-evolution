class IsSourceCode():
    """
    An IsSourceCode object is used to help define source code.

    :param source_code_exclude_list: a list of either
        file extensions or directories to exclude
        For example,
        source_code_exclude_list = ["py", "other", "gitignore"]
        or source_code_exclude_list = ["tests/", "bin/"]
    :param algorithm_class: A reference to the
        algorithm class to be used
    """

    def __init__(self, source_code_exclude_list=None, algorithm_class=None):
        self.source_code_exclude_list = source_code_exclude_list
        self.algorithm_class = algorithm_class

    def check(self, file):
        """
        Returns the check method of the algorithm to be used.

        :param file: a dictionary, an element of commit['files'] list
            where commit is a structure returned by commit._flatten_data

        :returns Boolean value: True if the file is part of source code,
            False otherwise
        """
        return self.algorithm_class.check(self.source_code_exclude_list, file)


class Algorithm:
    """
    Parent class to all algorithms.
    """

    def __init__(self):
        pass

    @staticmethod
    def check(source_code_exclude_list, file):
        raise NotImplementedError


class Naive(Algorithm):
    """
    Instantiates an object of Naive. It is one of the several
    "algorithms" used to define source code.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def check(source_code_exclude_list, file):
        """
        This implementation is naive, meaning that is assumes that
        all the files, a commit deals with, are a part of the source code
        irrespective of how the source code is defined.

        :param source_code_exclude_list: a list of either
            file extensions or directories to exclude
            For example,
            source_code_exclude_list = ["py", "other", "gitignore"]
            or source_code_exclude_list = ["tests/", "bin/"]

        :param file: a dictionary, an element of commit['files'] list
            where commit is a structure returned by commit._flatten_data

        :returns Boolean value: True if the file is part of source code,
            False otherwise
        """
        return True


class FolderExclude(Algorithm):
    """
    Instantiates an object of FolderExclude. It is one of several
    "algorithms" used to define source code.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def check(source_code_exclude_list, file):
        """
        This implementation is based on the directory a file
        is present in, such as "tests/" or "bin/".
        If all the files affected by a commit are present
        in directories which are mentioned source_code_exclude_list,
        that commit will not be considered for analysis.

        :param source_code_exclude_list: a list of either
            file extensions or directories to exclude
            For example,
            source_code_exclude_list = ["py", "other", "gitignore"]
            or source_code_exclude_list = ["tests/", "bin/"]

        :param file: a dictionary, an element of commit['files'] list
            where commit is a structure returned by commit._flatten_data

        :returns Boolean value: True if the file is part of source code,
            False otherwise
        """
        if source_code_exclude_list is None:
            return True

        if not any(file['file'].startswith(path)
                   for path in source_code_exclude_list):
            return True
        return False


class ExtensionExclude(Algorithm):
    """
    Instantiates an object of ExtensionExclude. It is one of several
    "algorithms" used to define source code.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def check(source_code_exclude_list, file):
        """
        This implementation is based on the extensions of the files involved
        in a commit, like "py", "json", etc.
        If all the files affected by a commit have extensions which are
        present in the source_code_exclude_list parameter, that commit will
        not be considered for analysis.

        :param source_code_exclude_list: a list of either
            file extensions or directories to exclude
            For example,
            source_code_exclude_list = ["py", "other", "gitignore"]
            or source_code_exclude_list = ["tests/", "bin/"]

        :param file: a dictionary, an element of commit['files'] list
            where commit is a structure returned by commit._flatten_data

        :returns Boolean value: True if the file is part of source code,
            False otherwise
        """

        extension = ExtensionExclude._get_extension(file)

        if source_code_exclude_list is None:
            return True
        if extension not in source_code_exclude_list:
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

        :returns file_extension: the extension of the file
        """
        file_name = file['file']
        if '.' in file_name:
            file_extension = file_name.split('.')[1]
        else:
            file_extension = "other"
        return file_extension
