from tkinter import *
from tkinter import ttk
from countries import Countries
from tkinter import messagebox

class Ventana(Frame):
    
    paises = Countries()

    def __init__(self, master=None):
        super().__init__(master,width=1460, height=400,bg="gray9")
        self.master = master
        self.pack()
        self.create_widgets()
        self.llenaDatos()
        self.habilitarCajas("disable")
        self.habilitarBtnOper("normal")
        self.habilitarBtnGuardar("disable")
        self.id=-1

    def habilitarCajas(self,estado):
        self.txtNombre.configure(state=estado)
        self.txtTipo.configure(state=estado)
        self.txtCantidad.configure(state=estado)
        self.txtUnidades.configure(state=estado)
    
    def habilitarBtnOper(self,estado):
        self.btnNuevo.configure(state=estado)
        self.btnModificar.configure(state=estado)
        self.btnEliminar.configure(state=estado)

    def habilitarBtnGuardar(self,estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def limpiarCajas(self):
        self.txtNombre.delete(0,END)
        self.txtTipo.delete(0,END)
        self.txtCantidad.delete(0,END)
        self.txtUnidades.delete(0,END)
    
    def limpiaGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)

    def llenaDatos(self):
        datos = self.paises.consulta_paises()
        for row in datos:
            self.grid.insert("",END,text=row[0], values=(row[1],row[2],row[3],row[4]))
        if len(self.grid.get_children())>0:
            self.grid.selection_set(self.grid.get_children()[0])

    def fNuevo(self): 
        self.habilitarCajas("normal")
        self.habilitarBtnOper("disable")
        self.habilitarBtnGuardar("normal")
        self.limpiarCajas()
        self.txtNombre.focus()

    def fGuardar(self):
        if self.id==-1:
            self.paises.inserta_pais(self.txtNombre.get(),self.txtTipo.get(),self.txtCantidad.get(),self.txtUnidades.get())
            messagebox.showinfo("Insertar",message="Elemento insertado correctamente")
        else:
            self.paises.modifica_pais(self.id,self.txtNombre.get(),self.txtTipo.get(),self.txtCantidad.get(),self.txtUnidades.get())
            self.id=-1
            messagebox.showinfo("Insertar",message="Elemento insertado correctamente")

        self.limpiaGrid()
        self.llenaDatos()
        self.limpiarCajas()
        self.habilitarBtnGuardar("disable")
        self.habilitarBtnOper("normal")
        self.habilitarCajas("disable")
    
    def fModificar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected,"text")
        if clave=="":
            messagebox.showerror("ALERTA",message="debes seleccionar un elemento")
        else:
            self.id=clave
            self.habilitarCajas("normal")
            valores=self.grid.item(selected,"values")
            self.limpiarCajas()
            self.txtNombre.insert(0,valores[0])
            self.txtTipo.insert(0,valores[1])
            self.txtCantidad.insert(0,valores[2])
            self.txtUnidades.insert(0,valores[3])
            self.habilitarBtnOper("disable")
            self.habilitarBtnGuardar("normal")
            self.txtNombre.focus()
    
    def fEliminar(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected,"text")
        if clave=="":
            messagebox.showerror("ALERTA",message="debes seleccionar un elemento")
        else:
            print(clave)
            valores = self.grid.item(selected,"values")
            data=str(clave) + ","+ valores[0] + ","+ valores[1]
            r= messagebox.askquestion("ELIMINAR",message="¿Deseas eliminar el registro seleccionado?\n" + data)

            if r == messagebox.YES:
                n = self.paises.elimina_pais(clave)
                if n==1:
                    messagebox.showinfo("Eliminar",message="Elemento eliminado correctamente")
                    self.limpiaGrid()
                    self.llenaDatos()
                else:
                    messagebox.showinfo("Eliminar",message="No fue posible eliminar el elemento")
            else:
                pass

    def fCancelar(self):
        m = messagebox.askquestion("Cancelar",message="Estas seguro que deseas cancelar la operación")
        if m == messagebox.YES:
            self.limpiarCajas()
            self.habilitarBtnGuardar("disable")
            self.habilitarBtnOper("normal")
            self.habilitarCajas("disable")
        else:
            pass

    def create_widgets(self):
        frame1 = Frame(self, bg="turquoise4")
        frame1.place(x=0,y=0,width=100, height=350)        
        
        self.btnNuevo=Button(frame1,text="New farmaco", command=self.fNuevo, bg="gray9", fg="white")
        self.btnNuevo.place(x=5,y=50,width=90, height=30 )        
        
        self.btnModificar=Button(frame1,text="Edit farmaco", command=self.fModificar, bg="gray9", fg="white")
        self.btnModificar.place(x=5,y=90,width=90, height=30)                
        
        self.btnEliminar=Button(frame1,text="Delete farmaco", command=self.fEliminar, bg="gray9", fg="white")
        self.btnEliminar.place(x=5,y=130,width=90, height=30)        
        
        frame2 = Frame(self,bg="thistle4" )
        frame2.place(x=103,y=0,width=150, height=350)                        
        
        lbl1 = Label(frame2,text="Nombre: ",bg="thistle2")
        lbl1.place(x=3,y=5)        
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=3,y=25,width=100, height=20)                
        
        lbl2 = Label(frame2,text="Tipo: ",bg="thistle2")
        lbl2.place(x=3,y=55)        
        self.txtTipo=Entry(frame2)
        self.txtTipo.place(x=3,y=75,width=100, height=20)        
        
        lbl3 = Label(frame2,text="Cantidad: ",bg="thistle2")
        lbl3.place(x=3,y=105)        
        self.txtCantidad=Entry(frame2)
        self.txtCantidad.place(x=3,y=125,width=100, height=20)        
        
        lbl4 = Label(frame2,text="Unidades: ",bg="thistle2")
        lbl4.place(x=3,y=155)        
        self.txtUnidades=Entry(frame2)
        self.txtUnidades.place(x=3,y=175,width=100, height=20)        
        
        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="gray9", fg="white")
        self.btnGuardar.place(x=10,y=310,width=60, height=30)
        
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="gray9", fg="white")
        self.btnCancelar.place(x=80,y=310,width=60, height=30)        
        
        frame3 = Frame(self,bg="thistle4" )
        frame3.place(x=256,y=0,width=1200, height=400)

        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4"))        
        self.grid.column("#0",width=180)
        self.grid.column("col1",width=250, anchor=CENTER)
        self.grid.column("col2",width=250, anchor=CENTER)
        self.grid.column("col3",width=250, anchor=CENTER)
        self.grid.column("col4",width=250, anchor=CENTER)        
        self.grid.heading("#0", text="Id", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Tipo", anchor=CENTER)
        self.grid.heading("col3", text="Cantidad", anchor=CENTER)
        self.grid.heading("col4", text="Unidades", anchor=CENTER)          
        
        self.grid.pack(side=LEFT,fill=Y)

        sb = Scrollbar(frame3,orient=VERTICAL)
        sb.pack(side=RIGHT,fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)

        self.grid["selectmode"]="browse"
        