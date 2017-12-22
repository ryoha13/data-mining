# workplat
    
    定位：
    为报表开发人员、及数据分析人员提供，不建议作为正式上报管理人员的工具
    
    功能概要：
    从使用
    固定报表
    --个人页面：上传数据、绘制图表、图片下载及链接--
    ****开发页面：数据源引入、拖拽选择、实时预览、发布、聚合计算、多条件计算
    邮件定制：附件选择、邮件模板制作、调度分配、个人邮件发送
    数据需求申请：申请流程界面
    元数据信息：指标、归属、计算口径 --参见java api
    需求处理进度集成：工单信息、分配操作、流转信息
    bug和更新建议反馈及处理进度：
        # 处理进度独立出来，
    个人信息：个人资料补充、权限管理
        # 个人资料部分随意，--增加通信或者邮件功能？
        # --权限分查询、修改
        # 角色分普通查询、开发者和super admin，不同角色按照模块进行划分，开发模块中，view函数用permission装饰器进行权限控制，
          加入before requerst在用户访问前进行权限验证
    开发文档和github源码
        # 在线文档查看及编辑？
        # github提供源码，供大家查看修改
    文件管理：
        # 上传数据，支持csv、xls及xlsx或者txt； Q：不规则或者存在合并单元格的信息如何读取
        # 数据预览 Q：预览如何实现，js传入数据，每次仅传输限定的行数，通过鼠标滑轮动作执行下一个js；PS：可能存在并发的上传，对内存对压力
          比较大，是否有必要提供此功能？
        # 图表转html、图片或者提供链接 文件存储位置，按照用户名分配路径；定期销毁；或者仅提供链接，加入cookie过期时间
    
    数据分析、数据挖掘、机器学习等概念文档、常见链接
        # 数据分析： 统计学概念及图解、微积分、线性代数等常见术语及应用场景描述
        # 机器学习算法： 算法介绍、目标函数最优化、算法应用场景等介绍
    
    
    图表模块
    图表js：echarts／D3；图表调整界面
    分析库：pandas、numpy
    机器学习库：sk、scipy等；算法调参界面
    
    登陆界面：
        # 注册申请：链接至负责人邮件，提供同意或者取消按钮，完成后邮件通知申请人；--可以用celery控制消息传递（可扩展功能，如果有大批量的
          注册同时进行的话）
        # 密码：密码输入可视
        # 忘记密码
    
    super admin后台管理：
    --权限管理及分配
    服务器性能监控
        # 服务器性能监控
        # IO监控，内存压力超过阀值时报警
    用户登陆情况监控
        # 登陆安全：密码不加过期信息，但是要对登陆ip进行监控，如果同一账户使用的ip数量超过阀值的话，监控报警
        # 登陆时长、频率和时间，保留日志存档，加入session控制关闭页面保留登陆用户信息
    常用查询优化管理
        # SQL查询监控
        # 用户查询耗时分析、IO吞吐分析
    日志分析
    服务器进程管理模块
    
    数据库连接
        # 预先写好接口，在用户页面选择DB时自动分配接口进行连接，确定后用pandas读入所需的表
    
    详细设计信息
    DBmodel：
        # Permission  --权限
        # Role  --角色及权限default信息，增加insert role的类方法，在实例化的时候写入角色的权限
        # User  --用户个人信息
        # Table  --父类，子类在进入数据源时自动创建
        
    数据库连接
        # 
    
    
    数据字典
    
    项目开发计划
    
    流程图
    
    备忘录
    
    操作手册
    
    用户手册
    
    测试计划
    
    测试报告
    
    框架
    应用视图层：
    
    ui框架：bootstrap、adminlte
    前端组件管理：react／angular
    图表js：echarts／D3
    
    
    
    功能模块及使用库
    数据库及查询性能分析可视化
    日志监控
    服务器性能监控

    公共页面
    固定页面
    自定义页面
    个人页面
  
    邮件推送定制
  
    文件上传及托管
  
    登陆信息和常用查询模块-- 利用flask信号机制进行处理，user_loader回调返回用户状态可以当前在线用户
  
    shell定制
  
    后台管理 dashboard --可用库：flask-admin
    性能分析、日志记录、session管理、请求验证 --可用库：werkzeug中的各个中间件
    
    Rest接口
    异步 --可用库：polyfill脚本及ajax
    缓存 --可用库：memcached／libmc + redis／codis
    
    数据库
    mysql
    mongo 复制和分片
    
    性能优化
    动静态页面分离
    动态页面静态化
    
    系统管理模块
    进程操作管理，启动、重启、关闭进程 --可用库：supervisor
    ssh及应用部署 --可用库：fabric
    服务器管理 --可用库：saltstack、ansible
    服务器和系统资源采集、监控和分析 --可用库：psutil
    实时事件日志和聚合管理 --可用库：sentry，需要配置postgresql
    监控和报警 --可用库：icinga 绘图：statsd+graphite+grafana+diamond
    
    测试
    消息队列
    服务化
    
    日志分析、流量分析 mapreduce
    邮件定制发送、excel附件制作
    
    
    
    
    