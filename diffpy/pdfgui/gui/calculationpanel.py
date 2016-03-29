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

# generated by wxGlade 0.4.1 on Mon Apr  3 19:12:03 2006

import wx
from diffpy.pdfgui.gui.wxExtensions.validators import TextValidator, FLOAT_ONLY
from diffpy.pdfgui.gui.wxExtensions.textctrlutils import textCtrlAsGridCell
from diffpy.pdfgui.gui.pdfpanel import PDFPanel

class CalculationPanel(wx.Panel, PDFPanel):
    def __init__(self, *args, **kwds):
        PDFPanel.__init__(self)
        # begin wxGlade: CalculationPanel.__init__
        kwds["style"] = wx.TAB_TRAVERSAL
        wx.Panel.__init__(self, *args, **kwds)
        self.sizer_panelname_staticbox = wx.StaticBox(self, -1, "")
        self.panelNameLabel = wx.StaticText(self, -1, "Calculation Configuration")
        self.radioBoxStype = wx.RadioBox(self, -1, "Scatterer Type", choices=["Neutron", "X-ray"], majorDimension=2, style=wx.RA_SPECIFY_COLS)
        self.labelCalcRange = wx.StaticText(self, -1, "Range", style=wx.ALIGN_RIGHT)
        self.textCtrlCalcFrom = wx.TextCtrl(self, -1, "1.0")
        self.labelTo = wx.StaticText(self, -1, "to", style=wx.ALIGN_RIGHT)
        self.textCtrlCalcTo = wx.TextCtrl(self, -1, "10.0")
        self.labelRStep = wx.StaticText(self, -1, "spacing", style=wx.ALIGN_RIGHT)
        self.textCtrlRStep = wx.TextCtrl(self, -1, "0.01")
        self.labelScaleFactor = wx.StaticText(self, -1, "Scale Factor", style=wx.ALIGN_RIGHT)
        self.textCtrlScaleFactor = wx.TextCtrl(self, -1, "1.0")
        self.labelQmax = wx.StaticText(self, -1, "Qmax", style=wx.ALIGN_RIGHT)
        self.textCtrlQmax = wx.TextCtrl(self, -1, "25.0")
        self.label_1 = wx.StaticText(self, -1, "")
        self.label_1_copy = wx.StaticText(self, -1, "")
        self.labelQdamp = wx.StaticText(self, -1, "Qdamp", style=wx.ALIGN_RIGHT)
        self.textCtrlQdamp = wx.TextCtrl(self, -1, "0.0")
        self.labelQbroad = wx.StaticText(self, -1, "Qbroad", style=wx.ALIGN_RIGHT)
        self.textCtrlQbroad = wx.TextCtrl(self, -1, "0.0")
        self.label_1_copy_2 = wx.StaticText(self, -1, "")
        self.label_1_copy_1 = wx.StaticText(self, -1, "")
        self.label_1_copy_6 = wx.StaticText(self, -1, "")
        self.label_1_copy_5 = wx.StaticText(self, -1, "")
        self.label_1_copy_3 = wx.StaticText(self, -1, "")
        self.label_1_copy_4 = wx.StaticText(self, -1, "")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.onStype, self.radioBoxStype)
        # end wxGlade
        self.__customProperties()

    def __set_properties(self):
        # begin wxGlade: CalculationPanel.__set_properties
        self.panelNameLabel.SetFont(wx.Font(18, wx.DEFAULT, wx.NORMAL, wx.BOLD, 0, ""))
        self.radioBoxStype.SetMinSize((330, 43))
        self.radioBoxStype.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: CalculationPanel.__do_layout
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        outerSizer = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.FlexGridSizer(4, 6, 5, 10)
        sizer_panelname = wx.StaticBoxSizer(self.sizer_panelname_staticbox, wx.HORIZONTAL)
        sizer_panelname.Add(self.panelNameLabel, 0, wx.LEFT|wx.RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        outerSizer.Add(sizer_panelname, 0, wx.LEFT|wx.RIGHT|wx.EXPAND, 5)
        outerSizer.Add((450, 5), 0, 0, 0)
        outerSizer.Add(self.radioBoxStype, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.labelCalcRange, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.textCtrlCalcFrom, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.labelTo, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 20)
        grid_sizer_1.Add(self.textCtrlCalcTo, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.labelRStep, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.textCtrlRStep, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.labelScaleFactor, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.textCtrlScaleFactor, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.labelQmax, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 20)
        grid_sizer_1.Add(self.textCtrlQmax, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.label_1, 0, 0, 0)
        grid_sizer_1.Add(self.label_1_copy, 0, 0, 0)
        grid_sizer_1.Add(self.labelQdamp, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.textCtrlQdamp, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.labelQbroad, 0, wx.LEFT|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.textCtrlQbroad, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add(self.label_1_copy_2, 0, 0, 0)
        grid_sizer_1.Add(self.label_1_copy_1, 0, 0, 0)
        grid_sizer_1.Add(self.label_1_copy_6, 0, 0, 0)
        grid_sizer_1.Add(self.label_1_copy_5, 0, 0, 0)
        grid_sizer_1.Add(self.label_1_copy_3, 0, 0, 0)
        grid_sizer_1.Add(self.label_1_copy_4, 0, 0, 0)
        outerSizer.Add(grid_sizer_1, 0, wx.ALL|wx.EXPAND, 5)
        sizer_1.Add(outerSizer, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        # end wxGlade

    # USER CONFIGURATION CODE #################################################

    def __customProperties(self):
        """Set up the custom properites."""
        self._focusedText = None
        self.calculation = None
        self.stypeMap = {0: 'N', 1: 'X'}

        self.ctrlMap = {'rmin'       :   'textCtrlCalcFrom',
                        'rmax'       :   'textCtrlCalcTo',
                        'qmax'       :   'textCtrlQmax',
                        'qdamp'      :   'textCtrlQdamp',
                        'qbroad'     :   'textCtrlQbroad',
                        'rstep'      :   'textCtrlRStep',
                        'dscale'     :   'textCtrlScaleFactor',
                        }

        # Give each textCtrl a name that can be referenced and setup the
        # validator
        for (key, value) in self.ctrlMap.items():
            textCtrl = getattr(self, value)
            textCtrl.SetName(key)
            textCtrl.SetValidator(TextValidator(FLOAT_ONLY))

        # Create specific bindings for the textCtrls
        self.textCtrlCalcFrom.Bind(wx.EVT_KILL_FOCUS, self.onCalcRange)
        self.textCtrlCalcTo.Bind(wx.EVT_KILL_FOCUS, self.onCalcRange)
        self.textCtrlQmax.Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)
        self.textCtrlQdamp.Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)
        self.textCtrlQbroad.Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)
        self.textCtrlScaleFactor.Bind(wx.EVT_KILL_FOCUS, self.onKillFocus)
        self.textCtrlRStep.Bind(wx.EVT_KILL_FOCUS, self.onCalcRange)

        # Bind the focus and key events
        for (key, value) in self.ctrlMap.items():
            textCtrl = getattr(self, value)
            textCtrl.Bind(wx.EVT_SET_FOCUS, self.onSetFocus)
            textCtrl.Bind(wx.EVT_KEY_DOWN, self.onTextCtrlKey)

        return

    # Create the onTextCtrlKey event handler from textCtrlAsGridCell from
    # wxExtensions.textctrlutils
    onTextCtrlKey = textCtrlAsGridCell

    def setConfigurationData(self):
        """Set the data in the panel."""
        if self.calculation:
            stype = self.calculation.stype

            if stype == 'N':
                self.radioBoxStype.SetSelection(0)
            elif stype == 'X':
                self.radioBoxStype.SetSelection(1)

        for (key, value) in self.ctrlMap.items():
            textCtrl = getattr(self, value)

            value = getattr(self.calculation, key)

            if value is not None:
                textCtrl.SetValue(str(value))
            else:
                textCtrl.SetValue('0.0')
        return

    def __coerseText(self, value):
        if not value:
            value = '0'
        if value[-1].lower() in ('-', 'e'):
            value += '0'
        return float(value)
    # EVENT CODE #############################################################

    def onStype(self, event): # wxGlade: CalculationPanel.<event_handler>
        value = event.GetInt()
        self.calculation.stype = self.stypeMap[value]
        self.mainFrame.needsSave()
        return

    def onCalcRange(self, event): # wxGlade: CalculationPanel.<event_handler>
        event.Skip()
        if self.calculation is None: return
        from diffpy.pdfgui.control.controlerrors import ControlValueError
        # Since calculation.rmax gets adjusted by setRGrid,
        # always obtain all range parameters.
        rminvalue = self.textCtrlCalcFrom.GetValue()
        rstepvalue = self.textCtrlRStep.GetValue()
        rmaxvalue = self.textCtrlCalcTo.GetValue()
        rmin = self.__coerseText(rminvalue)
        rstep = self.__coerseText(rstepvalue)
        rmax = self.__coerseText(rmaxvalue)
        oldrmin = self.calculation.rmin
        oldrstep = self.calculation.rstep
        oldrmax = self.calculation.rmax
        if oldrmin == rmin and oldrstep == rstep and oldrmax == rmax:
            return

        try:
            self.calculation.setRGrid(rmin, rstep, rmax)
        except ControlValueError:
            pass
        # Make sure the panels and the control are consistent
        self.textCtrlCalcFrom.SetValue(str(self.calculation.rmin))
        self.textCtrlRStep.SetValue(str(self.calculation.rstep))
        self.textCtrlCalcTo.SetValue(str(self.calculation.rmax))
        self.mainFrame.needsSave()
        return

    def onSetFocus(self, event):
        """Saves a TextCtrl value, to be used later."""
        self._focusedText = event.GetEventObject().GetValue()
        event.Skip()
        return

    def onKillFocus(self, event):
        textCtrl = event.GetEventObject()
        value = textCtrl.GetValue()
        value = self.__coerseText(value)
        name = textCtrl.GetName()
        oldval = getattr(self.calculation, name)
        if oldval != value:
            setattr(self.calculation, name, value)
            self.mainFrame.needsSave()
        event.Skip()
        return

    def onExport(self, event): # wxGlade: CalculationPanel.<event_handler>
        event.Skip()

    # Methods overloaded from PDFPanel
    def refresh(self):
        """Refresh the panel."""
        self.setConfigurationData()
        return

# end of class CalculationPanel
