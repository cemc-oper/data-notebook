# cedarkit数据指南

本指南介绍如何使用 cedarkit 工具栈实现对数值天气预报模式数据的加载。

cedarkit 是 CEMC 地球系统数据分析和可视化工具套件 (**C**EMC **E**arth **D**ata **A**nalysis and **R**endering Tool**kit**，cedarkit) 的简称，提供一组 Python 工具集，用于分析地球系统数值预报数据。
该套件基于 Python 科学计算社区的开源工具库开发，并开源发布。

cedarkit 目前正在开发中，包括以下工具库：

- [reki](https://github.com/cemc-oper/reki)：气象数据准备工具库
- [cedarkit-comp](https://github.com/cemc-oper/cedarkit-comp)：气象数据计算工具库
- [cedarkit-maps](https://github.com/cemc-oper/maps)：气象数据绘图工具库

本指南以 CMA 超算平台上的数值天气预报业务系统数据为例，介绍如何使用 reki 及相关工具库来加载模式数据。

```{note}
本文所有代码均在 CMA 超算平台子系统 1 (CMA-HPC2023-SC1) 上运行，直接使用超算平台上的业务系统数据进行测试。

如果想在其他环境中运行，需要修改数据访问部分的代码，将在数据来源章节详细介绍。
```
