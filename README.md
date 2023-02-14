# daphne_hang

Steps to reproduce hang:

Make a python3.11 virtual env and install requirements:

    pip install -r requirements.txt

Run node app:

    node server.js

Run Django server using daphne:

    daphne daphne_hang.asgi:application

Call API endpoint that hangs, and cancel it, several times:

    curl --location --request GET 'http://127.0.0.1:8000/api/v1/hang/'
    ^C
    curl --location --request GET 'http://127.0.0.1:8000/api/v1/hang/'
    ^C
    curl --location --request GET 'http://127.0.0.1:8000/api/v1/hang/'
    ^C

Try to call good API endpoint:

    curl --location --request GET 'http://127.0.0.1:8000/api/v1/good/'

You should see the following error:

    2023-02-14 05:01:42,735 WARNING  Application instance <Task pending name='Task-6' coro=<ProtocolTypeRouter.__call__() running at /Users/jessamynsmith/Development/daphne_hang/venv/lib/python3.11/site-packages/channels/routing.py:62> wait_for=<Future pending cb=[_chain_future.<locals>._call_check_cancel() at /Users/jessamynsmith/.pyenv/versions/3.11.0/lib/python3.11/asyncio/futures.py:387, Task.task_wakeup()]>> for connection <WebRequest at 0x108603890 method=GET uri=/api/v1/hang/ clientproto=HTTP/1.1> took too long to shut down and was killed.

At this point, the server is non-responsive and must be killed.
