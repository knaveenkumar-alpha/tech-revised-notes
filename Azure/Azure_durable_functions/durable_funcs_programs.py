#  ############### Function Chaining  ####################  #

import azure.functions as func
import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    x = yield context.call_activity('F1', None)
    y = yield context.call_activity('F2', x)
    z = yield context.call_activity('F3', y)
    result = yield context.call_activity('F4', z)
    return result


main = df.Orchestrator.create(orchestrator_function)


#  ############### Fan-out/Fan-in  ####################  #

import azure.durable_functions as df


def orchestrator_function(context: df.DurableOrchestrationContext):
    # Get a list of N work items to process in parallel
    work_batch = yield context.call_activity('F1', None)
    parallel_tasks = [context.call_activity('F2', b) for b in work_batch]
    output = yield context.task_all(parallel_tasks)

    # Aggregate all N outputs and send the result to F3
    total = sum(output)
    yield context.call_activity('F3', total)


main1 = df.Orchestrator.create(orchestrator_function)


#  ############### Async HTTP APIs  ####################  #

"""
> curl -X POST https://myfunc.azurewebsites.net/api/orchestrators/DoWork -H "Content-Length: 0" -i
HTTP/1.1 202 Accepted
Content-Type: application/json
Location: https://myfunc.azurewebsites.net/runtime/webhooks/durabletask/instances/b79baf67f717453ca9e86c5da21e03ec

{"id":"b79baf67f717453ca9e86c5da21e03ec", ...}

> curl https://myfunc.azurewebsites.net/runtime/webhooks/durabletask/instances/b79baf67f717453ca9e86c5da21e03ec -i
HTTP/1.1 202 Accepted
Content-Type: application/json
Location: https://myfunc.azurewebsites.net/runtime/webhooks/durabletask/instances/b79baf67f717453ca9e86c5da21e03ec

{"runtimeStatus":"Running","lastUpdatedTime":"2019-03-16T21:20:47Z", ...}

> curl https://myfunc.azurewebsites.net/runtime/webhooks/durabletask/instances/b79baf67f717453ca9e86c5da21e03ec -i
HTTP/1.1 200 OK
Content-Length: 175
Content-Type: application/json

{"runtimeStatus":"Completed","lastUpdatedTime":"2019-03-16T21:20:57Z", ...}
"""

#  ############### Monitor ####################  #

import azure.durable_functions as df
import json
from datetime import timedelta


def orchestrator_function(context: df.DurableOrchestrationContext):
    job = json.loads(context.get_input())
    job_id = job['jobId']
    polling_interval = job['pollingInterval']
    expiry_time = job['expiryTime']

    while context.current_utc_datetime < expiry_time:
        job_status = yield context.call_activity('GetJobStatus', job_id)
        if job_status == "Completed":
            #  Perform an action when a condition is met
            yield context.call_activity('SendAlert', job_id)
            break

        #  Orchestration sleeps until this time.
        next_check = context.current_utc_datetime + timedelta(seconds=polling_interval)
        yield context.create_timer(next_check)
    # Perform more work here, or let the Orchestration end.


main2 = df.Orchestrator.create(orchestrator_function)


