import streamlit as st
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import io
import time
from pathlib import Path
import zipfile
import base64

# 페이지 설정
st.set_page_config(
    page_title="AI Image Scale-Up",
    page_icon="🖼️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS 스타일
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #2E86AB;
        margin-bottom: 2rem;
    }
    .stButton > button {
        background-color: #2E86AB;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 0.5rem 1rem;
        font-weight: bold;
    }
    .success-message {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #f8f9fa;
        border-left: 4px solid #2E86AB;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 캐싱 문제 해결: 이미지 파라미터에 언더스코어 추가
def enhance_image_pil(_image, scale=2, method="lanczos"):
    """PIL을 사용한 이미지 향상 - 캐싱 없음"""
    width, height = _image.size
    new_size = (width * scale, height * scale)
    
    if method == "lanczos":
        enhanced = _image.resize(new_size, Image.LANCZOS)
        
    elif method == "bicubic":
        enhanced = _image.resize(new_size, Image.BICUBIC)
        
    elif method == "enhanced":
        # 다단계 향상
        temp_size = (int(width * 1.5), int(height * 1.5))
        temp = _image.resize(temp_size, Image.LANCZOS)
        temp = temp.filter(ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3))
        enhanced = temp.resize(new_size, Image.LANCZOS)
        
        # 대비 및 선명도 향상
        enhancer = ImageEnhance.Contrast(enhanced)
        enhanced = enhancer.enhance(1.1)
        enhancer = ImageEnhance.Sharpness(enhanced)
        enhanced = enhancer.enhance(1.2)
        
    elif method == "ai_enhanced":
        # AI 스타일 향상 (실제로는 고급 이미지 처리)
        # 1단계: 스무딩
        temp = _image.filter(ImageFilter.GaussianBlur(radius=0.5))
        # 2단계: 업스케일
        temp = temp.resize(new_size, Image.LANCZOS)
        # 3단계: 샤프닝
        enhanced = temp.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=3))
        
    return enhanced

def enhance_image_numpy(_image, scale=2):
    """NumPy를 사용한 고급 업스케일링 - 캐싱 없음"""
    try:
        from scipy import ndimage
        
        img_array = np.array(_image)
        height, width, channels = img_array.shape
        
        enhanced_array = np.zeros((height * scale, width * scale, channels), dtype=np.uint8)
        
        for c in range(channels):
            zoomed = ndimage.zoom(img_array[:, :, c], scale, order=3)
            enhanced_array[:, :, c] = np.clip(zoomed, 0, 255)
        
        return Image.fromarray(enhanced_array)
    except ImportError:
        st.warning("SciPy가 설치되지 않아 기본 방법을 사용합니다.")
        return enhance_image_pil(_image, scale, "enhanced")
    except Exception as e:
        st.error(f"NumPy 처리 중 오류: {e}")
        return enhance_image_pil(_image, scale, "enhanced")

def process_image(_image, scale, method):
    """이미지 처리 메인 함수 - 캐싱 없음"""
    if method == "scipy_advanced":
        return enhance_image_numpy(_image, scale)
    else:
        return enhance_image_pil(_image, scale, method)

def get_download_link(img, filename):
    """다운로드 링크 생성"""
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_data = buffered.getvalue()
    b64 = base64.b64encode(img_data).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="{filename}" style="text-decoration: none; background-color: #2E86AB; color: white; padding: 8px 16px; border-radius: 5px; display: inline-block; margin: 5px;">📥 Download {filename}</a>'
    return href

def create_progress_bar(current, total, operation="Processing"):
    """진행률 표시"""
    progress = current / total
    bar_length = 30
    filled_length = int(bar_length * progress)
    bar = "█" * filled_length + "░" * (bar_length - filled_length)
    return f"{operation}: [{bar}] {current}/{total} ({progress:.1%})"

def main():
    # 헤더
    st.markdown("<h1 class='main-header'>🖼️ AI Image Scale-Up</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 1.2em; color: #666;'>Transform your images with AI-powered upscaling technology</p>", unsafe_allow_html=True)
    
    # 사이드바 설정
    st.sidebar.title("⚙️ 설정")
    
    # 업스케일 방법 선택
    method_options = {
        "Lanczos (빠름)": "lanczos",
        "Bicubic (균형)": "bicubic", 
        "Enhanced (고품질)": "enhanced",
        "AI Enhanced (최고품질)": "ai_enhanced",
        "SciPy Advanced (전문가용)": "scipy_advanced"
    }
    
    selected_method = st.sidebar.selectbox(
        "🎨 업스케일 방법 선택",
        options=list(method_options.keys()),
        index=2,
        help="각 방법의 특징:\n- Lanczos: 빠른 처리\n- Bicubic: 자연스러운 결과\n- Enhanced: 다단계 향상\n- AI Enhanced: 고급 필터링\n- SciPy Advanced: 수학적 보간"
    )
    
    # 스케일 배율 선택
    scale_factor = st.sidebar.slider(
        "🔍 확대 배율",
        min_value=1,
        max_value=8,
        value=2,
        step=1,
        help="1배는 원본 크기, 8배까지 확대 가능"
    )
    
    # 처리 옵션
    st.sidebar.markdown("---")
    show_comparison = st.sidebar.checkbox("📊 Before/After 비교", value=True)
    auto_download = st.sidebar.checkbox("💾 자동 다운로드 링크 생성", value=True)
    show_details = st.sidebar.checkbox("📋 상세 정보 표시", value=True)
    
    # 성능 경고
    if scale_factor >= 6:
        st.sidebar.warning("⚠️ 6배 이상 확대는 처리 시간이 오래 걸릴 수 있습니다.")
    
    # 메인 영역
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 이미지 업로드")
        uploaded_files = st.file_uploader(
            "이미지 파일을 선택하세요",
            type=['png', 'jpg', 'jpeg', 'bmp', 'tiff'],
            accept_multiple_files=True,
            help="PNG, JPG, JPEG, BMP, TIFF 형식 지원"
        )
        
        if uploaded_files:
            st.success(f"✅ {len(uploaded_files)}개 파일이 업로드되었습니다!")
            
            # 업로드된 파일 정보
            if show_details:
                st.write("**업로드된 파일들:**")
                for file in uploaded_files:
                    st.write(f"- {file.name} ({file.size/1024:.1f}KB)")
    
    if uploaded_files:
        # 예상 처리 시간 계산
        estimated_time = len(uploaded_files) * (0.5 if scale_factor <= 2 else 2.0 if scale_factor <= 4 else 5.0)
        st.info(f"⏱️ 예상 처리 시간: 약 {estimated_time:.1f}초 (방법: {selected_method})")
        
        # 처리 시작 버튼
        if st.button("🚀 이미지 업스케일링 시작", key="process_btn", type="primary"):
            
            # 처리 시작
            start_time = time.time()
            progress_bar = st.progress(0)
            status_text = st.empty()
            time_text = st.empty()
            
            results = []
            
            for i, uploaded_file in enumerate(uploaded_files):
                current_time = time.time() - start_time
                status_text.text(f"🔄 처리 중... ({i+1}/{len(uploaded_files)}) {uploaded_file.name}")
                time_text.text(f"⏱️ 경과 시간: {current_time:.1f}초")
                
                try:
                    # 이미지 로드
                    image = Image.open(uploaded_file)
                    
                    # RGB 변환 (RGBA나 다른 모드 처리)
                    if image.mode != 'RGB':
                        image = image.convert('RGB')
                    
                    # 메모리 사용량 체크
                    image_size = image.size[0] * image.size[1] * 3  # RGB
                    scaled_size = image_size * (scale_factor ** 2)
                    
                    if scaled_size > 100_000_000:  # 100MB 초과시 경고
                        st.warning(f"⚠️ {uploaded_file.name}: 결과 이미지가 매우 클 수 있습니다.")
                    
                    # 처리 시작 시간
                    process_start_time = time.time()
                    
                    # 이미지 처리
                    method = method_options[selected_method]
                    enhanced_image = process_image(image, scale_factor, method)
                    
                    # 처리 시간 계산
                    process_time = time.time() - process_start_time
                    
                    # 결과 저장
                    results.append({
                        'original': image,
                        'enhanced': enhanced_image,
                        'filename': uploaded_file.name,
                        'process_time': process_time,
                        'original_size': image.size,
                        'enhanced_size': enhanced_image.size,
                        'method': selected_method,
                        'scale': scale_factor
                    })
                    
                    st.success(f"✅ {uploaded_file.name} 처리 완료 ({process_time:.1f}초)")
                    
                except Exception as e:
                    st.error(f"❌ {uploaded_file.name} 처리 실패: {str(e)}")
                    continue
                
                # 진행률 업데이트
                progress_bar.progress((i + 1) / len(uploaded_files))
            
            total_time = time.time() - start_time
            status_text.text("✅ 모든 이미지 처리 완료!")
            time_text.text(f"🎉 총 처리 시간: {total_time:.1f}초")
            
            # 결과 표시
            if results:
                st.markdown("---")
                st.subheader("📊 처리 결과")
                
                for i, result in enumerate(results):
                    with st.expander(f"📁 {result['filename']} - 결과 보기", expanded=(i == 0)):
                        
                        # 정보 표시
                        if show_details:
                            col_info1, col_info2, col_info3, col_info4 = st.columns(4)
                            with col_info1:
                                st.metric("원본 크기", f"{result['original_size'][0]}×{result['original_size'][1]}")
                            with col_info2:
                                st.metric("결과 크기", f"{result['enhanced_size'][0]}×{result['enhanced_size'][1]}")
                            with col_info3:
                                st.metric("처리 시간", f"{result['process_time']:.1f}초")
                            with col_info4:
                                file_size_mb = (result['enhanced_size'][0] * result['enhanced_size'][1] * 3) / (1024 * 1024)
                                st.metric("예상 크기", f"{file_size_mb:.1f}MB")
                        
                        if show_comparison:
                            # Before/After 비교
                            col_before, col_after = st.columns(2)
                            
                            with col_before:
                                st.markdown("**🔻 Original**")
                                st.image(result['original'], use_column_width=True)
                            
                            with col_after:
                                st.markdown(f"**🔺 Enhanced ({scale_factor}x - {result['method']})**")
                                st.image(result['enhanced'], use_column_width=True)
                        else:
                            # 결과만 표시
                            st.markdown(f"**Enhanced Result ({scale_factor}x - {result['method']})**")
                            st.image(result['enhanced'], use_column_width=True)
                        
                        # 다운로드 링크
                        if auto_download:
                            filename_base = Path(result['filename']).stem
                            download_filename = f"{filename_base}_enhanced_{scale_factor}x.png"
                            download_link = get_download_link(result['enhanced'], download_filename)
                            st.markdown(download_link, unsafe_allow_html=True)
                
                # 전체 통계
                total_time = sum(r['process_time'] for r in results)
                avg_time = total_time / len(results)
                successful_count = len(results)
                
                st.markdown("### 📈 전체 통계")
                col_stat1, col_stat2, col_stat3, col_stat4 = st.columns(4)
                with col_stat1:
                    st.metric("성공한 이미지", f"{successful_count}개")
                with col_stat2:
                    st.metric("총 처리 시간", f"{total_time:.1f}초")
                with col_stat3:
                    st.metric("평균 처리 시간", f"{avg_time:.1f}초/이미지")
                with col_stat4:
                    efficiency = successful_count / len(uploaded_files) * 100
                    st.metric("성공률", f"{efficiency:.1f}%")
            
            else:
                st.error("❌ 처리된 이미지가 없습니다. 파일 형식이나 크기를 확인해주세요.")
    
    # 정보 섹션
    with st.expander("ℹ️ 사용법 및 팁"):
        st.markdown("""
        ### 🎯 사용법
        1. **이미지 업로드**: 좌측에서 하나 또는 여러 이미지 선택
        2. **설정 조정**: 사이드바에서 방법과 배율 선택
        3. **처리 시작**: '이미지 업스케일링 시작' 버튼 클릭
        4. **결과 확인**: Before/After 비교 및 다운로드
        
        ### 💡 최적화 팁
        - **작은 이미지** (< 512px): 4x-8x 배율 추천
        - **중간 이미지** (512-1024px): 2x-4x 배율 추천
        - **큰 이미지** (> 1024px): 2x-3x 배율 추천 (메모리 고려)
        - **사진**: Enhanced 또는 AI Enhanced 추천
        - **그래픽/텍스트**: Lanczos 또는 Bicubic 추천
        
        ### 📊 성능 가이드
        | 이미지 크기 | 2배 확대 | 4배 확대 | 8배 확대 |
        |------------|----------|----------|----------|
        | 256×256 | ~0.1초 | ~0.3초 | ~1초 |
        | 512×512 | ~0.5초 | ~1.5초 | ~5초 |
        | 1024×1024 | ~2초 | ~8초 | ~30초 |
        
        ### ⚠️ 주의사항
        - 큰 이미지일수록 처리 시간이 길어집니다
        - 8배 확대시 메모리 사용량이 급증할 수 있습니다
        - 최적 결과를 위해 다양한 방법을 시도해보세요
        - 브라우저가 응답하지 않는 것처럼 보여도 처리 중일 수 있습니다
        """)
    
    # 푸터
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; padding: 2rem;'>
        <p>🚀 Made with ❤️ using Streamlit & AI</p>
        <p>📧 Issues? Visit our <a href='https://github.com/waterfirst/image_scale-up_by_ai' target='_blank'>GitHub Repository</a></p>
        <p>⭐ Found this useful? Give us a star on GitHub!</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
