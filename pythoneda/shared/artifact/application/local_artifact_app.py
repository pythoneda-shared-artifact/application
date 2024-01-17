# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/application/__init__.py

This file defines the LocalArtifactApp class.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/application

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import abc
from pythoneda.shared.application import PythonEDA
from pythoneda.shared.artifact import Artifact


class LocalArtifactApp(PythonEDA, abc.ABC):
    """
    Runs the LocalArtifact PythonEDA app.

    Class name: LocalArtifactApp

    Responsibilities:
        - Provides common logic for artifact applications backed by local repositories.

    Collaborators:
        - Command-line handlers from pythoneda-shared-artifact/infrastructure
    """

    def accept_repository_folder(self, folder: str):
        """
        Annotates the repository folder.
        :param folder: The folder.
        :type folder: str
        """
        artifact_class = self.__class__.artifact_class()
        if artifact_class is not None:
            artifact_class.initialize(folder)

    @classmethod
    @abc.abstractmethod
    def artifact_class(cls) -> type[Artifact]:
        """
        Retrieves the subclass of Artifact.
        :return: Such class.
        :rtype: type[Artifact]
        """
        pass
# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
