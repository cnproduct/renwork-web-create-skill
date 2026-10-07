# Turnstile 服务端验证与故障处理

仅在项目选用 Turnstile 时读取。实际接收端与轮换操作遵循当前项目授权，本说明不要求创建或更换现有密钥。

## 验证

接收端向 `https://challenges.cloudflare.com/turnstile/v0/siteverify` 提交 `secret` 与客户端 `response`，检查成功状态和预期 hostname/action。令牌有效期5分钟且只能使用一次；过期/重复令牌需刷新。客户端控件成功不等于服务端验证通过。[官方验证说明](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)

前端传递 `cf-turnstile-response`，失败时保留表单并允许重新挑战；业务接收成功后再清空。服务不可用时按实际接口契约报错，不伪装提交成功。

## 排查与修复

先核对实际站点的 sitekey、允许域名、部署环境与后端 secret 是否对应。Cloudflare widget 管理使用 `/accounts/{account_id}/challenges/widgets`；读取或轮换返回体可能含敏感字段，仅提取所需非敏感信息，不打印原始响应。[Widget API](https://developers.cloudflare.com/api/resources/turnstile/subresources/widgets/methods/get/)

确认需要轮换且在授权范围内后，按当前官方接口执行，将返回密钥直接写入目标环境的秘密存储，保留回退与验证记录。不要在命令参数、普通文件、日志、聊天或公开提交中展示密钥。

## 测试

自动化成功/失败路径使用官方测试 sitekey/secret，测试配置只用于测试环境；生产挑战需要真实可用的验证路径，出现人工挑战时请用户完成。假令牌被拒仅证明拒绝路径，不能证明生产密钥配对和邮件接收都正确。[官方测试说明](https://developers.cloudflare.com/turnstile/troubleshooting/testing/)
