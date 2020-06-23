import seldom

if __name__ == '__main__':
    # seldom.main(path="./test_dir",
    #             browser="firefox",
    #             title="百度测试用例",
    #             description="测试环境：Firefox",
    #             rerun=0)
    seldom.main(path="./test_dir", debug=False, rerun=1)

'''
说明：
path ： 指定测试目录。
browser: 指定浏览，默认chrome。
report：日志报告文件名称&格式，若为空，则默认report+时间+.html
title ： 指定测试报告中标题。
description ： 指定测试报告中环境描述。
debug ： debug模式，设置为True不生成HTML测试报告。
rerun ： 测试失败重跑次数，默认为0
save_last_run：默认为False，若为True，则只保存最后一次运行的结果
driver_path：默认为None，指定浏览器驱动路径
param grid_url：指定远程执行用例ip地址

'''

