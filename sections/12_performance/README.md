# Performance Optimisation

Even though there are many advanced concepts for optimisations, it must be limited to the resources and common knowledge that is among teams and team members involved 
for specific implementations.

## Best Practices

- Stick to built-in data types and libraries

- limit external dependencies
  - specifically try to avoid dependencies that have a high learning curve or bad documentation

- regularily refactor the code and remove unnecessary code

- more code = more bugs = more maintenance 

- write understandable code

- share knowledge and help others understand

- https://youtu.be/Fot3_9eDmOs?t=50

## Scalability Considerations

- opt for microservices that solve a problem and can be scaled via infrastructure

- design for flexibility, but don't implement the base for the perfect solution first
  - by the a module based solution makes sense the project might have died or changed so much that the inital though process and implementation has become obsolete
  - it is better to work according to the requirements and only when they change to implement the "better solution with more work"

- utilise cloud solutions like Azure

- embrace CI / CD in your project
