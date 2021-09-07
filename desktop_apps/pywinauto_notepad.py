from pywinauto.application import Application

## open application
app = Application(backend='uia').start('notepad.exe') 

## connect with the application
# app = Application(backend='uia').connect(title='Untitled - Notepad', timeout=30)

## get app identifiers
# app.UntitledNotepad.print_control_identifiers()

## automate

# type into windows
text_editor = app.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object() # create editor object
text_editor.type_keys("Trying out automation\nworks...", with_spaces=True) # type into editor window

# interact with menu
file_menu = app.UntitledNotepad.child_window(title="File", control_type="MenuItem").wrapper_object()
file_menu.click_input()
# app.UntitledNotepad.print_control_identifiers()

# save as..
app.UntitledNotepad.menu_select("File -> Save As")
# app.UntitledNotepad.print_control_identifiers()

save_text = app.UntitledNotepad.child_window(title="File name:", auto_id="1001", control_type="Edit")
file_name = 'testing3.txt'
save_text.type_keys(file_name)
# app.UntitledNotepad.print_control_identifiers()
save_button = app.UntitleNotepad.child_window(title="Save", auto_id="1", control_type="Button")
save_button.click_input()

# close notepad
app[file_name+' - Notepad'].menu_select("File -> Exit")

# draw outline
# app.UntitledNotepad.draw_outline()