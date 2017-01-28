Title:Mysql事务隔离。
Date:2016-11-12
Category:笔记
Tags:Mysql

[TOC]

### 事务隔离

SQL标准定义了4类隔离级别，包括了一些具体规则，用来限定事务内外的哪些改变是可见的，哪些是不可见的。低级别的隔离级一般支持更高的并发处理，并拥有更低的系统开销。

### Read Uncommitted (读取未提交内容)

在该隔离级别，所有事务都可以看到其他未提交事务的执行结果。本隔离级别很少用于实际应用，因为它的性能也不比其他级别好多少。读取未提交的数据，也被称之为脏读（Dirty Read）。

### Read Committed (读取提交内容)

这是大多数数据库系统的默认隔离级别（但不是MySQL默认的）。它满足了隔离的简单定义：一个事务只能看见已经提交事务所做的改变。这种隔离级别 也支持所谓的不可重复读（Nonrepeatable Read），因为同一事务的其他实例在该实例处理其间可能会有新的commit，所以同一select可能返回不同结果。

### Repeatable Read（可重读）

这是MySQL的默认事务隔离级别，它确保同一事务的多个实例在并发读取数据时，会看到同样的数据行。不过理论上，这会导致另一个棘手的问题：幻读 （Phantom Read）。简单的说，幻读指当用户读取某一范围的数据行时，另一个事务又在该范围内插入了新行，当用户再读取该范围的数据行时，会发现有新的“幻影” 行。InnoDB和Falcon存储引擎通过多版本并发控制（MVCC，Multiversion Concurrency Control）机制解决了该问题。

### Serializable（可串行化）

这是最高的隔离级别，它通过强制事务排序，使之不可能相互冲突，从而解决幻读问题。简言之，它是在每个读的数据行上加上共享锁。在这个级别，可能导致大量的超时现象和锁竞争。

### 优缺点

这四种隔离级别采取不同的锁类型来实现，若读取的是同一个数据的话，就容易发生问题。例如：

脏读(Drity Read)：

某个事务已更新一份数据，另一个事务在此时读取了同一份数据，由于某些原因，前一个RollBack了操作，则后一个事务所读取的数据就会是不正确的。

不可重复读(Non-repeatable read):

在一个事务的两次查询之中数据不一致，这可能是两次查询过程中间插入了一个事务更新的原有的数据。

幻读(Phantom Read):

在一个事务的两次查询中数据笔数不一致，例如有一个事务查询了几列(Row)数据，而另一个事务却在此时插入了新的几列数据，先前的事务在接下来的查询中，就会发现有几列数据是它先前所没有的。

在MySQL中，实现了这四种隔离级别，分别有可能产生问题如下所示：

<table class="table table-bordered">
  <tr>
  	<td>隔离级别</td>
  	<td>脏读</td>
  	<td>不可重复读</td>
  	<td>欢读</td>
  </tr>
  <tr>
  	<td>Read Uncommitted (读取未提交内容)</td>
  	<td>Y</td>
  	<td>Y</td>
  	<td>Y</td>
  </tr>
  <tr>
  	<td>Read Committed (读取提交内容)</td>
  	<td>N</td>
  	<td>Y</td>
  	<td>Y</td>
  </tr>
  <tr>
    <td>Repeatable Read(可重读)</td>
  	 <td>N</td>
  	 <td>N</td>
  	 <td>Y</td>
  </tr>
  <tr>
    <td>Serializable（可串行化</td>
  	  <td>N</td>
  	  <td>N</td>
  	  <td>N</td>
  </tr>
</table>

### 修改事务隔离级别

	SELECT @@global.tx_isolation; 

	SELECT @@session.tx_isolation; 

	SELECT @@tx_isolation;

	SET [SESSION | GLOBAL] TRANSACTION ISOLATION LEVEL {READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE}
	
如果选择global，意思是此语句将应用于之后的所有session，而当前已经存在的session不受影响。

如果选择session，意思是此语句将应用于当前session内之后的所有事务。

如果什么都不写，意思是此语句将应用于当前session内的下一个还未开始的事务。
