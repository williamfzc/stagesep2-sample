# stagesep2-sample

[stagesep2](https://github.com/williamfzc/stagesep2) 的使用示例

# 使用

## 下载 sample

```bash
git clone https://github.com/williamfzc/stagesep2-sample.git
cd stagesep2
```

## 用docker（推荐）

```shell
docker run --rm -v ${PWD}:/root/stagesep2 williamfzc/stagesep2 python sample.py
```

## 常规方法

### 安装本体

使用python3。

```
pip install stagesep2
```

### 安装 tesseract-ocr

参考[官方文档](https://github.com/tesseract-ocr/tesseract/wiki)安装ocr。就常规应用而言，OCR达到的效果是相当好的，推荐使用。

如果不想使用ocr，可以用下列方法将其去除：

```python
from stagesep2 import NormalConfig


NormalConfig.ANALYSER_LIST = ['match_template', 'trend']

# 默认：
# NormalConfig.ANALYSER_LIST = ['ocr', 'match_template', 'trend']
```

### 运行

```bash
python sample.py
```

## 结果处理

在分析结束后，全部的结果会以json的形式导出。比较推荐的做法是通过实际需要，自行编写脚本对json进行收集整理，最后转化成为自己需要的形式。

你也可以通过stagesep2自带的结果图标对结果进行预览。
