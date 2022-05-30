# macie-blog-autotag

Automate the archival and deletion of sensitive data using Amazon Macie
https://aws.amazon.com/cn/blogs/big-data/automate-the-archival-and-deletion-of-sensitive-data-using-amazon-macie/
This blog can be successfully deployed but the lambda has runtime error, the blog writer is updating.
在🇺🇸作者修改完成之前,请使用以下workaround
## Workaround
lambda-runtime setting-handler-把macie.handler修改为index.handler.将默认代码保存为一个version然后将[macie-tag.py](https://github.com/jessicawyc/macie-blog-tag/blob/main/macie-tag.py)中的代码替换成新version,可以成功运行给bucket中被macie识别出为High的object打上tag.tag为 sensitivity:High
# 改进内容
根据公司内部分级规则给扫描出相应信息的S3的Object打tag标签,标签可以在环境变量中自由定义:
Based on your defined classification levels
![This is an image](https://github.com/jessicawyc/macie-blog-tag/blob/main/macie-self-defined-level.png)
So far in my code, higher the level, more critical tag
标签取所有finding中最高级别
![This is an image](https://github.com/jessicawyc/macie-blog-tag/blob/main/%E7%BB%93%E6%9E%9C%E6%98%BE%E7%A4%BA%E4%B8%AD%E8%8B%B1%E6%96%87%E6%94%AF%E6%8C%81.png)

请下载lambda文件
[macie-tag-customize.py](https://github.com/jessicawyc/macie-blog-tag/blob/main/macie-tag-customize.py)
