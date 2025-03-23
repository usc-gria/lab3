# LAB3: Estructuras de Datos en el Sistema de Música en Streaming

## **Objetivos Generales**
1. Implementar estructuras de datos avanzadas (listas enlazadas, colas y pilas) en Python con POO.
2. Integrar estas estructuras en el sistema de música en streaming desarrollado en LAB2.
3. Aplicar los principios de encapsulación y modularidad para mejorar la organización del código.

---

## **Actividades**

#### Comentarios generales
Implementa en las clases que creas conveniente, la función especial `__eq__(self)`.
Esto permitirá especificar como se deben comparar dos objetos de la misma clase (dos canciones, por ejemplo).
Es posible que sea necesario implementar alguna otra función especial, revisa cuales son.

Actualiza el UML con las nuevas funcionalidades, clases y atributos.


### **0. Implementa los TAD**

Implementa las clases Pila y Cola, en sus archivos correspondientes, como subclases de ListaEnlazada.
Prueba cada una de las clases con diferentes instancias (usando números enteros o cadenas de caracteres, por ejemplo) y comprueba que todo funciona como se espera. 


### **1. Implementación de una Lista Enlazada para el Catálogo de Canciones**
#### **Descripción:**
Se reemplazará la lista "actuales" y "eliminadas" utilizada en la clase `Catalogo` por una **lista enlazada**. 
Cada nodo de la lista representará una canción.

#### **Clase `Nodo`**
Ya se encuentra implementado.
- `nodo`: Objeto de la clase `Cancion`.
- `siguiente`: Referencia al siguiente nodo en la lista.

#### **Clase `Catalogo`**
Adapta las funcionalidades de la clase catálogo para hacer uso de las listas enlazadas.

### **2. Implementación de una Pila para el Historial de Reproducción**
#### **Descripción:**
Cada usuario tendrá un historial de canciones reproducidas, implementado como una **pila**.
Únicamente deben ser canciones de su biblioteca o sus listas de reproducción.

#### **Clase Usuario**
Extendemos la clase Usuario para incluir el historial.
- `historial`: instancia de la clase Pila
- Métodos:
  - `agregar_a_historial(cancion)`: Apila una canción recién reproducida.
  - `deshacer_reproduccion()`: Desapila la última canción reproducida.
  - `mostrar_historial()`: Muestra todas las canciones en el historial.

### **3. Implementación de una Cola para la Cola de Reproducción**
#### **Descripción:**
Se creará una **cola** que manejará las canciones en espera para ser reproducidas.

#### **Clase Usuario**
- `cola_reproducción`: instancia de la clase Cola
- Métodos:
  - `agregar_a_espera(cancion)`: Encola una nueva canción para reproducción.
  - `reproducir_siguiente()`: Desencola y reproduce la siguiente canción, pasando al historial.
  - `mostrar_lista_espera()`: Muestra todas las canciones en la lista de espera.

### **4. Sistema de filtrado inteligente**
Implementa un sistema de filtrado para la búsqueda y selección de canciones basada en el nombre del artista.
Le pedimos al usuario el nombre del artista primero y le mostramos únicamente esas canciones para la selección.
Para selección del artista podemos también mostrar un listado, implementando en el cátalogo.

### **4. Pasa el resto de listas a listas enlazadas**
Todas las listas son ahora listas enlazadas (amigos, listas de reproducción, etc).

### **5. Ficheros**
El programa debe leer la información de canciones, usuarios y listas públicas desde 3 ficheros CSV diferentes.
Se proporciona el archivo `caniones.csv` para ver como es el formato, con 200 canciones.
Cuando el programa finaliza, también debe guardar toda la información en los archivos.

### **6. Crea un sistema de recomendación de canciones para el usuario**
El sistema recomendará a cada usuario las canciones más reproducidas en la plataforma por otros usuarios. La idea es que el usuario descubra canciones populares, aunque no estén aún en su historial o favoritos.
Funciona de la siguiente manera:
1. Cada vez que un usuario reproduce una canción: incrementa tanto su contador personal (en su perfil) de la canción como el contador global en el catálogo.
2. Al solicitar recomendaciones:
   - El sistema ordena las canciones en reproducciones_globales por número de reproducciones, de mayor a menor.
   - Se filtran las canciones que el usuario ya ha escuchado, tiene en su historial o biblioteca o listas de reproducción.
   - Se muestran las canciones populares restantes como recomendación.

*Nota*: Deberás extender la clase canción para añadir el número de reproducciones como atributo.




### Sugerencias de organización para las 3 sesiones:

Primera sesión:
1. Implementación de ListaEnlazada, Pila, Cola → pruebas básicas.
2.	Cambiar la lista de Catalogo por lista enlazada. 
3.	Introducir la necesidad de métodos especiales como __eq__.
4.	Lectura inicial del CSV (dejando guardado para después).

Objetivo: Que al final las listas, pilas, colas funcionando.

Segunda sesión (2.5h):
1.	Cambiar historial y cola de reproducción en Usuario para usar pila y cola.
2.	Refactorizar listas → listas enlazadas.
3.	Implementar sistema de filtrado por artista.
4.	Empiezan a integrar lectura/escritura CSV para usuarios, listas públicas.


Tercera sesión (2.5h):
1.	Sistema de recomendación: contador global, contador por usuario.
2.	Métodos para ordenar y filtrar recomendaciones.
3.	Actualización del UML.
4.	Guardado de toda la información en CSVs al final.
5.	Pruebas completas.


---

## **Entrega Final**
- Código bien estructurado y documentado.
- Uso correcto de listas enlazadas, colas y pilas.
- Aplicación de restricciones y validaciones.
- Pruebas demostrando la integración de las estructuras de datos en el sistema de música en streaming.

