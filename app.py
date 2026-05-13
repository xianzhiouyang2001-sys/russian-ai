import streamlit as st
import base64
import requests

st.set_page_config(page_title="俄语识物助手", page_icon="🇷🇺")
st.title("📸 俄语 AI 识物助手")

# --- 关键：在这里填入你的 API KEY ---
# 如果你现在没有 Key，可以先用这个界面给老师演示“前端效果”
API_KEY = "你的_OPENAI_API_KEY" 

img_file = st.camera_input("请对着物品拍照")

if img_file:
    st.info("AI 正在努力思考中... 请稍后")
    
    # 将图片转为 AI 能看懂的格式
    bytes_data = img_file.getvalue()
    base64_image = base64.b64encode(bytes_data).decode('utf-8')

    # 准备发给 AI 的指令
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "识别图片中的物体，给出它的俄语单词、中文意思，并提供两个地道的俄语生活例句。"},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                ]
            }
        ]
    }

    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    try:
        # 发送给 AI 
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        result = response.json()['choices'][0]['message']['content']
        st.success("识别成功！")
        st.markdown(result)
    except:
        st.error("哎呀，AI 大脑还没连上（API Key 未配置）。")
        st.write("老师，这是我的前端演示原型，目前已完成摄像头调用和界面设计。")

