# :)
from stagesep2 import VideoManager, AnalysisRunner, OCRConfig
import os


# 路径配置
TARGET_VIDEO_PATH = './videos/demo.mp4'
TEMPLATE_AMAZON_PATH = './pictures/amazon.jpg'
TEMPLATE_CHROME_PATH = './pictures/chrome.jpg'
TEMPLATE_CHROME_CLICKED_PATH = './pictures/chrome_clicked.jpg'
JSON_RESULT_PATH = './result1.json'
HTML_RESULT_PATH = './result_report1.html'


# 添加待测视频
video = VideoManager.add(TARGET_VIDEO_PATH)

# 添加match template的样本图
video.template_manager.add(TEMPLATE_AMAZON_PATH)
video.template_manager.add(TEMPLATE_CHROME_PATH)
video.template_manager.add(TEMPLATE_CHROME_CLICKED_PATH)

# 设定语言（这里与官方配置语法是一致的）
# 默认 eng+chi_sim （英文+简体中文，可根据自身需要修改）
OCRConfig.lang = 'eng+chi_sim'

# 启动分析
result1 = AnalysisRunner.run()

# 分析的结果（dict）
dict_data = result1.data

# 或者输出到文件内（json）
result1.export(JSON_RESULT_PATH)

# 绘制结果报告
result1.draw(HTML_RESULT_PATH)

# assert for travis CI
assert os.path.exists(JSON_RESULT_PATH), '{} not existed!'.format(JSON_RESULT_PATH)
assert os.path.exists(HTML_RESULT_PATH), '{} not existed!'.format(HTML_RESULT_PATH)
