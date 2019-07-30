import os
import sys
import subprocess
from datetime import datetime

tsvFolder = "c:/kidpmig/"
stdMboxName = {
    "받은편지함": "INBOX",
    "보낸편지함": "Sent",
    "임시보관함": "Drafts",
    "지운편지함": "Trash",
    "개인편지함": "Personal folder",
    "광고편지함": "Junk E-Mail"
}

# if os.path.isfile(tsvFolder + "log.txt"):
#     os.system("rm -f " + tsvFolder + "log.txt")

startDate = datetime.now()
os.system("echo " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " > " + tsvFolder + "log.txt")

def getUserList():
    with open(tsvFolder + "users.tsv", "r", encoding="utf-8") as tsvin:
        usersList = [row.split("@")[0] for row in tsvin]

        print(usersList)
    return usersList

def getUsers_mbox():
    usersMboxList = {}
    with open(tsvFolder + "users_mbox.tsv", "r", encoding="utf-8") as tsvin:
        for row in tsvin:
            tmplist = row.split("\t")
            userId = tmplist[0].split("@")[0]
            mboxId = tmplist[1].rstrip()

            if userId in usersMboxList:
                usersMboxList[userId].append(mboxId)
            else:
                usersMboxList[userId]=[mboxId]

        print(usersMboxList)
    return usersMboxList


def getMboxList():
    mboxList = {}
    with open(tsvFolder + "mbox.tsv", "r", encoding="utf-8") as tsvin:
        for row in tsvin:
            tmplist = row.split("\t")
            mboxId = tmplist[0]
            mboxName = tmplist[1].replace(".", "").replace("*", "star") # 편지함 이름에 ., * 붙은 것 제거
            mboxRef = tmplist[2].rstrip()

            if stdMboxName.get(mboxName):
                mboxName = stdMboxName[mboxName]
                
            if mboxRef == '0':
                mboxList[mboxId] = mboxName
            else:
                mboxList[mboxId] = mboxList[mboxRef] + "/" + mboxName

        print(mboxList)
    return mboxList

def getMboxMailList():
    mboxMailList = {}
    dataPath = "c:/jittest/kebiportal/kebi_data"
    with open(tsvFolder + "mbox_mail.tsv", "r", encoding="utf-8") as tsvin:
        for row in tsvin:
            tmplist = row.split("\t")
            mboxId = tmplist[0]
            mailId = tmplist[1]
            mFilePath = dataPath + tmplist[2].rstrip()

            if mboxId in mboxMailList:
                mboxMailList[mboxId].append({"mailId": mailId, "mFilePath": mFilePath})
            else:
                mboxMailList[mboxId] = [{"mailId": mailId, "mFilePath": mFilePath}]

        print(mboxMailList["9"])
    return mboxMailList

def copyMailFile(usersList, usersMboxList, mboxList, mboxMailList):
    for user in usersList:
        #테스트용 아이디
        # if user == 'conso':
        #     break
        if user in usersMboxList:
            for userMbox in usersMboxList[user]:
                #새로 만들어줄 경로에 맞춰서 수정해야함.
                newDir = tsvFolder + "test/" + user + "/" + mboxList[userMbox]
                
                try:
                    if not os.path.isdir(newDir):
                        os.makedirs(newDir)
                        print("create folder:" + newDir)
                    else:
                        print("existing folder: " + newDir)
                except:
                    print("unexcepted error:" , sys.exc_info()[0])
                    os.system("echo [" + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + "] " + newDir + " is error >> " + tsvFolder + "dirErrlog.txt")
                    continue

                if userMbox in mboxMailList:
                    logStr = ""
                    copyLogStr = ""
                    cnt = 0
                    for mail in mboxMailList[userMbox]:
                        oldPath = mail["mFilePath"]
                        mailId = mail["mailId"]

                        EmlFilePath = getEmlFilePath(mailId, oldPath)
                        
                        if EmlFilePath and EmlFilePath.find("maildata/kidp.or.kr/user1/") > -1:
                            cnt += 1
                            #os.system(["cp", EmlFilePath, newDir])
                            #copyStr = "cd " + os.path.dirname(EmlFilePath) + "&&tar cf - " + os.path.basename(EmlFilePath) + " | (cd " + newDir + "&& tar xf -)"
                            #subprocess.call(copyStr, shell=True)
                            subprocess.Popen(["cp", EmlFilePath, newDir], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            copyLogStr += "copying file: " + EmlFilePath + "\n"
                            # print("파일복사: " + EmlFilePath)
                        else:
                            logStr += oldPath + " could not found\n"
                    del mboxMailList[userMbox]
                    print("%s >> %s >> copied mail file count: %d" % (user, mboxList.get(userMbox), cnt))
                    print(copyLogStr)
                    with open(tsvFolder + "log.txt", "at", encoding="utf-8") as fw:
                        fw.write(logStr);

            del usersMboxList[user]
    return


def getEmlFilePath(mailId, oldPath):
    oldDir = os.path.dirname(oldPath)
    emlFilePath = ""
    if os.path.exists(oldDir + mailId + ".eml"):
        emlFilePath = oldDir + mailId + ".eml"
    elif os.path.exists(oldPath):
        emlFilePath = oldPath
    return emlFilePath

def makeTestFiles():
    #테스트 파일 생성하고 싶은 위치에 따라서 경로 수정해야함.
    tmpPath = "c:/jittest/kebiportal/kebi_data/maildata/kidp.or.kr/user1/"
    for user in usersList:
        try:
            os.makedirs(tmpPath + user + "/mail")
        except:
            print("폴더가 이미 있습니다.")
            continue
        if user in usersMboxList:
            for userMbox in usersMboxList[user]:
                if userMbox in mboxMailList:
                    for mail in mboxMailList[userMbox]:
                        if mail["mFilePath"].find("maildata/kidp.or.kr/user1/") > -1:
                            os.system("fsutil file createnew " + tmpPath + user + "/mail/" + os.path.basename(mail["mFilePath"]) + " 1")
                            print(user + " 파일 생성: " + os.path.basename(mail["mFilePath"]))
                    del mboxMailList[userMbox]
            del usersMboxList[user]
    return

usersList = getUserList()
usersMboxList = getUsers_mbox()
mboxList = getMboxList()
mboxMailList = getMboxMailList()

copyMailFile(usersList, usersMboxList, mboxList, mboxMailList)

endDate = datetime.now()
period = (endDate - startDate).seconds
print(period, "초")
with open(tsvFolder + "timelog.txt", "at", encoding="utf-8") as fw:
    fw.write(str(period) + "초\n");
os.system("echo " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " >> " + tsvFolder + "log.txt")