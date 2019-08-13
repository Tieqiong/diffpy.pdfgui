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

# generated by wxGlade 0.9.3 on Fri Jul 19 16:01:22 2019

import wx
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui.tooltips import datasetresultspanel as toolTips

class DataSetResultsPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        # begin wxGlade: DataSetResultsPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.panelNameLabel = wx.StaticText(self, wx.ID_ANY, "Data Set Results")
        self.labelScaleFactor = wx.StaticText(self, wx.ID_ANY, "Scale Factor")
        self.textCtrlScaleFactor = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.labelQdamp = wx.StaticText(self, wx.ID_ANY, "Qdamp")
        self.textCtrlQdamp = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.labelQbroad = wx.StaticText(self, wx.ID_ANY, "Qbroad")
        self.textCtrlQbroad = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_READONLY)
        self.buttonExport = wx.Button(self, wx.ID_OPEN, "Export PDF")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.onExport, self.buttonExport)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: DataSetResultsPanel.__set_properties
        self.panelNameLabel.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, ""))
        self.buttonExport.Hide()
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: DataSetResultsPanel.__do_layout
        sizer_7 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(3, 2, 5, 10)
        sizer_panelname = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, ""), wx.HORIZONTAL)
        sizer_panelname.Add(self.panelNameLabel, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 5)
        sizer_7.Add(sizer_panelname, 0, wx.EXPAND | wx.LEFT | wx.RIGHT, 5)
        grid_sizer_1.Add(self.labelScaleFactor, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 5)
        grid_sizer_1.Add(self.textCtrlScaleFactor, 0, wx.ALIGN_CENTER_VERTICAL, 20)
        grid_sizer_1.Add(self.labelQdamp, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 5)
        grid_sizer_1.Add(self.textCtrlQdamp, 0, wx.ALIGN_CENTER_VERTICAL, 20)
        grid_sizer_1.Add(self.labelQbroad, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.LEFT, 5)
        grid_sizer_1.Add(self.textCtrlQbroad, 0, wx.ALIGN_CENTER_VERTICAL, 20)
        sizer_7.Add(grid_sizer_1, 0, wx.ALL | wx.EXPAND, 5)
        sizer_7.Add(self.buttonExport, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)
        self.SetSizer(sizer_7)
        sizer_7.Fit(self)
        self.Layout()
        # end wxGlade

    # USER CONFIGURATION CODE #################################################

    def __customProperties(self):
        self.results = {}
        self.ctrlMap = {'dscale'        :   'textCtrlScaleFactor',
                        'qdamp'         :   'textCtrlQdamp',
                        'qbroad'        :   'textCtrlQbroad',
                        }
        # Define tooltips.
        self.setToolTips(toolTips)
        return

    def setResultsData(self):
        """Set the values in the results panel.

        The values are taken from the results member dictionary.
        dscale      --  float
        qdamp       --  float
        qbroad      --  float
        """
        for name in self.ctrlMap:
            value = self.results.get(name, None)
            ctrlName = self.ctrlMap[name]
            textCtrl = getattr(self, ctrlName)
            if value is not None:
                textCtrl.SetValue(str(value))
            else:
                textCtrl.SetValue('')
        return

    # EVENT CODE #############################################################

    def onExport(self, event): # wxGlade: DataSetResultsPanel.<event_handler>
        print "Event handler `onExport' not implemented"
        event.Skip()

    # Methods overloaded from PDFPanel
    def refresh(self):
        """Refresh the panel."""
        # Set the results data
        self.setResultsData()
        return



# end of class DataSetResultsPanel
