root@DESKTOP-N7ST735:~# ping
ping: usage error: Destination address required
root@DESKTOP-N7ST735:~# sudo service redis-server start
root@DESKTOP-N7ST735:~# redis-cli
127.0.0.1:6379> set username "Ira"
OK
127.0.0.1:6379> RPUSH todo_list "Приготувати обід"
(integer) 1
127.0.0.1:6379> RPUSH todo_list "Вивчити Redis"
(integer) 2
127.0.0.1:6379> lrange todo_list 0 -1
1) "\xd0\x9f\xd1\x80\xd0\xb8\xd0\xb3\xd0\xbe\xd1\x82\xd1\x83\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb8 \xd0\xbe\xd0\xb1\xd1\x96\xd0\xb4"
2) "\xd0\x92\xd0\xb8\xd0\xb2\xd1\x87\xd0\xb8\xd1\x82\xd0\xb8 Redis"
127.0.0.1:6379> hmset user_data age "18" country "Ukraine"
OK
127.0.0.1:6379> hgetall user_data
1) "age"
2) "18"
3) "country"
4) "Ukraine"
127.0.0.1:6379> SADD tags "programming" "redis" "tutorial"
(integer) 3
127.0.0.1:6379> SMEMBERS tags
1) "programming"
2) "redis"
3) "tutorial"
127.0.0.1:6379> set page_views 5
OK
127.0.0.1:6379> get page_views
"5"
127.0.0.1:6379> SETEX session_token 120 "abc123"
OK
127.0.0.1:6379> DEL username
(integer) 1
127.0.0.1:6379> set user:1:name "Ira"
OK
127.0.0.1:6379> keys user:*
1) "user:1:name"
127.0.0.1:6379> SETBIT online_status 0 1
(integer) 0
127.0.0.1:6379> get online_status
"\x80"
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379(TX)> SET balance 1000
QUEUED
127.0.0.1:6379(TX)> EXEC
1) OK
127.0.0.1:6379> SADD cache:popular_articles "id1" "id2" "id3" "id4"
(integer) 4
127.0.0.1:6379> SADD set1 "h" "e" "l" "l" "o"
(integer) 4
127.0.0.1:6379> SADD set1 "r" "e" "d" "i" "s"
(integer) 4
127.0.0.1:6379> SUNIONSTORE union_set set1 set2
(integer) 8
127.0.0.1:6379> SINTERSTORE intersection_set set1 set2
(integer) 0
127.0.0.1:6379> SUBSCRIBE messages
1) "subscribe"
2) "messages"
3) (integer) 1
127.0.0.1:6379> GEOADD geo_locations 30.5234 50.4501 "Kyiv" 46.2908 30.4436 "Odesa"
(integer) 1
127.0.0.1:6379> RPUSH tasks "task1" "task2" "task3"
(integer) 3
127.0.0.1:6379> LRANGE tasks 0 -1
1) "task1"
2) "task2"
3) "task3"
127.0.0.1:6379> RPUSH tasks "task4"
(integer) 4
127.0.0.1:6379> LPOP tasks
"task1"
127.0.0.1:6379> LRANGE tasks 0 -1
1) "task2"
2) "task3"
3) "task4"
127.0.0.1:6379> PFADD unuque_users "user1" "user2" "user3" "user4"
(integer) 1
127.0.0.1:6379> RPUSH message_queue "mess 1" "mess2" "mess3"
(integer) 3
127.0.0.1:6379> LRANGE message_queue 0 -1
1) "mess 1"
2) "mess2"
3) "mess3"
127.0.0.1:6379>