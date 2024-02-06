# Notas de Física experimental

```{figure} logo.png
```

(sec-prefacio)=
## Prefacio

Por el año 2010, en los albores de la década, el Instituto de Física de la Universidad de Antioquia se había embarcado en una transformación curricular, con el objetivo de actualizar el programa de física a los retos que presentaba el nuevo milenio. Es así como bajo el liderazgo del profesor Oscar Arnache se diseñó y comenzó a implementar una transformación completa de los cursos experimentales. Dicha transformación no se limitaba a una reorganización de los contenidos, sino que contemplaba un cambio de paradigma con respecto al papel que dichos cursos venían cumpliendo en el programa de física. Hasta entonces, la mayoría de los cursos experimentales eran de tipo demostrativo de los conceptos y leyes  estudiados en los cursos teórico, dejando en segundo plano el manejo de instrumentos de medida, la comunicación de resultados experimentales, y en particular, el análisis de la incertidumbre. Con la transformación, el nuevo objetivo primordial de los cursos experimentales era enseñar a los estudiantes los conceptos básicos para el diseño y realización de experimentos, el ánalisis de los resultados, incluyendo el ánalisis de la incertidumbre, y el reporte y comunicación de los resultados. Este cambio dejó a los cursos sin un texto guía de análisis de la incertidumbre, que sirviera tanto para el aprendizaje como de consulta. En los siguientes años comencé a escribir algunos borradores de guías en lenguaje Python que además de presentar los conceptos, permitieran la interacción de los estudiantes a partir de la simulación de experimentos o el procesamientos de datos experimentales. Surge entonces la idea de crear un texto, basado en lenguaje Python, que sirviera de texto guía para el análisis de la incertidumbre a todos los cursos básicos experimentales del Instituto de Física. En mayo de 2022 la Universidad me otorgó un año sabático con el objetivo de escribir el borrador de dicho texto guía, el cuál ha culminado con la primera versión de las notas de física experimental en mayo de 2023.

El libro está pensado para ir escalando en rigurosidad a medida que el estudiante avanza en su programa de física y astronomía. Para ello, se ha dividido en tres volúmenes que comprenden nueve capítulos. El primer volumen está concebido de tal forma que contiene el mínimo necesario para realizar un análisis de incertidumbre de datos experimentales, con énfasis en sensibilizar al estudiante sobre la importancia y relevancia que tiene la experimentación en cualquier área de estudio. El nivel de matemáticas necesario es básico, pensando que los estudiantes no han visto cursos de cálculo. El segundo volumen, presenta el análisis de la incertidumbre de manera rigurosa, haciendo énfasis en las demostraciones más importantes, y entrega al estudiante nuevas herramientas para un mejor análisis de los datos experimentales. El nivel matemático de este volumen requiere de cálculo diferencial e integral. El volumen tres es un compendio de herramientas complementarias en el análisis de la incertidumbre, que permiten la extracción de información mas valiosa y confiable de los datos experimentales.

A diferencia de los textos guías habituales, en estas notas he cambiado el esquema de interacción entre el libro y el lector, con el objetivo de propender una interacción más dinámica, como creo deben de ser los libros del futuro. Es por esto que el libro está escrito en formato `html` usando la plataforma [Jupyter Book](https://jupyterbook.org) {cite}`executable_books_community_2020_4539666`, que integra una serie de herramientas en el ecosistema de `Python` para la publicación de documentos en línea, permitiendo la integración de código Python en el texto. La idea es que las notas estén a disposición de toda la comunidad en forma de *página web* que pueda ser consultada en cualquier momento. No obstante, es posible tener una versión `pdf` del libro, pero su potencial se desperdicia.

Estas notas son una primera versión, por lo que a futuro espero complementar el volumen tres con más herramientas, así como escribir un volumen cuatro con conceptos avanzados para aquellos que quieran profundizar en el análisis de la incertidumbre experimental.

Agradezco a todos aquellos que contribuyeron a lograr llevar a buen término la escritura de estas notas, en especial a mi padre quien me ayudó a mejorar la redacción, a Carlos Parra quien se tomó el tiempo de leer y hacer comentarios valiosos, y a Alejandro Mira por sus sugerencias con respecto al contenido. A todos, muchas gracias.

--- Edgar Rueda, mayo 2023


+++

---

+++


>Este libro se lo dedico a todos aquellos átomos que se organizaron de tal forma que permitieron la existencia de mi familia y amigos.

+++

---

+++

(sec-introGeneral)=
## Introducción

En el siglo 16 un eriduto de apellido Copernico se atrevió a proponer que la Tierra giraba alrededor del Sol, cuando para la época era aceptado que el Sol y los demás cuerpos celestes giraban alrededor de la Tierra, mientras que las estrellas a una gran distancia, permanecían estáticas en una esfera. El movimiento relativo medido experimentalmente de los cuerpos celestes no podía sanjar cuál teoría era la correcta, porque ambas teorías daban cuenta del movimiento. No obstante, para la época era bien conocida la técnica de paralaje[^paralaje]. De ser cierta la teoría de Copérnico, las medidas experimentales de paralaje mostrarían que la posición relativa de las estrellas mas cercanas con respecto a las más lejanas, cambiaría a medida que la Tierra girase alrededor del Sol. El astronomo Tycho Brahe, quien había hecho las medidas más precisas para la época de la posición de las estrellas, realizó el experimento sin detectar ningún movimiento por paralaje, concluyendo que contrario a lo dicho por Copérnico, la Tierra no se movía. El experimento de Tycho Brahe no necesariamente era erróneo, pero no era lo suficientemente preciso como para medir las pequeñisimas variaciones angulares que ocurrían con el paralaje, puesto que las estrellas están extremadamente distantes. Hubo que esperar a 1838 para tener la precisión suficiente en la medición de los ángulos, permitiendo al astrónomo alemán, Friedrich Bessel, detectar el paralaje de las estrellas del sistema 61 Signy, ubicándolas a $10.3$ años-luz, errando en tan sólo un $10\,\%$ del valor actualmente aceptado. Mas recientemente, el descubrimiento en 1998 de que el universo no solamente se está expandiendo, sino que también dicha expansión se está acelerando, llevó a la necesidad de medir con la mayor precisión posible dicha aceleración, conocida como la constante de Hubble $H_o$. Las medidas hechas hasta el momento se pueden organizar en dos grupos: el primer grupo calcula la constante usando la teoría más avanzada que se tiene hasta el momento, $\Lambda CDM$, a partir de la información que se tiene del universo primigenio: obteniendo un valor cercano a $67.4$ kilómetros por segundo por megaparsec. El segundo grupo usa el método de la escalera de distancia, que comienza con la medición de paralaje de las estrellas más cercanas: obteniendo resultados cercanos a $73.3$ kilómetros por segundo por megaparsec. El problema, es que ambas mediciones tienen una precisión lo suficientemente buena como para concluir que discrepan. Esto básicamente significa que el modelo $\Lambda CDM$ está incompleto, y por lo tanto hay nueva física por descubrir. Pero la historia no termina allí, pues recientemente otro grupo, usando un método basado en el estudio de estrellas gigantes rojas encontró el valor de $69.8$, que no coincide con ninguno de los anteriores, pero que tiene una incetidumbre tal que no permite concluir. Luego el debate sigue abierto, y la consigna es realizar más y mejores mediciones de la constante antes de decidir si hay nueva física por descubrir. Cómo este, hay muchos ejemplos en al historia antigua y reciente de la ciencia, en la cuál el experimento juega un papel preponderante [^QM].

[^paralaje]: La técnica de paralaje se basa en observar un objeto distante desde dos puntos distintos cuya distancia de separación se conoce. En cada posición se mide el ángulo que forma el objeto con respecto a un punto distante, para luego usando trigonometría determinar la distancia a la que se encuentra el objeto. Usted puede experimentar el paralaje ubicando un lapiz cerca a sus ojos, y observando como este se mueve con respecto al fondo, al observarlo con un solo ojo a la vez.

[^QM]: Los artículos completos sobre esta historia se pueden encontrar en Quanta Magazine: ["Astronomers get their wish, and a cosmic crisis get worse"](https://www.quantamagazine.org/astronomers-get-their-wish-and-the-hubble-crisis-gets-worse-20201217/) y ["Cosmologist debate how fast the space is expanding"](https://www.quantamagazine.org/cosmologists-debate-how-fast-the-universe-is-expanding-20190808/).

Desde el advenimiento de la ciencia moderna la teoría y la experimentación han mantenido una relación simbiótica e interdependiente. No obstante, mientras que la teoría puede ser arriesgada haciendo uso de una creatividad sin límites, la experimentación, en su papel de juez supremo, no puede correr riesgos en sus deliberaciones, pues sus juicios de verdad siempre estarán cargados de una gran responsabilidad.

La física, y en general todas las ciencias naturales, se apoyan en la experimentación para la validación de sus teorías y predicciones. El experimento se convierte en el juez supremo que refuta o apoya una idea o forma de entender el universo en el que vivimos. Tan importante tarea nos obliga a realizar nuestros experimentos de la manera más correcta posible con el objeto de evitar juicios de error subjetivos o surgidos de errores humanos o experimentales. Como experimentalistas debemos hacer entonces todo lo posible por realizar los mejores experimentos y aceptar de forma humilde las limitaciones en las conclusiones que se pueden sacar de los resultados obtenidos.

En los siguientes capítulos y secciones, se pretende ofrecer al lector las herramientas y conceptos básicos que le permitan analizar y reportar de forma correcta los resultados de un experimento.


+++

## Tabla de contenidos

```{tableofcontents}
```
