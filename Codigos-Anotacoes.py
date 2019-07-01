import sys

meu_nome = "joao"
def hello(meu_nome):
    print ("OLá",meu_nome)
    return

print ("teste")
hello(meu_nome)



print ("Referência: ", w)
print ("")
print ("A temperatura em Barueri é de: ",temperature)
print ("")

#Quando eu passo o str(wind.get("speed"), eu pego o valor dentro da key do JSON
#:4 eu pego apenas 4 posições do valor
print ("Está ventando a ", str(wind.get("speed")*1.60934)[:4], " Km/h")
#print (len(wind))


#quando eu forneço um FOR com uma variável (nesse caso, o objeto do wind) ele retorna o nome da chave, e o wind.get(str(j)) me retorna o valor desse objeto
for j in wind:
    print("item:  ", j, " / ", wind.get(str(j)))
print ("")
print ("Amanhã: ", tomorrow)

#to_JSON() faz com que ele exiba todos os valores do JSON
print(w.to_JSON())

#Prints
print ("A temperatura em Barueri é de",str(temperature.get('temp')),"ºC")
print ("Está ventando a ", str(wind.get("speed")*1.60934)[:4], " Km/h")
print ("A temperatura em Barueri é de",str(temperature.get('temp')),"ºC")
print ("Está ventando a ", str(wind.get("speed")*1.60934)[:4], " Km/h")
print (status.title())

# Log
    hoje = "%s" % (time.strftime("%Y_%m_%d"))
    arquivo = open("log.%s.txt" % (date), "a")
    if temperatureC != temperature:
        arquivo.write("mudou")
        temperatureC = temperature
    arquivo.write("[%s]" % (hoje))
    arquivo.write("[%s]" % (temperature.get('temp')))
    arquivo.write("[%s]\n" % str(wind.get("speed")*1.60934)[:4])
    arquivo.close()




from tkinter import *

class Application(Frame):
    def say_hi(self):
        print ("hi there, everyone!")

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "green"
        self.QUIT["bg"]   = "black"
        self.QUIT["height"] = "10"
        self.QUIT["width"]  = "10"
        
        self.QUIT["command"] =  self.quit
      

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

#tkinter
from tkinter import *

root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()
root.mainloop()
