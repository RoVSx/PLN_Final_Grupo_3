# PLN_Final_Grupo_3
Examen final de PLN
=======
# Clasificador de reclamos municipales

La version oficial del proyecto es un clasificador supervisado entrenado con data historica real usando la columna `prestacion` como entrada y `categoria` como etiqueta.

## Flujo principal

1. Entrenar el modelo con el historico municipal.
2. Guardar el modelo entrenado en `artifacts/supervised_model.joblib`.
3. Clasificar nuevos reclamos con ese modelo.

## Archivos principales

- `entrenar_reclamos.py`: entrena el modelo supervisado
- `clasificar_reclamos.py`: clasifica nuevos CSV con el modelo entrenado
- `src/supervised_classifier.py`: logica compartida de entrenamiento e inferencia
- `requirements.txt`: dependencias necesarias
- `atencion_ciudadana_lima_2023.csv`: dataset historico de entrenamiento
- `ejemplo_reclamos.csv`: archivo de ejemplo para probar inferencia

## Modelo oficial

El modelo usa:

- `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- embeddings normalizados para cada `prestacion`
- `LogisticRegression` de `scikit-learn`
- categorias reales de la columna `categoria`

Categorias detectadas en el historico:

- `Limpieza Pública`
- `Tránsito/Transporte`
- `Otros`
- `Áreas Verdes`
- `Alumbrado Público`
- `Seguridad Ciudadana (Serenazgo)`
- `Ruido/Contaminación sonora`

## Instalacion

```bash
python -m pip install -r requirements.txt
```

## Entrenamiento

```bash
python entrenar_reclamos.py atencion_ciudadana_lima_2023.csv
```

## Inferencia

```bash
python clasificar_reclamos.py ejemplo_reclamos.csv salida_clasificada.csv
```

## Salida

El clasificador conserva todas las columnas originales y agrega:

- `categoria_sugerida`
- `confianza_modelo`
- `requiere_revision`

## Baseline

La version anterior por similitud coseno y el baseline legado quedaron movidos a la carpeta `baseline/` para referencia y comparacion, pero no forman parte del flujo principal.
>>>>>>> c8d5a0c (nuevo)
