# data-notebook

数据分析示例 Jupyter 笔记本。

## 编译

因为使用到 CEMC 业务系统数据产品，需要在 CMA 国家级超算平台子系统 1 中编译。

安装依赖包

```bash
pip install -r requirements.txt
```

编译，会自动运行 jupyter 笔记本

```bash
jupyter-book build docs
```

生成的网站放在 docs/_build/html 目录中

## 浏览

运行 `tool/run_server.py` 在随机端口上运行 Web 服务，例如：

```bash
python data-notebook/tool/run_server.py data-notebook/docs/_build/html
```

输出示例如下：

```
Starting http server...
Please visit http://10.40.150.29:46925
```

使用浏览器打开命令行输出的 URL 网址即可查看生成的文档网站。

## License

Copyright &copy; 2024, developers at cemc-oper.

`data-notebook` is licensed under [Apache License, Version 2.0](./LICENSE)