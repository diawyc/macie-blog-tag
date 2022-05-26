# macie-blog-autotag

Automate the archival and deletion of sensitive data using Amazon Macie
https://aws.amazon.com/cn/blogs/big-data/automate-the-archival-and-deletion-of-sensitive-data-using-amazon-macie/
This blog can be successfully deployed but the lambda has runtime error, the blog writer is updating.
在🇺🇸作者修改完成之前,请使用以下workaround
## Workaround
lambda-runtime setting-handler-把macie.handler修改为index.handler.将默认代码保存为一个version然后将[macie-tag.py](https://github.com/jessicawyc/macie-blog-tag/blob/main/macie-tag.py)中的代码替换成新version,可以成功运行给bucket中被macie识别出为High的object打上tag.tag为 sensitivity:High
# 改进内容
##根据公司内部分级规则给扫描出相应信息的S3 Object打tag标签,标签可以在环境变量中自由定义:
标签取所有finding中最高级别
[macie-tag-customise.py](https://github.com/jessicawyc/macie-blog-tag/blob/main/macie-tag-customize.py)
