import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from CodigoAritm import CodigoAritm

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._boxSimbolos = System.Windows.Forms.TextBox()
		self._boxProbabilidades = System.Windows.Forms.TextBox()
		self._boxMensaje = System.Windows.Forms.TextBox()
		self._procesar = System.Windows.Forms.Button()
		self._boxResultado = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# boxSimbolos
		# 
		self._boxSimbolos.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._boxSimbolos.Location = System.Drawing.Point(25, 56)
		self._boxSimbolos.Name = "boxSimbolos"
		self._boxSimbolos.Size = System.Drawing.Size(191, 29)
		self._boxSimbolos.TabIndex = 0
		self._boxSimbolos.Text = "a,b,c,d,."
		# 
		# boxProbabilidades
		# 
		self._boxProbabilidades.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._boxProbabilidades.Location = System.Drawing.Point(280, 56)
		self._boxProbabilidades.Name = "boxProbabilidades"
		self._boxProbabilidades.Size = System.Drawing.Size(217, 29)
		self._boxProbabilidades.TabIndex = 1
		self._boxProbabilidades.Text = "0.2,0.4,0.2,0.1,0.1"
		# 
		# boxMensaje
		# 
		self._boxMensaje.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._boxMensaje.Location = System.Drawing.Point(603, 56)
		self._boxMensaje.Name = "boxMensaje"
		self._boxMensaje.Size = System.Drawing.Size(176, 29)
		self._boxMensaje.TabIndex = 2
		self._boxMensaje.Text = "dabac."
		# 
		# procesar
		# 
		self._procesar.Location = System.Drawing.Point(374, 119)
		self._procesar.Name = "procesar"
		self._procesar.Size = System.Drawing.Size(75, 23)
		self._procesar.TabIndex = 3
		self._procesar.Text = "Procesar"
		self._procesar.UseVisualStyleBackColor = True
		self._procesar.Click += self.ProcesarClick
		# 
		# boxResultado
		# 
		self._boxResultado.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._boxResultado.Location = System.Drawing.Point(25, 158)
		self._boxResultado.Multiline = True
		self._boxResultado.Name = "boxResultado"
		self._boxResultado.Size = System.Drawing.Size(839, 250)
		self._boxResultado.TabIndex = 4
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("Bookman Old Style", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(25, 27)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(191, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "Símbolos"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Bookman Old Style", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(280, 26)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(217, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "Probabilidades"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Bookman Old Style", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(603, 27)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(176, 23)
		self._label3.TabIndex = 7
		self._label3.Text = "Mensaje"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(887, 435)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._boxResultado)
		self.Controls.Add(self._procesar)
		self.Controls.Add(self._boxMensaje)
		self.Controls.Add(self._boxProbabilidades)
		self.Controls.Add(self._boxSimbolos)
		self.Name = "MainForm"
		self.Text = "Código Aritmético"
		self.ResumeLayout(False)
		self.PerformLayout()


	def ProcesarClick(self, sender, e):
		self._boxResultado.Text = 'Verificar los valores en los campos'
		campos_vacios = (self._boxSimbolos.Text!='' and self._boxProbabilidades.Text!='' and self._boxMensaje.Text!='')
		if campos_vacios and len(self._boxMensaje.Text)>1:
			alfabeto, probs, mensj = self._boxSimbolos.Text, self._boxProbabilidades.Text, self._boxMensaje.Text
			try:
				inst = CodigoAritm(alfabeto, probs)
			except SimbProbsError as e:
				self._boxResultado.Text = e
			else:
				self._boxResultado.Text = 'Verificar los valores en los campos'
				if inst.simbTermina() in self._boxMensaje.Text:
					inst.preCodMsg(mensj)
					msj = 'Mensaje codificado: ' + inst.codificarMensaje() + ' ___><___ Mensaje decodificado: ' + inst.decodificarMensaje()
					
					self._boxResultado.Text = msj
		
			
def getConjunto(string, separador):
	lista = string.split(separador)
	
	return lista