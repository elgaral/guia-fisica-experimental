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


(sec-graficas)=
# Graficación de datos experimentales
Los humanos tenemos facilidad para interpretar imágenes por lo que la presentación de datos experimentales utilizando una gráfica siempre será la mejor opción. Por lo tanto, siempre se debe dedicar un buen tiempo, y espacio, a generar las mejores gráficas posibles, que permitan analizar de forma rápida, fácil y acertada, los resultados experimentales. Para lograrlo hay una serie de pasos que se recomienda seguir y que se presentan a continuación con base en la guía propuesta por Hughes et al. {cite}`Hughes2010`.

1. La variable independiente se grafica en el eje horizontal o eje de las abscisas, y la variable dependiente en el eje vertical o eje de las ordenadas. La variable independiente debe ser también la variable que se conoce con mayor precisión: en la mayoría de los casos considerándose como exacta.

2. Use las escalas correctas en cada eje, de forma tal que se aproveche al máximo todo el espacio de la gráfica.

3. Darle un nombre a cada eje incluyendo las unidades, según la cantidad física que se está presentando. Usar prefijos para las unidades que faciliten su lectura.

4. Graficar los puntos de las parejas ordenadas con sus respectivas barras de incertidumbre de forma tal que su lectura sea clara. No utilice una línea para conectar los diferentes puntos, excepto si esto facilita la interpretación de los datos. 

5. Si la densidad de puntos es muy grande, se pueden reemplazar por una línea, graficar las barras de error sólo en algunos valores o reemplazarlas por una zona sombreada, aclarando esto en la leyenda de la figura.

6. De ser posible acompañar los puntos con una línea de tendencia derivada de un modelo matemático. Si la línea no se deriva de ningún modelo matemático deje claro en la leyenda que está allí sólo para servir de guía.

7. Acompañar la gráfica con una leyenda que contenga toda la información relevante de la misma. En algunas revistas es permitido presentar los detalles en el texto del artículo y dejar la leyenda con solo un título que sirva para referenciar la figura.

8. El tamaño de la fuente tipográfica usada en la gráfica debe de ser, como mínimo, igual al tamaño de la fuente de la leyenda.

9. Si es posible, linearice los datos y grafíquelos. Siempre será más fácil interpretar y extraer información de una línea.

+++

(subsec-ejemploBola2)=
## Ejemplo: bola rodando (parte 2)[^ejemplo]
Luego de tabulados los datos ({numref}`tabla-bola`) el investigador decide graficarlos para poder visualizarlos en conjunto. Cómo el interés real es el desplazamiento ocurrido para un intervalo de tiempo, decide restarle a todos los valores el primer valor medido. Dado que la posición tiene una incertidumbre, se debe determinar la incertidumbre del desplazamineto usando la técnica de la {numref}`subsec-errorIndirecta`. Por lo tanto, los desplazamientos hasta el intervalo de tiempo correspondiente a $0.36 \ \text{s}$ tienen una incertidumbre de $2 \ \text{cm}$. Para intervalos de tiempo superiores, la incertidumbre en el desplazamiento es de $4 \ \text{cm}$.
La expresión que él piensa que puede modelar el problema, expresando la posición de la bola $x$ en función de la velocidad inicial $v_0$, el intervalo de tiempo transcurrido $t$ y una desaceleración $a$, es

$$ x = v_0 t - a t^2 $$

El problema es que aquí la desaceleración corresponde matemáticamente a la inflexión de la curva experimental, por lo que concluir algo sobre la aceleración a partir de solo mirar la gráfica de la posición en función del intervalo de tiempo no es posible, o por lo menos muy difícil ({numref}`fig-bola2`).

[^ejemplo]: Las otras partes del problema están en la {numref}`subsec-ejemploBola1`, {numref}`subsec-ejemploBola3` y {numref}`subsec-ejemploBola4`.

```{code-cell} ipython3
:tags: [hide-cell]

### CÓDIGO PARA REALIZAR LA GRÁFICA

import numpy as np
import pylab as plt
import matplotlib
matplotlib.rcParams.update({'font.size': 18})
# Datos tiempo y posición


t = np.array([2.48,2.58,2.68,2.79,2.88,3.02,3.29,3.43,3.58,3.77]) - 2.32 # tiempo en segundos
x = np.array([21,27,34,40,47,55,69,78,85,93]) - 10 # posición en centímetros
e = np.array([1,1,1,2,2,2,2,2,2,2]) # Error estimado en la posición

## Determinación del error del desplazamiento
despM = x + 2*e
despm = x - 2*e
ex = abs(despM - despm)/2
print('ex = {}'.format(ex))

plt.figure(figsize=(16,8))
plt.errorbar(t,x,yerr=ex,fmt='.',ms=10,capsize=7,ecolor='r',color='k')
plt.ylabel('Posición/cm')
plt.xlabel('Tiempo/s')
plt.show()

```

```{figure} imagenes/bola2.png
---
scale: 80%
name: fig-bola2
---
Posición de la bola en función del tiempo. La resolución del tiempo es de una centésima de segundo por lo que se considera exacto.
```

```{note}
Más sobre graficación de datos experimentales en la sección 5.1 de {cite}`Hughes2010`, en la sección 2.2.1 de {cite}`Mahecha2009`, o en la sección 2.6 de {cite}`Taylor1996`.
```