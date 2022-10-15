

# M2NM2NBot

（）和 {} 的互转！

支持群组内转换回复内容 /mn  /nm

支持私聊的智能互转

支持代理设置


### 部署


```bash
cd M2NM2NBot

ls

pip install -r requirements.txt

cat Config/app_exp.toml

#copy the content
# fill token
nano Config/app.toml

#run
nohup python3 main.py > output.log 2>&1 &
```

### 查看

```bash
ps -aux|grep python3
```

### 应用以下 MVC 框架

https://github.com/TelechaBot/BaseBot