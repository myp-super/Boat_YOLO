# 🚤 WTR-System (Water Trash Recovery)
> 基于 YOLOv11 与边缘计算的水面智能清污无人船视觉感知系统

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![YOLOv11](https://img.shields.io/badge/YOLO-v11n-yellow.svg)
![Flask](https://img.shields.io/badge/Flask-Web-lightgrey.svg)
![Embedded](https://img.shields.io/badge/Embedded-Edge_AI-success.svg)
![Hardware](https://img.shields.io/badge/Hardware-STM32-red.svg)

## 🌟 项目简介

WTR-System 是一个面向复杂水域环境的“眼-手-船”协同智能垃圾回收框架。本项目聚焦于 **Embedded + Edge AI** 的深度融合，上层依托轻量级 YOLOv11 算法实现水面浮游垃圾的精准识别，下层通过串口通信与 STM32 嵌入式系统联动，驱动无人船与机械臂完成自动化打捞。

系统内置了轻量级 Web 服务界面，支持跨设备无缝监控，旨在为城市内河治理与智慧水利提供一套低成本、高效率的软硬件协同解决方案。

## ✨ 核心特性

- **🌊 专用水面视觉模型**：基于 3090 张真实水面实测图像训练，覆盖 11 类典型漂浮物，有效克服水面反光与波纹干扰。
- **⚡ 边缘计算优化**：采用 YOLOv11n (Nano) 轻量化架构，兼顾高 mAP 与边缘设备 (如 RDK X3) 上的高帧率推理。
- **🌐 双模态 Web 控制台**：基于 Flask 与推流协议，支持无延迟的摄像头实时监控与本地静态图像上传离线检测。
- **🔌 软硬协同闭环**：预留标准的串口 JSON/Hex 协议接口，可将二维视觉坐标实时解算并下发至 STM32，实现对舵机与双体船电机的伺服控制。

## 🛠️ 技术栈

* **深度学习框架**: PyTorch, Ultralytics YOLOv11
* **计算机视觉**: OpenCV
* **Web 后端**: Flask
* **前端交互**: HTML5, Vanilla JavaScript, CSS3
* **硬件预留**: STM32F1 / RDK X3 / 串口通信 (PySerial)

---

## 🚀 快速开始

### 1. 环境准备
确保你的计算机或边缘开发板已安装 Python 3.9+，然后克隆本项目并安装依赖：

```bash
git clone [https://github.com/yourusername/WTR-System.git](https://github.com/yourusername/WTR-System.git)
cd WTR-System
pip install -r requirements.txt