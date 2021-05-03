先启动selenium的docker容器：

```bash
$ docker run -d -p 4444:4444 --shm-size=2g selenium/standalone-chrome:3.141.59-titanium
```

然后运行pipenv环境：

```bash
$ pipenv shell
```

然后执行代码：

```bash
$ python helloworld.py
```
