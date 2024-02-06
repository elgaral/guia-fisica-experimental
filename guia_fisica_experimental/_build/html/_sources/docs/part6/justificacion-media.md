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

(sec-demosMediadesvi)=
# Demostraciones del valor más probable y de la incertidumbre estándar

En la {numref}`sec-errorEstandar` se llegó a las ecuaciones {eq}`ec-errorEstandar`, {eq}`ec-errorEstandar-media` y {eq}`ec-errorEstandar-varianza`, que definen, una vez hechas las medidas experimentales de la cantidad física, la forma como se debe calcular el valor más problable y la incertidumbre. Lo que se hará ahora es demostrar por qué se pueden usar dichas ecuaciones.

(subsec-desv-mediaMuestral)=
## Desviación estándar de la media muestral
Hasta ahora se ha usado el teorema del límite central para justificar el valor de la incertidumbre estándar como la desviación estándar de la muestra $s$ multiplicada por el factor $1/\sqrt N$, donde $N$ es el tamaño de la muestra. Se usará ahora una aproximación alternativa. Supongamos que se tiene una variable aleatoria $x_i$ cuyo valor esperado es la media de la población:

$$ E\{x_i\} = \mu . $$ (ec-valorEsperado)

De la misma forma, el valor esperado del cuadrado de la diferencia de la variable, con respecto a la media de la población, es la varianza de la población:

$$ E\{(x_i-\mu)^2\} = \sigma^2 . $$ (ec-valorEsperadoVarianza)

Ahora se construye una nueva variable correspondiente a la media aritmética de $N$ variables aleatorias $x_i$: $\bar x = \frac{1}{N}\sum_i^N x_i$. El valor esperado de esta nueva variables es

$$ \mu_m = E\{ \bar x \} = E\Bigg\{ \frac{1}{N}\sum_i^N x_i \Bigg\} = \frac{1}{N}\sum_i^N E\{x_i\} = \frac{1}{N}\sum_i^N \mu = \mu $$

$$ \mu_m = \mu , $$

es decir, la media de la distribución muestral de las medias es igual a la media de la distribución original. Finalmente, el valor esperado del cuadrado de la diferencia de la nueva variable con respecto a la media de la población es

$$\begin{align}
\sigma_m^2 &= E\bigg\{ (\bar x - \mu)^2 \bigg\} = E\bigg\{ \bigg(\frac{1}{N}\sum_i^N x_i - \mu\bigg)^2 \bigg\} \\
&= E\bigg\{ \bigg(\frac{1}{N}\sum_i^N x_i - \frac{N\mu}{N}\bigg)^2 \bigg\} 
 = E\bigg\{ \bigg(\frac{1}{N}\sum_i^N x_i - \frac{1}{N}\sum_i^N \mu\bigg)^2 \bigg\} \\ &= E\bigg\{ \frac{1}{N^2} \bigg(\sum_i^N x_i - \sum_i^N \mu\bigg)^2 \bigg\} = \frac{1}{N^2} E\bigg\{ \bigg(\sum_i^N (x_i - \mu) \bigg)^2 \bigg\} \\
&= \frac{1}{N^2} E\bigg\{ \sum_i^N (x_i - \mu)^2 + \sum_{i\neq j}^N (x_i - \mu)(x_j - \mu)  \bigg\} \\
&= \frac{1}{N^2} E\bigg\{ \sum_i^N (x_i - \mu)^2 \bigg\} + \frac{1}{N^2}E\bigg\{ \sum_{i\neq j}^N (x_i - \mu)(x_j - \mu)  \bigg\} \\
&= \frac{1}{N^2}  \sum_i^N E\big\{(x_i - \mu)^2 \big\} + \frac{1}{N^2}\sum_{i\neq j}^N E\big\{(x_i - \mu)(x_j - \mu)  \big\} 
\end{align}$$

El valor esperado en la primera sumatoria es precisamente la varianza de la población $\sigma^2$, mientras que la segunda sumatoria es igual a cero. 

Esto es de esperarse en una población infinita: dado un valor esperado $E\big\{(x_i - \mu)(x_j - \mu)  \big\}$, se espera encontrar también  el valor $E\big\{(x_j - \mu)(x_i - \mu)  \big\} = -E\big\{(x_i - \mu)(x_j - \mu)  \big\}$. 

Entonces se tiene finalmente que

$$\sigma_m^2 = \frac{N\sigma^2}{N^2} = \frac{\sigma^2}{N} ,$$

y en términos de las desviaciones estándar, la desviación estándar de la nueva variable es 

$$\sigma_m = \frac{\sigma}{\sqrt N} .$$

+++

(subsec-formulaS)=
## Expresión para la desviación estándar de la muestra

Supongamos que se tiene una variable aleatoria $x_i$ cuyo valor esperado es la media de la población:

$$ E\{x_i\} = \mu . $$ (ec-valorEsperado2)

De la misma forma, el valor esperado del cuadrado de la diferencia de la variable, con respecto a la media de la población, es la varianza de la población:

$$ E\{(x_i-\mu)^2\} = \sigma^2 . $$ (ec-valorEsperadoVarianza2)

Ahora se toman $N$ variables de la distribución: $\{ x_1, x_2, ..., x_i, ..., x_N \}$. La media aritmética de esta muestra de la distribución es $ \bar x = \frac{1}{N} \sum_i^N x_i $. Determinando el valor esperado de esta media aritmética:

$$ E\bigg\{ \frac{1}{N} \sum_i^N x_i \bigg\} = \frac{1}{N} \sum_i^N E\{x_i\} = \mu . $$

Se puede concluir que el valor esperado de la media aritmética de la muestra, es la media de la población. Esto quiere decir que se puede esperar obtener la media de la población, o un valor muy aproximado, con una muestra de la población.

Recordando la definición de la varianza de una muestra de la población,

$$ s^2 = \frac{\sum_{i=1}^{N} (x_i - \bar x)^2}{N} ,$$ (ec-desviacionMuestraN)

determinemos el valor esperado:

$$\begin{align}
E\Bigg\{ \frac{\sum_{i=1}^{N} (x_i - \bar x)^2}{N}& \Bigg\} = \frac{1}{N}\sum_{i=1}^{N} E\big\{(x_i - \bar x)^2 \big\} = \frac{1}{N}\sum_{i=1}^{N} E\bigg\{\big((x_i-\mu) - (\bar x-\mu)\big)^2 \bigg\} \\
&= \frac{1}{N}\Bigg(\sum_{i=1}^{N} E\big\{(x_i-\mu)^2 \big\} + \sum_{i=1}^{N} E\big\{(\bar x-\mu)^2 \big\} - 2E\bigg\{\sum_{i=1}^{N} (x_i-\mu)(\bar x-\mu)\bigg\}\Bigg) \\
&= \frac{1}{N}\Bigg( N\sigma^2 + \frac{N\sigma^2}{N} - 2E\bigg\{(\bar x-\mu)\sum_{i=1}^{N} (x_i-\mu)\bigg\} \Bigg ) \\
&= \frac{1}{N}\Bigg( (N+1)\sigma^2 - 2E\bigg\{(\bar x-\mu)\bigg(\sum_{i=1}^{N} x_i-N\mu\bigg)\bigg\} \Bigg ) \\
&= \frac{1}{N}\Bigg( (N+1)\sigma^2 - 2E\bigg\{(\bar x-\mu)\bigg(N \bar x -N\mu\bigg)\bigg\} \Bigg ) \\
&= \frac{1}{N}\Bigg( (N+1)\sigma^2 - 2N E\bigg\{(\bar x-\mu)^2\bigg\} \Bigg ) \\
&= \frac{1}{N}\Bigg( (N+1)\sigma^2 - 2N \frac{\sigma^2}{N} \Bigg ) = \frac{(N-1)}{N}\sigma^2
\end{align}$$

Contrario a lo esperado, al usar la ecuación {eq}`ec-desviacionMuestraN`, se obtiene una varianza menor $(N-1)/N$ veces la de la población. Como realmente la varianza esperada de la muestra debe ser la de la población, en la ecuación {eq}`ec-desviacionMuestraN` se debe cambiar el factor $N$ del denominador por $N-1$. De esta forma, la varianza esperada de la muestra será la de la población, y la forma correcta de estimar la desviación estándar de la muestra es

$$ s = \sqrt{\frac{\sum_{i=1}^{N} (x_i - \bar x)^2}{N-1}} ,$$ (ec-desviacionMuestraNm1)

Una forma de explicar esto es recordando la condición inicial: que las variables sean aleatorias. Pero como se tuvo que determinar primero $\bar x$ de la muestra, usando las $N$ variables, ahora con $\bar x$ y con $N-1$ variables se puede determinar la variable restante, es decir, ahora solo tenemos $N-1$ variables aleatorias para determinar la desviación estándar de la muestra.

+++

(subsec-bestEstimadores)=
## Media y desviación estándar como mejores estimadores
Hasta ahora se ha aceptado, sin demostrarlo, a la ecuación {eq}`ec-errorEstandar-media` y la raiz cuadrada de la ecuación {eq}`ec-errorEstandar-varianza` como los mejores estimadores del valor más probable y de su incertidumbre, respectivamente. Aprovechando que el teorema del límite central demostró que las fluctuaciones del valor más probable de la cantidad física de interés siguen una distribución normal, se demostrará, usando el método de **máxima verosimilitud**[^verosimilitud], que las expresiones que se han venido usando son las correctas. 

[^verosimilitud]: En inglés se conoce como "principle of maximum likelihood".

Suponga que se tiene una variable aleatoria que sigue una distribución normal, tal que la probabilidad de que al medir la variable el valor esté entre $x_i$ y $x_i + dx_i$ está dada por la expresión

$$\large P(x_i) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x_i - \mu)^2}{2\sigma^2}}\,dx_i, $$ (ec-Gpdf)

donde $\mu$ y $\sigma$ son respectivamente la media y desviación estándar que definen la distribución. Ahora suponga que se mide las $N$ variables $\{ x_1, x_2, ..., x_i, ..., x_N \}$. La máxima probabilidad de obtener estos $N$ valores es

$$\large P_{\mu , \sigma}(x_1,x_2,...,x_N) = \Bigg(\frac{1}{\sigma \sqrt{2\pi}}\Bigg)^N e^{-\sum_{i=1}^N \frac{(x_i - \mu)^2}{2\sigma^2}}\, (dx)^N , $$ (ec-maximaProb)

donde se ha considerado a todos los infinitesimales $\text{d}x_i$ del mismo tamaño. En la práctica se desconocen los valores $\mu$ y $\sigma$. Para lograr la mejor estimación de $\mu$ y $\sigma$, se usa el método de máxima verosimilitud consistente en  maximizar la ecuación {eq}`ec-maximaProb` para los valores de media y desviación estándar, $\bar x$ y $s$ respectivamente. Entonces sea la probabilidad

$$\large P_{\bar x , s}(x_1,x_2,...,x_N) = \Bigg(\frac{1}{s \sqrt{2\pi}}\Bigg)^N e^{-\sum_{i=1}^N \frac{(x_i - \bar x)^2}{2s^2}}\,(dx)^N , $$ (ec-maximaProb2)

usando el método de mínimos y máximos de cálculo, para hallar la mejor estimación de la media, se deriva {eq}`ec-maximaProb2` con respecto a $\bar x$, se iguala a cero y se despeja $\bar x$:

$$\large \frac{\partial P_{\bar x , s}}{\partial \bar x} = \Bigg(\frac{1}{s \sqrt{2\pi}}\Bigg)^N e^{-\sum_{i=1}^N \frac{(x_i - \bar x)^2}{2s^2}} \sum_{i=1}^N \frac{-(x_i - \bar x)}{s^2}\,(dx)^N = 0 . $$ (ec-maximaProbDm)

Para garantizar que la ecuación {eq}`ec-maximaProbDm` sea igual a cero, basta con garantizar que

$$ -\sum_{i=1}^N \frac{(x_i - \bar x)}{s^2} = 0 .$$

Entonces se puede decir que la mejor estimacion de $\bar x$ es

$$ \bar x = \frac{\sum_{i=1}^N x_i}{N} . $$

Derivando ahora la ecuación {eq}`ec-maximaProb2` con respecto a $s$ e igualando a cero,

$$ \frac{\partial P_{\bar x , s}}{\partial s} = \Bigg( \frac{-N}{s^{N+1}}  + \frac{1}{s^N} \sum_{i=1}^N \frac{(x_i - \bar x)^2}{s^3} \Bigg) \bigg(\frac{1}{\sqrt{2\pi}}\bigg)^N e^{-\sum_{i=1}^N \frac{(x_i - \bar x)^2}{2s^2}}\,(dx)^N  = 0 . $$ (ec-maximaProbDs)

Luego se debe cumplir que

$$  \frac{1}{s^{N+3}} \sum_{i=1}^N (x_i - \bar x)^2  = \frac{N}{s^{N+1}} , $$ 

es decir, la mejor estimación de $s$ es

$$ s = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar x)^2}{N}} . $$ (ec-sSub)

Recordando el análisis hecho en la {numref}`subsec-formulaS`, la ecuación {eq}`ec-sSub` subestima el valor de la desviación estándar, y por lo tanto la mejor estimación será

$$ s = \sqrt{\frac{\sum_{i=1}^N (x_i - \bar x)^2}{N-1}} . $$ (ec-s)

+++

```{seealso}
Sobre la desviación estándar de la media muestral se puede consultar la sección 9.2 de {cite}`GorgasGarcia2011` y la página 24 de {cite}`LyonsL1991`. Otra demostración para la expresión de la desviación estándar de la muestra se encuentra en la sección 9.3 de {cite}`GorgasGarcia2011`. La justificación de la media y la desviación estándar como mejores estimadores se encuentra en la sección 5.5 de {cite}`Taylor1996`.
```