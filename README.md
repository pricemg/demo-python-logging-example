# Python logging example

A demonstration of how to use the python `logging` module across a main and
sub module. In this example the logging level verbosity is set at the entry
point. 

Also included is a custom log level (`dev`) that sits between the `info` and
`debug` levels (integer value `15`). To enable this level, the module
containing the `log_dev` setup should be imported (and not necessarily have any
functions called).

```python
>>> python3.9 main.py

2022-11-23 12:59:47 INFO utils.talk: hello world 👋
2022-11-23 12:59:47 DEV utils.talk: hello heaven - here is some more info 😇
2022-11-23 12:59:47 DEBUG utils.talk: 
    hello behind the curtain 
    here is a big dump of debug things 
    🛠 ⚙️ 🪛 🪚 🗜 ⛏ 🪓 🧰 🔩 ✏️ 🔧 🔨
    
2022-11-23 12:59:47 ERROR utils.talk: HELLO HELL 👹
NoneType: None
Traceback (most recent call last):
  File "logging_example/main.py", line 33, in <module>
    run()
  File "logging_example/main.py", line 17, in run
    talk.hello_hell()
  File "logging_example/utils/talk.py", line 30, in hello_hell
    raise Exception(msg)
Exception: HELLO HELL 👹
```
