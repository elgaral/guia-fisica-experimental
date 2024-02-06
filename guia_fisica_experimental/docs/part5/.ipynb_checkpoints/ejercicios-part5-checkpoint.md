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

(sec-ejerciciosV2P5)=
# Ejercicios

**Distribución normal**

**1**. (a) Con base en las definición de función de densidad de probabilidad normal, escriba la expresión para la probabilidad entre los valores $-k\sigma$ y $k\sigma$, donde $k$ es un número real. (b) Escriba la expresión de la parte (a) en términos de la función integral, usando la transformación $z = (x-\mu)/\sigma$. (c) Aunque ya no es común, anteriormente se reportaba la incertidumbre con una confiabilidad del $50\,\%$, y se le conocía como *error probable*. Determine numéricamente el valor de $k$ para una probabilidad del $50\,\%$ (utilice la regla compuesta del trapezoide para calcular numéricamente la integral). (d) Grafique la función integral para el rango de $k$ igual a $[0,5]$. (e) Determine aproximadamente el número de intervalos necesarios, en la regla compuesta del trapezoide, para que con $k=3$, la probabilidad sea $99.7\,\%$ (con tres cifras significativas).

**Distribución Poisson**

**2**. A un estudiante se le pide que mida el promedio de partículas que emite una muestra de cobalto-56 en un tiempo de $10\,\text{s}$. El estudiante ubica un detector Geiger-Muller a una distancia de $2\,\text{cm}$ de la muestra y realiza las mediciones (Los datos se entregan como un arreglo de `Python` en la parte de abajo, cada posición corresponde al número de partículas detectadas en el intervalo, y el valor en la posición corresponde al número de veces que se repitió dicho número de partículas detectadas). El estudiante debe hacer lo siguiente: (a) Realizar un histograma de los datos graficando el número de repeticiones. (b) Suponiendo que los datos siguen una distribución de Poisson, calcular la media, desviación estándar y el número total de medidas hechas. (c) Reportar correctamente el promedio de partículas en el intervalo definido, y la razón promedio de partículas en un segundo. (d) Realizar el histrograma de fracciones, y superponer una función densidad de probabilidad de Poisson que tenga los mismos parámetros, ¿visualmente coinciden?. (e) La probabilidad de detectar al menos 5 partículas, y la probabilidad de que al menos en una ocasión, de todas las mediciones, no se detecte ninguna partícula. (f) Repetir el numeral (d) pero superponiendo una función densidad de probabilidad normal.

```{code-cell} ipython3
:tags: ['hide-cell']

import numpy as np
datosS = np.array([   0,    0,    3,   11,   50,   99,  226,  355,  600,  772,  939,
       1012, 1038,  910,  870,  717,  492,  337,  225,  153,   89,   60,
         18,   16,    4,    3,    0,    0,    1,    0,    0,    0,    0,
          0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
          0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
          0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
          0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
          0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
          0,    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
          0])
```
