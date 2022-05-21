# macie-blog-tag

Automate the archival and deletion of sensitive data using Amazon Macie
https://aws.amazon.com/cn/blogs/big-data/automate-the-archival-and-deletion-of-sensitive-data-using-amazon-macie/
This blog can be successfully deployed but the lambda has runtime error, the blog writer is updating.

## Workaround
lambda-runtime setting-handler-把macie.handler修改为index.handler.将默认代码保存为一个version然后上传修改版本,可以成功运行.
