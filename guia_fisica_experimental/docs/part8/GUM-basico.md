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

(sec-gum-basico)=
# GUM: Guía para el reporte de la incertidumbre experimental

La sigla *GUM* significa "Guide to the expression of uncertainty in measurements", y corresponde a un esfuerzo internacional por unificar la forma en que se reporta la incertidumbre en la medición de un *mensurando*[^mensurando]. La iniciativa surge en el año 1977 cuando la mayor autoridad mundial en metrología, Comité International des Poids et Mesures (CIPM), le pide al Bureau International des Poids et Mesures ([BIPM](https://www.bipm.org/en/home)) que se encargue, junto con los laboratorios nacionales de estándares, de presentar una recomendación. A partir de las recomendaciones hechas, el CIPM le asignó al Internatinal Organization for Stardardization (ISO), la publicación de una guía con los objetivos de promover el acceso a la información completa de como llegar al valor de la incertidumbre, y proveer las bases que permitan la comparación internacional de medidas. La primera publicación se realizó en 1995 siendo la versión actual de 2008 {cite}`JCGMGUM`. En 2010 se realizaron algunas correcciones.

[^mensurando]: El *mensurando* es la cantidad física que se pretende medir experimentalmente.

La guía es extensa, y ha sido cubierta, hasta cierto punto, en las anteriores secciones de este texto, por lo que aquí se presentarán sólo los conceptos más básicos y que se consideran más relevantes, basados en el libro de Les Kirkup {cite}`kirkup2012data`.

+++

(subsec-gum-clasificacion)=
## Clasificación de las formas de evaluar la incertidumbre

Según la *GUM*, la incertidumbre de una medida es un parámetro, asociado con el resultado de una medición, que caracteriza la dispersión de los valores que pueden ser de forma razonable asociados al mensurando.

A partir de la definición para la incertidumbre, la *GUM* propone clasificar los tipos de incertidumbres en dos categorías:

* La incertidumbre **tipo A**, correspondiente a toda incertidumbre que se haya determinado a partir de aplicar métodos estadísticos a una serie de medidas del mensurando.

* La incertidumbre **tipo B**, es toda incertidumbre que no cumpla con la condición del *tipo A*.

La condición impuesta para la incertidumbre *tipo A* es estricta, por lo que, si para un investigador "X" que realiza una serie de medidas para determinar el valor esperado y la incertidumbre de la reflectancia de una muestra, dicha incertidumbre corresponde al tipo A, para otro investigador "Y" en otro laboratorio que no cuente con el tiempo para hacer las medidas de la reflectancia, y decida tomar el valor obtenido por el investigador "X", la incertidumbre de la reflectancia para el investigador "Y" será del tipo B sin importar que la incertidumbre de la reflectancia haya sido originalmente tipo A.

Otros ejemplos de incertidumbres tipo B son las correspondientes a resolución del instrumento de medida, valores tomados de artículos científicos, catálogos, "handbooks" o libros.

+++

(subsec-gum-evaluacion)=
## Evaluación de las incertidumbres tipo A y tipo B

Para evaluar una incertidumbre *tipo A* se aplica el procedimiento visto en la {numref}`sec-errorEstandar`. Para la evaluación de las incertidumbres *tipo B* se debe analizar el problema, particular, para poder definir que tipo de *densidad de probabilidad* sigue la cantidad física, o mensurando, con el fin de poder estimar su valor más probable e incertidumbre. A continuación se presentan dos ejemplos.

(subsubsec-gum-pdfUniforme)=
### Incertidumbre tipo B: distribución uniforme

Cuando la probabilidad de que la medida del mensurando este dentro de un intervalo es la misma para cualquier punto comprendido dentro del intervalo, la distribución de las medidas será uniforme o rectangular. Un ejemplo de este caso de distribución se encuentra cuando queremos ubicar el punto exacto en el que llega una partícula, pero nuestro detector está dividido en segmentos de lado $l$ talque cuando una partícula llega a un segmento, sólo podemos decir que la partícula llega a una zona comprendida entre $a$ y $b$, donde $l = b-a$. La densidad de probabilidad en este caso está dada por la expresión

$$ p_u(x) = \frac{1}{b-a} .$$ (ec-gum1)

Una vez conocida la densidad de probabilidad se puede calcular el valor esperado $\mu$ y la incertidumbre $\sigma$:

$$\mu = \int_{a}^{b} xp_u(x) dx = \int_{a}^{b} \frac{x}{b-a} dx = \frac{(b-a)^2}{2(b-a)} = \frac{a+b}{2} ,$$ 

y

$$\begin{split} \sigma^2 &= \int_{a}^{b} (x-\mu)^2p_u(x) dx = \int_{a}^{b} (x-\mu)^2\frac{1}{b-a} dx \\
&= \int_{a}^{b} x^2\frac{1}{b-a} dx - \int_{a}^{b} 2x\mu\frac{1}{b-a} dx + \int_{a}^{b} \mu^2\frac{1}{b-a} dx \\
&= \frac{(b^3 - a^3)}{3(b-a)} - \frac{2\mu^2}{b-a} + \frac{\mu^2}{b-a} = \frac{a^2 +ab + b^2}{3} - \frac{a^2+2ab+b^2}{4} = \frac{(b-a)^2}{12}
\end{split} .$$

Finalmente, el valor a reportar del mensurando es

$$ x = \frac{a+b}{2} \pm \frac{b-a}{\sqrt{12}} .$$ (ec-gum2)

La probabilidad de que $x$ se encuentre dentro del intervalo definido por {eq}`ec-gum2` es

$$ p_u(\mu-\sigma \leq \mu + \sigma) = \int_{\mu - \sigma}^{\mu+\sigma} p_u(x) dx = \int_{\mu - \sigma}^{\mu+\sigma} \frac{1}{b-a} dx = \frac{2\sigma}{b-a} = \frac{1}{\sqrt{3}} \approx 0.577$$

**Ejemplo**:

Según lo visto en la {numref}`sec-unaMedida`, para un cronómetro con una resolución de $1\,\text{cs}$, la incertidumbre a reportar en segundos sería $\pm 0.01\,\text{s}$. Por lo tanto, al medir un tiempo de $44\,\text{cs}$ el valor a reportar sería:

$$ t = (0.44 \pm 0.01) \,\text{s} .$$

Para un nuevo razonamiento, donde a partir de la resolución el tiempo con igual probabilidad se encuentra entre $43\,\text{cs}$ y $45\,\text{cs}$, al considerar una distribución uniforme la incertidumbre será:

$$ \alpha_t= \frac{(0.45 - 0.43)\,\text{s}}{\sqrt{12}} = 0.00577 \,\text{s} ,$$

y el valor a reportar con una confiabilidad del $58\,\%$ es

$$ t = (0.440 \pm 0.006) \,\text{s} .$$


+++

(subsubsec-gum-pdftriangular)=
### Incertidumbre tipo B: distribución triangular

Suponiendo que el valor de un mensurando se encuentra dentro del intervalo $l= b-a$, cuando se tiene mayor certeza de que el valor del mensurando se encuentre con mayor probabilidad cerca del centro del intervalo que en sus extremos, la distribución triángular puede ser una buena opción para modelar dicha distribución (ver {numref}`fig-pdfTriangular`). Un ejemplo de este caso de distribución es cuando se usa la resolución del instrumento de medida para definir la incertidumbre de la medida ({numref}`sec-unaMedida`). La función densidad de probabilidad para la distribución triángular esta definida como

$$
  p_{\Delta}(x) =
    \begin{cases}
      \frac{4}{(b-a)^2}(x-a) & a \leq x \leq \frac{a+b}{2} \\
      \frac{4}{(b-a)^2}(b-x) & \frac{a+b}{2} < x \leq b \\
      0 & \text{en cualquier otro caso}
    \end{cases}       
$$ (ec-gum3)


```{figure} imagenes/pdfTriangular.svg
:name: fig-pdfTriangular

Función densidad de probabilidad de la distribución triangular.
```

Aplicando las ecuaciones {eq}`ec-media` y {eq}`ec-desviacionEst`, se obtiene para la media 

$$\mu = \frac{a+b}{2} ,$$

y para la desviación estándar

$$ \sigma = \frac{b-a}{2\sqrt{6}} .$$

Por lo tanto, el valor a reportar del mensurando será

$$ x = \frac{a+b}{2} \pm \frac{b-a}{2\sqrt{6}} ,$$ (ec-gum4)

y la probabilidad de que $x$ se encuentre dentro del intervalo definido por {eq}`ec-gum4` es $p_{\Delta}(\mu-\sigma \leq x \leq \mu + \sigma) \approx 0.6498. $

**Ejemplo**

Si en el razonamiento hecho para la incertidumbre del tiempo, se considera que sigue una distribución triángular, la incertidumbre será:

$$ \alpha_t= \frac{(0.45 - 0.43)\,\text{s}}{2\sqrt{6}} = 0.00408 \,\text{s} ,$$

y el valor a reportar en este caso con una confiabilidad del $65\,\%$ es

$$ t = (0.440 \pm 0.004) \,\text{s} .$$

+++

(subsubsec-gum-combinacionError)=
### Combinación de incertidumbres tipo A y tipo B

El *GUM* hace uso de la propagación de la incetidumbre ({numref}`subsec-errorPequeno`) para combinar las incertidumbres tipo A y tipo B. Un caso especial se presenta cuando se determina el valor más probable de un mensurando cuya incertidumbre es tipo A, es decir, se realizaron varias medidas y se aplican métodos estadísticos para determiner el valor más probable y la incertidumbre. Si, posteriormente se quiere incluir una incertidumbre tipo B (por ejemplo la incertidumbre relativa a la resolución del instrumento de medida) las dos incertidumbres se deben sumar en cuadratura, y la raiz cuadrada de dicha suma será la incertidumbre combinada. Lo interesante de este caso es que la incertidumbre tipo B limitará la precisión que se puede alcanzar en la incertidumbre tipo A, es decir, *la precisión que se puede obtener realizando muchas medidas del mensurando no prodrá ser mejor que la precisión debida a la resolución del instrumento de medida*. 

**Ejemplo**:

Recordando el ejemplo de la {numref}`subsec-estimacionEjemplo1b`, sobre la medición del tiempo de caída de un objeto, luego de realizar siete mediciones del tiempo se obtuvo el valor

$$ t = (0.486 \pm 0.013)\,\text{s} ,$$

con una confiabilidad del $68\,\%$. Con el objetivo de dar un valor de incertidumbre más cercano al real, al tener en cuenta la resolución del equipo que se considera sigue una distribución triangular, la incertidumbre combinada será

$$ \alpha_c = \sqrt{(0.013\,\text{s})^2 + (0.004\,\text{s})^2} = 0.0136\,\text{s} ,$$

y el valor correcto de tiempo a reportar es

$$ t = (0.486 \pm 0.014)\,\text{s} .$$

Note que la incertidumbre debida a la resolución del cronómetro es todavía inferior a la incertidumbre debida a las fluctuaciones en la medida del tiempo. Lo cuál nos lleva a dos conclusiones: para las siete mediciones se puede ignorar la incertidumbre debida a la resolución, y todavía se pueden hacer mas mediciones para obtener una mejor precisión en la medida del tiempo.

```{warning}
Puesto que para encontrar la incertidumbre combinada se ha realizado la suma de los cuadrados de dos incetidumbres que siguen distribuciones diferentes, la confiabilidad que se reporta para el nuevo valor es sólo una aproximación, dado que no estamos completamente seguros sobre que tipo de distribución se genera con la suma. Para el ejemplo, como ambas variables tienen una confiabilidad cercana al $68\,\%$, diremos que el tiempo reportada con la incertidumbre combinada, tiene una confiabilidad aproximada del $68\,\%$. 

```

```{seealso}

Para leer más sobre *GUM* mirar las secciones 5.7, 5.8 y 5.9 de {cite}`kirkup2012data`, o la guía de *GUM* {cite}`JCGMGUM`.

```
