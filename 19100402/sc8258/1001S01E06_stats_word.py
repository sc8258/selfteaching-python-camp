def  stats_text_en（a）：＃创造函数
    b = a.split（“  ”）＃分割文本
    c = {}
    对于我在 b：
        count = b.count（i）
        r1 = {i：count} ＃计算出现频率
        c.update（r1）＃更新计算频率
    C1 = 排序（c.items（），键= 拉姆达 X：X [ 1 ]，反向= 真）＃升序排序
    print（c1）＃打印
   

text =  '''蒂姆·彼得斯的禅之谜
美丽胜过丑陋。
显式优于隐式。
简单比复杂更好。
复杂比复杂更好。
Flat优于嵌套。
稀疏优于密集。
可读性很重要。
特殊情况不足以打破规则。
虽然实用性胜过纯洁。
错误不应该默默地传递。
除非明确沉默。
面对困惑，拒绝猜测的诱惑。
应该有一个 - 最好只有一个 - 明显的方法来做到这一点。
虽然这种方式起初可能并不明显，除非你是荷兰人。
现在比永远好。
虽然现在永远不会比*正确好。
如果实施很难解释，这是一个坏主意。
如果实现很容易解释，那可能是个好主意。
命名空间是一个很棒的主意 - 让我们做更多的事情吧！“””
stats_text_en（文本）


def  stats_text_cn（text）：＃设定函数
    A = []
    c = {}
    对于我的文字：
        i.strip（' “，”,,,！，。，？，“， - '）
        A.append（i）＃转变形式
        对于 X 在一个：
            count = A.count（x）
            d = {x：count} ＃计算出现次数
            c.update（d）＃更新出现次数
    c1 =已排序（c.items（），key = lambda  x：x [ 1 ]，reverse = True）＃降序排列
    打印（c1）
e =  '''细想想，每个人都有很多很多“积ん読”。小时候我们拿回家的教科书中就有相当一部分，其实就是“积ん読”，虽然那时候掏钱买书的是父母，不仔细看，或者干脆不看的时候，也知道自己在偷懒......再后来就是“主动犯罪”了 - 比如，很多人买到手里的英语词汇书是根本就没有翻到过第二个列表的，乃至于过去我常常开玩笑说，中国学生都认识一个单词，abandon，不是吗？这个单词是很多很多人“决心重新做人”而后“就这样罢”的铁板钉钉的见证者。'''
stats_text_cn（e）中