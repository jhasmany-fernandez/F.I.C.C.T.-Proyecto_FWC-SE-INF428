# Importar libreria tkinter
import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width = 300, height = 300)
    
        
# -----------------------------------------------------------------------------------------------------------------------
    # MENU
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label = 'Inicio', menu = menu_inicio)
    
# -----------------------------------------------------------------------------------------------------------------------
    # MAIMENU
    menu_inicio.add_command(label = 'Crear registro bd')
    menu_inicio.add_command(label = 'Eliminar registro bd')
    menu_inicio.add_command(label = 'Salir', command = root.destroy)
    
    barra_menu.add_cascade(label = 'Consultas')
    barra_menu.add_cascade(label = 'Configuracion')
    barra_menu.add_cascade(label = 'Ayuda')
    
# -----------------------------------------------------------------------------------------------------------------------
    
# Importar libreria tkinter
class Frame(tk.Frame): # aclicando herencia
    # 
    def __init__(self, root = None): # constructor
        super().__init__(root, width=480, height=320) # heredar el constructor con el tamano formulario
        self.root = root
        self.pack() # enpaquetado
        self.config(bg='green') # configuracion de backgramo color verde
        
    #
    def campo_formulario(self):
        self.chB_Ictericia = tk.Checkbutton(self, text = 'Ictericia: ', variable=selIctericia, onvalue=1, offvalue=0).place(x=100, y=40)