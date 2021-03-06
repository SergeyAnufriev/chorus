#
# (C) 2014-2017 Seiji Matsuoka
# Licensed under the MIT License (MIT)
# http://opensource.org/licenses/MIT
#

from chorus.model.Abstractatom import AbstractAtom


def collapse(self):
    """ recognize sugar moiety and convert into Sugar object """
    # TODO: not implemented
    pass


class Sugar(AbstractAtom):
    def __init__(self):
        self.symbol = None
        self.composition
        self.mw

    def formula_html(self):
        return self.symbol

    def composition(self):
        return self.composition

    def mw(self):
        return self.mw


class Hexose(Sugar):
    def __init__(self):
        self.name = "Hexose"
        self.symbol = "Hex"
        self.composition = None
        self.mw = None
