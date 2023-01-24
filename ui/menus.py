from tkinter import Menu
import ui.menu_actions as ma

def print_command(the_command):
    print("menu selected-->" + the_command) #debugging and a placeholder

def config_menubar(root):
    menubar = Menu(root)

    # File menu
    file_menu = Menu(menubar, tearoff=0)

    file_menu.add_command(
        label='New',
        command=lambda: ma.create_new_map(root)
    )

    file_menu.add_command(
        label='Open',
        command=lambda: ma.open_map(root)
    )

    file_menu.add_command(
        label='Save as ...',
        command=lambda: ma.save_as_map(root)
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
        command=lambda: print_command('Type north')
    )

    edit_menu.add_command(
        label='Type northeast',
        command=lambda: print_command('Type northeast')
    )

    edit_menu.add_command(
        label='Type east',
        command=lambda: print_command('Type east')
    )

    edit_menu.add_command(
        label='Type southeast',
        command=lambda: print_command('Type southeast')
    )

    edit_menu.add_command(
        label='Type south',
        command=lambda: print_command('Type south')
    )

    edit_menu.add_command(
        label='Type southwest',
        command=lambda: print_command('Type southwest')
    )

    edit_menu.add_command(
        label='Type west',
        command=lambda: print_command('Type west')
    )

    edit_menu.add_command(
        label='Type northwest',
        command=lambda: print_command('Type northwest')
    )

    menubar.add_cascade(label="Edit", menu=edit_menu)

    # Config menu
    config_menu = Menu(menubar, tearoff=0)

    config_menu.add_command(
        label='Teleporter letters',
        command=lambda: print_command('Teleporter letters')
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

