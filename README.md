# 🖼️ AI 이미지 업스케일링

**Streamlit으로 구축된 AI 기반 이미지 업스케일링 웹 애플리케이션**

저해상도 이미지를 고급 AI 알고리즘과 이미지 처리 기술을 사용하여 고품질로 업스케일링하는 도구입니다.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://imagescale-upbyai.streamlit.app/)

---

# 🖼️ AI Image Scale-Up

**AI-powered image upscaling web application built with Streamlit**

Transform your low-resolution images into high-quality, upscaled versions using advanced AI algorithms and image processing techniques.

---

## ✨ 주요 기능 / Features

- 🚀 **5가지 업스케일링 방법** / **Multiple Upscaling Methods**: 다양한 알고리즘 선택 가능
- 📏 **유연한 배율 조정** / **Flexible Scaling**: 1배~8배 확대 옵션
- 🔄 **일괄 처리** / **Batch Processing**: 여러 이미지 동시 업로드 및 처리
- 📊 **전후 비교** / **Before/After Comparison**: 원본과 향상된 이미지 시각적 비교
- 💾 **간편한 다운로드** / **Easy Download**: 원클릭 다운로드 기능
- 🎨 **사용자 친화적 인터페이스** / **User-Friendly Interface**: 깔끔하고 직관적인 웹 인터페이스
- ⚡ **CPU 최적화** / **CPU Optimized**: GPU 없이도 작동

## 🎯 업스케일링 방법 / Upscaling Methods

| 방법 / Method | 속도 / Speed | 품질 / Quality | 최적 용도 / Best For |
|--------|-------|---------|----------|
| **Lanczos (빠름)** | ⚡⚡⚡ | ⭐⭐⭐ | 빠른 처리, 그래픽 / Quick processing, graphics |
| **Bicubic (균형)** | ⚡⚡ | ⭐⭐⭐⭐ | 균형잡힌 결과, 사진 / Balanced results, photos |
| **Enhanced (고품질)** | ⚡ | ⭐⭐⭐⭐⭐ | 고품질, 상세한 이미지 / High quality, detailed images |
| **AI Enhanced (최고품질)** | ⚡ | ⭐⭐⭐⭐⭐ | 최고 품질, 사진 / Maximum quality, photographs |
| **SciPy Advanced (전문가용)** | ⚡⚡ | ⭐⭐⭐⭐⭐ | 전문가 사용, 기술적 이미지 / Professional use, technical images |

## 🚀 빠른 시작 / Quick Start

### 1. 저장소 복제 / Clone the Repository
```bash
git clone https://github.com/waterfirst/image_scale-up_by_ai.git
cd image_scale-up_by_ai
```

### 2. 의존성 설치 / Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. 애플리케이션 실행 / Run the Application
```bash
streamlit run app.py
```

### 4. 브라우저에서 열기 / Open in Browser
웹 브라우저에서 `http://localhost:8501`로 이동하세요.

Navigate to `http://localhost:8501` in your web browser.

## 📖 사용법 / How to Use

1. **이미지 업로드** / **Upload Images**: "파일 찾기"를 클릭하고 하나 또는 여러 이미지 선택
2. **설정 선택** / **Choose Settings**: 
   - 사이드바에서 업스케일링 방법 선택 / Select upscaling method in the sidebar
   - 배율 조정 (1x-8x) / Adjust scale factor (1x-8x)
   - 비교 및 다운로드 옵션 토글 / Toggle comparison and download options
3. **처리 시작** / **Process**: "🚀 이미지 업스케일링 시작" 버튼 클릭 / Click "🚀 이미지 업스케일링 시작" to start processing
4. **다운로드** / **Download**: 다운로드 링크를 사용하여 향상된 이미지 저장 / Use the download links to save enhanced images

## 📊 지원 형식 / Supported Formats

- **입력 / Input**: PNG, JPG, JPEG, BMP, TIFF
- **출력 / Output**: PNG (고품질, 무손실 / high quality, lossless)

## 💡 성능 팁 / Performance Tips

### 최적 결과를 위한 권장사항 / For Best Results:
- **작은 이미지** (< 512px): 4x-8x 배율 사용 / **Small images** (< 512px): Use 4x-8x scaling
- **중간 이미지** (512-1024px): 2x-4x 배율 사용 / **Medium images** (512-1024px): Use 2x-4x scaling  
- **큰 이미지** (> 1024px): 2x-3x 배율 사용 / **Large images** (> 1024px): Use 2x-3x scaling
- **사진**: "Enhanced" 또는 "AI Enhanced" 시도 / **Photos**: Try "Enhanced" or "AI Enhanced"
- **그래픽/텍스트**: "Lanczos" 또는 "Bicubic" 사용 / **Graphics/Text**: Use "Lanczos" or "Bicubic"

### 시스템 요구사항 / System Requirements:
- **RAM**: 최소 4GB, 대용량 이미지용 8GB+ 권장 / 4GB minimum, 8GB+ recommended for large images
- **CPU**: 최신 프로세서 (멀티코어 권장) / Any modern processor (multi-core recommended)
- **저장공간**: 임시 처리용 1GB 여유공간 / 1GB free space for temporary processing

## 🔧 기술 세부사항 / Technical Details

### 핵심 기술 / Core Technologies:
- **Streamlit**: 웹 애플리케이션 프레임워크 / Web application framework
- **PIL/Pillow**: 이미지 처리 라이브러리 / Image processing library
- **NumPy**: 수치 연산 / Numerical computing
- **SciPy**: 고급 수학 함수 / Advanced mathematical functions

### 사용된 알고리즘 / Algorithms Used:
- **Lanczos 리샘플링** / **Lanczos Resampling**: 빠르고 선명한 업스케일링 / Fast, sharp upscaling
- **Bicubic 보간법** / **Bicubic Interpolation**: 부드럽고 자연스러운 결과 / Smooth, natural results
- **다단계 향상** / **Multi-stage Enhancement**: 점진적 품질 개선 / Progressive quality improvement
- **언샤프 마스킹** / **Unsharp Masking**: 가장자리 향상 및 선명화 / Edge enhancement and sharpening
- **수학적 보간법** / **Mathematical Interpolation**: 정밀한 픽셀 값 계산 / Precise pixel value calculation

## 📈 성능 벤치마크 / Performance Benchmarks

| 이미지 크기 / Image Size | 방법 / Method | 2배 확대 시간 / 2x Scale Time | 4배 확대 시간 / 4x Scale Time |
|------------|--------|---------------|---------------|
| 256×256 | Lanczos | ~0.1초 / ~0.1s | ~0.3초 / ~0.3s |
| 512×512 | Enhanced | ~0.5초 / ~0.5s | ~1.5초 / ~1.5s |
| 1024×1024 | AI Enhanced | ~2초 / ~2s | ~8초 / ~8s |
| 2048×2048 | SciPy Advanced | ~8초 / ~8s | ~30초 / ~30s |

*일반적인 데스크톱 CPU (Intel i5/AMD Ryzen 5 동급) 기준 벤치마크*
*Benchmarks on typical desktop CPU (Intel i5/AMD Ryzen 5 equivalent)*

## 🛠️ 개발 / Development

### 프로젝트 구조 / Project Structure:
```
image_scale-up_by_ai/
├── app.py              # 메인 Streamlit 애플리케이션 / Main Streamlit application
├── requirements.txt    # Python 의존성 / Python dependencies
├── README.md          # 이 파일 / This file
├── .gitignore         # Git 무시 패턴 / Git ignore patterns
└── assets/            # 데모 이미지 및 스크린샷 / Demo images and screenshots
    ├── demo_before.png
    ├── demo_after.png
    └── screenshot.png
```

### 로컬 개발 / Local Development:
```bash
# 개발 의존성 설치 / Install development dependencies
pip install -r requirements.txt

# 자동 새로고침으로 실행 / Run with auto-reload
streamlit run app.py --server.runOnSave true

# 특정 포트에서 실행 / Run on specific port
streamlit run app.py --server.port 8502
```

## 🤝 기여 방법 / Contributing

기여를 환영합니다! Pull Request를 자유롭게 제출해주세요.
Contributions are welcome! Please feel free to submit a Pull Request.

### 기여 분야 / Areas for Contribution:
- 🧠 **새로운 AI 모델** / **New AI Models**: 더 고급 업스케일링 모델 통합 / Integration with more advanced upscaling models
- ⚡ **GPU 지원** / **GPU Support**: CUDA/ROCm 가속 / CUDA/ROCm acceleration
- 🎨 **UI 개선** / **UI Improvements**: 더 나은 디자인과 사용자 경험 / Better design and user experience  
- 📱 **모바일 최적화** / **Mobile Optimization**: 반응형 디자인 개선 / Responsive design improvements
- 🔧 **성능 최적화** / **Performance**: 알고리즘 최적화 / Algorithm optimizations

## 📄 라이센스 / License

이 프로젝트는 MIT 라이센스 하에 제공됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하세요.
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 감사의 말 / Acknowledgments

- 놀라운 웹 프레임워크를 제공한 [Streamlit](https://streamlit.io/)에 감사합니다 / Built with [Streamlit](https://streamlit.io/) for the amazing web framework
- 고전적인 이미지 처리와 현대 AI 업스케일링 기술에서 영감을 받았습니다 / Inspired by classical image processing and modern AI upscaling techniques
- 기본 라이브러리들을 제공한 오픈소스 커뮤니티에 특별한 감사를 드립니다 / Special thanks to the open-source community for the underlying libraries

## 🐛 이슈 및 지원 / Issues & Support

문제가 발생하거나 질문이 있으시면 / If you encounter any issues or have questions:
1. 기존 [Issues](https://github.com/waterfirst/image_scale-up_by_ai/issues) 확인 / Check existing [Issues](https://github.com/waterfirst/image_scale-up_by_ai/issues)
2. 상세한 설명과 함께 새 이슈 생성 / Create a new issue with detailed description
3. 해당되는 경우 샘플 이미지와 오류 메시지 포함 / Include sample images and error messages if applicable

## 🌟 이 저장소에 별표 주기 / Star this Repository

이 프로젝트가 유용하다면 GitHub에서 ⭐를 눌러주세요!
If you find this project useful, please give it a ⭐ on GitHub!

---

**❤️ [waterfirst](https://github.com/waterfirst)가 만들었습니다**
**Made with ❤️ by [waterfirst](https://github.com/waterfirst)**

*한 번에 하나씩 픽셀을 변환합니다* 🖼️✨
*Transforming pixels, one image at a time* 🖼️✨
