


#Packages
import os
import tkinter as tk
from tkinter import ttk
from PIL  import ImageTk, Image
# Local library imports
import Scores
import Juego2
from  Constantes import imagen_papel,imagen_piedra,imagen_tijera

LARGE_FONT= ("Verdana", 12)
newsize = (100,100)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Juego Piedra Papel Tijera')


class ControlFrame(ttk.LabelFrame):

    def __init__(self,container):
        
        super().__init__(container)
        
        self.name = "Player1"
        self.jugada_jugador1 = None
        self.jugada_jugador2 = None
        self.ganador = None
        container.grid_rowconfigure(0, weight=3)
        container.grid_columnconfigure(0, weight=3)
        self.frames = {}

        for F in (StartPage, frame_menu,frame_top,menu_jugador,menu_partida,menu_resultado):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
       


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
    
    def get_name(self):
        return self.name

    def set_name(self,name): 
        self.name = name
        return None
    
    def set_jugada(self,n,jugada):
        "'n: numero de jugador: jugador 1 n=1, n=2 jugador2 '"
        if n==1:
            self.jugada_jugador1 = jugada
 
        if n==2: 
            self.jugada_jugador2 = jugada
        print(jugada)
        return None
    
    def get_jugada(self,n):
        jugada = None
        if n==1:
            jugada = self.jugada_jugador1 
 
        if n==2: 
            jugada = self.jugada_jugador2 
        
        return jugada
    
    def get_ganador(self):
        return self.ganador
    
    def set_ganador(self,ganador):
        self.ganador = ganador
        return None

    def reset(self):
        self.set_ganador(None)
        self.set_jugada(1,None)
        self.set_jugada(2,None)
        return None

class StartPage(tk.Frame):

    def __init__(self,container,controller):
        
        super().__init__(container)

        photo = ImageTk.PhotoImage(Image.open("./imagenes/Inicio.jpg"))
        img_inicial = tk.Label(self, text = "JANKENPOX",image=photo,anchor='center')
        img_inicial.grid(column =0,row = 0)
        img_inicial.image = photo
        label_inicio = tk.Button(self, text = "JANKENPO",command=lambda: controller.show_frame(frame_menu))
        label_inicio.grid(column =0,row = 1)



class frame_menu(tk.Frame):

    def __init__(self,container,controller):
        
        super().__init__(container)

        label_menu = tk.Label(self, text = "JANKENPON",padx=5,pady=5,font=LARGE_FONT)
        label_raya = tk.Label(self, text = "---------------------------",font=LARGE_FONT)
        menu_nueva_partida = tk.Button(self, text = "Nueva partida",command=lambda: controller.show_frame(menu_partida))
        menu_tops = tk.Button(self, text = "Tops",command=lambda: controller.show_frame(frame_top))
        menu_nuevo_jugador= tk.Button(self, text = "Seleccionar jugador",command=lambda: controller.show_frame(menu_jugador))
  
        label_menu.grid(column=0,row=0)
        label_raya.grid(column=0,row=1)
        menu_nueva_partida.grid(column=0,row=2)
        menu_nuevo_jugador.grid(column=0,row=3)
        menu_tops.grid(column=0,row=4)

class frame_top(tk.Frame):
    def __init__(self,container,controller):
        
        super().__init__(container)

        self.tv = self.__create_tree()
        vuelta = tk.Button(self, text = "Volver menu Principal",padx=5,pady=5 ,command=lambda: controller.show_frame(frame_menu))

        vuelta.grid(column=0,row=0)
        self.tv.grid(column=0,row=0,sticky='nsew')
        vuelta.grid(column=0,row=1)

    def __create_tree(self):
            tree = ttk.Treeview(self, columns=(1,2,3,4,5,6), show= "headings")
            tree.heading(1, text='Fecha', anchor='center')
            tree.heading(2, text='Nombre Jugador 1', anchor='center')
            tree.heading(3, text='Nombre Jugador 2', anchor='center')
            tree.heading(4, text='Ganador', anchor='center')
            tree.heading(5, text='Jugada 1', anchor='center')
            tree.heading(6, text='Jugada 2', anchor='center')
            return tree

    def insert_valor(self,lista):
            for row in lista:
                self.tv.insert('', tk.END, values=row)
            return None        

class menu_jugador(tk.Frame):

    def __init__(self,container,controller):
        
        super().__init__(container)

        label_menu = tk.Label(self, text = "Menu Jugador",padx=5,pady=5,font=LARGE_FONT)
        label_raya = tk.Label(self, text = "---------------------------",font=LARGE_FONT)       
        self.listbox = tk.Listbox(self)
        selec_nombre = tk.Button(self, text = "Seleccionar",command=lambda: change_player(self,controller))
        volver = tk.Button(self, text = "Menu Principal",command=lambda: controller.show_frame(frame_menu))
        new_name = tk.Button(self, text = "Nuevo nombre",command=lambda: reset_new_name(self))
        self.entry_name = tk.Entry(self)
        self.var = tk.StringVar()
        self.jugador_label_1 =  tk.Label(self, text = "Jugador actual: ",padx=5,pady=5,font=LARGE_FONT)
        self.jugador_label_2 =  tk.Label(self, textvariable=  self.var,padx=5,pady=5,font=LARGE_FONT)
        

        label_menu.grid(column=0,row=0)
        label_raya.grid(column=0,row=1)
        self.listbox.grid(column=0,row=2)
        new_name.grid(column=2,row=2)
        self.entry_name.grid(column=3,row=2)
        self.jugador_label_1.grid(column=2,row=3)
        self.jugador_label_2.grid(column=2,row=4)
        selec_nombre.grid(column=0,row=3)
        volver.grid(column=0,row=5,rowspan=4)
      
        self.listbox.insert(1, controller)
        self.var.set(controller.get_name())

        
        def reset_new_name(self):
            name = self.entry_name.get()
            self.entry_name.delete(0, "end")

            n = self.listbox.size()
            self.listbox.insert(1, name)
            return None

        def __create_lb(self):
            lb = ttk.Listbox(self)
            return lb

        def change_player(self,controller):
            name = self.listbox.get(self.listbox.curselection())
            controller.set_name(name)
            self.var.set(name)

class menu_partida(tk.Frame):

    def __init__(self,container,controller):
        self.eleccion = None
        super().__init__(container)
        newsize = (100, 100)
        global photo_papel
        global photo_tijeras
        global photo_piedra
        #Letras de arriba
        label_menu = tk.Label(self, text = "JANKENPON",font=LARGE_FONT)
        label_menu.grid(column = 0,row = 0,columnspan=3)  

        #Papel
        photo_papel = ImageTk.PhotoImage(imagen_papel)
        img_papel = tk.Button(self, image=photo_papel)
        img_papel.grid(column = 0,row = 1)
        img_papel.bind('<Button>', lambda event: eleccion_jugador(self,event,n="Papel"))
        img_papel.bind('<Button>',lambda event: controller.show_frame(menu_resultado), add='+')
        img_papel.bind('<Button>', lambda event: jugar(self,controller,"Papel"), add='+')
        img_papel.bind('<Button>', lambda event: update_resultados(self,controller), add='+')
        img_papel.image = photo_papel


        #Tijeras
        photo_tijeras = ImageTk.PhotoImage(imagen_tijera)
        img_tijeras = tk.Button(self,image=photo_tijeras)
        img_tijeras.grid(column = 1,row = 1)
        img_tijeras.bind('<Button>', lambda event: eleccion_jugador(self,event,n="Tijera"))
        img_tijeras.bind('<Button>', lambda event: controller.show_frame(menu_resultado), add='+')
        img_tijeras.bind('<Button>', lambda event: jugar(self,controller,"Tijera"), add='+')
        img_tijeras.bind('<Button>', lambda event: update_resultados(self,controller), add='+')
        img_tijeras.image = photo_tijeras
   

        #Piedra
        photo_piedra = ImageTk.PhotoImage(imagen_piedra)
        img_piedra = tk.Button(self, image=photo_piedra)
        img_piedra.grid(column = 2,row = 1)
        img_piedra.bind('<Button>', lambda event: eleccion_jugador(self,event,n="Piedra"))
        img_piedra.bind('<Button>', lambda event: controller.show_frame(menu_resultado), add='+')
        img_piedra.bind('<Button>', lambda event: jugar(self,controller,"Piedra"), add='+')
        img_piedra.bind('<Button>', lambda event: update_resultados(self,controller), add='+')
        img_piedra.image = photo_piedra

        #Letras de arriba
        label_info = tk.Label(self, text = "SELECCIONE ELECCION")
        label_info.grid(column = 0,row = 2,columnspan=3)  

        #boton menu principal
        volver = tk.Button(self, text = "Menu Principal",command=lambda: controller.show_frame(frame_menu))
        volver.grid(column=0,row=3,columnspan=3)
        
     

        def eleccion_jugador(self,event,n):
            elecciones =["Piedra", "Papel", "Tijera"]
            lb_eleccion = tk.Label(self, text= n)
            lb_eleccion.grid(column=1,row=4)
            return None



        def jugar(self,controller,jugada):
            "'Aqui se produce la partida."
            ''' 
            jugador: seria el jugador humano
            robot sería un programa que elige automaticamente
            play: se encarga de decidir quien gana
            '''
            nombre_jugador_1 = controller.get_name()
            jugador = Juego2.jugador(nombre_jugador_1)
            jugador.set_eleccion(jugada)
            robot = Juego2.NPC()
            play = Juego2.partida(jugador,robot)
            
            jugada_jugador_1 = jugador.get_eleccion()
            jugada_jugador_2 = robot.get_eleccion()
            ganador = play.get_resultado()
            
            controller.set_jugada(1, jugada_jugador_1)
            controller.set_jugada(2, jugada_jugador_2)
            controller.set_ganador(ganador)
            return None

        def update_resultados(self,controller):
            controller.frames[menu_resultado].update_images(controller)
            controller.frames[menu_resultado].update_labels(controller)
            controller.frames[menu_resultado].update_nombre_jugador1(controller.get_name())

            return None


class menu_resultado(tk.Frame):

    def __init__(self,container,controller):
        self.eleccion = None
        super().__init__(container)

        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.update_labels(controller)
        
        ######  Frame izquierda
        self.frame_izda = tk.Frame(self)
        self.frame_izda.grid(column=0,row=0)
        #label name
        self.var_name = tk.StringVar()
        label_izda_1 = tk.Label(self.frame_izda, textvariable = self.var_name)
        label_izda_1.grid(column=0,row=0)

        # Label resultado izda
        label_izda_2 = tk.Label(self.frame_izda, textvariable= self.var1 )
        label_izda_2.grid(column=0,row=2)
        
        # Label imagen izda
        self.label_izda_imgen = tk.Label(self.frame_izda, text= 'Jugador 1' )
        self.label_izda_imgen.grid(column=0,row=1)

        ##### Frame derecha
        self.frame_dcha = tk.Frame(self)
        self.frame_dcha.grid(column=1,row=0)
        #label name
        label_dcha_1 = tk.Label(self.frame_dcha, text= 'NPC' )
        label_dcha_1.grid(column=0,row=0)
        
        # Label resultado dcha
        label_dcha_2 = tk.Label(self.frame_dcha, textvariable= self.var2 )
        label_dcha_2.grid(column=0,row=2)
        
        # Label imagen derecha
        self.label_dcha_imgen = tk.Label(self.frame_izda, text= 'Jugador 2' )
        self.label_dcha_imgen.grid(column=0,row=1)

        #volver
        volver = tk.Button(self, text = "Menu Principal")
        volver.bind('<Button>',lambda event: controller.show_frame(frame_menu))
        volver.bind('<Button>',lambda event: controller.reset(), add='+')
        volver.bind('<Button>',lambda event: self.clear(event), add='+')
        volver.grid(column=0,row=1, columnspan=2)

    def update_nombre_jugador1(self,name):
        '''actualiza el nombre del jugador'''
        self.var_name.set(name)
        return None

    def update_images (self, controller):
            #Jugador 1: quita imagen anterior y la actualiza
            self.label_izda_imgen.grid_forget()
            jugada_jugador_1 = controller.get_jugada(1)
            self.label_izda_imgen = self.__update_imagen(jugada_jugador_1,self.frame_izda)
            self.label_izda_imgen.grid(column=0,row=1)
            
            #Jugador 2: quita imagen anterior y la actualiza
            self.label_dcha_imgen.grid_forget()
            jugada_jugador_2 = controller.get_jugada(2)
            self.label_dcha_imgen = self.__update_imagen(jugada_jugador_2,self.frame_dcha)
            self.label_dcha_imgen.grid(column=0,row=1)
            return None
    
    def __update_imagen(self,  jugada,frame):
            '''creacion de la imagen según la jugada
            frame:Frame
                valor:  izda o derecha
            jugada: str 
                 valor: Piedra, Papel o Tijera
            '''
            if jugada == 'Papel' :   
                photo_papel = ImageTk.PhotoImage(imagen_papel)
                label = tk.Label(frame, image= photo_papel)
                label.image =  photo_papel
                
                return label
            
            elif jugada == 'Piedra':

                photo_piedra = ImageTk.PhotoImage(imagen_piedra)
                label = tk.Label(frame, image= photo_piedra) 
                label.image =  photo_piedra
              
                return label
            
            elif jugada == 'Tijera':

                photo_tijera = ImageTk.PhotoImage(imagen_tijera)
                label = tk.Label(frame, image= photo_tijera) 
                label.image =  photo_tijera
            
                return label

    def update_labels(self,controller):
        ''' actualiza los resultados de victoria y derrota por cada jugador'''

        resultado_izda = self.__resultado_label(controller,'jugador 1')
        self.var1.set(resultado_izda)

        resultado_dcha = self.__resultado_label(controller,'jugador 2')
        self.var2.set(resultado_dcha)

        return None

    
    def __resultado_label(self,controller,jugador):
        '''jugador: str
                valores posibles: jugador 1 o jugador 2'''
        if controller.get_ganador() is not None:
            if controller.get_ganador() == 'empate':
                return 'empate'
            elif jugador == controller.get_ganador():
                return 'VICTORIA'
            elif jugador != controller.get_ganador():
                return 'DERROTA'
            else:
               return 'error'
        else:
            return 'no partida'
        
    
    def clear(self,event): 
        os.system('cls') 
        return None #borrar consola


if __name__ == "__main__":

    app = App()
    ControlFrame(app)
    app.mainloop()

