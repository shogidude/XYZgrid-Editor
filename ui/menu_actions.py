
from ui.code_gen_toplevel import CodeGenToplevel
from ui.new_map_dialog import NewMapDialog


def create_new_map(root):
    NewMapDialog(root)


def import_map(root):

    print("Import map.")


def generate_code(root):

    print("Generating code.")
    CodeGenToplevel(root)
