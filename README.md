# airflow

# pre-commit

```bash
uv pip install pre-commit
```

Add a `pre-commit` configuration by generating a basic `.pre-commit-config.yaml` file using:

```bash
pre-commit sample-config
```

> The full set of options for the configuration are listed [here](https://pre-commit.com/#plugins).

Move the `.pre-commit-config.yaml` file under `config/` and set up the git hook scripts:

```bash
pre-commit install --config config/.pre-commit-config.yaml
```

Now `pre-commit` will run automatically on git commit.


