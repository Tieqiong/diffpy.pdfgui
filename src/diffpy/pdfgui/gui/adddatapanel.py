#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-
##############################################################################
#
# PDFgui            by DANSE Diffraction group
#                   Simon J. L. Billinge
#                   (c) 2006 trustees of the Michigan State University.
#                   (c) 2024 trustees of the Columbia University in the City
#                   All rights reserved.
#
# File coded by:    Chris Farrow
#
# See AUTHORS.txt for a list of people who contributed.
# See LICENSE.txt for license information.
#
##############################################################################

# generated by wxGlade 0.9.3 on Fri Jul 19 15:56:56 2019

import wx

from diffpy.pdfgui.gui.fittree import incrementName
from diffpy.pdfgui.gui.pdfpanel import PDFPanel


class AddDataPanel(wx.Panel, PDFPanel):
    """Panel for adding or changing data.

    Data members:
    Several items must be known to this panel so it knows where to try to insert
    the dataset.
    entrypoint  --  The FitTree item id from which we entered this panel.
    entryfit    --  The parent of the new dataset.
    entryset    --  The dataset below which to place the new set. This can be
                    None, which means the new dataset is appended to the end of
                    the entryfit.
    """

    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: AddDataPanel.__init__
        kwds["style"] = kwds.get("style", 0) | wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_4, 0, wx.BOTTOM | wx.EXPAND | wx.TOP, 5)

        self.textLoadData = wx.StaticText(self, wx.ID_ANY, "Load a data set from file.")
        self.textLoadData.SetFont(
            wx.Font(
                12,
                wx.FONTFAMILY_DEFAULT,
                wx.FONTSTYLE_NORMAL,
                wx.FONTWEIGHT_NORMAL,
                0,
                "Sans",
            )
        )
        sizer_4.Add(self.textLoadData, 1, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.buttonOpen = wx.Button(self, wx.ID_OPEN, "Open")
        sizer_4.Add(self.buttonOpen, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.static_line_2 = wx.StaticLine(self, wx.ID_ANY)
        sizer_1.Add(self.static_line_2, 0, wx.BOTTOM | wx.EXPAND, 10)

        self.buttonCancel = wx.Button(self, wx.ID_CANCEL, "Cancel")
        sizer_1.Add(self.buttonCancel, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

        sizer_1.Add((450, 0), 0, 0, 0)

        self.SetSizer(sizer_1)
        sizer_1.Fit(self)

        self.Layout()

        self.Bind(wx.EVT_BUTTON, self.onOpen, self.buttonOpen)
        self.Bind(wx.EVT_BUTTON, self.onCancel, self.buttonCancel)
        # end wxGlade
        self.__customProperties()

    # UTILITY FUNCTIONS ####

    def __customProperties(self):
        """Custom Properties go here."""
        self.entrypoint = None  # The entrypoint on the tree
        self.entryfit = None  # The fit under which to insert an item
        self.entryset = None  # The dataset in which to insert an item
        self.fullpath = ""  # The last loaded dataset
        return

    def readConfiguration(self):
        """Read the 'DATASET' configuration.

        In the 'DATASET' section of the project ConfigurationParser the
        following is set by this panel.

        'last'      --  The last dataset file added to the project. This is
                        stored in the class variable fullpath.
        """
        remember = False
        if self.cP.has_option("DATASET", "remember"):
            remember = self.cP.getboolean("DATASET", "remember")

        if remember:
            if self.cP.has_option("DATASET", "last"):
                self.fullpath = self.cP.get("DATASET", "last")
                import os.path

                if not os.path.exists(self.fullpath):
                    self.fullpath = ""
            else:
                self.fullpath = ""
        return

    def updateConfiguration(self):
        """Update the configuration for the 'DATASET'."""
        if not self.cP.has_section("DATASET"):
            self.cP.add_section("DATASET")
        self.cP.set("DATASET", "last", self.fullpath)
        return

    # EVENT CODE ####

    def onOpen(self, event):  # wxGlade: AddDataPanel.<event_handler>
        """Add a dataset to the tree from a file."""
        import os.path

        newnode = None
        dir, filename = os.path.split(self.fullpath)
        if not dir:
            dir = self.mainFrame.workpath
        matchstring = "|".join(
            (
                "PDF files",
                "*.gr;*.fgr;*.fit;*.cgr;*.calc",
                "PDF data files (*.gr)",
                "*.gr",
                "PDF fit files (*.fgr)",
                "*.fgr",
                "PDF fit files (*.fit)",
                "*.fit",
                "PDF calculation files (*.cgr)",
                "*.cgr",
                "PDF calculation files (*.calc)",
                "*.calc",
                "All Files",
                "*",
            )
        )
        d = wx.FileDialog(None, "Choose a file", dir, "", matchstring)
        if d.ShowModal() == wx.ID_OK:
            self.fullpath = d.GetPath()
            self.mainFrame.workpath = os.path.dirname(self.fullpath)

            # Update the configuration
            self.updateConfiguration()

            # Add the item to the tree.
            name = os.path.basename(self.fullpath)

            # Check the name and alter it if necessary
            siblings = self.treeCtrlMain.GetChildren(self.entryfit)
            names = [self.treeCtrlMain.GetItemText(i) for i in siblings]
            name = incrementName(name, names)
            newnode = self.treeCtrlMain.AddDataSet(
                self.entryfit, name, insertafter=self.entryset, filename=self.fullpath
            )

            self.mainFrame.setMode("fitting")
            self.treeCtrlMain.SetItemBold(self.entrypoint, False)
            self.treeCtrlMain.UnselectAll()
            self.mainFrame.makeTreeSelection(newnode)
        d.Destroy()
        return

    def onCancel(self, event):  # wxGlade: AddDataPanel.<event_handler>
        """Cancel this addition. Go back to the last panel."""
        if self.entrypoint is None:
            return
        self.mainFrame.setMode("fitting")
        self.treeCtrlMain.SetItemBold(self.entrypoint, False)
        self.treeCtrlMain.UnselectAll()
        self.mainFrame.makeTreeSelection(self.entrypoint)
        return

    # Methods overloaded from PDFPanel
    def refresh(self):
        """Check the necessary tree nodes and bold text the entry point.

        Update the configuration
        """
        self.readConfiguration()

        selections = self.treeCtrlMain.GetSelections()
        entrypoint = selections[0]
        entryset = entrypoint
        entryfit = self.treeCtrlMain.GetFitRoot(entrypoint)

        # Check on the entryset and entryfit. Data sets can only be
        # inserted from datasets or fits. If the entry is on a dataset, the
        # entryset is the id of that dataset. Otherwise it is None. If the
        # entry is on a fit, this is the entryfit. If the entry is on a
        # dataset, the entryfit is its parent.
        entrytype = self.treeCtrlMain.GetNodeType(entrypoint)
        if entrytype != "dataset":
            entryset = None

        # Prepare the window
        self.entrypoint = entrypoint
        self.entryset = entryset
        self.entryfit = entryfit

        # Let's see it!
        self.treeCtrlMain.SetItemBold(entrypoint)
        self.treeCtrlMain.UnselectAll()
        return


# end of class AddDataPanel
