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

(sec-errores)=

# Incertidumbres aleatorias y errores sistemáticos

En toda medida experimental hay una incertidumbre inherente a la misma, también conocida como *error*[^errAle], que no se puede eliminar del todo, y que solo se puede esperar reducir a valores que permitan obtener información útil de las mediciones. Dichas incertidumbres se pueden agrupar en dos grandes grupos: **incertidumbres aleatorias** e **errores sistemáticos**.

[^errAle]: Hay que tener cuidado con la palabra "error" porque no quiere decir necesariamente que se esté cometiendo una equivocación. Aún sin cometer ninguna equivocación en la medida experimental es de esperarse que nunca se obtenga exactamente el mismo valor. La palabra correcta debería ser "incertidumbre" o "fluctuación", no obstante, usted debe estar preparado para interpretar la palabra "error" en este contexto porque se suele usar de forma indiscriminada y como sinónimo de "incertidumbre".

+++

(subsec-ErrorAleatorio)=

## Incertidumbre aleatoria

Las incertidumbres aleatorias son las responsables de que las medidas experimentales fluctuen de forma impredecible alrededor del valor real de la cantidad física medida. Que fluctuen aletoriamente indica que no se tiene forma de saber que valor saldrá en cada medida particular, pero por lo menos existirá la certeza de que dichos valores saldrán alrededor de un valor central o promedio. Qué tanto se agrupen o no, alrededor del valor central, indicará la calidad de la medida hecha, es decir su [precisión](subsec-precision). Un ejemplo son las fluctuaciones en la temperatura ambiente, que pueden expandir o contraer la escala de una regla, de forma tal que la medida hecha con esta varía de forma aleatoria. Igualmente, si en una serie de medidas se observa la escala de la regla desde distintos ángulos es posible inducir un error aleatorio en la lectura por paralaje, es decir, la posición del objeto a medir y de la marca en la regla cambian en función del punto desde donde se este observando. Otro ejemplo pueden ser las variaciones en la medida de la potencia de un láser debidas a fluctuciones en la corriente eléctrica suministrada; o incluso, si se logrará eliminar completamente dichas fluctuaciones de la corriente eléctrica, desde el punto de vista del fenómeno de emisión de luz, la emisión de fotones en un intervalo de tiempo no es uniforme, es aletoaria y sigue una [distribución de Poisson](sec-distPoisson). En el ejemplo de la {numref}`subsec-EjemploErrores` podrá observar el efecto de las incertidumbres aleatorias en una medida.

+++

(subsec-ErrorSistematico)=

## Error sistemático
Los errores sistemáticos son aquellos que se repiten sin modificación, por lo que son todo lo contrario a una incertidumbre aleatoria. Esta particularidad es la que hace de este tipo de "incertidumbres" las más complejas de controlar, y que finalmente requeriran de toda la experiencia y habilidad del experimentador para dar cuenta de ellas y así eliminarlas. Como se había dicho, una incertidumbre aleatoria se distribuye alrededor de un valor central que finalmente se espera coincida con el valor real, es decir, las fluctuaciones aleatorias en los valores medidos terminan compensándose. En cambio, un error sistemático siempre generará que las medidas se encuentren alrededor del mismo valor erróneo, por lo que nunca se compensarán, provocando que el valor real y central no coincidan; esto afectará directamente la [exactitud](subsec-exactitud) de la medida. En el ejemplo de la regla, si el experimentador siempre observa la escala desde un mismo punto, el error de paralaje será prácticamente el mismo y por lo tanto no se compensará, lo que generará un desplazamiento del valor de longitud medido respecto al valor real. En el caso de la potencia láser, si nuestro detector está descalibrado, siempre puede asignar, por ejemplo, un valor inferior de potencia a todos los valores medidos, generando un reporte de potencia inferior al real. En el ejemplo de la {numref}`subsec-EjemploErrores` podrá observar el efecto de un error sistemático en una medida.

