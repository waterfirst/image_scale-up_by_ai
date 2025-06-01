# 🖼️ AI Image Scale-Up

**AI-powered image upscaling web application built with Streamlit**

Transform your low-resolution images into high-quality, upscaled versions using advanced AI algorithms and image processing techniques.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url-here.streamlit.app)

## ✨ Features

- 🚀 **Multiple Upscaling Methods**: Choose from 5 different algorithms
- 📏 **Flexible Scaling**: 1x to 8x upscaling options
- 🔄 **Batch Processing**: Upload and process multiple images at once
- 📊 **Before/After Comparison**: Visual comparison of original vs enhanced images
- 💾 **Easy Download**: One-click download of processed images
- 🎨 **User-Friendly Interface**: Clean, intuitive web interface
- ⚡ **CPU Optimized**: Works without GPU requirements

## 🎯 Upscaling Methods

| Method | Speed | Quality | Best For |
|--------|-------|---------|----------|
| **Lanczos** | ⚡⚡⚡ | ⭐⭐⭐ | Quick processing, graphics |
| **Bicubic** | ⚡⚡ | ⭐⭐⭐⭐ | Balanced results, photos |
| **Enhanced** | ⚡ | ⭐⭐⭐⭐⭐ | High quality, detailed images |
| **AI Enhanced** | ⚡ | ⭐⭐⭐⭐⭐ | Maximum quality, photographs |
| **SciPy Advanced** | ⚡⚡ | ⭐⭐⭐⭐⭐ | Professional use, technical images |

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/waterfirst/image_scale-up_by_ai.git
cd image_scale-up_by_ai
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

### 4. Open in Browser
Navigate to `http://localhost:8501` in your web browser.

## 📖 How to Use

1. **Upload Images**: Click "Browse files" and select one or multiple images
2. **Choose Settings**: 
   - Select upscaling method in the sidebar
   - Adjust scale factor (1x-8x)
   - Toggle comparison and download options
3. **Process**: Click "🚀 이미지 업스케일링 시작" to start processing
4. **Download**: Use the download links to save enhanced images

## 📊 Supported Formats

- **Input**: PNG, JPG, JPEG, BMP, TIFF
- **Output**: PNG (high quality, lossless)

## 💡 Performance Tips

### For Best Results:
- **Small images** (< 512px): Use 4x-8x scaling
- **Medium images** (512-1024px): Use 2x-4x scaling  
- **Large images** (> 1024px): Use 2x-3x scaling
- **Photos**: Try "Enhanced" or "AI Enhanced"
- **Graphics/Text**: Use "Lanczos" or "Bicubic"

### System Requirements:
- **RAM**: 4GB minimum, 8GB+ recommended for large images
- **CPU**: Any modern processor (multi-core recommended)
- **Storage**: 1GB free space for temporary processing

## 🔧 Technical Details

### Core Technologies:
- **Streamlit**: Web application framework
- **PIL/Pillow**: Image processing library
- **NumPy**: Numerical computing
- **SciPy**: Advanced mathematical functions

### Algorithms Used:
- **Lanczos Resampling**: Fast, sharp upscaling
- **Bicubic Interpolation**: Smooth, natural results
- **Multi-stage Enhancement**: Progressive quality improvement
- **Unsharp Masking**: Edge enhancement and sharpening
- **Mathematical Interpolation**: Precise pixel value calculation

## 📈 Performance Benchmarks

| Image Size | Method | 2x Scale Time | 4x Scale Time |
|------------|--------|---------------|---------------|
| 256×256 | Lanczos | ~0.1s | ~0.3s |
| 512×512 | Enhanced | ~0.5s | ~1.5s |
| 1024×1024 | AI Enhanced | ~2s | ~8s |
| 2048×2048 | SciPy Advanced | ~8s | ~30s |

*Benchmarks on typical desktop CPU (Intel i5/AMD Ryzen 5 equivalent)*

## 🛠️ Development

### Project Structure:
```
image_scale-up_by_ai/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .gitignore         # Git ignore patterns
└── assets/            # Demo images and screenshots
    ├── demo_before.png
    ├── demo_after.png
    └── screenshot.png
```

### Local Development:
```bash
# Install development dependencies
pip install -r requirements.txt

# Run with auto-reload
streamlit run app.py --server.runOnSave true

# Run on specific port
streamlit run app.py --server.port 8502
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Areas for Contribution:
- 🧠 **New AI Models**: Integration with more advanced upscaling models
- ⚡ **GPU Support**: CUDA/ROCm acceleration
- 🎨 **UI Improvements**: Better design and user experience  
- 📱 **Mobile Optimization**: Responsive design improvements
- 🔧 **Performance**: Algorithm optimizations

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the amazing web framework
- Inspired by classical image processing and modern AI upscaling techniques
- Special thanks to the open-source community for the underlying libraries

## 🐛 Issues & Support

If you encounter any issues or have questions:
1. Check existing [Issues](https://github.com/waterfirst/image_scale-up_by_ai/issues)
2. Create a new issue with detailed description
3. Include sample images and error messages if applicable

## 🌟 Star this Repository

If you find this project useful, please give it a ⭐ on GitHub!

---

**Made with ❤️ by [waterfirst](https://github.com/waterfirst)**

*Transforming pixels, one image at a time* 🖼️✨
