#!/usr/bin/env python
# -*- coding: UTF-8 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.9.3 on Fri Jul 19 16:05:44 2019

import wx
from diffpy.pdfgui.gui.pdfpanel import PDFPanel

class ResultsPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ResultsPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.fitResLabel = wx.StaticText(self, wx.ID_ANY, "Fit Summary")
        self.resultsTextCtrl = wx.TextCtrl(self, wx.ID_ANY, "Fit results will display here once the fit is complete.", style=wx.HSCROLL | wx.TE_MULTILINE | wx.TE_READONLY)

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: ResultsPanel.__set_properties
        self.fitResLabel.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ResultsPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_2.Add(self.fitResLabel, 0, wx.ALL, 5)
        sizer_1.Add(sizer_2, 0, wx.ALL | wx.EXPAND, 5)
        sizer_1.Add(self.resultsTextCtrl, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    # UTILITY METHODS #################################
    def __customProperties(self):
        """Set the custom properties."""
        self.fit = None
        self.defres = "Fit results will display here once the fit is complete."
        self.results = self.defres

        # Set the font to monospace
        font = self.resultsTextCtrl.GetFont()
        font = wx.Font(font.GetPointSize(), wx.FONTFAMILY_TELETYPE,
                font.GetWeight(), font.GetStyle(), font.GetUnderlined())
        self.resultsTextCtrl.SetFont(font)
        return

    # Methods overloaded from PDFPanel
    def refresh(self):
        """Fill in the resultsTextCtrl with the fit results if they exist."""
        if self.fit:
            self.results = self.fit.res
        else:
            self.results = ''
        if not self.results:
            self.results = self.defres
        displayed = self.resultsTextCtrl.GetValue()
        if displayed != self.results:
            lastpos = self.resultsTextCtrl.GetLastPosition()
            self.resultsTextCtrl.Replace(0, lastpos, self.results)
        return

# end of class ResultsPanel
