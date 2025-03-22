from flask import Flask, request, jsonify
from flask_cors import CORS  # 必须添加 CORS 支持
import os

app = Flask(__name__)
CORS(app)  # 允许所有域名跨域访问

@app.route("/")
def home():
    return "Hello from Vercel Python!"

@app.route("/chat", methods=["POST"])
def chat():
    # 获取 JSON 数据并提取问题
    data = request.get_json()
    question = data.get("question", "")
    # 返回模拟回答（替换为你的实际逻辑）
    return jsonify({"answer": f"你问的是：{question}"})

if __name__ == "__main__":
    # 动态获取 Vercel 分配的端口
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
