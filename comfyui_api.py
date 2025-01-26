import requests
from io import BytesIO
import json
import uuid

class ComfyUIUtil:
    def __init__(self, base_url):
        self.base_url = base_url
        self.timeout = 5  # 设置请求超时时间为5秒

    def get_prompt_queue_remaining(self):
        url = f"{self.base_url}/api/prompt"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def submit_prompt(self, prompt_data:str):
        url = f"{self.base_url}/api/prompt"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=json.dumps(prompt_data, ensure_ascii=False).encode('utf-8'), timeout=self.timeout)
        return response.json()

    def view_result(self, filename:str):
        url = f"{self.base_url}/view?filename={filename}"
        response = requests.get(url, timeout=self.timeout)
        return response.content

    def get_history_list(self, max_items=100):
        url = f"{self.base_url}/api/history?max_items={max_items}"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_history_single(self, history_id:str):
        url = f"{self.base_url}/api/history/{history_id}"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_queue(self):
        url = f"{self.base_url}/api/queue"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_embeddings(self):
        url = f"{self.base_url}/api/embeddings"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_models(self):
        url = f"{self.base_url}/api/models"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_model_configs(self, model_name):
        url = f"{self.base_url}/api/models/{model_name}"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_extensions(self):
        url = f"{self.base_url}/api/extensions"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def upload_image(self, image_path:str):
        url = f"{self.base_url}/api/upload/image"
        files = {'image': open(image_path, 'rb')}
        response = requests.post(url, files=files, timeout=self.timeout)
        return response.json()

    def download_image_to_memory(self, url):
        # 发送 GET 请求以下载图像
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 检查请求是否成功
        
        # 将图像内容加载到 BytesIO 对象中
        file_object = BytesIO(response.content)
        return file_object,response.headers.get('Content-Type', 'application/octet-stream')
    
    def upload_image_url(self, image_url:str):
        url = f"{self.base_url}/api/upload/image"
        # 将 URL 转换为文件对象
        file_object, content_type = self.download_image_to_memory(image_url)
        # 提取文件名（可选）
        filename = uuid.uuid4().hex + '.' + content_type.split('/')[-1]
        files = {'image': (filename, file_object,content_type)}
        response = requests.post(url, files=files, timeout=self.timeout)
        return response.json()
    
    def upload_mask(self, image_path, mask_type, subfolder, original_ref):
        url = f"{self.base_url}/api/upload/mask"
        files = {'image': open(image_path, 'rb')}
        data = {
            'type': mask_type,
            'subfolder': subfolder,
            'original_ref': json.dumps(original_ref)
        }
        response = requests.post(url, files=files, data=data, timeout=self.timeout)
        return response.json()

    def get_system_stats(self):
        url = f"{self.base_url}/api/system_stats"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_model_metadata(self, filename):
        url = f"{self.base_url}/api/view_metadata/checkpoints?filename={filename}"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_all_node_object_info(self):
        url = f"{self.base_url}/api/object_info"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def get_specific_node_object_info(self, node_name):
        url = f"{self.base_url}/api/object_info/{node_name}"
        response = requests.get(url, timeout=self.timeout)
        return response.json()

    def clear_or_delete_queue(self, clear=True, delete_ids=None):
        url = f"{self.base_url}/api/queue"
        data = {
            'clear': clear,
            'delete': delete_ids if delete_ids else []
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=self.timeout)
        return response.json()

    def clear_or_delete_history(self, clear=True, delete_ids=None):
        url = f"{self.base_url}/api/history"
        data = {
            'clear': clear,
            'delete': delete_ids if delete_ids else []
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=self.timeout)
        return response.json()

    def interrupt_current_run(self):
        url = f"{self.base_url}/api/interrupt"
        response = requests.post(url, timeout=self.timeout)
        return response.json()

    def get_settings(self):
        url = f"{self.base_url}/api/settings"
        response = requests.get(url, timeout=self.timeout)
        return response.json()
