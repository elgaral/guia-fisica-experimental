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

(sec-distNormal)=
# Distribución normal o *Gaussiana*

La función de distribución normal será el pilar para el tratamiento de las incertidumbres aleatorias, para variables continuas, como se verá en la {numref}`sec-incertidumbreProcesosAleatorios`. En esta sección, se presentará la distribución normal o *Gaussiana*, también conocida como función densidad de probabilidad normal o *Gaussiana*.

(subsec-funcDensidadNormal)=
## Función densidad de probabilidad normal o *Gaussiana*

La función densidad de probabilidad normal se define como

$$ G(x;\mu,\sigma) = \frac{1}{\sigma \sqrt{2\pi}}\ \exp\bigg[-\frac{(x-\mu)^2}{2\sigma^2}\bigg], $$ (ec-distNormal)

donde $x$ es la variable continua, y $\mu$ y $\sigma$ son los dos parámetros necesarios para definir completamente la distribución: correspondientes a la media y a la desviación estándar, respectivamente. El factor que multiplica la exponencial es el factor de normalización para que la probabilidad total sea igual a uno (ecuación {eq}`ec-probaTotal`). En la {numref}`distNormal` se puede observar un ejemplo de una distribución normal. Note la forma de campana de la distribución, la simetría alrededor de la media $\mu$ y la rápida caída del valor de la función a medida que se distancia de la media $\mu$. Note también en la figura que la posición donde el doble de la desviación estándar coincide con el ancho de la curva es, precisamente, donde la curva tiene una inflexión: lo que significa que la mayor parte del área (probabilidad) definida por la curva está en el rango definido por la desviación estándar.

```{figure} imagenes/distNormal.png
:name: distNormal
:scale: 80%

Distribución normal o *Gaussiana*. La curva azul corresponde a la función densidad de probabilidad. La línea roja discontinua es dos veces la desviación estándar $\sigma$, y la línea verde discontinua marca la posición de la media $\mu$. 
```

```{admonition} ¡Hazlo tu mismo!
Si quieres cambiar los parámetros de la gráfica puedes desplegar la siguiente ventana, donde encontrarás un programa para hacerlo.
```

```{code-cell} ipython3
:tags: ['hide-cell']

#### Parámetros de la distribución ###
mu = 2.0 # media aritmética
sigma = 1.5 # desviación estándar
######################################

import numpy as np
import pylab as plt
plt.rcParams.update({'font.size': 16})

x = np.arange(-10,10,0.1)
G = (1./np.sqrt(2*np.pi*sigma**2))*np.exp(-(x-mu)**2/(2*sigma**2))

plt.figure(figsize=(16,8))
plt.plot(x,G,linewidth=3)
plt.ylabel('$G(x)$')
plt.axvline(mu, linestyle='--', linewidth=2, c="green", label='$\mu$=%.1f'%mu)
plt.plot([mu-sigma, mu+sigma], [1/(np.sqrt(np.e)*np.sqrt(2*np.pi*sigma**2)), 
                                1/(np.sqrt(np.e)*np.sqrt(2*np.pi*sigma**2))], linewidth=3, 
         linestyle="--", color="red", solid_capstyle="butt", label='$2\sigma$=%.1f'%(2*sigma))
plt.legend()
plt.xlabel('$x$')
plt.show()

```

(subsec-calProbabilidades)=
## Cálculo de probabilidades y nivel de confianza
Como $G(x;\mu,\sigma)$ es una función de densidad de probabilidad, se puede calcular la probabilidad de obtener un valor dentro de un intervalo. Por ejemplo, la probabilidad de obtener un dato entre $x_1$ y $x_2$, con $x_1 < x_2$, será

$$ P(x_1 < x < x_2) = \int\limits_{x_1}^{x_2} G(x;\mu,\sigma) \ dx = \frac{1}{\sigma \sqrt{2\pi}}\int\limits_{x_1}^{x_2}  \exp\bigg[-\frac{(x-\mu)^2}{2\sigma^2}\bigg] \ dx .$$ (ec-distNormalProbabilidad)

De la misma manera, se puede determinar la probabilidad acumulada de obtener un valor desde $-\infty$ hasta $x_1$, que comúnmente se conoce como función error $\text{erf}(x_1;\mu,\sigma)$[^erf]:

$$ \text{erf}(x_1;\mu,\sigma) = \frac{1}{\sigma \sqrt{2\pi}}\int\limits_{-\infty}^{x_1}  \exp\bigg[-\frac{(x-\mu)^2}{2\sigma^2}\bigg] \ dx $$ (ec-erf)

Un caso particular de mayor interés es la probabilidad de obtener un dato en el intervalo definido por la desviación estándar $\sigma$:

$$ P(\mu - \sigma < x < \mu + \sigma) = \int\limits_{\mu -\sigma}^{\mu +\sigma} G(x;\mu,\sigma) \ dx = 0.68 .$$ (ec-nivelConfianza)

El valor $0.68$, que corresponde aproximadamente a dos tercios, se puede interpretar como el nivel de confianza por el cual se puede asegurar que al medir un nuevo dato, el valor de este se encontrará a no mas de una desviación estándar de la media. Entonces, se puede decir que se tiene una confianza del $68\,\%$, o una incerteza del $32\,\%$, o que de tres medidas que se realicen hay una alta probabilidad de que dos estén dentro del rango definido por la desviación estándar, o, que solo una estará a más de una desviación estándar de la media ($0.32 \approx 1/3$).

```{warning}
Recordar que los niveles de confianza, aquí definidos, son válidos siempre que la distribución de los datos se corresponda con una distribución normal.
```

[^erf]: La forma como se presenta la función error corresponde a la forma presentada en  {cite}`Hughes2010`, pág. 24. No obstante, la función error se suele presentar para el caso partícular de $\mu = 0$ y $\sigma = 1$. Otra función de interés es la función integral definida como $\phi(z) = \sqrt{\frac{2}{\pi}} \int_0^z e^{-t^2/2}\,dt$, que nos da la probabilidad en un rango entre $-z$ y $z$ para una distribución normal de media igual a cero y desviación estándar igual a uno ({cite}`Squires2001`, pág. 21). Cabe resaltar que con la transformación $z = \frac{x-\mu}{\sigma}$ cualquier distribución normal se puede llevar a la distribución normal de media igual a cero y desviación estándar igual a uno. Finalmente, se llama la atención que en el libro de Taylor a la función integral la llaman función error {cite}`Taylor1996`, pág. 136.

La ecuación {eq}`ec-nivelConfianza` también se puede aplicar para múltiplos de la desviación estándar con el fin de determinar el nivel de confianza en estos casos. En la {numref}`tabla-nivelConfianza` se presentan los porcentajes para múltiplos de la desviación estándar.

```{list-table} Niveles de confianza distribución normal.
:header-rows: 1
:name: tabla-nivelConfianza

* - 
  - $\sigma$
  - $2\sigma$
  - $3\sigma$
* - Certeza
  - 68 % 
  - 95 %
  - 99.7 %
* - Incerteza
  - 32 % 
  - 5 %
  - 0.3 %
* - Fuera del rango
  - 1 en 3 
  - 1 en 20
  - 1 en 400
```

(subsec-distNormal-ejemplo)=  
## Ejemplo: ruido estática
Se graba una señal de radio correspondiente a ruido estática y se quiere determinar como es la distribución de la amplitud de los datos registrados. El audio tiene una duración de $9.4\,\text{s}$, con una frecuencia de grabación de $44\,100$ datos por segundo. En la {numref}`fig-estatica` se presenta una porción de la señal. Allí se puede apreciar que los puntos parecen distribuirse de manera aleatoria alrededor del valor de amplitud cero, la gran mayoría concentrados en un rango definido por las amplitudes $-1\,000$ y $1\,000$. 

```{code-cell} ipython3
:tags: ['hide-input']
import IPython.display as ipd

ipd.Audio('audios/estatica.wav') # load a local WAV file

```

```{figure} imagenes/estatica.svg
:name: fig-estatica

Señal de radio correspondiente  a ruido estático. 
```

Entonces se tiene una variable aleatoria continua[^variable], que se distribuye alrededor de un valor dentro de un rango bien definido. Todo indica que nuestros datos se distribuyen de forma normal o *Gaussiana*. El siguiente paso será graficar el histograma, determinar la media y la desviación estándar, y comparar el histograma experimental con la función de densidad de la distribución normal respectiva. Analizando la {numref}`fig-estatica-hist`, visualmente es evidente que la distribución de los datos del ruido estático corresponden a una distribución normal. Entonces podemos inferir que dos de cada tres datos de la señal tendrán una magnitud igual o inferior a $1\,232$, que uno de cada 20 datos tendrá una magnitud superior a $2\,464$, y que el $99.7\,\%$ de los datos tienen magnitudes no superiores a $4\,928$.

[^variable]: Es importante aclarar aquí que la cantidad física que estamos midiendo es continua: las variaciones de presión traducidas como una intensidad sonora. No obstante, el transductor que utilizamos es digital, por lo que los valores continuos de la cantidad física se aproximan al entero más cercano. La fidelidad con la que almacenemos los datos dependerá de la resolución de nuestro sistema digital.

```{figure} imagenes/estatica-hist.svg
:name: fig-estatica-hist

Histograma de la señal de radio correspondiente a ruido estático. La línea discontinua roja corresponde a la función de densidad obtenida con la ecuación {eq}`ec-distNormal` usando la media y desviación estándar obtenida de la distribución de los datos. Note que se llamó $\bar x$ a la media y $s$ a la desviación estándar. Esto con el fin de hacer énfasis que fueron obtenidos a partir de una muestra $N$ finita.
```

```{code-cell} ipython3
:tags: ['hide-cell']

import numpy as np
import pylab as plt
from scipy.io import wavfile
from scipy.stats import norm
plt.rcParams.update({'font.size': 18})

# Datos de la distribución e histograma
s, data = wavfile.read('audios/estatica.wav')
data = data[:,0]/1000
M = 30
plt.figure(figsize=(16,8))
n, bins, patches = plt.hist(data, bins=M,density=True,align='mid',
                   color='silver')

# Parámetros y función densidad de probabilidad
mu = np.mean(data)
sigma = np.std(data)
y = norm.pdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=1)

plt.xlabel('Amplitud en unidades arbitrarias/$10^3$')
plt.ylabel('$f_i$')
plt.title(r'$\bar x$ = {:.0f},  $s$ = {:,.0f}'.format(mu*1000,sigma*1000).replace(',',' '))
plt.grid(True)
plt.show()

```

```{seealso}
Más sobre distribución normal en las secciónes 5.3 y 5.4 de {cite}`Taylor1996`, la sección 2.3 de {cite}`Bevington`, la sección 2.5 de {cite}`Hughes2010`, la sección 1.4.1 de {cite}`Mahecha2009` y la sección 8.2 de {cite}`GorgasGarcia2011`.

```