# Modulo 5 CI/CD Demo

Demo pequeno para mostrar una promocion automatizada con pruebas:

1. Un cambio se hace en la rama `dev`.
2. GitHub Actions ejecuta pruebas unitarias.
3. Si pasan, se genera un artefacto y se "despliega" a QA.
4. QA ejecuta smoke tests automatizados.
5. Produccion se promueve manualmente desde la pestana Actions.

La aplicacion es intencionalmente simple para que el foco sea el pipeline, no el framework.

## Demo rapido para la clase

### 1. Hacer un cambio que pasa

Edita `src/pipeline_demo/calculator.py` y cambia:

```python
FEATURE_MESSAGE = "Modulo 5: pruebas automatizadas activas"
```

por algo visible, por ejemplo:

```python
FEATURE_MESSAGE = "Modulo 5: cambio aprobado en dev"
```

Luego:

```bash
git checkout dev
git add src/pipeline_demo/calculator.py
git commit -m "demo: update feature message"
git push origin dev
```

En GitHub ve a `Actions` y abre el workflow `Dev to QA`. Veras:

- `unit-tests`
- `deploy-qa`
- `qa-smoke-tests`

### 2. Hacer un cambio que falla

Edita `calculate_total` en `src/pipeline_demo/calculator.py` y cambia:

```python
return round(subtotal * (1 - discount_rate), 2)
```

por:

```python
return subtotal
```

Haz commit y push a `dev`. El pipeline se detiene en pruebas unitarias y no llega a QA.

### 3. Promover a produccion manualmente

Cuando QA esta verde:

1. En GitHub abre `Actions`.
2. Selecciona `Promote to Production`.
3. Clic en `Run workflow`.
4. Selecciona la rama `dev`.
5. Ejecuta.

Ese workflow vuelve a correr pruebas, crea el artefacto de produccion y ejecuta smoke tests.

## Ejecutar localmente

El paquete vive en `src/`, asi que `build_site.py` necesita `PYTHONPATH=src`
para encontrar `pipeline_demo` (igual que en el workflow de CI). `pytest` ya lo
resuelve solo gracias a `pyproject.toml`.

En macOS / Linux (bash):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
PYTHONPATH=src python scripts/build_site.py --environment local --output dist
python scripts/smoke_test.py --environment local --site dist
```

En Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest
$env:PYTHONPATH = "src"
python scripts/build_site.py --environment local --output dist
python scripts/smoke_test.py --environment local --site dist
```

## Estructura

- `.github/workflows/dev-to-qa.yml`: pipeline automatico para `dev`.
- `.github/workflows/promote-production.yml`: promocion manual a produccion.
- `src/pipeline_demo/calculator.py`: codigo facil de cambiar en vivo.
- `tests/test_calculator.py`: pruebas unitarias.
- `scripts/build_site.py`: genera un sitio estatico como artefacto de despliegue.
- `scripts/smoke_test.py`: valida el despliegue por ambiente.
