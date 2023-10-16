from django.http import HttpResponse
from django.template import Template, Context

#Funcion comun
def saluda(req):
    return HttpResponse('App inicializada')

#Funcion comun
def despedirse(req):
    return HttpResponse(
        """
        <h1>gracias por visitarnos</h1>
        """
    )
#Funcion con parametros en path
def saluda_con_nombre(req, nombre):
    texto = f'Hola, mi nombre es {nombre}'
    return  HttpResponse(texto)

#Funcion con Template
def saluda_con_template(req):
    #debemos abrir el archivo html, esto lo guardamos en una variable.
    mi_html = open("C:/Users/fotero/Downloads/Acceso Rapido/Personal/Python/Coder_v2/AplicacionPrueba/MiApp/MiApp/Templates/template.html")
    #Ahora tengo que leer ese archivo, para ello debo importar template y context from django.template
    #genero asi una instancia del template
    plantilla = Template(mi_html.read())
    
    #cerramos el archivo para que no siga consumiendo recursos una vez utilizado
    mi_html.close()
    
    #Ahora creo un contexto en el que va a viajar ese template
    
    mi_contexto = Context()
    
    #ahora debo utilizar el metodo Render para generar lo que voy a mostrar en el browser
    documento = plantilla.render(mi_contexto)
    
    #por ultimo retornamos el http response con el template renderizado
    return HttpResponse(documento)
    