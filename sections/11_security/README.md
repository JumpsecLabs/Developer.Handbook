# Security Practices

## Secure Coding Guidelines

### Python

- use f-Strings

- use an ORM instead of hand written SQL queries

- run [trivy](https://github.com/aquasecurity/trivy) locally

```
trivy.exe fs <folder_name>
```


## Data Protection

- don't commit secrets to git, use .env file locally, use vault in deployment

You can check this also with [detect-secrets](https://github.com/Yelp/detect-secrets)