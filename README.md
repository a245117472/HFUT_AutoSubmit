# HFUT_AutoSubmit
合肥工业大学今日校园疫情信息收集自动打卡签到

# 使用说明

1. **Fork 本项目**
2. **获取sckey**
   1. 前往 [sc.ftqq.com](http://sc.ftqq.com/3.version) 点击登入，创建账号（建议使用 GitHub 登录）。
   2. 点击点[发送消息](http://sc.ftqq.com/?c=code) ，生成一个 Key。之后会将其增加到 Github Secrets 中，变量名为 `sckey`
   3. [绑定微信账号](http://sc.ftqq.com/?c=wechat&a=bind) ，开启微信推送。  ![图示](docs/imgs/serverpush.png)
3. **点击项目 Settings -> Secrets -> New Secrets 添加以下 3 个 Secrets，其中server酱微信推送的sckey可见上一步**
   
|Name|Value|
|-----|-----|
| username | 学号 |
| password | 新信息门户密码 |
| sckey | server酱推送的sckey |

![图示](docs/imgs/1.jpg)

4. 运行结果将会通过微信的server酱通知给您

# 后记
这破系统如果正常发http请求要经过好几道验证，实属搞不来，只能用浏览器自动化这种蠢办法，如果有网安大佬带带我最好了！

# 致谢
JunzhouLiu/BILIBILI-HELPER 提供Action思路