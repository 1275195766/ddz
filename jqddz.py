
#cmd：命令
# def IsXXCmd(line, cmd):
#
# 	temp=[]
# 	n = len(cmd)
# 	temp[n] = 0
# 	temp.extend(line)   #将line列表的值添加到temp列表
# 	if temp==cmd:
# 		return True


def Exit():
    exit()

def DoudizhuVer():
	print("NAME 重庆三峡学院计算机博弈大赛斗地主AI")

def Info(void):
	print("OK INFO\n")

def Error(void):
	print("OK ERROR\n")

drf Bid(line):
	n = line.split( ',')
	SetBid((line[4] - position + 3) % 3, d[0]);
	printf("OK BID\n");

if __name__=="__main__":
    buff = list(input().split(','))

    switch = {"DOUDIZHUVER": DoudizhuVer(),
              "NAME": "NAME",
              "INFO": Info(),
              "DEAL": Deal(buff),
              "BID": Bid(buff),
              "BID WHAT": BidWhat(),
              "LEFTOVER": Leftover(buff),
              "PLAY": Play(buff),
              "PLAY WHAT": PlayWhat(),
              "GAMEOVER": Gameover(),
              "ERROR":Error(),
              "EXIT": Exit()
              }



