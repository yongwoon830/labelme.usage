# labelme.usage

<img width="771" height="768" alt="Demo Screenshot" src="https://github.com/user-attachments/assets/952abbdf-e055-44c3-a3c4-08625c68da11" />

This repository demonstrates how to create simple training labeling data for image segmentation using a GUI-based approach.  
The workflow is based on [Labelme](https://github.com/wkentaro/labelme), a popular open-source annotation tool.

Using Labelme, users can easily annotate images with polygon-based labels through a graphical interface, making it suitable for preparing segmentation datasets for machine learning and deep learning models.

---

## 설명
이 프로젝트는 GUI 기반 라벨링을 통해 이미지 분할 학습 데이터를 만드는 방법을 보여줍니다.  
Polygon 형태로 라벨링을 하여, 모델 학습용 데이터셋을 빠르게 준비할 수 있습니다.  

---

## 내 테스트 환경
- OS: Windows 11 / Ubuntu 22.04
- Python: 3.10
- Labelme version: 5.2.0
- 기타 패키지: numpy, opencv-python

---

## 설치 방법
```bash
# 1. 가상환경 생성 (선택)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 2. 필요한 패키지 설치
pip install labelme numpy opencv-python
