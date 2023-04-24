### Bring your own AI to augment Watson Services

To augment services with AI and applications in general, it is advantageous to be able to agnostically call web services to achieve the desired results. In this TechZone asset, a simple Flask-Python Web Application will be created and deployed on the IBM Cloud using Code-Engine.  The application will demonstrate the ease in which a developer can deploy an application on the IBM Cloud using Code-Engine. Use of Code-Engine allows a developer to focus on their code instead of the complexities associated with deployment.  The development effort is then taken one step further to demonstrate a way to make the code OpenAPI 3.0 specification compliant.  This allows the REST application to be called an “extension”.  Tools such as Watson Assistant and others, allow for business partners and general users to customize and enhance native IBM Watson services to incorporate proprietary algorithms making the IBM service unique and sustainable. 

As an example, imagine that a company has a custom AI model (written in python) to predict the largest loan a person would be qualified to obtain. The company wants to inform prospective clients with the information via Watson Assistant Q&A. Using a variety of factors, the AI produces an amount, and this information is fed back to a person using the Watson Assistant creating a personalized response to the inquiry.

Once the model is deployed, it can be used in several situations, and in combination with other AI algorithms. Such implementations can be integrated into Watson Assistant, Discovery, and several other popular IBM services. Applications may also be used to augment embedded-AI providing the proper level of processing needed to achieve an objective.

# Considerations:
Fast responses to user queries. To address speed, three techniques are leveraged.
1.) Highly available containerized operations
2.) Asynchronous operations where possible
3.) Parallel processing where applicable

In addition to speed, complex and customized operations can be implemented out as well.

# Build – REST Application
In order to realize the objectives, the first order of business is to build a simple REST API that is highly available. This will be done using a Python Flask Web API, and deployed onto the IBM Cloud using Code-Engine. This choice was made because of the rich AI and data processing features offered by the Python platform, and the capabilities of Code-Engine to allow developers to focus on code instead of deployment.

Deploy a simple Flask-Python Web Application using IBM Code Engine
Each part of the build process will include methods to test operations before proceeding to the next section.
This objective consists of 4 parts as illustrated below.

1.) Build a REST API using Python Flask
2.) Build and test a docker container (Postman is an alternative to docker)
3.) Push the container to the IBM Cloud Registry
4.) Deploy and manage the application using Code-Engine
5.) Make application OpenAPI 3.0 Compliant

