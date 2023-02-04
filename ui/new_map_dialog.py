import tkinter as tki
from tkinter import RAISED, BOTH, RIGHT

import map.mapping_frame as mf

class NewMapDialog(object):

    def __init__(self, root):

        root.update_idletasks()

        dialog_width = 250
        dialog_height = 100

        at_y = int(root.winfo_rooty() + (root.winfo_height() / 4) - (dialog_height/2))
        at_x = int(root.winfo_rootx() + (root.winfo_width() / 2) - (dialog_width/2))

        self.top = tki.Toplevel(root)
        self.top.geometry(f"{dialog_width}x{dialog_height}+{at_x}+{at_y}")
        self.top.title('New map ...')

        frm = tki.Frame(self.top, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        inner_frame = tki.Frame(frm, borderwidth=2)
        inner_frame.pack(fill=BOTH, expand=True)

        width_label = tki.Label(inner_frame, text="Width?")
        width_label.grid(row=0, column=0)

        self.width_entry = tki.Entry(inner_frame)
        self.width_entry.grid(row=0, column=1)
        self.width_entry.focus_set()

        height_label = tki.Label(inner_frame, text="Height?")
        height_label.grid(row=1, column=0)

        self.height_entry = tki.Entry(inner_frame)
        self.height_entry.grid(row=1, column=1)

        #frm.pack(fill=BOTH, expand=True)

        #submit and cancel need to be on a row, not a column
        b_submit = tki.Button(frm, text='Submit')
        b_submit['command'] = lambda: self.entry_to_dict()
        b_submit.pack(side=RIGHT, padx=5, pady=5)

        b_cancel = tki.Button(frm, text='Cancel')
        b_cancel['command'] = self.top.destroy
        b_cancel.pack(side=RIGHT)

        self.top.grab_set()


    def entry_to_dict(self):
        try:
            width = self.width_entry.get()
            height = self.height_entry.get()

            mf.XYZgridFrame.draw_new_grid(int(width), int(height))

            print("width ... ", width)
            print("height ... ", height)
            self.top.destroy()
        except:
            print("Bad width or height given.")
