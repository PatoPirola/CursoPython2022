# Proyecto Curso Python 2022 - AppBanco 

## Contenido
- Contiene 3 modelos: clientes, productos y sucursales.
- Se crearon 3 formularios, 1 para cada modelo.
- Tiene 1 .html para cada modelo donde en ellos se puede ingresar datos en el formulario
para grabar datos en la BD. Cada uno tiene herencia de HTML.
- El formulario para leer datos se realizó sobre clientes, se debe ingresar en django a buscar_cliente,
luego se debe colocar un número de código de cliente, ej: 9999.
- Los resultados de la búsqueda son arrojados en el resuldatoCliente.html, si no se ingresa un código, 
debe aparecer una respuesta en rojo.
-Todos los métodos fueron generados en el archivo views.py de AppBanco.



## Como crear un usuario

```python 
from django.contrib.auth.models import User
user = User.objects.create_user('Patricia', 'ppirola@gmail.com', '123') 
```
