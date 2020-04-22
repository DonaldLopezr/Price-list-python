from tkinter import ttk
from tkinter import  *
import sqlite3

class Product:
    dbname='Precios_marzo_2020.db'

    def __init__(self,window): #toma la variable ventana 
        self.wind = window   #Almacena la ventana en una propiedad 
        self.wind.title('ENTAER TOYOTA') # modifica las caracteristicas de la ventana caso titulo hasta aqui tenemos una ventana con titulo

        # creando el contenedor
        frame = LabelFrame(self.wind, text = 'Lista de precios') # Crea un contenedor donde estaran los elementos 
        frame.grid( row = 0, column = 0, columnspan = 3, pady = 20) #posiciona el cuadro columnspan (deja espacio), pady (espacio interno) no funciona

        Label(frame, text = 'Introduzca el codigo ').grid(row = 1, column = 1 )
        self.name = Entry(frame, ) #Crea la caja de texto
        self.name.focus()
        self.name.grid(row =1 , column = 2)
       
        # boton de adicionar producto
        ttk.Button(frame, text = 'Buscar',command=self.get_products).grid(row = 3, column = 2, sticky = W + E) #, command = self.add_product

        self.message= Label(text=' ', fg='red')
        self.message.grid(row=3, column = 0, columnspan=2, sticky = W + E)

        self.tree = ttk.Treeview(h=1)
        self.tree.grid(row = 4, column = 0, columnspan = 1)
        self.tree["columns"]=("#1","#2","#3")
        self.tree.column("#0", width=400, minwidth=270)
        self.tree.column("#1", width=250, minwidth=150, stretch=3)
        self.tree.column("#2", width=150, minwidth=200)
        self.tree.column("#0", width=80, minwidth=50, stretch=4)
        self.tree.heading('#0', text = 'Codigo',anchor = CENTER)
        self.tree.heading('#1', text = 'Descripcion',anchor = CENTER)
        self.tree.heading('#2', text = 'Sustituto',anchor = CENTER)
        self.tree.heading('#3', text = 'Precio',anchor = CENTER)
        self.get_products()
    # Conecta con la base de datos
    def run_query(self,query,parameters = ()):
        with sqlite3.connect(self.dbname) as conn: # gconecta a la base de datos y la almacena en conn
            cursor = conn.cursor() # me permite posicionarme en la base de datos
            result = cursor.execute(query, parameters) # ejecuta desde cursor unua consulta y si existen parametros tomalos si no devuelve una tupla vacia
            conn.commit() #ejecuta la sintaxis
            
            return result #retorna el resultado 
    def validation(self):
       return len(self.name.get()) != 0

    def get_products(self):
        if self.validation():
            self.message['text']= ''
            records=self.tree.get_children()
            for elements in records:
                self.tree.delete(elements)
            #quering data 
            query = 'SELECT * FROM Marzo2020 ORDER BY Descripcion DESC'
            db_rows = self.run_query(query)
            #Codigo=('13540 22022')
            Codigo=(self.name.get()) 
            for row in db_rows:
                if row[1]==Codigo:
            #lista=row[]
                    self.tree.insert('',0,text=row[1],values= (row[2],row[3],row[4]))
                    self.message['text'] = 'Producto {} encontrado '.format(self.name.get())
                    self.name.delete(0,END)
                else:
                    self.message['text'] = 'Producto no encontrado  '.format(self.name.get())
        else:
           self.message['text'] = 'Codigo es necesario '
            #self.get_products()  
                    

if __name__== "__main__": #hace la verificacion 
    window = Tk()         #Ejecuta la ventana 
    application = Product(window) #Variable que almacen la clase  y proct pasa la ventana como parametro
    window.mainloop()    #Abre la ventana 


           