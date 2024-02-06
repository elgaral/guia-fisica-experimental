---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"tags": []}

(sec-estimacionIncertidumbre)=

# Estimación incertidumbre

Recordando lo visto en la sección sobre la [**precisión**](subsec-precision) de la medida, para cada medida que se haga de una misma cantidad física invariable en el tiempo, el valor que se obtiene es siempre diferente pero las medidas se dispersan alrededor de un valor central, cómo se observa en la {numref}`fig-preci-exact`. Esto obliga a reportar siempre un valor central (o más probable) y una incertidumbre, siguiendo las reglas de la {numref}`sec-reporteIncertidumbre`. La pregunta que surge es ¿cómo determinar el valor más probable y su incertidumbre a partir de los datos medidos?

```{Note}
Antes de continuar, intente responder la pregunta proponiendo un procedimiento. Luego podrá comparar su solución con la propuesta del libro, y discutirlo con su profesor.
```

Si la dispersión que tienen los datos realmente se debe a incertidumbres aleatorias, se debe esperar dos cosas: tener dos valores extremos que encierren los demás, y encontrar que la mayoría de los valores se encuentran aproximadamente a una distancia menor a la mitad del camino entre los valores extremos. Es de esperarse que la media aritmética de los valores indique el valor más probable de la cantidad física, y que la incertidumbre de esta afirmación corresponda a una fracción de la distancia media entre los valores extremos. El procedimiento a seguir para determinar el valor más probable y la incertidumbre sera:

1. Determinar la media aritmética de los valores, correspondiente al valor central (valor más probable) de la cantidad física.
2. Determinar la mitad de la distancia entre los valores extremos y multiplicar por dos tercios.
3. Dividir el valor obtenido en el numeral 2 por la raiz cuadrada del número total de datos y reportar ese valor como la incertidumbre.

```{warning}
El valor dos tercios surge del análisis estadístico de los datos, y básicamente se refiere a que existe aproximadamente un 68 % de probabilidad de que el valor real de la cantidad física esté dentro del intervalo definido[^validez]. El principio para poder decir esto se estudiará en la {numref}`sec-intervaloConfianza`.

[^validez]: Esto solo es cierto cuando la distribución es normal. Para asegurar que sea normal se deben tomar muchas medidas: más de $30$. Para menos de $30$ se debe usar un factor de corrección conocido como [corrección de t-student](sec-t-student).

Por otro lado, el factor correspondiente a la raiz cuadrada del número de datos será explicado en la {numref}`sec-errorEstandar`. Pero para tener una idea, este factor surge del hecho de que el interés es sobre cuánto se dispersan los posibles valores centrales que podríamos encontrar, si el experimento se repitiera varias veces. También indica que si se toman más medidas el experimento se hace cada vez más preciso.

```

+++

(subsec-estimacionEjemplo1)=
## Ejemplo altura mesa: primera parte[^ejemplo2]
Un estudiante quiere estimar la altura de una mesa pero no cuenta con una regla, solamente tiene un cronómetro y conoce el valor aceptado de la aceleración de la gravedad $g$ en el sitio.

[^ejemplo2]: La segunda parte está en la {numref}`subsec-estimacionEjemplo2`.

```{admonition} Pausa
Antes de continuar piense como procedería usted para medir la altura de la mesa con el cronómetro y el dato de la aceleración de la gravedad.
```

```{admonition} Despliegue para ver el procedimiento que usará el estudiante
:class: dropdown
Al estudiante se le ocurre medir el tiempo que tarda en caer un objeto del borde de la mesa al piso, y usar la expresión que relaciona el tiempo $t$, la aceleración de la gravedad $g$ y la altura $h$:

$$ h = \frac{1}{2}g t^2 $$
```

El primer paso que debe realizar el estudiante es determinar el tiempo que tarda el objeto en caer. Por el tiempo que tiene disponible para el experimento, logra realizar siete medidas que se listan en la {numref}`tabla-tiemp-caida` y se pueden observar en la {numref}`fig-ejemp-estIncert`.

```{list-table} Tiempos de caída en centésimas de segundo.
:name: tabla-tiemp-caida
* - 44
  - 53
  - 47
  - 47
  - 46
  - 50
  - 53
```

```{figure} imagenes/ejemplo-estIncertibumbre.png
:name: fig-ejemp-estIncert

Tiempos de caída del objeto desde el borde de la mesa.
```

Siguiendo el procedimiento para la estimación rápida de la incertidumbre, el estudiante determina la media aritmética de los datos, $\bar t = 0.485 \ 7 \ \text{s}$, y la incertidumbre, $\alpha_t = \frac{1}{\sqrt 7}\frac{2}{3}\frac{(0.53-0.44)}{2} = 0.011 \ 33 \ \text{s}$.

Usando lo aprendido en la {numref}`sec-reporteIncertidumbre`, el valor del tiempo obtenido fue:

$ t = 0.486 \pm 0.011 \ \text{s} $.



```{code-cell} ipython3
:tags: [remove-cell]

import numpy as np
g = 979.748
t = np.array([44,53,47,47,46,50,53])/100
t_mean = np.mean(t)
print('t_mean',t_mean)
t_diff = np.max(t)-np.min(t)
print('t_diff',t_diff)
t_e = 2*t_diff/(3*2)
print('t_e',t_e)
t_f = t_e/np.sqrt(len(t))
print('t_f',t_f)
error = np.std(t,ddof=1)/np.sqrt(len(t))
print('error',error)

print(0.5*g*t_mean**2)
print(0.5*g*(t_mean+t_f)**2)
print(0.5*g*(t_mean-t_f)**2)
```

+++

```{seealso}
Otra propuesta para estimar la incertidumbre se puede encontrar en la sección  2.3.1 de {cite}`Hughes2010`.
```