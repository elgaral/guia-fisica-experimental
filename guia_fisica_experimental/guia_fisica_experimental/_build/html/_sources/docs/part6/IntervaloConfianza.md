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

(sec-intervaloConfianza)=
# Intervalos de confianza

En la ecuación {eq}`ec-errorEstandar` se deifinió que la forma correcta de reportar el resultado de la medida de una cantidad física era

$$ X = \bar x \pm \frac{s}{\sqrt N} , $$ 

donde $\bar x$ era el valor más probable esperado de la cantidad física, y $s_m = \frac{s}{\sqrt N}$ definía un intervalo en el que se espera se encuentre la cantidad física  [^interpreta]. Para que esta interpretación quede completa se debe hablar en términos de probabilidades, es decir, el intervalo que se ha definido con los dos parámetros de la ecuación realmente habla de la probabilidad de encontrar el valor real allí. Se definirá entonces un *intervalo de confianza* acompañado de una probabilidad.}

[^interpreta]: Existen otras interpretaciones, mirar la nota de la {numref}`subsec-ConfianzaDistNormal`.

Sea el intervalo de confianza $[ L_i, L_s ]$, donde $L_i = \bar x - s_m$ y $L_s = \bar x + s_m$, la probabilidad de que el valor real $\mu$ se encuentre en dicho intervalo es

$$ P_{\mu,\sigma_m}(L_i \leq \mu \leq L_s) = 1 - \alpha $$ (ec-probabilidadConfianza)

donde $1 - \alpha$ es el nivel de confianza o certeza. $\alpha$ será conocido como la incerteza de encontrar el valor real dentro del intervalo. En conclusión, **siempre que se reporte una cantidad física se deberá reportar el valor más probable, la incertidumbre, y el *nivel de confianza* de que el valor real se encuentre dentro de dicho intervalo.

Lo importante ahora es poder conocer la función densidad de probabilidad que permite calcular los intervalos de confianza.

+++

(subsec-ConfianzaDistNormal)=
## Intervalo de confianza distribución normal

Puesto que el interés en la mayoría de los casos es determinar el valor de la cantidad física, que se corresponde con la media de la distribución de los datos, por el teorema del límite central se sabe que la distribución normal es la distribución que seguirán los promedios de las medidas que hagamos, sin importar cual es la distribución original de los datos aleatorios. Igualmente, si se hace una cantidad de medidas razonable[^n30], es de esperar que $\bar x \approx \mu$ y $s_m \approx \sigma_m$, y por lo tanto se podrá usar la función densidad de probabilidad de la distribución normal para determinar el nivel de confianza del resultado experimental. Usando la {numref}`fig-confianzaNormal` se puede inferir el nivel de confianza en función de múltiplos de la desviación estándar de la media.

[^n30]: En general, se entiende como un número razonable de medidas hacer $30$ o más.

```{figure} imagenes/confianzaNormal.svg
:name: fig-confianzaNormal

Probabilidades según la distribución normal. Para un intervalo igual a la desviación estándar (zona azul) la probabilidad es de $68\, \%$. Para un intervalo igual a dos desviaciones estándar (zonas roja y azul) la probabilidad es de $95\,\%$. Para un intervalo de tres desviaciones estándar (zonas roja, azul y gris) la probabilidad es de $99.7\,\%$.
```

Reescribiendo la ecuación {eq}`ec-errorEstandar` como

$$ X = \bar x \pm n s_m , $$ 

con $n = 1, 2, 3, ...$ podremos reportar nuestro resultado experimental con diferentes niveles de confianza. Por ejemplo, para $n = 1$, correspondiente a una desviación estándar, el nivel de confianza de nuestro resultado es del $68\,\%$.

```{list-table} Intervalos de confianza distribución normal
:header-rows: 1
:name: tabla-confianzaNormal

* - n
  - $1-\alpha$
  - $\alpha$
  -
* - 1
  - $68\,\%$
  - $32\,\%$
  - 1/3
* - 2
  - $95\,\%$
  - $5\,\%$
  - 1/20
* - 3
  - $99.7\,\%$
  - $0.3\,\%$
  - 1/400
```

```{note} 

Una interpretación alternativa del nivel de confianza es cuando se quiere saber cuál es la probabilidad de obtener un resultado dentro del intervalo definido, si realiza una nueva medida. Por ejemplo, si el nivel de incerteza es de $32\,\%$, una desviación estándar, se puede decir que existe una probabilidad $1/3$ de que la medida no quede dentro del intervalo, es decir, que por cada tres medidas hechas se espera que al menos una quede por fuera del intervalo definido. De la misma forma, para dos desviaciones estándar, con un nivel de incerteza de $5\,\%$, se espera que por cada 20 medidas que se hagan una quede por fuera del intervalo ($1/20$).

En resumen, un intervalo de confianza de $68\,\%$ se puede interpretar como:
1. Que existe una certeza del $68\,\%$ de que la cantidad física esté dentro del intervalo definido.
2. Que existe una certeza del $68\,\%$ de que al realizar una nueva medida esta esté dentro del intervalo definido.
3. Que el $68\,\%$ de las veces que se mide se logra predecir el valor de la cantidad física[^sutileza].
```
[^sutileza]: (2) y (3) son dos formas de decir lo mismo, mientras que la diferencia entre (1) y (3) es muy sutil. En términos de predecir la lluvia para mañana se podría decir para el primer caso que se tiene una certeza del $68\,\%$ de que mañana efectivamente lloverá: aquí se piensa que aún al ser un fenómeno aleatorio hay un $68\,\%$ de probabilidad de predecir el próximo resultado. Para el tercer caso se tiene una certeza del $68\,\%$ sobre la capacidad de predicción del experimentador: aquí se piensa que al ser un evento aleatorio no se sabe que sucederá mañana, pero el $68\,\%$ de las veces que el experimentador intenta predecir el resultado este acierta.

```{warning}
Siempre que se reporte un resultado experimental se debe indicar el nivel de confianza. La única excepción es cuando se reporta usando una desviación estándar. En este caso se sobreentiende que el nivel de confianza es de $68\,\%$.

```

```{admonition} Nota histórica: bosón de Higgs
Para finales de 2011 el experimento ATLAS había encontrado en los datos analizados una señal de la existencia del bosón de Higgs para una masa de $125\,\text{GeV}$ con una significancia de $3\sigma$. Esto corresponde a decir que, para el intervalo de confianza de $68\,\%$, el valor más probable de la señal medida se encuentra con respecto al modelo que no predice el bosón de Higgs a una distancia igual a tres veces el semi-intervalo de confianza definido ({numref}`fig-bosonHiggs`a). El resultado daba indicios de la existencia del Bosón de Higgs, pero no se consideraba un descubrimiento. En 2012, luego de recopilar más datos, los experimentos ATLAS y CMS presentaron para una masa de $125\,\text{GeV}$ los resultados de una señal con una significancia de $5\sigma$ ({numref}`fig-bosonHiggs`b). Esta señal tiene la significancia suficiente para considerar el resultado como un descubrimiento: el descubrimiento del Bosón de Higgs. Más sobre el tema en la página del [experimento ATLAS](https://atlas.cern/updates/feature/higgs-boson).

```

```{figure} imagenes/BosonHiggs.jpg
:name: fig-bosonHiggs

Gráfica señal del "decaimiento difotónico" que predice la existencia del bosón de Higgs. Esquema de la señal con datos hasta (a) el 2011 con una significancia de $3\sigma$ o $99.7\,\%$, y (b) datos hasta 2012 con una significancia de $5\sigma$ o $99.99994\,\%$. (azul) modelo que no tiene en cuenta el bosón de Higgs y (rojo) modelo que predice el bosón de Higgs. Los puntos negros son los datos experimentales.
```

+++

(subsec-estimacionEjemplo1c)=
## Ejemplo altura mesa: intervalos de confianza

En la {numref}`subsec-estimacionEjemplo1b` el estudiante encontró que el tiempo de caída era $ t = (0.486 \pm 0.013) \ \text{s} $. Cómo no reportó el nivel de confianza, deducimos que es del $68\,\%$. Recuerden que esto significa que existe una probabilidad del $32\,\%$ de que el tiempo de caída no se encuentre en el rango $[0.473,0.499]\,\text{s}$. Si el estudiante quiere dar un resultado más confiable que incluya el tiempo real con una muy baja incerteza, puede reportar usando tres desviaciones estándar para la incertidumbre. El estudiante entonces reportaría un tiempo de caída de $ t = (0.486 \pm 0.039) \ \text{s} $ con una confiabilidad de $99.7\,\%$.

```{note}

Puesto que en el caso en que reportó sin mencionar el nivel de confiabilidad, se sabe que es del $68\,\%$, cualquiera puede reescribir el resultado para otro nivel de confiabilidad, simplemente multiplicando la incertidumbre por un factor que se relacione directamente con una probabilidad de la distribución normal.

```

+++

(subsec-errorError)=
## Incertidumbre en la incertidumbre

Hasta ahora se ha hablado de la incertidumbre en el valor más probable de la cantidad física, pero no se ha mencionado que la propia incertidumbre tiene incertidumbre. La razón surge del hecho de que también se determina a partir de un número finito de medidas. Esto es de gran importancia porque finalmente limita el número de cifras significativas en la incertidumbre reportada. Para el caso, en que la distribución de los datos corresponde a una distribución normal, existe una expresión analítica para la incertidumbre relativa de la incertidumbre ({cite}`Squires2001`, en el apéndice B):

$$\frac{\alpha_{em}}{\alpha_m} = \frac{1}{\sqrt{2N-2}} ,$$ (ec-errorError)

donde $\alpha_{m}$ es la incertidumbre de la media muestral, y $\alpha_{em}$ es la incertidumbre de la incertidumbre de la media muestral, para una muestra de $N$ valores. La función {eq}`ec-errorError` inicialmente tiende de forma rápida a cero, pero al ser asintótica, cada vez disminuye más lento sin nunca alcanzar el cero. Este comportamiento lo que provoca es la prácticamente imposibilidad de reportar una incertidumbre con tres cifras significativas, la gran dificultad para reportarla con dos, y la regla general de reportarla con una sola cifra significativa. Por ejemplo, en la {numref}`tabla-eerror`, queda claro en la columna tres que para disminuir la incertidumbre relativa a $1\,\%$, debemos hacer mínimo $5\,000$ mediciones. De hecho, para que la incertidumbre de la incertidumbre no modifique la segunda cifra significativa, se tienen que hacer del orden de $50\,000$ mediciones.


```{list-table} Incertidumbre de la incertidumbre: Tiempo de caida de un objeto a una altura de $121 \ \text{cm}$, medido con un reloj que tiene una resolución de una centécima de segundo. Los valores aleatorios de tiempo se generaron suponiendo una desviación de $10$ %.
:header-rows: 1
:name: tabla-eerror

* - $N$
  - $t/(\text{s})$
  - $\frac{\alpha_{et}}{\alpha_t}/(\%)$
  - $[\alpha_{t_{min}},\alpha_{t_{max}}]\,\text{s}$
  
* - $7$
  - $0.55(2)$
  - $28$
  - $[0.015, 0.026]$
  
* - $30$
  - $0.520(10)$
  - $13$
  - $[0.009, 0.011]$

  
* - $100$
  - $0.501(5)$
  - $7$
  - $[0.004\,7, 0.005\,4]$
  
* - $1\,000$
  - $0.4960(16)$
  - $2.2$
  - $[0.001\,5, 0.001\,6]$
  
* - $5\,000$
  - $0.49749(69)$
  - $1.0$
  - $[0.000\,68, 0.000\,70]$
  
* - $10\,000$
  - $0.49731(49)$
  - $0.7$
  - $[0.000\,49, 0.000\,50]$
  
* - $15\,000$
  - $0.49770(40)$
  - $0.6$
  - $[0.000\,40, 0.000\,41]$

* - $50\,000$
  - $0.49803(22)$
  - $0.3$
  - $[0.000\,221, 0.000\,223]$

```

El código para encontrar los valores de la {numref}`tabla-eerror` se pone a disposición en el siguiente desplegable.


```{code-cell} iphyton3
:tags: ['hide-cell']

#### Altura y tiempo esperado ####
H = 121.6         # Altura cm
He = 0.1          # Incertidumbre altura cm
g = 979.748       # Aceleración de la gravedad cm/s^2
erelativo = 0.1   # Incertidumbre relativa en la medida del tiempo en s
N = 30            # Número de medidas
############################
import numpy as np

def eerror(N):
    return 1/np.sqrt(2*N-2)

t = np.sqrt(2*H/g)
te = 0.5*t*He/H
print('Tiempo real = {} s +/- {} s'.format(t,te))

np.random.seed(0)
vals = []
for ii in range(N):
    vals.append(np.random.normal(loc=t,scale=t*erelativo))

desv = np.std(vals,ddof=1)/np.sqrt(N)
fracerror = eerror(N)
    
print('Media = {} s'.format(np.mean(vals)))
print('Incertidumbre = {} s'.format(desv))
print('Error Incertidumbre = {} %'.format(100*fracerror))
print('Rango Incertidumbre = [{}, {}] s'.format(desv*(1-fracerror),desv*(1+fracerror)))

import matplotlib.pyplot as plt

fig, (ax1) = plt.subplots(1,1,figsize=(8,1))

data = np.copy(vals)
eje = np.zeros(len(data))
ax1.fill_between([t-te,t+te],0.01)
ax1.plot(data,eje,'r|',ms=10)
ax1.set(yticklabels=[])  # remove the tick labels
ax1.tick_params(left=False)  # remove the ticks
ax1.set_xlabel('t/s',fontsize=18)
ax1.set_xlim(0.3,0.7)
#ax1.set_ylim(-1,1)

# use set_position
ax1.spines['top'].set_color('none')
ax1.spines['left'].set_color('none')
ax1.spines['right'].set_color('none')
ax1.spines['bottom'].set_position('zero')

plt.show()
```

Queda claro que para reportar más de dos cifras significativas en la incertidumbre se deben hacer mínimo $5\,000$ mediciones. No obtante, al reportar una única cifra significativa se podría estar incurriendo en una disminución o aumento importante de la incertidumbre por causa del redondeo que toque realizar. Por ejemplo, si la incertidumbre es $0.14$, y se redondea a una sola cifra significativa, $0.1$, la reducción puede llegar a ser del orden de $29\,\%$. Igualmente, si la incertidumbre es $0.15$, pero reportamos $0.2$, puede haber una sobreestimación del $33\,\%$ en la incertidumbre. La recomendación dada por {cite}`Hughes2010` es reportar dos cifras cuando la primera cifra significativa es $1$. En la referencia {cite}`Taylor1996` incluso sugieren reportar dos cifras significativas cuando la primera es un $2$.

Cómo ya se había sugerido en la {numref}`subsec-csIncertidumbre`, a continuación se vuelve a presentar la recomendación general para el reporte de la incertidumbre:

```{tip}
Reporte la incertidumbre con una sola cifra significativa. Las únicas excepciones son cuando la primera cifra significativa sea el número $1$, o haya realizado $5\,000$ o más medidas. En estos casos reporte dos cifras significativas.
```

+++

```{seealso}
El tema de intervalos de confianza se puede consultar en el capítulo 11 de {cite}`GorgasGarcia2011`, o la sección 3.3.1 de {cite}`Hughes2010`. El tema de incertidumbre de la incertidumbre se puede encontrar en la sección 2.7.1 de {cite}`Hughes2010`, en la sección 5.5 de {cite}`Taylor1996` y en la sección 3.7 de {cite}`Squires2001`

```