from personalColor.personal_color_analysis import personal_color
'''
봄웜톤(spring) : SPRING WARM
가을웜톤(fall) : FALL WARM
여름쿨톤(summer) : SUMMER COOL
겨울쿨톤(winter) : WINTER COOL
'''

def main(file_path):
    tone = personal_color.analysis(file_path)
    return tone
'''
file_path = '../ex_0.png'  ## 실행시킬 때 이미지 파일 경로 + .dat파일 경로도 실행시킬 때 기준으로 바꿔야함

tone = main(file_path)
#tone = "SPRING WARM"
print("reuslt is " + str(tone))

'''
