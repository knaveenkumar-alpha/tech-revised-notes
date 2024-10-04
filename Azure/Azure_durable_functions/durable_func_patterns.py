"""
Def Durable Function:
====================
Durable Functions is an extension of Azure Functions that lets you write stateful functions in a serverless
compute environment. The extension lets you define stateful workflows by writing orchestrator functions and stateful
entities by writing entity functions using the Azure Functions programming model. Behind the scenes, the extension
manages state, checkpoints, and restarts for you, allowing you to focus on your business logic.

Application patterns The primary use case for Durable Functions is simplifying complex, stateful coordination
requirements in serverless applications. The following sections describe typical application patterns that can
benefit from Durable Functions:

Function chaining
Fan-out/fan-in
Async HTTP APIs
Monitoring
Human interaction
Aggregator (stateful entities)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Pattern #1: Function chaining:
=============================
In the function chaining pattern, a sequence of functions executes in a specific order.
In this pattern, the output of one function is applied to the input of another function.

A diagram of the function chaining pattern
          ---          ----            ----
  f1 ==> |  |  ==> f2 |   | == f3 ==> |   | ==> f4
         ---          ----            ----

You can use Durable Functions to implement the function chaining pattern concisely as shown in the following example.

In this example, the values F1, F2, F3, and F4 are the names of other functions in the same function app. You can
implement control flow by using normal imperative coding constructs. Code executes from the top down. The code can
involve existing language control flow semantics, like conditionals and loops. You can include error handling logic
in try/catch/finally blocks.

Pattern #2: Fan out/fan in:
==========================
In the fan out/fan in pattern, you execute multiple functions in parallel and then wait
for all functions to finish. Often, some aggregation work is done on the results that are returned from the functions.

A diagram of the fan out/fan pattern

With normal functions, you can fan out by having the function send multiple messages to a queue. Fanning back in is
much more challenging. To fan in, in a normal function, you write code to track when the queue-triggered functions
end, and then store function outputs.

The Durable Functions extension handles this pattern with relatively simple code:

The fan-out work is distributed to multiple instances of the F2 function. The work is tracked by using a dynamic list
of tasks. Task.WhenAll is called to wait for all the called functions to finish. Then, the F2 function outputs are
aggregated from the dynamic task list and passed to the F3 function.

The automatic checkpointing that happens at the await call on Task.WhenAll ensures that a potential midway crash or
reboot doesn't require restarting an already completed task.

 Note:
In rare circumstances, it's possible that a crash could happen in the window after an activity function completes but
before its completion is saved into the orchestration history. If this happens, the activity function would re-run
from the beginning after the process recovers.

Pattern #3: Async HTTP APIs:
===========================
The async HTTP API pattern addresses the problem of coordinating the state of long-running operations with external
clients. A common way to implement this pattern is by
having an HTTP endpoint trigger the long-running action. Then, redirect the client to a status endpoint that the
client polls to learn when the operation is finished.

A diagram of the HTTP API pattern

Durable Functions provides built-in support for this pattern, simplifying or even removing the code you need to write
to interact with long-running function executions. For example, the Durable Functions quickstart samples (C# and
JavaScript) show a simple REST command that you can use to start new orchestrator function instances. After an

instance starts, the extension exposes webhook HTTP APIs that query the orchestrator function status.

The following example shows REST commands that start an orchestrator and query its status. For clarity, some protocol
details are omitted from the example.

Because the Durable Functions runtime manages state for you, you don't need to implement your own status-tracking
mechanism.

The Durable Functions extension exposes built-in HTTP APIs that manage long-running orchestrations. You can
alternatively implement this pattern yourself by using your own function triggers (such as HTTP, a queue,
or Azure Event Hubs) and the orchestration client binding. For example, you might use a queue message to trigger
termination. Or, you might use an HTTP trigger that's protected by an Azure Active Directory authentication policy
instead of the built-in HTTP APIs that use a generated key for authentication.

For more information, see the HTTP features article, which explains how you can expose asynchronous, long-running
processes over HTTP using the Durable Functions extension.


Pattern #4: Monitor
The monitor pattern refers to a flexible, recurring process in a workflow. An example is polling until specific
conditions are met. You can use a regular timer trigger to address a basic scenario, such as a periodic cleanup job,
but its interval is static and managing instance lifetimes becomes complex. You can use Durable Functions to create
flexible recurrence intervals, manage task lifetimes, and create multiple monitor processes from a single orchestration.

An example of the monitor pattern is to reverse the earlier async HTTP API scenario. Instead of exposing an endpoint
for an external client to monitor a long-running operation, the long-running monitor consumes an external endpoint,
and then waits for a state change.

A diagram of the monitor pattern

In a few lines of code, you can use Durable Functions to create multiple monitors that observe arbitrary endpoints. The
monitors can end execution when a condition is met, or another function can use the durable orchestration client to
terminate the monitors. You can change a monitor's wait interval based on a specific condition (for example,
exponential backoff.)

The following code implements a basic monitor:


When a request is received, a new orchestration instance is created for that job ID. The instance polls a status until
a condition is met and the loop is exited. A durable timer controls the polling interval. Then, more work can be
performed, or the orchestration can end. When nextCheck exceeds expiryTime, the monitor ends.

Pattern #5: Human interaction:
==============================
Many automated processes involve some kind of human interaction. Involving humans in an automated process is tricky
because people aren't as highly available and as responsive as cloud services. An automated process might allow for this
 interaction by using timeouts and compensation logic.

An approval process is an example of a business process that involves human interaction. Approval from a manager might
be required for an expense report that exceeds a certain dollar amount. If the manager doesn't approve the expense
report within 72 hours (maybe the manager went on vacation), an escalation process kicks in to get the approval from
someone else (perhaps the manager's manager).

A diagram of the human interaction pattern

You can implement the pattern in this example by using an orchestrator function. The orchestrator uses a durable timer
 o request approval. The orchestrator escalates if timeout occurs. The orchestrator waits for an external event, such
 as a notification that's generated by a human interaction.

These examples create an approval process to demonstrate the human interaction pattern:



"""