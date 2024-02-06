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

(sec-notacion)=

# Notación correcta[^prefijos]

Una guía más completa sobre la correcta escritura de los números y las unidades se puede encontrar en la guía del National Institute of Standars and Technology (NIST) sobre el uso del sistema de unidades SI {cite}`Thompson2008`. En las siguientes secciones se presentarán los temas más relevantes que debe conocer el estudiante que pretenda reportar resultados experimentales y teóricos.

[^prefijos]: En esta sección se usan prefijos para las unidades como $\text{km}$ o $\mu\text{V}$. Sobre esto se hablará en la {numref}`subsec-prefijo`.

+++

(subsec-escrituraNum)=

## Escritura de números grandes
Cuando se reportan números grandes los valores se deben agrupar de forma tal que su lectura sea fácil y no se induzca a errores. Las reglas para la agrupación de los números son:

1. Los números decimales se separan usando un punto denominado: punto decimal.
2. No se usa ningún símbolo para separar miles, millones, etc.
3. Los números enteros se deben agrupar en grupos de tres dígitos empezando de derecha a izquierda del punto decimal y dejando un espacio entre grupos. 
4. La parte decimal de un número se debe agrupar en grupos de tres dígitos empezando de izquierda a derecha y dejando un espacio entre grupos.
5. La cifra significativa más a la izquierda es la *más* significativa, mientras que la cifra significativa más a la derecha es la *menos* significativa.
5. Se debe evitar dejar un valor solo cuando este corresponde a la cifra menos significativa y tiene incertidumbre (ver ejemplos 13 y 14).

Veamos algunos ejemplos:

1. $299 \ 790$
2. $2\,997 \ 900$
3. $29 \ 979 \ 000$
4. $0.022 \ 413$
5. $0.022 \ 413 \ 8$
6. $0.022 \ 413 \ 83$
7. $29 \ 979.022 \ 41$
8. TRM del día: $4 \ 270$ pesos.
9. Aceleración de la gravedad: $977 \ \text{cm s}^{-2}$, $9.77 \ \text{m s}^{-2}$
10. Velocidad de la luz en el vacío: $299 \ 792 \ 458 \ \text{m s}^{-1}$, $299 \ 792.458 \ \text{km s}^{-1}$
11. Constante gravitacional Newtoniana: $6.674 \ 30 \times 10^{-11} \ \text{m}^3\text{ kg}^{-1}\text{ s}^{-2}$
12. Constante de Planck reducida por la velocidad de la luz en el vacío: $197.326 \ 980 \ 4 \ \text{MeV fm}$
13. Permitividad eléctrica en el vacío (cantidad sin error): $8.854 \ 187 \ 812 \ 8 \times 10^{12} \ \text{F m}^{-1}$
14. Permitividad eléctrica en el vacío: $8.854 \ 187 \ 8128(13) \times 10^{12} \ \text{F m}^{-1}$[^error]

[^error]: En esta cantidad física se usa una forma de notación de la incertidumbre que corresponde, en este caso, a poner entre paréntesis la incertidumbre de las dos cifras menos significativas.

+++

(subsec-unidades)=
## Cantidades físicas con sus unidades de medida

A lo largo de este libro las unidades de medida aceptadas como correctas son las del sistema internacional de unidades (SI), que se deriva del frances *Le Systéme International d´Unités*. En dicho sistema se diferencian dos tipos de unidades: las unidades básicas, que se encuentran en la {numref}`SI-basicas`, y las unidades derivadas como la velocidad o fuerza (en la {numref}`SI-derivadas` se pueden observar algunos ejemplos). Una lista más completa se encuentra en el capítulo 4 de {cite}`Thompson2008` o en la [versión HTML](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-4-two-classes-si-units-and-si-prefixes).

```{list-table} Tabla unidades SI básicas.
:header-rows: 1
:name: SI-basicas
* - Cantidad física
  - Símbolo
  - Nombre
* - Longitud
  - m
  - metro
* - Masa
  - kg
  - kilogramo
* - Tiempo
  - s
  - segundo
* - Corriente eléctrica
  - A
  - amperio
* - Temperatura termodinámica
  - K
  - kelvin
* - Cantidad de sustancia
  - mol
  - mol
* - Intensidad luminosa
  - cd
  - candela
```


```{list-table} Tabla unidades SI derivadas.
:header-rows: 1
:name: SI-derivadas
* - Cantidad física
  - Nombre 
  - Unidades SI básicas
  - Símbolo especial
* - Velocidad
  - metros por segundo
  - $\text{m}\cdot\text{s}^{-1}$
  - 
* - Fuerza
  - newton
  - $\text{m}\cdot\text{kg}\cdot\text{s}^{-2}$
  - N
* - Frecuencia
  - hertz
  - $\text{s}^{-1}$
  - Hz
```


Sobre otras unidades de medida que están por fuera del sistema SI pero que son aceptadas, y sobre las unidades de medida que no son aceptadas y de las cuales se recomienda su desuso, se puede encontrar más información en el capítulo 5 de {cite}`Thompson2008` y en la [versión HTML](https://www.nist.gov/pml/special-publication-811/nist-guide-si-chapter-5-units-outside-si). 

Las reglas básicas para la notación de cantidades físicas con sus unidades de medida son:


* El símbolo de las unidades siempre se separa un espacio del valor numérico y se escribre con letra tipográfica "redonda"[^letra]:
```{list-table}
:header-rows: 1
* - Correcto
  - Incorrecto
* - $54 \ \text{m}$
  - $54m$
```
```{note}
La única excepción con respecto al espacio entre el valor numérico y la unidad es el caso del reporte de un ángulo plano en grados, minutos y segundos: °, ´, ´´, respectivamente. En este caso se reportaría el valor de un ángulo como 76°12´5´´, sin dejar espacios.
```

[^letra]: La letra "redonda" es la forma básica que se usa normalmente en los textos, no es "cursiva". Mas sobre el tema en [texnia](http://www.texnia.com/styles.html#:~:text=La%20letra%20redonda%20es%20la,v%C3%A9ase%20Uso%20de%20la%20redonda).

* Las unidades siempre se escriben en singular y el punto sólo se pone por ortografía:
```{list-table}
:header-rows: 1
* - Correcto
  - Incorrecto
* - $54 \ \text{cm}$
  - $54 \ \text{cms.}$
```

* La multiplicación de unidades se expresa con un punto centrado o con un espacio:
```{list-table}
:header-rows: 1
* - Correcto
  - Incorrecto
* - $54 \ \text{m}\cdot\text{s}^{-1}$  ó  $54 \ \text{m} \ \text{s}^{-1}$
  - $54 \ \text{ms}^{-1}$
```

* La división de unidades se expresa con una "barra", que se traza de arriba hacia abajo, y de derecha a izquierda; si hay varias unidades se usa paréntesis:
```{list-table}
:header-rows: 1
* - Correcto
  - Incorrecto
* - $54 \ \text{m/s}$
  - $54 \ \text{m / s}$
* - $25 \ \text{J/(s m}^{2}\text{)}$
  - $ 25 \ \text{J/s/m}^2 $  
```

* No se pueden mezclar nombres de unidades con símbolos de unidades en una misma expresión
```{list-table}
:header-rows: 1
* - Correcto
  - Incorrecto
* - $7 \ \text{m/s}$
  - $7 \ \text{m/segundo}$
* - $7 \ \text{metros por segundo}$
  - $ 7 \ \text{metros por s} $  
```

* No se pueden usar abreviaciones como por ejemplo, sec para segundo o cc para centímetros cúbicos.

* Otros ejemplos importantes son los casos de adición o multiplicación de valores, o en la presentación de rangos:
```{list-table}
:header-rows: 1
* - Correcto
  - Incorrecto
* - $2 \ \text{m/s} + 3 \ \text{m/s}$ o $(2 + 3) \ \text{m/s}$
  - $2 + 3 \ \text{m/s}$
* - $4 \ \text{cm} \times 5 \ \text{cm}$
  - $4 \times 5 \ \text{cm}$
* - $700 \ \text{nm a} \ 1100 \ \text{nm}$ ó $(700 \ \text{a} \ 1100) \ \text{nm}$
  - $700 \ \text{a} \ 1100 \ \text{nm}$
* - $(20.0, 19.8, 19.9) \ \text{°C}$
  - $20.0, 19.8, 19.9 \ \text{°C}$
* - $20.0 \ \text{°C} \pm 0.2 \ \text{°C}$ ó $(20.0 \pm 0.2) \ \text{°C}$
  - $20.0 \pm 0.2 \ \text{°C}$
```

* El símbolo de porcentaje es aceptado y se debe poner separado un espacio del valor numérico:
```{list-table}
:header-rows: 1
* - Correcto
  - Incorrecto
* - $7\,\%$
  - $7\%$
```

* Dado que el significado de palabras como billón y trillón no está estandarizado, por ejemplo, en Colombia billón es $10^{12}$ mientras que en EE. UU. es $10^{9}$, las palabras "partes por millón (ppm)", "partes por billón (ppb)", o "partes por trillón (ppt)" no se deben usar. En su reemplazo se debe escribir indicando las unidades:
```{list-table}
:header-rows: 1
* - Correcto
  - Incorrecto
* - La incertidumbre es de $8 \ \mu\text{V/V}$
  - La incertidumbre es de $8 \ \text{ppm}$
* - La concentración es de $2 \ \text{ ng/g}$
  - La concentración es de $2 \ \text{ppb}$
* - La concentración es de $2 \ \text{ ng/kg}$
  - La concentración es de $2 \ \text{ppt}$
```  
  
* En los casos en que en una ecuación se deba introducir una variable $V$ en unas unidades específicas $\text{u}$, la notación correcta es $\{V\}_{\text{u}}$. Por ejemplo, en la siguiente expresión la potencia óptica $f$ de la lente en $\text{1/m}$ se obtiene a partir del valor de corriente eléctrica de la lente electro-óptica en unidades de $\text{mA}$:

$$\{f\}_{\text{1/m}} = \frac{1}{0.044\{J\}_{\text{mA}} + 1.52}$$

* Una segunda opción aceptada para las ecuaciones con variables que requieren unidades específicas, pero que no es recomendable para evitar confuciones, es la siguiente:
    
$$\big(f\big/\text{1/m}\big) = \frac{1}{0.044 \big(J\big/\text{mA}\big) + 1.52}$$
