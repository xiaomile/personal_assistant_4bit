from openxlab.model import download
import os

download(model_repo='xiaomile/personal_assistant_4bit', output='xiaomile')

os.system("lmdeploy convert  internlm-chat-7b /home/xlab-app-center/xiaomile --model-format awq --group-size 128")

os.system("lmdeploy serve gradio /home/xlab-app-center/workspace")
