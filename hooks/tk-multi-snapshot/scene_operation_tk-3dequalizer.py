# Copyright (c) 2013 Shotgun Software Inc.
#
# CONFIDENTIAL AND PROPRIETARY
#
# This work is provided "AS IS" and subject to the Shotgun Pipeline Toolkit
# Source Code License included in this distribution package. See LICENSE.
# By accessing, using, copying or modifying this work you indicate your
# agreement to the Shotgun Pipeline Toolkit Source Code License. All rights
# not expressly granted therein are reserved by Shotgun Software Inc.

import os
import tde4

import tank
from tank import Hook
from tank import TankError


class SceneOperation(Hook):
    """
    Hook called to perform an operation with the
    current scene
    """

    def execute(self, operation, file_path, **kwargs):
        """
        Main hook entry point
        :operation: String
                    Scene operation to perform
        :file_path: String
                    File path to use if the operation
                    requires it (e.g. open)
        :returns:   Depends on operation:
                    'current_path' - Return the current scene
                                     file path as a String
                    all others     - None
        """

        if operation == "current_path":
            # return the current scene path
            return tde4.getProjectPath()
        elif operation == "open":
            # do new scene as Maya doesn't like opening
            # the scene it currently has open!
            tde4.loadProject(file_path)
        elif operation == "save":
            current_file = tde4.getProjectPath()
            tde4.saveProject(current_file)
