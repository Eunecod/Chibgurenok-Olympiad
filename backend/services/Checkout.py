def GetAssessedReply(Quiz_Reply: dict, User_Reply: dict) -> int:
    if (len(User_Reply) == 0):
        return -1
    
    if (len(Quiz_Reply) != len(User_Reply)):
        return -1

    nAssessed: int = 0
    for index in range (len(Quiz_Reply)):
        if (__CheckAnswer(Quiz_Reply[index].get("correct"), User_Reply[index].get("answer"))):
            nAssessed += Quiz_Reply[index].get("score")

    return nAssessed


def GetReplyBody(Quiz_Reply: dict, User_Reply: dict) -> list:
    if (len(User_Reply) == 0):
        return []
    
    if (len(Quiz_Reply) != len(User_Reply)):
        return []

    listReplyBody: list = []
    for index in range (len(Quiz_Reply)):
        nPoint: int = 0;
        if (__CheckAnswer(Quiz_Reply[index].get("correct"), User_Reply[index].get("answer"))):
            nPoint += Quiz_Reply[index].get("score")

        listReplyBody.append({
            "id":       User_Reply[index].get("id"),
            "answer":   User_Reply[index].get("answer"),
            "point":    nPoint
        })

    return listReplyBody


def __CheckAnswer(CorrectAnswer, UserAnswer) -> bool:
    bResult: bool = False

    if (isinstance(CorrectAnswer, list) and isinstance(UserAnswer, list)):
        bResult = set(CorrectAnswer) == set(UserAnswer)    
    elif (isinstance(CorrectAnswer, list) and isinstance(UserAnswer, str)):
        bResult = any(_answer in CorrectAnswer for _answer in [UserAnswer])    
    elif (isinstance(CorrectAnswer, str) and isinstance(UserAnswer, str)):
        bResult = CorrectAnswer == UserAnswer
    elif (isinstance(CorrectAnswer, int) and isinstance(UserAnswer, int)):
        bResult = CorrectAnswer == UserAnswer

    return bResult

