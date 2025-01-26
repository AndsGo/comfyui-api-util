from comfyui_api import ComfyUIUtil
# 创建 ComfyUIUtil 实例
comfy_ui = ComfyUIUtil("http://10.0.0.36:8188")

# 获取 prompt 队列剩余
try:
    queue_remaining = comfy_ui.get_system_stats()
    print(queue_remaining)
except Exception as e:
    # 判断是否是超时异常
    if isinstance(e, requests.exceptions.Timeout):
        print("请求超时，请检查网络连接")
    else:
        # 其他异常
        print(f"Error: {e}")
    exit()

# 提交 prompt
prompt_data = {
    "client_id": "ff4e1f1eb0294c559126fddbfb4df8fa",
    "prompt": {
        # ... 提示数据 ...
    }
}
response = comfy_ui.submit_prompt(prompt_data)  
print(response)

# 查看结果
result = comfy_ui.view_result("ComfyUI_03600_.png")
print(result) 
