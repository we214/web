#streamlit_app.py

import streamlit as st
from fastai.vision.all import *
from PIL import Image, ImageOps
import gdown
import os

# --- 1. 페이지 기본 설정 ---
st.set_page_config(
    page_title="Fastai 이미지 분류기",
    page_icon="🤖",
)

# --- 2. 커스텀 CSS ---
st.markdown("""
<style>
h1 {
    color: #1E88E5;
    text-align: center;
    font-weight: bold;
}
.stFileUploader {
    border: 2px dashed #1E88E5;
    border-radius: 10px;
    padding: 15px;
    background-color: #f5fafe;
}
.prediction-box {
    background-color: #E3F2FD;
    border: 2px solid #1E88E5;
    border-radius: 10px;
    padding: 25px;
    text-align: center;
    margin: 20px 0;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}
.prediction-box h2 {
    color: #0D47A1;
    margin: 0;
    font-size: 2.0rem;
}
.prob-card {
    background-color: #FFFFFF;
    border-radius: 8px;
    padding: 15px;
    margin: 10px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    transition: transform 0.2s ease;
}
.prob-card:hover { transform: translateY(-3px); }
.prob-label {
    font-weight: bold;
    font-size: 1.05rem;
    color: #333;
}
.prob-bar-bg {
    background-color: #E0E0E0;
    border-radius: 5px;
    width: 100%;
    height: 22px;
    overflow: hidden;
}
.prob-bar-fg {
    background-color: #4CAF50;
    height: 100%;
    border-radius: 5px 0 0 5px;
    text-align: right;
    padding-right: 8px;
    color: white;
    font-weight: bold;
    line-height: 22px;
    transition: width 0.5s ease-in-out;
}
.prob-bar-fg.highlight { background-color: #FF6F00; }
</style>
""", unsafe_allow_html=True)
