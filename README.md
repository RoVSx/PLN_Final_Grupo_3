# PLN_Final_Grupo_3
Examen final de PLN
=======
# Clasificador de reclamos municipales con embeddings

Este proyecto contiene un modulo en Python para clasificar reclamos municipales a partir de la columna `prestacion` usando:

- `sentence-transformers`
- el modelo `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- similitud coseno entre cada reclamo y descripciones semanticas de categorias

## Archivos principales

- `clasificador_reclamos.py`: modulo principal y CLI
- `requirements.txt`: dependencias necesarias
- `ejemplo_reclamos.csv`: archivo de entrada de ejemplo con 12 reclamos

## Categorias sugeridas

- `Limpieza publica`
- `Alumbrado publico`
- `Transito`
- `Areas verdes`
- `Ruido`
- `Seguridad`
- `Otros`

Si la mejor similitud es menor al umbral configurado, el script asigna `Otros / Revision manual`.

## Instalacion

```bash
pip install -r requirements.txt
```

## Uso

```bash
python clasificador_reclamos.py ejemplo_reclamos.csv salida_clasificada.csv
```

Tambien puedes ajustar el umbral:

```bash
python clasificador_reclamos.py ejemplo_reclamos.csv salida_clasificada.csv --threshold 0.45
```

## Salida

El script conserva todas las columnas originales y agrega:

- `categoria_sugerida`
- `similitud_maxima`
- `requiere_revision`
>>>>>>> c8d5a0c (nuevo)
