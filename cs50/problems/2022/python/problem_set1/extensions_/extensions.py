def main():
    file_ = input("File name: ")

    mime_ = get_MIME(file_.lower())
    
    print(mime_)


def get_MIME(mime_):
    if mime_.find(".png") != -1:
        return "image/png"
    elif mime_.find(".jpeg") != -1 or mime_.find(".jpg") != -1:
        return "image/jpeg"
    elif mime_.find(".gif") != -1:
        return "image/gif"
    elif mime_.find(".txt") != -1:
        return "text/plain"
    elif mime_.find(".pdf") != -1:
        return "application/pdf"
    elif mime_.find(".zip") != -1:
        return "application/zip"
    else:
        return "application/octet-stream"


main()