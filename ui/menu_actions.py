import tkinter as tki
from tkinter import simpledialog

from map.teleporter_letters import TeleporterLetters
from ui.code_gen_toplevel import CodeGenToplevel
from ui.new_map_dialog import NewMapDialog


def create_new_map(root):
    NewMapDialog(root)


def import_map(root):
    print("Import map.")


def generate_code(root):
    print("Generating code.")
    CodeGenToplevel(root)


def change_teleporter_letters(root):
    TeleporterLetters() #just in case needs initializing
    letters = simpledialog.askstring("Teleporter Letters",
                                     "Comma separated list of teleporter letters:",
                                     initialvalue=TeleporterLetters.get_teleporter_letters(),
                                     parent=root)
    #print("letters:", letters)
    if (letters is not None):
        TeleporterLetters.set_teleporter_letters(letters)
