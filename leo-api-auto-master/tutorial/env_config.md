### 2_环境配置
>此平台 **环境配置** 为 *必须配置项*。  
>作用： 配置接口用例执行的环境。

>一般来说，IT项目的环境 分为：开发环境、测试环境、预发布环境、生产环境。  
>既然接口服务部署在多套环境中，那么接口测试自然也要支持多套环境。  
>当服务开发完成后，需要在集成测试环境进行集成测试，上线前需要在预发布环境进行回归测试。  
>只有在此平台上预先配置好测试环境，才能在执行用例时，选择正确的测试环境进行测试。

只有超级管理员有 **环境配置** 权限  
管理员账号登录后，点击左侧 Menu **环境配置** 进入环境配置页面
#### 2.1 测试环境管理
环境信息包含： 环境名称、HTTP协议、服务域名、环境描述、环境状态  
关于**服务域名Domain**： 
设置服务域名的目的是 避免在每个接口用例中重复添加域名，只需替换不同的部分即可。
服务域名 不包含 传输协议(http:// or https://)   
由于有些接口服务域名中包含 服务名，所以此平台支持在服务域名中设置一个全局变量${service}，可在执行时进行赋值，value为 接口信息中的 service的值。  
>举例说明：  
>某电商平台 生产环境域名为： buy.com，预发布环境域名为 pre.buy.com, 测试环境 域名为 test.buy.com,  平台存在多个服务，其中两个服务 购物车 和 订单服务 域名为： cart.buy.com 、 order.buy.com  
>对于此种情况 可将预发布环境中的域名设置为 ${service}.pre.buy.com, 在接口信息中设置 service = cart/order，即可在接口用例执行时，替换为相应的值。

**注意：域名中需要区分环境信息**
##### 2.1.1 添加测试环境
1. 进入环境配置页面后，点击 **新增测试环境**
2. 输入 环境名称、选择HTTP协议(http or https)、输入域名（域名不包含http:// or https://)、描述 信息
3. 点击 **提交** 保存环境信息
##### 2.1.2 编辑测试环境
1. 进入环境配置页面后，页面会展示 **环境列表**
2. 可以在页面右上角 进行查询，查询条件为 环境名称，支持模糊查询
3. 选择要编辑的 环境信息，点击右侧 **编辑** 按钮
4. 输入 要修改的 名称、HTTP协议、域名Domain（域名不包含http:// or https://)、描述 信息
5. 点击 **提交** 保存环境信息
##### 2.1.3 禁用/启用测试环境
1. 进入环境配置页面后，页面会展示 **环境列表**
2. 可以在页面右上角 进行查询，查询条件为 环境名称，支持模糊查询
3. 选择要禁用的 环境信息，点击右侧 **禁用** 按钮（如果环境状态为禁用，则按钮为 **启用**）， 即可禁用/启用 测试环境
4. *如果 测试环境为禁用状态，那么 测试用例执行时，将无法选择到被禁用的测试环境*。

#### 2.2 DB配置管理
DB配置 用于数据初始化，设置接口DB的连接信息  
由于不同接口可能使用不同的DB，所以可能需要多个DB配置  
**数据初始化 目前支持 接口服务数据库为 MongoDB 或 MySQL， 其他 数据库待实现**  
*进行DB配置前，需先配置好环境信息*  
只有超级管理员有 **DB配置** 权限  
管理员账号登录后，点击左侧 Menu **环境配置** 进入环境配置页面  
点击上方 **DB配置** 进入DB配置页面
##### 2.2.1 添加DB配置
1. 进入DB配置页面后，点击 **新增DB配置**
2. 输入 DB名称、选择DB类型（目前只支持MongoDB 和 MySQL)、输入描述 信息
3. 点击 **提交** 保存DB配置
##### 2.2.2 编辑DB配置
1. 进入DB配置页面后，页面会展示 **DB配置列表**
2. 选择要编辑的 DB配置，点击右侧 **编辑** 按钮
2. 输入 DB名称、选择DB类型（目前只支持MongoDB 和 MySQL)、输入描述 信息
3. 点击 **提交** 保存DB配置
##### 2.2.3 禁用/启用DB配置
1. 进入DB配置页面后，页面会展示 **DB配置列表**
2. 选择要禁用的 DB配置，点击右侧 **禁用** 按钮（如果DB配置状态为禁用，则按钮为 **启用**）， 即可禁用/启用 DB配置
3. *如果 DB配置为禁用状态，那么 测试用例执行时，将无法选择到被禁用的DB配置*。
##### 2.2.4 DB连接信息管理
由于测试环境有多个，所以DB连接信息需要配置多个环境
1. 进入DB配置页面后，页面会展示 **DB配置列表**
2. 选择要编辑的 DB配置，点击右侧 **连接信息** 按钮， 进入DB环境连接配置页面
3. 页面会根据配置的测试环境展示DB连接信息，点击右侧 **编辑** 按钮
4. 输入DB Host、 Port、 User、 Password、 Name信息
3. 点击 **提交** 保存DB连接配置
6. *需要为每个环境都配置好 DB 连接信息，不然用例执行可能会报错。*