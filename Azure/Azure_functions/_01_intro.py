"""
Azure Functions:
===============
Azure functions lets you develop serverless applications on Microsoft Azure. You can write just the code you need
for the problem at hand, without worrying about a whole application or the infrastructure to run it.

After completing this module, you'll be able to:
* Explain functional difference between Azure Functions, Azure Logic Apps, and WebJobs
* Describe Azure Functions hosting plan options
* Describe how Azure Functions scale to meet business needs.

DISCOVER AZURE FUNCTIONS:
------------------------
1. Azure functions are a great solution for processing data, integrating systems, working with the internet-of-things
 IOT, and building simple APIs and Microservices.
2. Functions for tasks like image or order processing, file maintenance, or for any tasks that you want to run on
 a schedule. Functions provides templates to get you started with key scenarios.
3. Azure Functions support TRIGGERS, which are ways to start execution of your code, and BINDINGS, which are ways
 to simplify coding for input and output data. There are other integration and automation service in Azure and they
 all can solve integration problems and automate business processes. They call all define input , actions, conditions,
 and output.

COMPARE AZURE FUNCTIONS AND AZURE LOGIC APPS:
--------------------------------------------
1. Both Functions and Logic Apps enable serverless workloads. Azure funcs. is a serverless compute service, whereas
Azure Logic Apps provides serverless workflows.
2. Both can create complex Orchestrations. An Orchestration is a collection of functions or steps, called Actions in
Logic Apps, that are executed to accomplish a complex task.
3. For Azure functions, you develop orchestrations by writing code and using the DURABLE FUNCTIONS extension. For Logic
Apps, you crate orchestrations by using a GUI or editing configuration files.
4. You can mix and match service when you build an orchestration, calling functions from logic apps and calling logic
apps from functions.
-------------------------------------------------------------------------------------------------------------------
                        AZURE FUNCTIONS                                 AZURE LOGIC APPS
--------------------------------------------------------------------------------------------------------------------
Development    Code-first(imperative)                        Designer-first(declarative)
Connectivity   About a dozen built-in binding types,         Large collection of connections,Enterprise Integration Pack
               write code for custom bindings                for B2B scenarios, Build custom connectors
Actions        Each activity is an Azure func; write         Large collection of ready-made actions
               code for activity functions
Monitoring     Azure Applications Insights                   Azure portal, Azure Monitor logs
Management     REST API, Visual Studio                       Azure portal, REST API, powershell, Visual Studio

Execution
Context        Can run locally or in the cloud               Supports Run-anywhere scenarios
------------------------------------------------------------------------------------------------------------------------

COMPARE AZURE FUNCTIONS AND WEBJOBS:
-----------------------------------
like Azure functions, Azure Apps Service Webjobs with the WebJobs SDK is a code-first integration service that is
designed for developers.Both are built on Azure App Service and support features such as source control integration,
authentication, and monitoring with Application Insights integration.

Azure functions is built on the WebJobs SDK, so it shares many of the same event triggers and connections to other
Azure services. Here are some factors to consider when you're choosing between Azure Functions and WebJobs with the
WebJobs SDK.

SCALE AZURE FUNCTIONS:
---------------------
In the Consumption and Premium plans, Azure Functions scales CPU and memory resource by adding additional instance
of the Functions host. The number of instances is determined on the number of events that trigger a function.

Each instance of the Functions host in the Consumption plan is limited to 1.5 GB of memory and one CPU. An instance
of the host is the entire function app, meaning all functions within a function app share resource within an instance
and scale at the same time. Function apps that share the same Consumption plan  independently.

"""