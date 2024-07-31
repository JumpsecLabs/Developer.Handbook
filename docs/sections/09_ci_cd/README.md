# Continious Integration & Continious Deployment (CI/CD)

![Docker pipeline](/images/docker-container-pipeline.png)

## CI/CD Pipelines
- Secrets must be stored in a Vault, not as environment variables


## Deployment Strategies

- Any merge into `main` branch must trigger an automatic deployment

- Only Jumpsec approved images are stored in a private registry

- Only Jumpsec approved images are used for working in production

- Every container must be slimmed down to the bare minimum 
  - Look into [Slim on Github](https://github.com/slimtoolkit/slim)

- Containers must be checked for vulnerabilities
  - Look into [Trivy on Github](https://github.com/aquasecurity/trivy)
