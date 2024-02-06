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

(sec-unaMedida)=

# Incertidumbre de una única medida

En la {numref}`sec-estimacionIncertidumbre` se vio que para obtener una estimación razonable del valor real de la cantidad física es necesario hacer varias medidas de forma repetida debido a las fluctuaciones inherentes al proceso de medida, o también inherentes al mismo fenómeno físico que se está estudiando. No obstante, en algunas ocasiones se debe hacer la estimación de la incertidumbre a partir de una única medida. 

La primera razón para estimar la incertidumbre a partir de una única medida se presenta cuando luego de realizar varias medidas de la cantidad física la gran mayoría dan el mismo valor. Esto básicamente quiere decir que la resolución del instrumento no tiene la capacidad de dar cuenta de las fluctuaciones que puedan existir, y por tanto la incertidumbre estará directamente relacionada con la resolución del instrumento; a este tipo de incertidumbre se le suele llamar **error instrumental**.

La segunda razón para estimar la incertidumbre a partir de una única medida es la imposibilidad de realizar más de una medida. Esto puede ser debido generalmente a restricciones en el acceso al instrumento o a limitaciones en el tiempo disponible para el experimento. Cómo en este caso no se sabe si la incertidumbre del instrumento prima sobre la incertidumbre debida a las fluctuaciones, se debe evitar en la medida de lo posible.

```{warning}

Las dos propuestas que se presentan a continuación, son formas rápidas de estimar la incertidumbre de una única medida. No obstante, la forma correcta, y aceptada internacionalmente, se presenta en la {numref}`subsec-gum-evaluacion`.

**Recuerde siempre mencionar el razonamiento aplicado para la obtención de este tipo de incertidumbres**.

```

+++

(subsec-unaAnaloga)=
## Escala análoga

Si la lectura del valor entregado por el instrumento se debe hacer sobre una escala análoga, por ejemplo, en las marcas de las divisiones de una regla, se considera que la incertidumbre corresponde a la mitad de una división. Esto es bajo la premisa de que quien realice la lectura es capaz de distinguir que el indicador para la medida está en una de las divisiones o entre dos divisiones. Por ejemplo, usando la imagen de la {numref}`fig-RJ-45-size`, y sabiendo que la distancia entre dos divisiones de la regla es de $1 \ \text{mm}$ (resolución), la lectura hecha en la escala nos da un tamaño para el conector RJ-45 de $24.5 \ \text{mm}$, y por tanto el valor a reportar sería 
$24.5\,\text{mm} \pm 0.5\,\text{mm}$. No obstante, una persona diferente pudo leer el valor $25 \ \text{mm}$, y por tanto reportaría $25.0\,\text{mm} \pm 0.5\,\text{mm}$. Ambas cantidades reportadas son correctas dada la incertidumbre que se tiene.

```{figure} imagenes/RJ-45-size.jpg
:name: fig-RJ-45-size

Tamaño de conector RJ-45. (Derechos libres de Internet).
```

```{note}
En algunas ocasiones el lector tiene la suficiente agudeza visual para dividir en más de dos mitades la separación entre dos marcas, y por lo tanto reportar con una menor incertidumbre.
```

+++

(subsec-unaDigital)=
## Escala digital

Cada vez más instrumentos presentan el valor de la medida en una pantalla digital, por lo que, a menos que el fabricante de información sobre la incertidumbre de una medida, se debe considerar que la incertidumbre corresponde a una unidad del último dígito que aparece en pantalla. La razón primordial para esta aproximación es que no se sabe si el instrumento está truncando o se ha redondeando el último dígito, por lo que tomar como incertidumbre la mitad de la unidad del último dígito podría generar errores en la medida. Bajo esta premisa, el voltaje que se presenta en la {numref}`fig-Lectura-digital` se reportaría como $(9.61 \pm 0.01) \ \text{V}$.

```{figure} imagenes/LecturaResistencia.jpg
:name: fig-Lectura-digital

Valor de voltaje medido con un multímetro.
```

```{warning}
Cuando en un texto se encuentra reportada una cantidad física sin indicar su incertidumbre, se suele estimar la misma como una unidad de la cifra menos significativa. No obstante, en realidad no hay certeza sobre si el autor siguió lo lineamientos que se han establecido aquí, por lo que se debe tener mucho cuidado con la incertidumbre que se le asigne a la cantidad física. **Nunca deje de reportar la incertidumbre en sus resultados**.
```

+++

(subsec-unoEjemplo)=
## Ejemplo

Recordando el ejemplo presentado en la {numref}`sec-estimacionIncertidumbre`, si por alguna razón solo se pudo tomar una medida de tiempo correspondiente a $44 \ \text{cs}$, y sabiendo que la resolución del cronómetro es de $1 \ \text{cs}$, el valor de tiempo a reportar sería $(0.44 \pm 0.01) \ \text{s}$. Note que este valor queda alejado del valor más probable, indicando que el error instrumental es inferior a la incertidumbre generada por otras fluctuaciones, como por ejemplo la reacción del experimentador para activar y desactivar el cronómetro. En este caso fue un *error* tomar una única medida.

En otro caso, suponiendo que el reloj tiene una resolución de $1 \ \text{ds}$, probablemente los valores medidos serían, en decisegundos: 4, 5, 5, 5, 5, 5, 5. Como todos los valores, menos uno, se repiten, el valor a reportar sería $(0.5 \pm 0.1) \ \text{s}$. Este resultado parece satisfactorio, pero su incertidumbre es tan grande que probablemente no sirva para estimar la altura de la mesa.
