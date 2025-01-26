# comfyui-api-util
comfyui api calling tool/comfyui api 调用工具
# comfyui api document
https://kakaclo.gitbook.io/kakclo-open-wiki/comfyui/comfyui-api-documentation
# simple example
```py
from comfyui_api import ComfyUIUtil
# create ComfyUIUtil instance
comfy_ui = ComfyUIUtil("http://10.0.0.36:8188")

# 获取 prompt 队列剩余/Get the remaining prompt queue
try:
    queue_remaining = comfy_ui.get_system_stats()
    print(queue_remaining)
except Exception as e:
    # 判断是否是超时异常/Determine whether it is a timeout exception
    if isinstance(e, requests.exceptions.Timeout):
        print("The request timed out, please check the network connection")
    else:
        # 其他异常/Other abnormalities
        print(f"Error: {e}")
    exit()

# Submit prompt
prompt_data = {
    "client_id": "ff4e1f1eb0294c559126fddbfb4df8fa",
    "prompt": {
        # ... 提示数据 ...
    }
}
response = comfy_ui.submit_prompt(prompt_data)  
print(response)

response = comfyUIUtil.get_history_single(reponse["prompt_id"])
print(response)
# 查看结果/View Results
result = comfy_ui.view_result("ComfyUI_03600_.png")
print(result) 
```
For more methods, please see the documentation https://kakaclo.gitbook.io/kakclo-open-wiki/comfyui/comfyui-api-documentation
