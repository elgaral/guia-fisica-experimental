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

(sec-propagacionError)=
# Propagación de la incertidumbre
Hasta ahora se ha determinado correctamente la incertidumbre de una *variable aleatoria directa*, así como la confiabilidad en el valor de la incetidumbre que se está registrando. Ahora la pregunta es como extender esto al caso de una [variable indirecta](subsec-varIndirecta). Para una *variable indirecta* que dependa sólamente de una variable directa $x$, tal que el valor de la variable indirecta se pueda determinar a través de la función $f(x)$, si el valor de la variable directa es $x_0$, entonces el valor de la variable indirecta será $f(x_0)$. Ahora bien, si el valor de la variable directa cambia en una cantidad $\Delta x = x -x_0$, el valor correspondiente de la variable indirecta será $f(x_0 + \Delta x)$, como se puede observar en la primera columna de la {numref}`fig-propaError`.

```{figure} imagenes/propaError.svg
:name: fig-propaError

Dependencia de la función $f(x)$. En el primer caso se tiene una relación lineal $f(x) \propto x$ con una incertidumbre relativa de (a) $10\,\%$ y (b) $1\,\%$. En el segundo caso la relación es de una potencia fraccional $f(x) \propto \sqrt x$ con incertidumbres relativas de (c) $10\,\%$ y (d) $1\,\%$. En el tercer caso la relación es cuadrática, $f(x) \propto x^2$, con incertidumbres relativas de (e) $10\,\%$ y (f) $1\,\%$.
```

En el caso (a) de la {numref}`fig-propaError` se puede observar que para una relación lineal el cambio en la función $f(x_0 + \Delta x)$ tiene la misma proporción sin importar el signo de $\Delta x$. En contraste, para los casos (b) y (c), es claro que la magnitud de la variación de $f(x_0 + \Delta x)$ dependerá del signo de $\Delta x$. 

(subsec-errorPequeno)=
## Incertidumbres pequeñas
Suponga ahora que las incertidumbres de las variables directas son lo suficientemente pequeñas como para que el cambio en la función $f(x_0 +\Delta x)$ sea lineal, sin importar el tipo de relación entre la variable directa e indirecta (ver segunda columna de la {numref}`fig-propaError`). En tal caso, haciendo uso de la expansión en series de Taylor, se puede hacer la siguiente aproximación:

$$ f(x_0 +\Delta x) = f(x_0) + \frac{df}{dx}\bigg|_{x_0} \Delta x ,$$ (ec-propaTaylor)

es decir,

$$ \Delta f = \frac{df}{dx}\bigg|_{x_0} \Delta x .$$ (ec-propaTaylor2)

En este punto se tiene que recordar que la variable $x$ es aleatoria. Por lo tanto, para determinar la incertidumbre, se debe encontrar el valor esperado de la expresión {eq}`ec-propaTaylor2` luego de evaluar un gran número de valores de $x$. Cómo estadísticamente se puede demostrar que el valor esperado de $\Delta x$ es nulo, $\langle \Delta x \rangle = 0$[^promedio], se evaluará el promedio del cuadrado de la diferencia, $\langle (\Delta x)^2 \rangle $, y luego sacaremos la raíz cuadrada. Entonces, a partir de la ecuación {eq}`ec-propaTaylor2`

[^promedio]: Piense que al evaluar un gran número de valores de $x$, si el valor $\Delta x = x - x_0$ existe, es de esperarse encontrar también el valor $\Delta x = -(x - x_0)$, los cuales se cancelan mutuamente. Al elevar al cuadrado, ambos $\Delta x$ son positivos, y por lo tanto no se cancelan mutuamente.

$$ \langle (\Delta f)^2 \rangle = \bigg\langle \bigg(\frac{df}{dx}\bigg|_{x_0} \Delta x \bigg)^2 \bigg\rangle = \bigg(\frac{df}{dx}\bigg|_{x_0}\bigg)^2 \langle (\Delta x)^2 \rangle$$

$$ \alpha_f^2 = \bigg(\frac{df}{dx}\bigg|_{x_0}\bigg)^2 \alpha_x^2 ,$$ 

y por lo tanto, la incertidumbre en la variable indirecta será

$$ \alpha_f = \frac{df}{dx}\bigg|_{x_0} \alpha_x .$$ (ec-propaTaylor3)

Repitiendo el procedimiento, pero ahora para una variable indirecta que dependa de dos funciones directas $x$ y $y$, según la relación dada por la función $f(x,y)$, suponiendo nuevamente que las variables directas tienen incertidumbres pequeñas, se puede escribir el cambio en la variable directa como

$$ f(x+\Delta x,y+\Delta y) = f(x_0,y_0) + \frac{\partial f}{\partial x}\bigg|_{x_0} \Delta x + \frac{\partial f}{\partial y}\bigg|_{y_0} \Delta y ,$$

es decir,

$$ \Delta f = \frac{\partial f}{\partial x}\bigg|_{x_0} \Delta x + \frac{\partial f}{\partial y}\bigg|_{y_0} \Delta y .$$ (ec-propaTaylor4)

Elevando al cuadrado la ecuación {eq}`ec-propaTaylor4` y determinando el valor esperado, se obtiene

$$\begin{align} \alpha_f^2 &= \bigg\langle \bigg(\frac{\partial f}{\partial x}\bigg|_{x_0} \Delta x + \frac{\partial f}{\partial y}\bigg|_{y_0} \Delta y \bigg)^2\bigg\rangle \\ &= \bigg\langle \bigg(\frac{\partial f}{\partial x}\bigg|_{x_0} \Delta x \bigg)^2 + \bigg( \frac{\partial f}{\partial y}\bigg|_{y_0} \Delta y \bigg)^2 + 2 \frac{\partial f}{\partial x}\bigg|_{x_0}\frac{\partial f}{\partial y}\bigg|_{y_0} \Delta x \Delta y\bigg\rangle \\ &= \bigg\langle \bigg(\frac{\partial f}{\partial x}\bigg|_{x_0} \Delta x \bigg)^2 \bigg\rangle + \bigg\langle \bigg( \frac{\partial f}{\partial y}\bigg|_{y_0} \Delta y \bigg)^2 \bigg\rangle + \bigg\langle 2 \frac{\partial f}{\partial x}\bigg|_{x_0}\frac{\partial f}{\partial y}\bigg|_{y_0} \Delta x \Delta y\bigg\rangle \\ &= \bigg(\frac{\partial f}{\partial x}\bigg|_{x_0} \alpha_x \bigg)^2 + \bigg( \frac{\partial f}{\partial y}\bigg|_{y_0} \alpha_y \bigg)^2 +  2 \frac{\partial f}{\partial x}\bigg|_{x_0}\frac{\partial f}{\partial y}\bigg|_{y_0} \langle\Delta x \Delta y \rangle .
\end{align}$$ (ec-propaTaylor5)

El tercer término de la ecuación {eq}`ec-propaTaylor5` indica lo correlacionadas que están ambas variables directas. Aquí se supondrá que las variables son independientes, y por lo tanto el valor esperado $\langle \Delta x \Delta y \rangle = 0$[^correlacion], pudiendo escribirse la incertidumbre de la variable indirecta como

[^correlacion]: En una próxima sección se abordará el caso en que las variables no son independientes.

$$\alpha_f = \sqrt{ \bigg(\frac{\partial f}{\partial x}\bigg|_{x_0} \bigg)^2 \alpha_x^2 + \bigg( \frac{\partial f}{\partial y}\bigg|_{y_0} \bigg)^2 \alpha_y^2 } .$$ (ec-propaTaylor6)

Extrapolando el anterior resultado para una variable indirecta que depende de $N$ variables directas, el cuadrado de la incertidumbre de la variable indirecta se escribe como

$$ \alpha_f^2 = \sum_{i=1}^N \bigg(\frac{\partial f}{\partial x_i}\bigg)^2 \alpha_{x_i}^2 .$$ (ec-propaTaylor7)

La ecuación {eq}`ec-propaTaylor7` es válida para variables directas obtenidas con una medida, con muchas medidas. Igualmente es válida para los casos en que algunas variables directas se determinan con una sola medida y otras con muchas medidas.

```{admonition} ¿Puede decir por qué la ecuación es válida sin importar si se mide una vez o muchas?
:class: dropdown

Hay que recordar que todo este tratamiento se hace para cantidades físicas con un ruido que fluctua de forma aleatoria. Por lo tanto, una cantidad física que se mida una única vez, sólo indica que su incertidumbre aleatoria ha sido determinada con la peor precisión posible. 
```

**Ejemplo**: nos piden reportar la densidad volumétrica de un cubo que tiene un lado de longitud $L = (1.20 \pm 0.03) \ \text{cm}$ y masa $(50.0 \pm 0.1) \ \text{g}$. Conociendo que la relación entre la densidad, la masa, y la longitud es $\rho = m/L^3$, y suponiendo que las incertidumbres son pequeñas:

1. $\bar{\rho} = m/L^3 = (50.0\,\text{g})/(1.20\,\text{cm})^3 = 28.935 \,2 \ \text{g/cm}^3$

Usando la ecuación {eq}`ec-propaTaylor7` encontramos que

$$ \alpha_{\rho}^2 = \rho^2 \Bigg[ \bigg(\frac{\alpha_m}{m}\bigg)^2 + \bigg(\frac{3\alpha_L}{L}\bigg)^2 \Bigg] = \big(28.935\,\text{g/cm}^3\big)^2 \Bigg[ \bigg(\frac{0.1}{50.0}\bigg)^2 + 9\bigg(\frac{0.03}{1.20}\bigg)^2 \Bigg] = 4.7129\,\text{g}^2\text{/cm}^6  .$$

Y por lo tanto, en este caso el valor a reportar de densidad volumétrica es

$$\rho = (29 \pm 2) \ \text{g/cm}^3 ,$$

```{warning}
La aproximación infinitesimal para el cálculo de la propagación de la incertidumbre es de uso extendido en la comunidad científica. No obstante, se debe tener una idea de como influye cada incertidumbre en la variable de interés, para no subestimar, o sobrestimar la incetidumbre de la cantidad física de interés. En una sección futura se darán algunas pautas para definir correctamente la forma de calcular la incertidumbre.
```

+++

(subsec-tablaErroresPequenos)=
## Tabla de propagación de incertidumbres pequeñas

```{list-table} Fórmulas de propagación de la incertidumbre pequeña
:header-rows: 1
:name: tabla-ErroresPequeños

* - $f(x,y,...)$
  - $\alpha_f$
* - $(x + y + z)$
  - $\sqrt{\big(\alpha_x\big)^2 + \big(\alpha_y\big)^2 + \big(\alpha_z\big)^2}$
* - $k\times(x^l + y^m - z^n)$
  - $k\sqrt{\big(lx^{l-1}\alpha_x\big)^2 + \big(my^{m-1}\alpha_y\big)^2 + \big(nz^{n-1}\alpha_z\big)^2}$
* - $\large k\times\frac{x^l \times y^m}{z^n}$
  - $ \large f\times\sqrt{\big(\frac{l\alpha_x}{x}\big)^2 + \big(\frac{m\alpha_y}{y}\big)^2 + \big(\frac{n\alpha_z}{z}\big)^2}$
* - $k\times \ln{nx}$
  - $\Large \frac{k\alpha_x}{x}$
* - $k\times\exp{nx}$
  - $n f \alpha_x$
```

(subsec-errorFormaFuncional)=
## Aproximación funcional
En la {numref}`subsec-errorIndirecta` se presentó una forma funcional rápida de estimar la incertidumbre de una variable indirecta. Ahora, teniendo presente que las variables son aleatorias e independentes, se reescribe aquí la metodología para reportar la incertidumbre de la variable aleatoria.

Para determinar la incertidumbre de la variable indirecta $F$, que depende de las variables directas (con sus incertidumbres) $x_i \pm \alpha_{x_i}$, con $i = 1, 2, ..., N$, a través de la relación $F = f(x_1, x_2, ...,x_i, ..., x_N)$, se procede de la siguiente manera:

1. Se calcula $F$ para los valores más probables de $x_i$: $F_0 = f(x_1, x_2, ...,x_N)$ 

2. Se calcula $\Delta F_i = F_i - F_0$ para los máximos de $x_i$ reemplazando uno a la vez: $\Delta F_i = f(x_1,..., x_i+\alpha_{x_i},...,x_N) - F_0$.

3. Se suman en cuadratura los deltas encontrados en 2.: $\alpha_{max}^2 = \sum_{i=0}^{N} \big(\Delta F_i \big)^2$.

4. Se calcula $\Delta F_i = F_i - F_0$ para los mínimos de $x_i$ reemplazando uno a la vez: $\Delta F_i = f(x_1,..., x_i-\alpha_{x_i},...,x_N) - F_0$.

5. Se suman en cuadratura los deltas encontrados en 4.: $\alpha_{min}^2 = \sum_{i=0}^{N} \big(\Delta F_i \big)^2$.

6. Se reporta el resultado: $F = F_0 \begin{matrix}
+\alpha_{max} \\
-\alpha_{min} 
\end{matrix}$.

7. Si $\alpha_{min}$ = $\alpha_{max}$, reportamos: $F = F_0 \pm \alpha_{max}$

```{warning}
Hay que tener precaución en usar para la variable indirecta determinada con la función $F$ los intervalos de confianza definidos en la {numref}`sec-intervaloConfianza` para una distribución normal. La razón para esto se debe a que la distribución de los valores de la función $F$ no necesariamente corresponden a una distribución normal. Esto es evidente cuando las incertidumbres en los límites superior e inferior son diferentes.
```

**Ejemplo**: Nos vuelven a pedir que midamos la densidad volumétrica del cubo, pero ahora se usa la aproximación funcional. Realizando los diferentes pasos presentados se obtiene:

1. $\bar{\rho} = m/L^3 = (50.0\,\text{g})/(1.20\,\text{cm})^3 = 28.935 \,2 \ \text{g/cm}^3$

2. y 3. $\alpha_{max}^2 = 4.271\,7 \, \text{g}^2\text{/cm}^6$ 

4. y 5. $\alpha_{min}^2 = 5.217\,0 \, \text{g}^2\text{/cm}^6$ 

Al tener en cuenta las cifras significativas en la incertidumbre $\alpha_{min} = \alpha_{max}$, por lo que el valor a reportar es:

$$\rho = (29 \pm 2) \ \text{g/cm}^3 .$$

**¡El mismo que para incertidumbres pequeñas!**.

Nos vuelven a pedir que midamos la densidad volumétrica de un cubo, pero ahora nos dan los valores de las variables directas con menor precisión, así: lado de longitud $L = (1.20 \pm 0.05) \ \text{cm}$ y masa $(50.0 \pm 0.2) \ \text{g}$. Realizando los diferentes pasos se obtiene:

1. $\bar{\rho} = m/L^3 = (50.0\,\text{g})/(1.20\,\text{cm})^3 = 28.935 \,2 \ \text{g/cm}^3$

2. y 3. $\alpha_{max}^2 = 11.136\,9 \, \text{g}^2\text{/cm}^6$ 

4. y 5. $\alpha_{min}^2 = 15.541\,9 \, \text{g}^2\text{/cm}^6$ 

Para este caso $\alpha_{min}$ es diferente a $\alpha_{max}$, por lo que el valor a reportar es:

$$\rho = \bigg( 29 \begin{smallmatrix}
+3 \\
-4 
\end{smallmatrix} \bigg) \ \text{g/cm}^3 $$

+++



```{seealso}

Para leer más sobre propagación de la incertidumbre mirar las secciones 4.1 y 4.2 de {cite}`Hughes2010`, las secciones 3.7, 3.11 y 5.6 de {cite}`Taylor1996`, las secciones 3.2 y 3.3 de {cite}`Bevington`, las secciones 4.1 y 5.3 de {cite}`Squires2001`, y la sección 1.7 de {cite}`LyonsL1991`.

```

