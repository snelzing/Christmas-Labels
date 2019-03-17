#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.9.2 on Thu Mar  7 12:53:21 2019
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainMenuFrameClass(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainMenuFrameClass.__init__
        kwds["style"] = kwds.get("style", 0) | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE | wx.MINIMIZE_BOX | wx.RESIZE_BORDER | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((400, 300))
        
        # Menu Bar
        self.MainMenuFrame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_NEW, "New Contact File...", "")
        self.Bind(wx.EVT_MENU, self.on_menu_file_new, id=wx.ID_NEW)
        wxglade_tmp_menu.Append(wx.ID_OPEN, "Open Contact File...", "")
        self.Bind(wx.EVT_MENU, self.on_menu_file_open, id=wx.ID_OPEN)
        wxglade_tmp_menu.Append(wx.ID_SAVE, "Save", "")
        self.Bind(wx.EVT_MENU, self.on_menu_file_save, id=wx.ID_SAVE)
        wxglade_tmp_menu.Append(wx.ID_SAVEAS, "Save As...", "")
        self.Bind(wx.EVT_MENU, self.on_menu_file_save_as, id=wx.ID_SAVEAS)
        self.MainMenuFrame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_CUT, "Cut", "")
        self.Bind(wx.EVT_MENU, self.on_menu_edit_cut, id=wx.ID_CUT)
        wxglade_tmp_menu.Append(wx.ID_COPY, "Copy", "")
        self.Bind(wx.EVT_MENU, self.on_menu_edit_copy, id=wx.ID_COPY)
        wxglade_tmp_menu.Append(wx.ID_PASTE, "Paste", "")
        self.Bind(wx.EVT_MENU, self.on_menu_edit_paste, id=wx.ID_PASTE)
        self.MainMenuFrame_menubar.Append(wxglade_tmp_menu, "Edit")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(wx.ID_ABOUT, "About", "")
        self.Bind(wx.EVT_MENU, self.on_menu_help_about, id=wx.ID_ABOUT)
        self.MainMenuFrame_menubar.Append(wxglade_tmp_menu, "Help")
        self.SetMenuBar(self.MainMenuFrame_menubar)
        # Menu Bar end
        self.MainMenuPanel = wx.Panel(self, wx.ID_ANY)
        self.ManageContactsButton = wx.Button(self.MainMenuPanel, wx.ID_ANY, "Manage Contacts")
        self.PrintLabelsButton = wx.Button(self.MainMenuPanel, wx.ID_ANY, "Print Labels")
        self.OtherActivityButton = wx.Button(self.MainMenuPanel, wx.ID_ANY, "Other Activities")
        self.QuitButton = wx.Button(self.MainMenuPanel, wx.ID_EXIT, "Quit")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.on_button_manage_contacts_clicked, self.ManageContactsButton)
        self.Bind(wx.EVT_BUTTON, self.on_button_print_labels_clicked, self.PrintLabelsButton)
        self.Bind(wx.EVT_BUTTON, self.on_button_other_activity_clicked, self.OtherActivityButton)
        self.Bind(wx.EVT_BUTTON, self.on_button_quit_clicked, self.QuitButton)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: MainMenuFrameClass.__set_properties
        self.SetTitle("Main Menu")
        self.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "DejaVu Sans"))
        self.ManageContactsButton.SetToolTip("Add, change, or delete contacts")
        self.PrintLabelsButton.SetToolTip("Choose this button to print labels for the contacts")
        self.OtherActivityButton.SetToolTip("Other activities such as import or export contacts, etc.")
        self.QuitButton.SetToolTip("Leave the Christmas Label program")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: MainMenuFrameClass.__do_layout
        sizer_1 = wx.WrapSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        label_1 = wx.StaticText(self.MainMenuPanel, wx.ID_ANY, "Main Menu")
        label_1.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        sizer_2.Add(label_1, 0, wx.ALIGN_CENTER, 0)
        sizer_2.Add(self.ManageContactsButton, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_2.Add(self.PrintLabelsButton, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_2.Add(self.OtherActivityButton, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        sizer_2.Add(self.QuitButton, 0, wx.ALIGN_CENTER | wx.EXPAND, 0)
        self.MainMenuPanel.SetSizer(sizer_2)
        sizer_1.Add(self.MainMenuPanel, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def on_menu_file_new(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_menu_file_new' not implemented!")
        event.Skip()

    def on_menu_file_open(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_menu_file_open' not implemented!")
        event.Skip()

    def on_menu_file_save(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_menu_file_save' not implemented!")
        event.Skip()

    def on_menu_file_save_as(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_menu_file_save_as' not implemented!")
        event.Skip()

    def on_menu_edit_cut(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_menu_edit_cut' not implemented!")
        event.Skip()

    def on_menu_edit_copy(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_menu_edit_copy' not implemented!")
        event.Skip()

    def on_menu_edit_paste(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_menu_edit_paste' not implemented!")
        event.Skip()

    def on_menu_help_about(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_menu_help_about' not implemented!")
        event.Skip()

    def on_button_manage_contacts_clicked(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_button_manage_contacts_clicked' not implemented!")
        event.Skip()

    def on_button_print_labels_clicked(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_button_print_labels_clicked' not implemented!")
        event.Skip()

    def on_button_other_activity_clicked(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_button_other_activity_clicked' not implemented!")
        event.Skip()

    def on_button_quit_clicked(self, event):  # wxGlade: MainMenuFrameClass.<event_handler>
        print("Event handler 'on_button_quit_clicked' not implemented!")
        event.Skip()

# end of class MainMenuFrameClass

class ChristmasLabelsApp(wx.App):
    def OnInit(self):
        self.MainMenuFrame = MainMenuFrameClass(None, wx.ID_ANY, "")
        self.SetTopWindow(self.MainMenuFrame)
        self.MainMenuFrame.Show()
        return True

# end of class ChristmasLabelsApp

if __name__ == "__main__":
    ChristmasLabels = ChristmasLabelsApp(0)
    ChristmasLabels.MainLoop()
