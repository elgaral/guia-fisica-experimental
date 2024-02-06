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

(sec-linearizacion)=
# Linearización de los datos experimentales
Para ver si los datos se ajustan a un determinado modelo matemático, siempre será más fácil concluir si el grupo de datos sigue una línea. Es por esto que en la medida de lo posible los datos se deben graficar de tal forma que la relación entre la variable dependiente y la independiente, sea lineal. Para lograrlo, se debe realizar el mismo tipo de operación matemática sobre cada conjunto de datos (dependientes e independientes) hasta que la relación sea lineal. Es de esperarse que la nueva variable dependiente no sea la variable dependiente original pero, en el caso de que la nueva relación siga un comportamiento lineal, se puede estar seguro de que los datos originales se ajustan al modelo matemático de interés. Hay que tener en cuenta que el proceso de linearización no se puede realizar siempre.

(subsec-ejemploBola3)=
## Ejemplo: bola rodando (parte 3)[^ejemplo]
Dado que a partir de la {numref}`fig-bola2` es difícil determinar que tipo de aceleración tiene la bola, el investigador decide linearizar la relación, es decir, la variable independiente $t$ debe de quedar a la derecha de la igualdad elevada a la primera potencia. Para esto se procede a multiplicar la expresión por el inverso de $t$, obteniendo

$$  \frac{x}{t} = v_0  - a t .$$

Esta nueva expresión tiene una relación lineal entre la variable dependiente $\frac{x}{t}$ y la variable independiente $t$. Si al graficar los datos se ajustan a una línea entonces se estará seguro que la bola se está desacelerando, y que el valor de la desaceleración coincide con la pendiente negativa de la curva, que en este caso es una línea recta, como puede verse en la {numref}`fig-bola3`.

[^ejemplo]: Las otras partes del problema están en la {numref}`subsec-ejemploBola1`, {numref}`subsec-ejemploBola2` y {numref}`subsec-ejemploBola4`.

```{code-cell} ipython3
:tags: [hide-cell]

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
# Linearización suponiendo que sigue la forma x -x0 = v0t -at^2

xnt = (x)/t
exnt = ex/t

plt.figure(figsize=(16,8))
plt.errorbar(t,xnt,yerr=exnt,fmt='.',ms=12,capsize=8,ecolor='r',color='k')
plt.ylabel('{x/t}$_{cm/s}$',fontsize=20)
plt.xlabel('Tiempo/s')
plt.show()
```

```{figure} imagenes/bola3.png
---
scale: 80%
name: fig-bola3
---
Razón entre la posición de la bola y el tiempo en función del tiempo.
```

De la {numref}`fig-bola3` se puede concluir que los datos se pueden ajustar a una curva lineal con pendiente negativa, que se ajusta a la idea de que la bola tiene una desaceleración constante. Cabe anotar que al operar entre variables con incertidumbre se debió realizar propagación del error para la nueva variable. No obstante, como el tiempo se está considerando exacto, la incertidumbre de $x/t$ sólo sufre un escalamiento con respecto a la incertidumbre de $x$, dado por el factor $1/t$. Como se puede apreciar en la figura, este escalamiento provocó una sobrestimación en los primeros valores de $x$, indicando que la precisión no es buena en estos primeros desplazamientos[^mincuad].

[^mincuad]: En la {numref}`sec-minimosCuad` se discutirá una forma de estimar que tanto se sobrestimó o subestimó, la incertidumbre.


```{note}
Más sobre graficación de datos experimentales en la sección 5.1 de {cite}`Hughes2010`, en la sección 2.2.3 de {cite}`Mahecha2009`, o en la sección 2.6 de {cite}`Taylor1996`.
```

