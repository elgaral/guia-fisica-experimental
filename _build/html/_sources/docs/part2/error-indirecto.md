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

(sec-errorIndirecto)=

# Determinación de la incertidumbre de una variable indirecta

Hasta ahora se tiene una serie de herramientas para determinar la incertidumbre de cantidades físicas que se pueden medir directamente con un instrumento, como por ejemplo: la temperatura con un termómetro, o la longitud con una regla. No obstante, existen cantidades físicas de interés que no se pueden medir directamente con un instrumento: generalmente lo que se tiene a disposición es una ecuación matemática que relaciona la cantidad física de nuestro interés con una o más cantidades físicas que sí es posible medir directamente con un instrumento. La pregunta ahora es ¿cómo determinar la incertidumbre de esta cantidad que no se puede medir directamente? En esta sección definiran las cantidades física medidas directa e indirectamente, y se presentará un método para determinar la incertidumbre de la cantidad física medida indirectamente.

+++

(subsec-varDirecta)=

## Variable directa

La cantidad física medida directamente, o variable directa, es aquella que se puede medir directamente con un instrumento y que no involucra un cálculo extra por parte del experimentalista para obtener su valor. Desde el punto de vista práctico, si para saber el valor de la variable física sólo es necesario mirar la pantalla, dial, o escala de un intrumento, entonces se considera variable directa. La determinación de la incertidumbre de este tipo de variable se hace según las indicaciones de la {numref}`sec-estimacionIncertidumbre` y la {numref}`sec-unaMedida`. Un ejemplo de una variable directa es la longitud de un lado de un cubo medida con una regla, o la masa de un cubo medida con una balanza.

+++

(subsec-varIndirecta)=

## Variable indirecta

La cantidad física medida indirectamente, o variable indirecta, es aquella que requiere para su determinación de la medición de una o más variables directas, y de una función matemática que relaciona las variables directas con la variable indirecta de interés. Un ejemplo de una variable indirecta es la densidad volumétrica $\rho$ de un cubo, que requiere la medición de la variable directa de longitud del lado $L$, la medición de la variable directa de masa $m$, y la ecuación $\rho = m/L^3$.

+++

(subsec-errorIndirecta)=

## Incertidumbre de una variable indirecta

Para determinar la incertidumbre de la variable indirecta $A$, que depende de las variables directas (con sus incertidumbres) $B \pm \alpha_B$ y $C \pm \alpha_C$ a través de la relación $A = F(B,C)$,  donde $F$ es una función matemática que depende de $B$ y $C$, se procede de la siguiente manera:

1. Se calcula $A$ para los máximos de $B$ y $C$: $A_{max} = F(B+\alpha_B,C+\alpha_C)$.

2. Se calcula $A$ para los mínimos de $B$ y $C$: $A_{min} = F(B-\alpha_B,C-\alpha_C)$.

3. Se calculan las diferencias de los valores $A_{max}$ y $A_{min}$ con respecto a $\bar{A} = F(A,B)$. Se reporta el valor absoluto del promedio de estas diferencias como la incertidumbre de $A$, usando el número de cifras significativas correctas: $\alpha_A = \frac{|A_{max} - A_{min}|}{2}$.

**Ejemplo**: nos piden reportar la densidad volumétrica de un cubo que tiene un lado de longitud $L = (1.20 \pm 0.03) \ \text{cm}$ y masa $(50.0 \pm 0.1) \ \text{g}$, conociendo que la relación entre la densidad, la masa y la longitud es $\rho = m/L^3$. Realizando los diferentes pasos antes mencionados obtenemos:

1. $\rho_{max} = (m+\alpha_m)/(L+\alpha_L)^3 = (50.1\,\text{g})/(1.23\,\text{cm})^3 = 26.922 \,9 \ \text{g/cm}^3$

2. $\rho_{min} = (m-\alpha_m)/(L-\alpha_L)^3 = (49.9\,\text{g})/(1.17\,\text{cm})^3 = 31.156 \,1 \ \text{g/cm}^3$

3. $\alpha_{\rho} = \frac{|\rho_{max} - \rho_{min}|}{2} = 2.116 \,6 \ \text{g/cm}^3 $ 

El valor más probable de la densidad volumétrica del cubo será igual a:

$$\bar{\rho} = m/L^3 = (50.0\,\text{g})/(1.20\,\text{cm})^3 = 28.935 \,2 \ \text{g/cm}^3$$

El valor a reportar de su densidad volumétrica, usando una cifra significativa en la incertidumbre es:

$$ \rho = (29 \pm 2) \ \text{g/cm}^3 $$

```{admonition} Observaciones
Una forma más exacta de determinar la incertidumbre sería calcular la variable indirecta usando todas las posibles combinaciones de las variables directas, dadas sus respectivas incertidumbres. No obstante, la diferencia con el procedimiento usado, consistente en evaluar la variable indirecta para los valores extremos de las variables directas, arroja una diferencia porcentual inferior al $1 \ \%$. Por lo tanto se continuará usando el procedimiento aquí esbozado y sólo será necesario hacer una revisión de su validez en el caso en que las incertidumbres obtenidas sean inferiores al $1 \ \%$. 

Por otro lado, cuando se tengan más herramientas de cálculo diferencial se usará la técnica de propagación del error, que es el método más extendido por su practicidad[^limite]; pero no se deben esperar resultados muy diferentes a los aquí obtenidos.

[^limite]: Aunque su uso es muy extendido, cuando las incertidumbres de las variables directas son grandes su validez disminuye, y la confiabilidad puede no corresponder a una distribución normal.

Finalmente, se han promediado las incertidumbres extremas por practicidad. Es de esperarse que para incertidumbres relativas pequeñas la diferencia sea despreciable y ambas incertidumbres extremas den aproximadamente iguales; afirmación de la que se parte en el método de propagación de errores. No obstante, la forma más general, y correcta en el caso de incertidumbres relativas grandes, es la de reportar ambas incertidumbres.
```

+++

(subsec-estimacionEjemplo2)=
## Ejemplo altura mesa: segunda parte[^ejemplo2]
Recordando el enunciado del problema: "un estudiante quiere estimar la altura de una mesa pero no cuenta con una regla, solamente tiene un cronómetro y conoce el valor aceptado de la aceleración de la gravedad $g$ en el sitio." El estudiante resuelve medir el tiempo que tarda en caer un objeto del borde de la mesa al piso, y usar la expresión que relaciona el tiempo $t$, la aceleración de la gravedad $g$ y la altura $h$:

$$ h = \frac{1}{2}g t^2 $$

[^ejemplo2]: La primera parte está en la {numref}`subsec-estimacionEjemplo1`.

Entonces para este problema $t$ es la variable directa y $h$ es la variable indirecta. Aunque $g$ es una cantidad física medida con incertidumbre, la precisión con la que se ha medido es tal que para este problema se considera como una constante igual a $979.748 \ \text{cm/s}^2$. De la {numref}`subsec-estimacionEjemplo1` se sabe que el valor para el tiempo obtenido por el estudiante fue de $t= 0.486 \pm 0.011 \ \text{s}$. Aplicando el procedimiento presentado en esta sección se obtiene para la altura de la mesa el valor de $h = (116 \pm 5) \ \text{cm}$, con una incertidumbre relativa de $5 \ \%$.

```{admonition} Resultados para obtener la altura
:class: dropdown

1. Altura máxima = $121.003 \,2 \ \text{cm}$
2. Altura mínima = $110.527 \,8 \ \text{cm}$
3. Altura más probable = $115.706 \,2 \ \text{cm}$
```

```{admonition} Pregunta
A partir del resultado obtenido por el estudiante ¿consideraría que el método usado es correcto para medir la altura de la mesa?¿Podría proponer otro? Si usara el mismo método ¿cómo podría mejorar la precisión?
```


