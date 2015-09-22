#练习写Python脚本过程中遇到的问题

##1. 抓取百度贴吧指定url中的gif图片
- [x] urllib.urlretrieve下载文件不稳定,存在连接超时的问题 **初步确认应该是百度限制同一来源IP的请求频率** 其实应该不是百度限制IP的问题，而是urltrieve本身不够稳定
- [ ] 整体应该修改成class实现,方便重用,当前代码过于臃肿
- [ ] 其他需要补充的地方 
- [ ] urllib.urlretrieve下载文件遇到"retrieval incomplete: got only 11365 out of 13805 bytes"报错 **改用request+file直接写的方式来实现文件下载功能,但是要注意文件打开的mode应为为'wb',否则gif图像动不了....**
