# macie-blog-tag

Automate the archival and deletion of sensitive data using Amazon Macie
https://aws.amazon.com/cn/blogs/big-data/automate-the-archival-and-deletion-of-sensitive-data-using-amazon-macie/
This blog can be successfully deployed but the lambda has runtime error, the blog writer is updating.

## Workaround
lambda-runtime setting-handler-把macie.handler修改为index.handler.将默认代码保存为一个version然后将macie-tag.py中的代码替换成新version,可以成功运行给bucket中被macie识别出为High的object打上tag.
tag为 sensitivity:High
