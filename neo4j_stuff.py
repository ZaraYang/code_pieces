删除所有节点和关系

MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n,r

创建新的节点和关系或者返回已有的节点和关系
并对新节点添加属性

merge(n:boss{id:0})
merge(s:emp{id:1,name:'bob'})
with n,s,case
when s.age is null then [1]
else [0] end as array
foreach (x in array|merge (s)-[r:relationship]->(n) set s.age = 10)
return n,s

import 导入
./neo4j-admin import --database=graph.db --nodes /state/heyang/virus_detec/code/build_tree/scv_node.csv  --relationships /state/heyang/virus_detec/code/build_tree/scv_relationship.csv
