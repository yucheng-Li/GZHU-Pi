from exam_handler import *


# 考试相关查询爬虫

class EX():

    def __init__(self):
        self.url = {
            'chineseTest': 'http://www.cltt.org/StudentScore/ScoreResult'
        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
        }
        self.client = requests.session()

    def chTestQuery(self, postData):
        res = self.client.post(
            url=self.url['chineseTest'], data=postData, headers=self.headers)
        if ('对不起没有查询到相关信息' in res.text):
            return '对不起没有查询到相关信息'
        else:
            return chTestHandle(res)
    # 四六级获取验证码图片

    def cetTestQueryGetImg(self, id_num, name):
        return get_img(self.client, id_num)

    # 四六级获取分数
    def cetTestQueryGetScore(self, id_num, name, capcha):
        return get_score(self.client, id_num, name, capcha)

    # 录取查询
    def admitQuery(self, stuID, stuName):
        url = 'http://zsjy.gzhu.edu.cn/gklqcxjgy.jsp?wbtreeid=1080'
        postData = {
            'stuID1': stuID,
            'stuName1': stuName
        }
        res = self.client.post(url, postData, headers=self.headers)
        getMeg = re.findall(r'align="left" >(.+?)</td>', res.text)
        try:
            MegData = {
                'stuID': getMeg[0],
                'stuName': getMeg[1],
                'stuDepht': getMeg[2]
            }
        except:
            MegData = {}
        return MegData


'''# 普通话考试测试
test = EX()
testData = {
    'name': '***REMOVED***',
    'stuID': '',
    'idCard': '***REMOVED***'
}
print(test.chTestQuery(testData))'''

# #cet考试测试
# test=EX()
# print(test.cetTestQueryGetImg('***REMOVED***','肖'))
# capcha=input()
# print(test.cetTestQueryGetScore('***REMOVED***','肖',capcha))

# 录取查询
test = EX()
test.admitQuery('***REMOVED***', '***REMOVED***')
