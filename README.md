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

- `Limpieza Publica`
- `Transito/Transporte`
- `Otros`
- `Areas Verdes`
- `Alumbrado Publico`
- `Seguridad Ciudadana (Serenazgo)`
- `Ruido/Contaminacion sonora`

## Instalacion

```bash
python -m pip install -r requirements.txt