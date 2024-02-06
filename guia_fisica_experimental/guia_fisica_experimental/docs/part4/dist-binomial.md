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

(sec-distBinomial)=

# Distribución binomial
A continuación se presenta la primera distribución estadística de interés, precedida por unas definiciones necesarias para poder construir la distribución. El objetivo es sentar las bases para entender y poder aplicar la distribución binomial, por lo que un tratamiento riguroso de la misma se dejará para los cursos con enfoque a estadística y probabilidad. Aunque la distribución binomial no se encuentra generalmente en el estudio de las incertidumbres, tiene una gran relevancia en términos teóricos, y más importante aún, de ella se puede derivar la distribución normal o Gaussiana, que es de gran valor en el análisis de la incertidumbre.

(subsec-dado)=

## Lanzamiento de un dado

```{figure} ../part4/imagenes/dado.jpg
---
figclass: margin
scale: 7%
name: fig-dado
---
Dado de seis caras
```

Para comprender la información que da la distribución binomial es bueno comenzar con un ejemplo. Suponga que para un dado perfecto de seis caras ({numref}`fig-dado`) se desea conocer la probabilidad de obtener dos veces "cuatro", luego de lanzar el dado tres veces. Lo primero que hay que conocer es la probabilidad de obtener un cuatro luego de un lanzamiento. Como el dado tiene seis caras y solo en una de ellas está el número cuatro, se espera una probabilidad de $1/6$ de obtener un cuatro. De forma complementaria, la probabilidad de obtener un número diferente a cuatro será de $5/6$. Dicho en términos de porcentaje, se tiene una probabilidad de $16.67 \ \%$ de obtener un cuatro y $83.33 \ \%$ de no obtenerlo. 

Llamando al evento de obtener "cuatro" **Acierto** y a cualquier otro evento **Desacierto**, y denotando los eventos como $A$ y $D$ respectivamente, todos los posibles resultados al lanzar el dado tres veces o al lanzar tres dados diferentes[^ergodicidad] se presentan en la {numref}`fig-permutacion` y son en total ocho. Esto se conoce como número de **permutaciones** posibles. 

[^ergodicidad]: Esto se conoce como ergodicidad. Para el ejemplo ocurre cuando estadísticamente es lo mismo lanzar $n$ dados idénticos al mismo tiempo o lanzar un mismo dado $n$ veces en tiempos diferentes.

```{figure} ../part4/imagenes/permutacion.svg
---
figclass: margin-caption
name: fig-permutacion
---
Número de permutaciones posibles al lanzar un dado tres veces y considerar el resultado "cuatro" como acierto y el resto desacierto.
```

Ahora, de todas las permutaciones posibles se llamará **combinacion** a todos los casos en que luego de los tres lanzamientos se obtienen dos aciertos, sin importar el orden en que ocurren dichos aciertos. En la {numref}`fig-combinacion` se puede observar que para el ejemplo hay tres combinaciones posibles para obtener dos aciertos.

```{figure} ../part4/imagenes/combinacion.svg
---
figclass: margin-caption
name: fig-combinacion
---
Número de combinaciones posibles al lanzar un dado tres veces y obtener dos aciertos (casos resaltados).
```

Otra forma de verlo es escribiendo las combinaciones posibles: $(A,A,D)$, $(A,D,A)$ y $(D,A,A)$, es decir tres combinaciones posibles. La probabilidad de que ocurra el primer caso sería $\Big(\frac{1}{6}\Big)\times\Big(\frac{1}{6}\Big)\times\Big(\frac{5}{6}\Big)$, la probabilidad de que ocurra el segundo caso es $\Big(\frac{1}{6}\Big)\times\Big(\frac{5}{6}\Big)\times\Big(\frac{1}{6}\Big)$, y la probabilidad de que ocurra el tercer caso es $\Big(\frac{5}{6}\Big)\times\Big(\frac{1}{6}\Big)\times\Big(\frac{1}{6}\Big)$. Por lo tanto, la probabilidad de obtener dos "cuatro" luego de tres lanzamientos es

$$ 3\times\Big(\frac{1}{6}\Big)^2\times\Big(\frac{5}{6}\Big) \approx 0.0694 , $$ (ec-bino-ejemp)

o $6.94 \, \%$ si se escribe como porcentaje. Este tipo de información es la que provee la distribución binomial. 

```{note}
En la ecuación {eq}`ec-bino-ejemp` se utilizó el símbolo de aproximado en vez del símbolo de igualdad. Esto es porque el resultado exacto tiene infinitos decimales, pero aquí se reporta solo hasta el cuarto decimal, redondeando. No obstante, como la cantidad tiene infinitos decimales exactos se pueden tomar tantos decimales como se desee. Otro asunto importante con este tipo de cantidades es que al multiplicarlo o sumarlo con una cantidad que tiene un número finito de cifras significativas, siempre se toma una cifra significativa extra para poderla considerar como una cantidad exacta. Por ejemplo, la cantidad de arriba con cinco cifras significativas sería $0.069444$. Si se multiplica por $1.2$ entonces el valor $0.0694$, que tiene tres cifras significativas, se puede considerar una cantidad exacta porque el resultado de la multiplicación solo tendrá dos cifras significativas: $0.083$. Por otro lado, si se multiplica por $1.23$ se tomaría el valor $0.06944$ y el resultado sería $0.0854$. Agregar más cifras significativas no altera el resultado. Otro ejemplo es si se suma, aquí el resultado debe tener el mismo número de decimales del valor con menor número de decimales: $1.2 + 0.07 = 1.3$ y $1.23 + 0.069 = 1.30$.
```

+++

(subsec-defBinomial)=

## Definición de la distribución de probabilidad binomial

La distribución de probabilidad binomial o función de probabilidad de masa (fpm) es la probabilidad de obtener $k$ aciertos, o éxitos, luego de $n$ eventos siempre que la probabilidad de obtener un acierto sea $p$. Dicha probabilidad se escribe como

$$ b(k;n,p) = \frac{n!}{k!(n-k)!}\times p^k \times q^{n-k}, $$ (ec-dist-prob-binomial)

donde $q=1-p$. En esta ecuación, {eq}`ec-dist-prob-binomial`, el primer término indica el número de combinaciones posibles, el segundo término indica la probabilidad de obtener $k$ aciertos, y el último término indica la probabilidad de no obtener un acierto en los $n-k$ eventos restantes.

Una vez conocida la probabilidad de un acierto se puede conocer la probabilidad de obtener $k$ aciertos para un número $n$ de eventos. Por ejemplo, la probabilidad de obtener tres "cuatro" luego de lanzar el dado nueve veces es:

$$ b(3;9,1/6) = \frac{9!}{3!(9-3!)}\times (1/6)^3 \times (5/6)^{9-3} = 0.1302 $$ 

Entonces se puede decir que la probabilidad de obtener tres "cuatro" luego de lanzar un dado nueve veces es de $13.02 \ \%$.

Usando la ecuación {eq}`ec-dist-prob-binomial` es posible graficar la fpm de la distribución binomial como se muestra en la {numref}`fig-binom-fpm` para los casos con $n=3$ y $n=9$; ambos casos con una probabilidad de acierto de $p=1/6$. De las figuras queda claro que la función es discreta y que para un valor específico de aciertos la probabilidad es máxima. Note también que la distribución no es simetrica con respecto al valor de mayor probabilidad.

```{figure} ../part4/imagenes/binom-fpm.svg
---
figclass: margin-caption
name: fig-binom-fpm
---
Funciones de probabilidad de masa de la distribución binomial. La fpm de la izquierda es para el caso de tres eventos, $n=3$, mientras que la figura de la derecha es para una fpm con $n=9$. Para ambos casos la probabilidad de acierto fue $p=1/6$.
```

```{code-cell} ipython3
:tags: ["hide-cell"]

# Con este código se generaron las figuras de las funciones de probabilidad de masa de la distribución binomial

from scipy.stats import binom
import pylab as plt
import matplotlib
import numpy as np
matplotlib.rcParams.update({'font.size': 16})
fig, (ax1,ax2) = plt.subplots(1, 2,figsize=(16,6))

####
n , p = 3 , 1/6
####

x = np.arange(0,5)
ax1.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label=r'n = {}'.format(n))
ax1.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
ax1.legend()
ax1.set_xlabel('x')
ax1.set_ylabel('fpm')

####
n , p = 9 , 1/6
####

x = np.arange(binom.ppf(0.01, n, p),
              binom.ppf(0.999, n, p))
ax2.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label=r'n = {}'.format(n))
ax2.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)
ax2.legend()
ax2.set_xlabel('x')
ax2.set_ylabel('fpm')
plt.show()

```

+++

(subsec-binom-parametros)=

## Media y desviación estándar de la distribución binomial

Usando las ecuaciones de la {numref}`subsec-media` y la {numref}`subsec-desvi`, y la ecuación {eq}`ec-dist-prob-binomial`, es posible determinar la media y la desviación estándar de la distribución binomial. La media o promedio es

$$ \mu = np, $$ (ec-binom-media)

y la desviación estándar es

$$ \sigma = \sqrt{npq}. $$ (ec-binom-desvi)

```{warning}
Note que se han usado los símbolos $\mu$ y $\sigma$ para la media y la desviación estándar de la distribución binomial. En cambio en la {numref}`subsec-media` y {numref}`subsec-desvi` se usaron los símbolos $\bar x$ y $s$, respectivamente. Se usarán los símbolos $\mu$ y $\sigma$ cuando el número de datos con el que se construyó la distribución es infinito. Para los casos en que el número de datos sea finito, y sean discretos, por lo general se usarán los símbolos $\bar k$ y $s$.
```

Para el ejemplo, en promedio se espera obtener $\mu = 0.5$ aciertos del número "cuatro" en tres lanzamientos del dado. Note que el promedio no tiene que ser un valor entero, y en este caso significa que lo más probable es no obtener ningún acierto lanzando solo tres veces el dado. Por otro lado, la desviación estándar es $\sigma = 0.6$, por lo que aún cuando lo más probable es no obtener ningún acierto es de esperarse que en ocaciones se obtenga un "cuatro" luego de tres lanzamientos ($k = 0.5 + 0.6 > 1$).

```{seealso}
Más sobre distribución binomial en el capítulo 10 de {cite}`Taylor1996`, la sección 2.1 de {cite}`Bevington` y la sección 7.2 de {cite}`GorgasGarcia2011`.

```