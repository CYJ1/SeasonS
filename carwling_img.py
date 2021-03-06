from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()


# num이 100개 이상 시 selenium을 사용
# 사용 시 크롬드라이버 설정 필요

def downloadimages(query):
    num = 10  # num은 이미지 출력개수
    arguments = {"keywords": "Black Waffle Chip Cream Frappuccino",  # 다운하고 싶은 이미지 키워드
                 "format": "jpg",  # 다운로드 확장자
                 "limit": num,  # 다운 이미지 개수
                 "output_directory": "image"}  # 'image'라는 폴더를 만들어서 그 안에 저장

    try:
        response.download(arguments)

    # Handling File NotFound Error
    except FileNotFoundError:
        arguments = {"keywords": "Black Waffle Chip Cream Frappuccino",
                     "format": "jpg",
                     "limit": num,
                     "output_directory": "image"}

        # Providing arguments for the searched query
        try:
            # Downloading the photos based
            # on the given arguments
            response.download(arguments)
        except:
            pass


downloadimages("Black Waffle Chip Cream Frappuccino")  # 이미지 다운
print()  # 다운 받은 이미지 출력
