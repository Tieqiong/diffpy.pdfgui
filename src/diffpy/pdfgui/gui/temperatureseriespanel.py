#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
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

# generated by wxGlade 0.9.3 on Fri Jul 19 16:06:35 2019

import sys
import os.path
import re
import wx
from diffpy.pdfgui.control.pdfguimacros import makeTemperatureSeries
from diffpy.pdfgui.gui.pdfpanel import PDFPanel
from diffpy.pdfgui.gui.tooltips import temperatureseriespanel as toolTips
from diffpy.pdfgui.gui.wxExtensions.listctrls import AutoWidthListCtrl
from diffpy.pdfgui.utils import numericStringSort

class TemperatureSeriesPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: TemperatureSeriesPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.instructionsLabel = wx.StaticText(self, wx.ID_ANY, "Select a fit from the tree on the left then add datasets and assign\ntemperatues below. If you have not set up a fit to be the template\nfor the series, hit cancel and rerun this macro once a fit has been\ncreated.")
        self.listCtrlFiles = AutoWidthListCtrl(self, wx.ID_ANY, style=wx.BORDER_SUNKEN | wx.LC_EDIT_LABELS | wx.LC_REPORT)
        self.buttonUp = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap)
        self.buttonDown = wx.BitmapButton(self, wx.ID_ANY, wx.NullBitmap)
        self.buttonAdd = wx.Button(self, wx.ID_ADD, "Add")
        self.buttonDelete = wx.Button(self, wx.ID_DELETE, "Delete")
        self.static_line_1 = wx.StaticLine(self, wx.ID_ANY)
        self.goButton = wx.Button(self, wx.ID_OK, "OK")
        self.cancelButton = wx.Button(self, wx.ID_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_LIST_COL_CLICK, self.onColClick, self.listCtrlFiles)
        self.Bind(wx.EVT_LIST_END_LABEL_EDIT, self.onEndLabelEdit, self.listCtrlFiles)
        self.Bind(wx.EVT_BUTTON, self.onUp, self.buttonUp)
        self.Bind(wx.EVT_BUTTON, self.onDown, self.buttonDown)
        self.Bind(wx.EVT_BUTTON, self.onAdd, self.buttonAdd)
        self.Bind(wx.EVT_BUTTON, self.onDelete, self.buttonDelete)
        self.Bind(wx.EVT_BUTTON, self.onOK, self.goButton)
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.cancelButton)
        # end wxGlade
        self.buttonUp.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_GO_UP))
        self.buttonDown.SetBitmapLabel(wx.ArtProvider.GetBitmap(wx.ART_GO_DOWN))
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: TemperatureSeriesPanel.__set_properties
        self.instructionsLabel.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Sans"))
        self.listCtrlFiles.SetToolTip("Click header to sort by temperature")
        self.buttonUp.SetSize(self.buttonUp.GetBestSize())
        self.buttonDown.SetSize(self.buttonDown.GetBestSize())
        # end wxGlade
        self.setToolTips(toolTips)

    def __do_layout(self):
        # begin wxGlade: TemperatureSeriesPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(1, 2, 10, 10)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(self.instructionsLabel, 0, wx.ALL | wx.EXPAND, 5)
        sizer_4.Add(self.listCtrlFiles, 1, wx.ALL | wx.EXPAND, 5)
        sizer_5.Add((0, 0), 1, 0, 0)
        sizer_5.Add(self.buttonUp, 0, wx.ALL, 5)
        sizer_5.Add(self.buttonDown, 0, wx.ALL, 5)
        sizer_5.Add((0, 0), 1, 0, 0)
        sizer_4.Add(sizer_5, 0, wx.EXPAND, 0)
        sizer_2.Add(sizer_4, 1, wx.EXPAND, 0)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
        grid_sizer_1.Add(self.buttonAdd, 0, 0, 0)
        grid_sizer_1.Add(self.buttonDelete, 0, 0, 0)
        sizer_1.Add(grid_sizer_1, 0, wx.ALL, 5)
        sizer_1.Add(self.static_line_1, 0, wx.EXPAND, 0)
        sizer_3.Add((20, 20), 1, wx.EXPAND, 0)
        sizer_3.Add(self.goButton, 0, wx.ALL, 5)
        sizer_3.Add(self.cancelButton, 0, wx.ALL, 5)
        sizer_1.Add(sizer_3, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

    def __customProperties(self):
        """Set the custom properties."""
        self.fit = None
        self.reverse = False # Reverse the sort?
        self.fullpath = '.'
        self.datasets = [] # Contains (temperature, filename) tuples
                           # temperature is a float and comes first for easy sorting

        self.listCtrlFiles.InsertColumn(0, "Temperature")
        self.listCtrlFiles.InsertColumn(1, "Data Set")
        self.listCtrlFiles.SetColumnWidth(0,-2)
        return

    def onEndLabelEdit(self, event): # wxGlade: TemperatureSeriesPanel.<event_handler>
        """Update the temperature in the datasets."""
        index = event.GetIndex()
        text = event.GetText()
        temperature = 300.0
        try:
            temperature = float(text)
        except ValueError:
            event.Veto()
            return
        if temperature <= 0:
            event.Veto()
            return
        # update the internal information
        self.datasets[index][0] = temperature
        self.reverse = False
        return

    def onOK(self, event): # wxGlade: TemperatureSeriesPanel.<event_handler>
        """Let's go!"""
        paths = [tp[1] for tp in self.datasets]
        temperatures = [tp[0] for tp in self.datasets]
        org = makeTemperatureSeries(self.mainFrame.control, self.fit,
                paths, temperatures)
        self.treeCtrlMain.ExtendProjectTree(org, clear=False)
        self.mainFrame.needsSave()
        self.onCancel(event)
        return

    def onCancel(self, event): # wxGlade: TemperatureSeriesPanel.<event_handler>
        """Let's go, but not actually do anything."""
        self.mainFrame.setMode("fitting")
        self.treeCtrlMain.UnselectAll()
        self.mainFrame.switchRightPanel("blank")
        return

    def onUp(self, event): # wxGlade: TemperatureSeriesPanel.<event_handler>
        """Move an item in the list up."""
        index = self.listCtrlFiles.GetFirstSelected()
        if index > 0:
            temp = self.datasets[index]
            self.datasets[index] = self.datasets[index-1]
            self.datasets[index-1] = temp
            self.fillList()
            self.listCtrlFiles.Select(index-1)
        return

    def onDown(self, event): # wxGlade: TemperatureSeriesPanel.<event_handler>
        """Move an item in the list down."""
        index = self.listCtrlFiles.GetFirstSelected()
        if index > -1 and index != len(self.datasets)-1:
            temp = self.datasets[index]
            self.datasets[index] = self.datasets[index+1]
            self.datasets[index+1] = temp
            self.fillList()
            self.listCtrlFiles.Select(index+1)
        return

    def onAdd(self, event): # wxGlade: TemperatureSeriesPanel.<event_handler>
        """Append files to the list."""
        dir, filename = os.path.split(self.fullpath)
        if not dir:
            dir = self.mainFrame.workpath

        matchstring = "PDF data files (*.gr)|*.gr|PDF fit files (*.fgr)|*.fgr|PDF fit files (*.fit)|*.fit|PDF calculation files (*.cgr)|*.cgr|PDF calculation files (*.calc)|*.calc|All Files|*"
        d = wx.FileDialog(None, "Choose files", dir, "", matchstring,
                wx.OPEN|wx.FILE_MUST_EXIST|wx.MULTIPLE)
        paths = []
        if d.ShowModal() == wx.ID_OK:
            paths = d.GetPaths()
            d.Destroy()

        # Assign the temperatures. Default to 300.0
        newdatasets = []
        for path in paths:
            self.fullpath = path
            self.mainFrame.workpath = os.path.dirname(path)

            # Look for the temperature in the filename
            temperature = 300.0
            rx = {'f' : r'(?:\d+(?:\.\d*)?|\d*\.\d+)' }
            # Search for T123, t123, Temp123, temp123, 123k, 123K.
            # Some filenames fool this, e.g. "test1.dat" will match '1' since it
            # is preceeded by a 't'.
            # Is there a better regexp? Probably...
            regexp = r"""(?:[Tt](?:emp(?:erature)?)?(%(f)s))|
                         (?:(?<![a-zA-Z0-9])(%(f)s)[Kk])
                """ % rx
            res = re.search(regexp, os.path.basename(path), re.VERBOSE)
            if res:
                groups = res.groups()
                if groups[0] is not None:
                    temperature = float(res.groups()[0])
                else:
                    temperature = float(res.groups()[1])
            else:
                # Look in the file
                infile = file(path,'r')
                datastring = infile.read()
                infile.close()
                # Look for it first in the file
                res = re.search(r'^#+ start data\s*(?:#.*\s+)*', datastring, re.M)
                # start_data is position where the first data line starts
                if res:
                    start_data = res.end()
                else:
                    res = re.search(r'^[^#]', datastring, re.M)
                    if res:
                        start_data = res.start()
                    else:
                        start_data = 0
                header = datastring[:start_data]
                # parse header to get temperature
                regexp = r"\b(?:temp|temperature|T)\ *=\ *(%(f)s)\b" % rx
                res = re.search(regexp, header)
                if res:
                    temperature = float(res.groups()[0])
            # Add the new path
            if temperature <= 0: temperature = 300.0
            newdatasets.append([temperature, path])

        # DONT Sort the new paths according to temperature
        #newdatasets.sort()
        self.datasets.extend(newdatasets)
        self.fillList()
        return

    def onDelete(self, event): # wxGlade: TemperatureSeriesPanel.<event_handler>
        """Delete selected files from the list."""
        idxlist = []
        item = self.listCtrlFiles.GetFirstSelected()
        while item != -1:
            idxlist.append(item)
            item = self.listCtrlFiles.GetNextSelected(item)

        idxlist.reverse()
        for item in idxlist:
            del self.datasets[item]
        self.fillList()
        return

    def onColClick(self, event): # wxGlade: TemperatureSeriesPanel.<event_handler>
        """Sort by temperature."""
        column = event.GetColumn()
        # sort by temperature
        if column == 0:
            sortkey = lambda tf : float(tf[0])
        # sort by filename with numerical comparison of digits
        elif column == 1:
            filenames = [f for t, f in self.datasets]
            numericStringSort(filenames)
            order = dict(zip(filenames, range(len(filenames))))
            sortkey = lambda tf : order[tf[1]]
        # ignore unhandled columns
        else:
            return
        self.datasets.sort(key=sortkey, reverse=self.reverse)
        self.reverse = not self.reverse
        self.fillList()
        return

    ## Utility functions
    def fillList(self):
        """Fill the list with the datasets."""
        self.listCtrlFiles.DeleteAllItems()
        names = [pair[1] for pair in self.datasets]
        cp = os.path.commonprefix(names)
        # We want to break at the last path/separator in the common prefix
        idx = cp.rfind(os.path.sep)
        if idx == -1: idx = len(cp)
        for temperature, filename in self.datasets:
            shortname = "..." + filename[idx:]
            index = self.listCtrlFiles.InsertStringItem(sys.maxint, str(temperature))
            self.listCtrlFiles.SetStringItem(index, 1, shortname)
        return

    ## Needed by mainframe
    def treeSelectionUpdate(self, node):
        """Set the current fit when the tree selection changes."""
        nodetype = self.treeCtrlMain.GetNodeType(node)
        if nodetype == 'fit':
            self.fit = self.treeCtrlMain.GetControlData(node)
        self.refresh()
        return

    ## Required by PDFPanel
    def refresh(self):
        """Block out OK button if there is no fit.

        This also blocks OK if the fit has no datasets or structures.
        """
        # We can't rely on Veto to block unwanted tree selections on windows.
        # So, we have to check for errors here.
        node = None
        nodetype = None
        selections = self.treeCtrlMain.GetSelections()
        if selections:
            node = selections[0]
            nodetype = self.treeCtrlMain.GetNodeType(node)

        if node and nodetype == "fit" \
                and self.fit and self.fit.hasDataSets() \
                and self.fit.hasStructures():
            self.goButton.Enable()
        else:
            self.goButton.Enable(False)
        return

# end of class TemperatureSeriesPanel
