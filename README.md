# The IDs Patterns (Los Patrones de los IDs)
This is my solution to one of the questions of the TASA Challenge pre-selection stage. The complete test can be found [here]( https://docs.google.com/document/d/1rI5UzbvUe2KcMefqCgUwZ2qjkS3OQ0Yf3NTL-teiYz4/edit).

The translated question (made by [DeepL](https://www.deepl.com/translator)) is the following:
> Last year, a client classification was performed using a segmentation algorithm and the algorithm was uploaded to the company's Git repository. Last week, they requested a count of how many customers belong to a category. Unfortunately, the segmentation algorithm was uploaded into a branch that no longer exists and was never integrated into the base code. The logic was lost and a customer type column was never saved.
>
> One of the members of the development team recalled that **customer identifiers were created from the type of customer**, and could theoretically be used to recreate the segment they belong to.
>
> The following pattern is found within the identifiers:
> - For type A customers, one character is repeated immediately after another, at least once (e.g. "XX", "111", "22", "77", "aaaaaa") and at least once vowel.
> - For type B customers, there are more upper case letters than lower case letters and/or at least one odd digit.
> - For type C clients, there is at least one of the following character sequences: "jn", "cg", "ar", "mp", "fs" o "ic".
>
> Additionally,
> - A customer cannot belong to more than one segment and the rules are in priority order (i.e. the rule for type A predominates over type B; thus, the customer can only be type B if it is not type A, and can only be type C if it is not type B).
> - If it does not match any pattern, then it is type D.
>
> The task is to determine **how many type A, B, C and D clients exists in the database**. For this question, use the file '`segmentation.txt`' inside the '`data`' folder.

The original question (in spanish) is the following:
> El año pasado se realizó una clasificación de clientes a través de un algoritmo de segmentación y el algoritmo se subió al repositorio Git de la empresa. La semana pasada, solicitaron un conteo de cuántos clientes pertenecen a una categoría. Lamentablemente, el algoritmo de segmentación se subió en una rama que ya no existe y que nunca fue integrada al código base. Se perdió la lógica y nunca se grabó una columna de tipo de cliente.
>
> Uno de los miembros del equipo de desarrollo recordó que **los identificadores de los clientes fueron creados a partir del tipo de cliente**, y que en teoría podrían utilizarse para recrear el segmento al que pertenecen.
>
> Dentro de los identificadores se encuentra el siguiente patrón:
> - Para los clientes tipo A, se repite un carácter justo después de otro, al menos una vez (por ejemplo, "XX", "111", “22”, “77”, “aaaaa”) y al menos una vocal.
> - Para los clientes tipo B, se tienen más letras mayúsculas que minúsculas y/o al menos un dígito impar.
> - Para los clientes tipo C, se tiene al menos una de las siguientes secuencias de caracteres: "jn", "cg", "ar", "mp", "fs" o "ic".
>
> Adicionalmente,
> - Un cliente no puede pertenecer a más de un segmento y las reglas están en orden prioridad (es decir, la regla para tipo A predomina sobre la tipo B; así, el cliente solo puede ser tipo B si es que no es tipo A, y solo puede ser tipo C si es que no es tipo B).
> - Si no cumple con ningún patrón, entonces es tipo D.
>
> La tarea consiste en **determinar cuántos clientes tipo A, B, C y D existen en la base de datos**. Para este problema, utilice el archivo dentro de la carpeta '`data`' llamado '`segmentation.txt`'.
