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


(sec-densidadProb)=

# Función densidad de probabilidad

Recordando de la {numref}`sec-EstadisticaBasico` las ecuaciones {eq}`dist-condicion-normalizacion` y {eq}`fraccion-bin`, definidas para un conjunto de $N$ variables aleatorias $x_i$, la probabilidad de encontrar una variable dentro del intervalo $\Delta_i = x_{i+1} - x_i$ era $f_i \Delta_i$, donde $f_i$ correspondía a la altura del intervalo. Así mismo, la suma total de las probabilidades era igual a la unidad

$$ \sum_{i = 0}^M f_i\Delta_i = 1. $$ (ec-sumaProbabilidad)

En esta ecuación, $M$ corresponde al número de intervalos, y por lo tanto el tamaño de los intervalos $\Delta_i$ dependerá del valor de $M$. Entonces, es de esperarse que si el número de intervalos aumenta, el tamaño de los intervalos disminuya, tal que en el límite en que $N \to \infty$ y $M \to \infty$ el intervalo tiende a un infinitesimal $dx$, y la ecuación {eq}`ec-sumaProbabilidad` se convierte en la integral

$$ \int_{-\infty}^{\infty} f(x)\,dx = 1 .$$ (ec-probaTotal)

La altura del intervalo $f_i$ en la ecuación {eq}`ec-sumaProbabilidad` se convierte ahora en $f(x)$, una función continua de la variable aleatoria continua $x$, que se denomina *función densidad de probabilidad* o *función de la distribución de probabilidad*.

En la {numref}`fig-normal-parametros` se puede ver esta transformación a medida que cambian los valores de $N$ y $M$.

```{figure} imagenes/normal.gif
:name: fig-normal-parametros

Dependencia de la distribución al tamaño $N$ de la muestra y al número $M$ de intervalos del histograma.
```

```{Admonition} ¡Hazlo tu mismo!

Si quieres cambiar tú mismo los parámetros puedes desplegar la siguiente ventana. Allí encontrarás el programa que genera la gráfica.
```

```{code-cell} ipython3
:tags: ["hide-cell"]

#### Valores a cambiar ###
##########################
N = 100    # Tamaño muestra. Cambiar por ejemplo hasta 1000 
M = 10      # Número de intervalos. Cambiar por ejemplo hasta 100
##########################

import numpy as np
import pylab as plt
plt.rcParams.update({'font.size': 16})

def normal(x,loc=0,scale=1):
    return (1/np.sqrt(2*np.pi))*np.exp(-x**2/2)

np.random.seed(0)
conjunto = np.random.normal(loc=0,scale=1,size=N)
infoHist = plt.hist(conjunto,bins=M,density=True,align='left',
                   color='silver')
x = np.linspace(-5,5,100)
plt.plot(x,normal(x,loc=0,scale=1),color='r',label=r'$f(x)$')
plt.title(r'N = {}, M = {}'.format(N,M))
plt.xlabel(r'$x_i$')
plt.ylabel(r'$f_i$')
plt.legend()
plt.show()
```

A partir de la definición {eq}`ec-probaTotal` se puede determinar la probabilidad de obtener un resultado $x$ para un rango definido,

$$ P(x_1 \leq x \leq x_2) = \int_{x_1}^{x_2} f(x)\,dx .$$ (ec-probRango)

También se puede determinar la media o *valor esperado* de la variable $x$,

$$ \bar x = \int_{-\infty}^{\infty} x f(x)\,dx, $$ (ec-media)

o incluso, se puede determinar el valor esperado de la potencia $n$ de la variable $x$[^npotencia]:

$$ \langle x^n \rangle = \int_{-\infty}^{\infty} x^n f(x)\,dx, $$ (ec-npotencia)

[^npotencia]: El valor esperado de la potencia uno de la variable $x$ es precisamente la media $\bar x$, que también se denota como $\langle x \rangle$.

Finalmente, recordando la ecuación {eq}`ec-relacion-dev-media`, ahora se puede definir el cuadrado de la desviación estándar, varianza, como

$$ \sigma^2 = \int_{-\infty}^{\infty} (x-\bar x)^2 f(x)\,dx .$$ (ec-desviacionEst)

```{seealso}
Más sobre la función densidad de probabilidad se puede encontrar en la sección 3.1 de {cite}`Hughes2010`, secciones 4.2, 5.1 y 5.2 de {cite}`Taylor1996`, sección 1.3 de {cite}`Bevington` y sección 1.4.2 de {cite}`Mahecha2009`.
```
