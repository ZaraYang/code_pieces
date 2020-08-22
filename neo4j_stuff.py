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

推荐内存配置
./neo4j-admin memrec --memory=64g


match (n1:scv_node{node_id:'2_0'})-[r1:scv_bind{bind_type:'2'}]->(n2:scv_node)-[r2:scv_bind{bind_type:'6'}]->(n3:scv_node)
return n1,n2,n3,r1,r2
