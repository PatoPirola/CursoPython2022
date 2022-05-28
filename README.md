Indicaciones de cómo se compone el proyecto y cómo probarlo:

1-Contiene 3 modelos: clientes, productos y sucursales.
2-Se crearon 3 formularios, 1 para cada modelo.
3-Tiene 1 .html para cada modelo donde en ellos se puede ingresar datos en el formulario
para grabar datos en la BD. Cada uno tiene herencia de HTML.
4-El formulario para leer datos se realizó sobre clientes, se debe ingresar en django a buscar_cliente,
luego se debe colocar un número de código de cliente, ej: 9999.
5-Los resultados de la búsqueda son arrojados en el resuldatoCliente.html, si no se ingresa un código, 
debe aparecer una respuesta en rojo.
6-Todos los métodos fueron generados en el archivo views.py de AppBanco.



# Create User

```python 
from django.contrib.auth.models import User
user = User.objects.create_user('Patricia', 'ppirola@gmail.com', '123') 
```