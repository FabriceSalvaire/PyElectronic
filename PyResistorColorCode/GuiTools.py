####################################################################################################
#
# PyResistorColorCode - Python Electronic Tools.
# Copyright (C) 2012 Salvaire Fabrice
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
####################################################################################################

""" This modules provides GUI tools. """

####################################################################################################

from PyQt5 import QtWidgets

####################################################################################################

def translate(context, source_text):

    """ Helper function to translate a source text within a context. """

    return source_text

    # Fixme: AttributeError: type object 'QApplication' has no attribute 'UnicodeUTF8'
    # return QtWidgets.QApplication.translate(context, source_text,
    #                                         None,
    #                                         QtWidgets.QApplication.UnicodeUTF8)
