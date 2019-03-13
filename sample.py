# :)
from stagesep2 import VideoManager, AnalysisRunner, OCRConfig


# 添加待测视频
video = VideoManager.add('./videos/demo.mp4')

# 添加match template的样本图
video.template_manager.add('./pictures/amazon.jpg')
video.template_manager.add('./pictures/chrome.jpg')

# 设定语言（这里与官方配置语法是一致的）
# 默认 eng+chi_sim （英文+简体中文，可根据自身需要修改）
OCRConfig.lang = 'eng+chi_sim'

# 启动分析
result1 = AnalysisRunner.run()

# 分析的结果（dict）
dict_data = result1.data

# 或者输出到文件内（json）
result1.export('./result1.json')

# 绘制结果报告
result1.draw('./result_report1.html')
