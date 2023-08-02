import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba
import numpy as np
from PIL import Image

def create_wordcloud_from_file(file_path, mask_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # 使用jieba对中文文本进行分词
    seg_list = jieba.cut(text)
    seg_text = " ".join(seg_list)

    # 常见字列表，可以根据需要继续扩展
    common_words_path = "./common_words"
    with open(common_words_path, 'r', encoding='utf-8') as words:
        common_words = words.read()

    # 加载词云形状的图像文件
    mask = np.array(Image.open(mask_path))

    # 创建一个WordCloud对象，并指定词云形状
    wordcloud = WordCloud(width=800, height=400,
                          background_color='white',
                          font_path='./simsun.ttc',
                          colormap='viridis',
                          stopwords=common_words,
                          max_words=100,
                          contour_width=3,
                          contour_color='steelblue',
                          collocations=False,
                          prefer_horizontal=0.8,
                          mask=mask,
                          scale=32,
                          )  # 指定词云形状

    # 生成词云
    wordcloud.generate(seg_text)

    # 可视化词云
    plt.figure(figsize=(16, 8))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Turn off the axes
    # plt.show()

    # 保存词云图像，不带坐标轴
    plt.savefig('ydsy_logo.jpg', dpi=300)
    plt.close()  # Close the figure to avoid displaying it with plt.show()

if __name__ == "__main__":
    file_path = "sample_text.txt"  # 设置文件路径和文件名，确保该文件包含要生成词云的文本内容
    mask_path = "./img.png"  # 自定义形状的图像文件路径

    create_wordcloud_from_file(file_path, mask_path)
