# Yul_CI-CD


## Description

Repositorio de una aplicación simple hecha **Flask (Python)**. Se trata de una formulario HTML cuya funcionalidad esta hecha con **Python**. Dispone de las siguientes operaciones: (sumar, restar, multiplicar y dividir). La aplicación corre sobre en un clúster de **Kubernetes** mediante **ArgoCD**.
La parte de **CICD** se realiza con **CircleCI** usando un **pipeline ( .yml )**.
Se somete a test con **pytest** y para la cobertura se usa **pytest-cov**. Para el linting de la aplicación se usa **pylint**.
Finalmente se realiza un análisis estático del código mediante SonarCloud.

## Video CI/CD (Loom)

[![Video Demo CI/CD Project](./pics/video.png)](https://www.loom.com/share/995a657881424b2a9f7e53ce24c39c5b)

## Estructura del Repositorio

![Estructura de directorios](./pics/tree_Project.png)

- **Dockerfile**: Instrucciones para crear la imagen Docker.

- **app**: Contiene archivos de la aplicación.

  - **cacl.py**: Código de la app en **Python**
  - **templates/form.html**: Código HTML para visualizar la app.

- **test**: Contiene el archivo para realizar los test en el Pipeline

  - **test.py**

- **argocd**: Contiene archivos para la configuración de ArgoCD.

  - **argoapp.yml** contiene el código para la configuración de ArgoCD
  - **values.yaml** contiene ls configuración para Helm

- **k8s**: Contiene los manifiestos de Kubernetes para en el clúster

  - **deployment.yaml**
  - **ingress.yaml**
  - **service.yaml**

    - **/helm/calcpy**: Contiene archivos para Helm

      - **Chart.yaml**
      - **values.yaml**
      - **templates/**
        - **deployment.yaml**
        - **ingress.yaml**
        - **service.yaml**

- **.circleci**: Contiene el archivo para ejecutar el pipeline en CicleCI.

  - **config.yml**

- **sonar-project.properties**: Contiene la configuración para SonarCloud.

- **requirements.txt**: Contiene los requerimientos para la app

## Calc

### Capturas de pantalla

#### App

![Alt text](./pics/argoCD_calcpy.png)

## CI/CD pipeline

### Capturas de pantalla

![Alt text](./pics/circleCI.png)

![Alt text](./pics/cicleCI_ggShield.png)

![Alt text](./pics/cicleCI_Build.png)

![Alt text](./pics/circleCI_Deploy.png)

![Alt text](./pics/cicleCI_Docs.png)

![Alt text](./pics/cicleCI_Docs_Artifacts.png)

![Alt text](./pics/cicleCI_Docs_1.png)

![Alt text](./pics/cicleCI_Test.png)

![Alt text](./pics/circleCI_Test_Artefacts.png)

![Alt text](./pics/circleCI_Test_Coverage_Report_XML.png)

![Alt text](./pics/circleCI_Test_Coverage_Report.png)

![Alt text](./pics/circleCI_Test_Coverage_Report_HTML.png)

## Capturas de pantalla de DockerHub

> ![Alt text](./pics/dockerHub_image.png)

> ## Nota (DockerHub)
>
> Para poder usar DockerHub dentro del pipeline se ha de meter la contraseña del usuario
>
> ![Alt text](./pics/cicleCI_ENV.png)

> ## Nota (SonarCloud)
>
> Para poder usar SonarCloud se ha de generar un contexto dentro de CircleCI y después generar un token y guardarlo en las variables de entorno del proyecto.
> Se debe de usar una ORB para su funcionamiento. 

> ![Alt text](./pics/cicleCI_Contextspng.png)
> 
> ![Alt text](./pics/cicleCI_ENV.png)
>
> ![Alt text](./pics/sonarCloud.png)
>
> ![Alt text](./pics/sonarCloud_1.png)

> ## Note (GitGuardian)
>
> Para poder usar la herramienta de análisis de vulnerabilidades GitGuardian se ha de utilizar una ORB. 
> Ademas se debe añadir un token generado guardándolo en las variables de entorno de CircleCI.

> ![Alt text](./pics/cicleCI_ENV.png)

![Alt text](images/../pics/ggShield.png)

## ArgoCD

Se va a utilizar ArgoCD para el despliegue de la app.

![Alt text](./pics/argoCD.png)

![Alt text](./pics/argoCD_Resources.png)

![Alt text](./pics/argoCD_calcpy.png)

## Resources app calculator kubernetes

![Alt text](./pics/calc_Resources.png)

## Fuentes

- **Kubernetes**: https://kubernetes.io/es/
- **Helm**: https://helm.sh/
- **Docker**: https://www.docker.com/
- **DockerHub**: https://hub.docker.com/
- **CircleCI**: https://circleci.com/
- **SonarCloud**: https://sonarcloud.io/
- **ArgoCD**: https://argoproj.github.io/argo-cd/
- **GitGuardian**: https://www.gitguardian.com/
- **Python**: https://www.python.org/
- **Flask**: https://flask.palletsprojects.com/en/2.0.x/
- **Pytest**: https://docs.pytest.org/en/6.2.x/
- **Coverage**: https://coverage.readthedocs.io/en/coverage-5.5/
- **Pylint**: https://www.pylint.org/
- **pdoc**: https://pdoc3.github.io/pdoc/
- **ChatGPT**: https://chat.openai.com/