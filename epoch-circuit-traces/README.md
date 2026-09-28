# 迟到响应下的熔断世代

public/engine.py是待实现的请求处理入口；public/main.py负责逐行JSON收发；public/example.json是公开输入示例。

在题包根目录运行。示例JSON可转换为单行后输入：

```sh
python3 -c 'import json; print(json.dumps(json.load(open("sources/public/example.json"))))' | python3 sources/public/main.py
```

仅依赖Python3.12标准库。完整行为契约见proposal.json中的C_agent_task。以上文件均为求解可见材料。
