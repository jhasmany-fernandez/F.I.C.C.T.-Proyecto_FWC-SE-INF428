# Importar libreria tkinter
import tkinter as tk

# Importar la clase 
from client.gui_app import Frame, barra_menu

def main():
    root = tk.Tk()
    root.title('Sistema Expertos') # titulo en la barra superior del formulario
    root.iconbitmap('img/notas.ico') # icon del formulario
    root.resizable(0,0) # renderizar el tamano del formulario por medio mause
    
    barra_menu(root) # (gui_app.py) barra
    
    app = Frame(root= root) # (gui_app.py) formulario
    
    app.mainloop() # tiempo de espera para que no cierre el formulario

if __name__ == '__main__':
    main()