from openxlab.model import download
import os
#import subprocess

download(model_repo='xiaomile/ChineseMedicalAssistant_internlm_4bit', output='xiaomile')

os.system("lmdeploy convert  internlm-chat-7b /home/xlab-app-center/xiaomile --model-format awq --group-size 128")

os.system("lmdeploy serve gradio /home/xlab-app-center/workspace --server_name 0.0.0.0 --server_port 7860")

#cmd = "lmdeploy serve api_server /home/xlab-app-center/workspace --server_name 0.0.0.0 --server_port 23333 --instance_num 64 --tp 1"
#subprocess.call(cmd)
#os.system("lmdeploy serve gradio http://0.0.0.0:23333 --server_name 0.0.0.0 --server_port 7860 --restful_api True")
