
# Proyecto integracion

Proyecto de integracion continua usando docker y jenkins


## Run Locally

Clone the project

```bash
  git clone https://github.com/JohnSanchez92/proyectoIntegracion.git
```

Go to the project directory

```bash
  cd proyectointegracion
```

Start the project

```bash
  docker compose -f docker-compose.yml up --build
```

Solve docker error in jenkins

```bash
  docker exec -it proyectointegracion-jenkins-1 bash
  apt-get update && apt-get install -y \
    docker.io \
    docker-compose 
```

