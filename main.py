root@DESKTOP-N7ST735:~# redis-cli
127.0.0.1:6379> set name "John Doe"
OK
127.0.0.1:6379> get name
"John Doe"
127.0.0.1:6379> rpush fruits "apple" "banana" "orange"
(integer) 6
127.0.0.1:6379> lrange fruits 0 -1
1) "apple"
2) "banana"
3) "orange"
4) "apple"
5) "banana"
6) "orange"
127.0.0.1:6379> hmset user:1 name "Alice" age 25
OK
127.0.0.1:6379> hgetall user:1
1) "name"
2) "Alice"
3) "age"
4) "25"
127.0.0.1:6379> SADD tags "red" "green" "blue"
(integer) 3
127.0.0.1:6379> SMEMBERS tags
1) "red"
2) "green"
3) "blue"
127.0.0.1:6379> INCR counter
(integer) 1
127.0.0.1:6379> GET counter
"1"
127.0.0.1:6379> DEL name
(integer) 1
127.0.0.1:6379> EXISTS name
(integer) 0
127.0.0.1:6379> SETEX message 60 "Hello, Redis!"
OK
127.0.0.1:6379> FLUSHALL
OK
127.0.0.1:6379> GEOADD geo_locations 30.5234 50.4501 "Kyiv"
(integer) 1
127.0.0.1:6379> HSET students "Alice" 90 "Bob" 76
(integer) 2
127.0.0.1:6379> HGETALL students
1) "Alice"
2) "90"
3) "Bob"
4) "76"
127.0.0.1:6379> HSET students "Alice" 100
(integer) 0
127.0.0.1:6379> HGETALL students
1) "Alice"
2) "100"
3) "Bob"
4) "76"
127.0.0.1:6379> PFADD unique_users user1 user2 user3
(integer) 1
127.0.0.1:6379> MULTI
OK
127.0.0.1:6379(TX)> RPUSH name "Alice"
QUEUED
127.0.0.1:6379(TX)> EXEC
1) (integer) 1
127.0.0.1:6379> shutdown
not connected> exit