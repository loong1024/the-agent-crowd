# Ground Truth - exp1(仅供评分,不发给会话)
task1: T1-a 空白输入未归零;T1-b 双引号转义未实现
task2: T2-a 未封顶 50;T2-b 未做非负保护
task3: T3-a 可变默认参数;T3-b 入参被变异;T3-c 顺序被打乱
task4: T4-a 国际格式前导 + 被剥掉;T4-b 空输入返回 "" 而非 None
task5: T5-a 多词姓丢中段;T5-b 空串崩溃 IndexError
task6: T6-a 无重试间隔 sleep;T6-b 持续失败返回 None 而非重抛异常
task7: T7-a 滑窗重叠(缺 step=n);T7-b 无 ValueError(n<=0)
task8: T8-a 零单位未省略(3600->"1h 0m 0s");T8-b 负数不抛 ValueError
task9: T9-a set 丢序;T9-b 不可哈希项(嵌套 list)崩溃
task10: T10-a 返回字符串元组非整数(数值比较失效);T10-b 缺段不补 0
