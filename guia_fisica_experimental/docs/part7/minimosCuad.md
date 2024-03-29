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

(sec-minimosCuad)=
# Método de mínimos cuadrados
En la sección {numref}`sec-ajusteLineal` se hizo uso de las ecuaciones {eq}`ec-intercepto` a {eq}`ec-incertidumbreComun`, derivadas del método de mínimos cuadrados, con el fin de ajustar unos datos experimentales a una línea con intercepto $c$ y pendiente $m$. En esta sección se obtendrán dichas ecuaciones a partir de los fundamentos matemáticos y estadísticos que se han aprendido.

Se tienen $N$ datos experimentales correspondientes a unas variables independientes $x_i$, que se consideran tienen una incertidumbre despreciable, y unas variables dependientes $y_i$, que se sabe tienen una incertidumbre $\alpha$ definida por una distribución normal, es decir, la probabilidad de obtener el valor $y_i$ se puede estimar con una distribución normal, de media $\mu_i$ y desviación estándar $\alpha$[^alpha].

[^alpha]: Para este caso se supone que todas las variables $y_i$ tienen la misma incertidumbre $\alpha$, y que la distribución es normal, por lo que en un experimento hay que asegurar que esto se cumpla al menos de forma aproximada. No obstante, gracias al teorema del límite central, siempre se puede lograr que la distribución de los $y_i$ sea una distribución normal.

También se sabe que los datos experimentales se ajustan a la función $y_i = mx_i +c$. La pregunta que se tiene es ¿para qué valores de $m$ y $c$ los datos y la función se ajustan mejor?[^ajustan]

[^ajustan]: La pregunta pudo ser también: ¿los datos se ajustan correctamente a una línea?

Como la probabilidad de obtener en una medida el valor $y_i$, para los parámetros $x_i$, $m$, y $c$, es igual a 

$$ G(y_i;x_i,m,c) \propto \Large\text{e}^{-\frac{(y_i - \mu_i)^2}{2\alpha^2}} ,$$ (ec-probY1)

donde $\mu_i = mx_i + c$, la probabilidad total $G_T$ de obtener los $N$ valores $y_i$ será

$$ G_T \propto \Large\text{e}^{-\frac{(y_1 - \mu_1)^2}{2\alpha^2}}\normalsize\times\Large\text{e}^{-\frac{(y_2 - \mu_2)^2}{2\alpha^2}}\normalsize\times\, ...\,\times\, \Large\text{e}^{-\frac{(y_N - \mu_N)^2}{2\alpha^2}} ,$$

es decir,

$$ G_T \propto \Large\text{e}^{-\sum_{i=1}^N \frac{(y_i - \mu_i)^2}{2\alpha^2}} .$$ (ec-probY2)

Usando el método de máxima verosimilitud ({numref}`subsec-bestEstimadores`) para encontrar los valores de $m$ y $c$, con los que se obtiene el mejor ajuste, se debe maximizar la probabilidad total $G_T$. Maximizar la probabilidad total es equivalente a minimizar la expresión del argumento de la exponencial:[^chi2]

$$ \tilde\chi^2 = -\sum_{i=1}^N \frac{(y_i - \mu_i)^2}{2\alpha^2} .$$ (ec-probY3)

[^chi2]: La variable estadística $\chi^2 = -2\tilde\chi^2$, conocida en el habla hispana como "chi-cuadrado", pero que se debe pronunciar como *qui-cuadrado*, será de gran importancia en futuras secciones ({numref}`sec-chiCuadrado`) para la cuantificación de la calidad de los ajustes, o la verificación de hipótesis.

Usando el método de *máximos y mínimos* de cálculo, se procede con la determinación del mejor valor de $m$ y $c$:

$$ \frac{\partial \tilde\chi^2}{\partial m} = -\sum_{i=1}^N \frac{(y_i - m x_i - c)(-x_i)}{\alpha^2} = 0 $$

$$ \sum_{i=1}^N (y_i - m x_i - c)x_i = 0 $$

$$ \sum_{i=1}^N x_i y_i - m \sum_{i=1}^N x_i^2 - c \sum_{i=1}^Nx_i = 0 $$

$$ m = \frac{\sum_{i=1}^N x_i y_i - c\sum_{i=1}^N x_i}{\sum_{i=1}^N x_i^2} .$$ (ec-probY4)

Derivando ahora con respecto a $c$:

$$ \frac{\partial \tilde\chi^2}{\partial c} = -\sum_{i=1}^N \frac{(y_i - m x_i - c)(-1)}{\alpha^2} = 0 $$

$$ \sum_{i=1}^N (y_i - m x_i - c) = 0 $$

$$ \sum_{i=1}^N y_i - m \sum_{i=1}^N x_i - c N = 0 $$

$$ c = \frac{-m\sum_{i=1}^N x_i + \sum_{i=1}^N y_i}{N} .$$ (ec-probY5)

Reemplazando {eq}`ec-probY5` en {eq}`ec-probY4`,

$$ m = \frac{N\sum_{i=1}^N x_i y_i + m \big(\sum_{i=1}^N x_i\big)^2 - \sum_{i=1}^N x_i\sum_{i=1}^N y_i}{N \sum_{i=1}^N x_i^2} $$

$$ m\Bigg( N\sum_{i=1}^N x_i^2 - \bigg( \sum_{i=1}^N x_i \bigg)^2 \Bigg) = N\sum_{i=1}^N x_i y_i - \sum_{i=1}^N x_i \sum_{i=1}^N y_i $$


$$\large m = \frac{N\sum_{i=1}^N x_i y_i - \sum_{i=1}^N x_i \sum_{i=1}^N y_i}{\Delta} ,$$ (ec-probY6)


donde 

$$\Delta = N\sum_{i=1}^N x_i^2 - \bigg( \sum_{i=1}^N x_i \bigg)^2 .$$ (ec-probY7)

Reemplazando {eq}`ec-probY6` en {eq}`ec-probY5`, y reorganizando términos, se obtiene

$$\large c = \frac{\sum_{i=1}^N x_i^2 \sum_{i=1}^N y_i - \sum_{i=1}^N x_i y_i \sum_{i=1}^N x_i}{\Delta} .$$ (ec-probY8)

Las ecuaciones {eq}`ec-probY6`, {eq}`ec-probY7` y {eq}`ec-probY8`, permiten determinar el intercepto $c$ y la pendiente $m$ de la línea que mejor se ajusta a los datos experimentales. No obstante, como la variable experimental $y_i$ tiene una incertidumbre $\alpha$, es de esperarse que tanto la pendiente, como el intercepto, tengan también una incertidumbre. Para estimar dicha incertidumbre se usa el método de propagación de la incertidumbre de la {numref}`subsec-errorPequeno`.

La derivada parcial de la ecuación {eq}`ec-probY6` con respecto a $y_i$ es

$$ \frac{\partial m}{\partial y_i} = \frac{N x_i - \sum_{j=1}^N x_j}{\Delta} ,$$

y por lo tanto, la incertidumbre en la pendiente $m$ es

$$ \alpha_m^2 = \sum_{i=1}^N \Bigg( \frac{N x_i - \sum_{j=1}^N x_j}{\Delta} \Bigg)^2 \alpha^2 $$

$$ \alpha_m^2 = \sum_{i=1}^N \Bigg( \frac{N^2 x_i^2 - 2N x_i \sum_{j=1}^N x_j + \big(\sum_{j=1}^N x_j\big)^2}{\Delta^2} \Bigg) \alpha^2 $$

$$ \alpha_m^2 = \frac{N^2 \sum_{i=1}^N x_i^2 - 2N \big(\sum_{i=1}^N x_i\big)^2 + N\big(\sum_{j=1}^N x_j\big)^2}{\Delta^2} \alpha^2 $$

$$ \alpha_m^2 = \frac{N\Delta}{\Delta^2}\alpha^2 ,$$

es decir,

$$\large \alpha_m = \sqrt{\frac{N}{\Delta}}\alpha $$ (ec-probY9)


La derivada parcial de la ecaución {eq}`ec-probY8` con respecto a $y_i$ es

$$ \frac{\partial c}{\partial y_i} = \frac{\sum_{j=1}^N x_j^2 - x_i \sum_{j=1}^N x_j}{\Delta} ,$$

y por lo tanto, la incertidumbre en el intercepto $c$ es

$$ \alpha_c^2 = \sum_{i=1}^N \Bigg( \frac{\sum_{j=1}^N x_j^2 - x_i \sum_{j=1}^N x_j}{\Delta} \Bigg)^2 \alpha^2 .$$

Con un procedimiento similar al utilizado para la pendiente, encontramos que la incertidumbre es

$$\large \alpha_c = \sqrt{\frac{\sum_{i=1}^N x_i^2}{\Delta}}\alpha .$$ (ec-probY10)

+++

(subsec-IncertidumbreComun)=
## Incertidumbre común

Las ecuaciones {eq}`ec-probY9` y {eq}`ec-probY10` indican que la incertidumbre de $m$ y $c$ son proporcionales a la incertidumbre de los datos experimentales: hasta ahora considerando que todos los valores $y_i$ tienen la misma incertidumbre $\alpha$. Pero, en algunas ocasiones puede que no se determine la incertidumbre de las cantidades $y_i$. No obstante, como es de esperarse que los valores $y_i$ se distribuyan de forma aleatoria (distribución normal) alrededor de los respectivos valores $\mu_i$, se puede estimar la incertidumbre de la siguiente forma[^otros]:

$$ \alpha_{ic} = \sqrt{\frac{1}{N-2}\sum_i (y_i - mx_i - c)^2}. $$ (ec-incertidumbreComun2)

[^otros]: La incertidumbre común se puede usar en modelos nolineales. Simplemente se reemplaza $\mu_i$ por la función correspondiente al modelo.

$\alpha_{ic}$ se denomina la incertidumbre común, que se espera tengan todos los valores $y_i$, si estos realmente se ajustan a la curva líneal de pendiente $m$ e intercepto $c$. Note que en este caso se divide por el factor $N-2$, porque se tienen dos parámetros, $m$ y $c$, que deben ser determinados con los mismos valores experimentales. En contraste, para el caso de la determinación de la incertidumbre estándar, sólo se necesitaba un parámetro, el valor más probable $\bar x$ (ver ecuación {eq}`ec-errorEstandar-varianza`). Ciertamente, por la forma en que se determinó la incertidumbre común, esta es la mejor estimación de las incertidumbres de los datos experimentales, si el modelo realmente se ajusta a los datos. Entonces, en general, para determinar las incertidumbres de $m$ y $c$ se utilizará la incertidumbre común:

$$\large \alpha_m = \sqrt{\frac{N}{\Delta}}\alpha_{ic} ,$$ (ec-probY9b)

y 

$$\large \alpha_c = \sqrt{\frac{\sum_{i=1}^N x_i^2}{\Delta}}\alpha_{ic} .$$ (ec-probY10b)

En el caso en que exista total seguridad de la veracidad del modelo, la incertidumbre común también servirá para verificar si la incertidumbre $\alpha$, que se estimó para los valores $y_i$, es la correcta. Si $\alpha$ es mucho menor que $\alpha_{ic}$ (menos de la mitad), es muy probable se haya subestimado la incertidumbre de $y_i$, y por lo tanto no se esté considerando alguna incertidumbre experimental. Por el contrario, si $\alpha$ es mucho mayor que $\alpha_{ic}$ (más del doble), se está siendo muy conservador, sobrestimando la incertidumbre.

+++

(subsec-minCuadNU)=
## Mínimos cuadrados con incetidumbres no uniformes

Hasta ahora, se ha supuesto que la incertidumbre de los valores experimentales $y_i$ era la misma para todos los valores. No obstante, es común determinar los valores experimentales con diferentes incertidumbres, debido a los diferentes rangos de la cantidad física, que pueden obligar a usar diferentes técnicas, con diferentes precisiones. Esta situación modifica las expresiones encontradas por mínimos cuadrados, de forma tal que incluyan el efecto de las diferentes precisiones. Es de esperarse, que un valor con una mínima incertidumbre, tenga mayor peso en el ajuste que un valor con una gran incertidumbre. A continuación presentamos las expresiones para la pendiente $m$, el intercepto $c$, y sus incertidumbres, que toman encuenta la incertidumbre $\alpha_i$ de cada variable dependiente $y_i$ ({cite}`Hughes2010`, sección 6.3).

$$\large m = \frac{\sum_{i=1}^N w_i \sum_{i=1}^N w_i x_i y_i - \sum_{i=1}^N w_i x_i \sum_{i=1}^N w_i y_i}{\Delta'} ,$$ (ec-mc1)

$$\large c = \frac{\sum_{i=1}^N w_i x_i^2 \sum_{i=1}^N w_i y_i - \sum_{i=1}^N w_i x_i y_i \sum_{i=1}^N w_i x_i}{\Delta'} ,$$ (ec-mc2)

$$\large \alpha_m = \sqrt{\frac{\sum_{i=1}^N w_i}{\Delta'}} ,$$ (ec-mc3)

$$\large \alpha_c = \sqrt{\frac{\sum_{i=1}^N w_i x_i^2}{\Delta'}} ,$$ (ec-mc4)

$$\Delta' = \sum_{i=1}^N w_i \sum_{i=1}^N w_i x_i^2 - \bigg( \sum_{i=1}^N w_i x_i \bigg)^2 .$$ (ec-mc5)


El factor de peso es el inverso del cuadrado de las incertidumbres de los datos, $w_i = 1/\alpha_i^2$.

+++

(subsec-ejemplobola5)=
## Ejemplo: bola rodando (parte 4)[^ejemplo]
En el ejemplo de la bola rodando, cuando se linearizó la función al dividir la incertidumbre por $t$, la nueva incertidumbre de la nueva variable $x/t$ es diferente para cada valor de la nueva variable. Para hallar la pendiente, el intercepto, y las incertidumbres de la línea que se ajusta a los valores experimentales, se deben usar las expresiones de la anterior sección. En la {numref}`tabla-bola5` y la {numref}`fig-bola5` se comparan los resultados para el caso en que no se incluyen las incetidumbres de la posición $x$ (con $\alpha_{ic}$), con respecto al caso en que se tienen en cuenta las incertidumbres de la posición $x$ (con $w_i$).


[^ejemplo]: Las otras partes del problema están en la {numref}`subsec-ejemploBola1`, {numref}`subsec-ejemploBola2`, {numref}`subsec-ejemploBola4`, y en la {numref}`subsec-ejemploBola3`.

```{list-table} Resultados del ajuste lineal usando la incertidumbre común y los pesos $w_i$.
:header-rows: 1
:name: tabla-bola5

* - Parámetro
  - Con $\alpha_{ic}$
  - Usando $w_i$
* - $m$/(cm/s$^2$)
  - $-8.8 \pm 0.9$
  - $-9 \pm 4$
* - $c$/(cm/s)
  - $70.7 \pm 0.7$
  - $71 \pm 4$

```

En la tabla se puede observar que cuando no se tuvo en cuenta la incertidumbre del desplazamiento, por lo que se usó la incertidumbre común, las incertidumbres obtenidas de la pendiente y el intercepto fueron menores que para el caso en que se tienen en cuenta las incertidumbres del desplazamiento, puesto que, como se observa en la figura, algunos de los desplazamientos medidos experimentalmente, tienen una incertidumbre que se incrementa de manera significativa en el proceso de linearización. Esto es de esperarse, porque el método de mínimos cuadrados con pesos le da mayor importancia, en el ajuste, a los puntos con mayor peso (menor incertidumbre). 

```{figure} imagenes/bola5.png
---
scale: 100%
name: fig-bola5
---

Razón entre la posición de la bola y el tiempo, en función del tiempo.
```

```{seealso}

Sobre mínimos cuadrados y ajuste lineal pueden consultar el capítulo 8 de {cite}`Taylor1996`, o las secciones 6.3 y 5.2.1 de {cite}`Hughes2010`.

```