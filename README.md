
# Proyecto integracion

Proyecto de integracion continua usando docker y jenkins


## Run Locally

Clone the project

```bash
  git clone https://github.com/JohnSanchez92/proyectoIntegracion.git
```

Go to the project directory

```bash
  cd my-project
```

Start the project

```bash
  docker compose -f docker-compose.yml -f docker-compose.jenkins.yml up --build
```

