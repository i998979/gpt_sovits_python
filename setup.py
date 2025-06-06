import os
import platform

import pkg_resources
from setuptools import find_packages, setup

setup(
    name="gpt_sovits_python",
    version="1.0.0",
    description="Python wrapper for fast inference with GPT-SoVITS",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    readme="README.md",
    python_requires=">=3.9",
    author="R3gm",
    url="https://github.com/R3gm/gpt_sovits_python",
    license="MIT",
    packages=find_packages(),
    package_data={'': ['*.txt', '*.rep', '*.pickle']},
    install_requires=[
        "ffmpeg-python",
        "pyopenjtalk",
        "einops",
        "LangSegment>=0.2.0",
        "cn2an",
        "pypinyin",
        "jieba_fast==0.53",
        "g2p_en",
        "typing_extensions==4.9.0",
        "typeguard==4.2.0",
        "einops",
        "pytorch_lightning==1.2.0",
    ],
    include_package_data=True,
    py_modules=['utils'],
    extras_require={"all": [
        "torch",
        "numpy",
        "scipy",
        "tensorboard==2.11.2",
        "librosa==0.9.2",
        "numba==0.56.4",
        "ffmpeg-python",
        "onnxruntime",
        "tqdm",
        "funasr==1.0.0",
        "torchaudio",
        "modelscope==1.10.0",
        "sentencepiece",
        "transformers",
        "chardet",
        "PyYAML",
        "psutil",
        "jieba",
        "Faster_Whisper",
        "wordsegment",
        ]},
)
