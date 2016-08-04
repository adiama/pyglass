# -*- coding: utf-8 -*-

from bootstrap import LOGS

class Common:
    """ Common methods

    Methods that do not fit any class' context should be in
    here.
    """
    @staticmethod
    def log(entry):
        # Write at LOGS['log']
        pass

    @staticmethod
    def error(entry):
        # Write at LOGS['error']
        pass

    @staticmethod
    def debug(entry):
        # Write at LOGS['debug']
        pass
