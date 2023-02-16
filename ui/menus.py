from tkinter import Menu
import ui.menu_actions as ma
from ui.typing_direction import TypingDirection


def print_command(the_command):
    print("menu selected-->" + the_command) #debugging and a placeholder

def config_menubar(root):
    menubar = Menu(root)

    # File menu
    file_menu = Menu(menubar, tearoff=0)

    file_menu.add_command(
        label='New map ...',
        command=lambda: ma.create_new_map(root)
    )

    file_menu.add_command(
        label='Import map ...',
        command=lambda: ma.import_map(root)
    )

    file_menu.add_separator()

    file_menu.add_command(
        label='Generate code ...',
        command=lambda: ma.generate_code(root)
    )

    file_menu.add_separator()

    file_menu.add_command(
        label='Exit',
        command=root.destroy
    )

    menubar.add_cascade(label="File", menu=file_menu)


    # Edit menu
    edit_menu = Menu(menubar, tearoff=0)

    edit_menu.add_command(
        label='Copy Map Selection',
        command=lambda: print_command('Copy Map Selection')
    )

    edit_menu.add_command(
        label='Cut Map Selection',
        command=lambda: print_command('Cut Map Selection')
    )

    edit_menu.add_command(
        label='Paste Map Selection',
        command=lambda: print_command('Paste Map Selection')
    )

    edit_menu.add_separator()

    edit_menu.add_command(
        label='Type north',
        command=lambda: TypingDirection.set_selected_direction('N')
    )

    edit_menu.add_command(
        label='Type northeast',
        command=lambda: TypingDirection.set_selected_direction('NE')
    )

    edit_menu.add_command(
        label='Type east',
        command=lambda: TypingDirection.set_selected_direction('E')
    )

    edit_menu.add_command(
        label='Type southeast',
        command=lambda: TypingDirection.set_selected_direction('SE')
    )

    edit_menu.add_command(
        label='Type south',
        command=lambda: TypingDirection.set_selected_direction('S')
    )

    edit_menu.add_command(
        label='Type southwest',
        command=lambda: TypingDirection.set_selected_direction('SW')
    )

    edit_menu.add_command(
        label='Type west',
        command=lambda: TypingDirection.set_selected_direction('W')
    )

    edit_menu.add_command(
        label='Type northwest',
        command=lambda: TypingDirection.set_selected_direction('NW')
    )

    menubar.add_cascade(label="Edit", menu=edit_menu)

    # Config menu
    config_menu = Menu(menubar, tearoff=0)

    config_menu.add_command(
        label='Teleporter letters',
        command=lambda: ma.change_teleporter_letters(root)
    )

    config_menu.add_separator()

    config_menu.add_command(
        label='Configure room',
        command=lambda: print_command('Configure room')
    )

    config_menu.add_command(
        label='Configure exit(s)',
        command=lambda: print_command('Configure exit(s)')
    )

    config_menu.add_separator()

    config_menu.add_command(
        label='Default room',
        command=lambda: print_command('Default room')
    )

    config_menu.add_command(
        label='Default exit',
        command=lambda: print_command('Default exit')
    )

    menubar.add_cascade(label="Config", menu=config_menu)

    root.config(menu=menubar)

