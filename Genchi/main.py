import wordcloud
myWordCloud = wordcloud.WordCloud()
with open('trip_to_academia.txt', encoding='utf-8') as f:
    myWordCloud.generate(f.read())
myWordCloud.to_file('myWordCloud.png')


myWordCloud = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='white',
    font_path='msyh.ttc'
)



import imageio
myMask = imageio.imread("picture.png")
myWordCloud = wordcloud.WordCloud(mask=myMask)