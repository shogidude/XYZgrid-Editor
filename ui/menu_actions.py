import tkinter as tki

def create_new_map(root):
    NewMapDialog()



class NewMapDialog(object):

    root = None

    def __init__(self):

        root = self.root = tki.Tk()
        root.title('New Map Dialog')

        frm = tki.Frame(self.root, borderwidth=4, relief='ridge')
        frm.pack(fill='both', expand=True)

        label = tki.Label(frm, text="What width and height should the new map be?")
        label.pack(padx=4, pady=4)

        self.width_entry = tki.Entry(frm)
        self.width_entry.pack(pady=4)

        self.height_entry = tki.Entry(frm)
        self.height_entry.pack(pady=4)

        #TODO: submit and cancel need to be on a row, not a column
        b_submit = tki.Button(frm, text='Submit')
        b_submit['command'] = lambda: self.entry_to_dict()
        b_submit.pack()

        b_cancel = tki.Button(frm, text='Cancel')
        b_cancel['command'] = self.root.destroy
        b_cancel.pack(padx=4, pady=4)

    def entry_to_dict(self):
        #TODO: set default values of width and height if none given
        width = self.width_entry.get()
        height = self.height_entry.get()

        print("width ... ", width)
        print("height ... ", height)
        self.root.destroy()







def open_map(root):

    print("Opening map.")


def save_as_map(root):

    print("Saving map.")
