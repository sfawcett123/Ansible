using NRedisStack;
using StackExchange.Redis;

ConnectionMultiplexer redis = ConnectionMultiplexer.Connect("controller.local");
IDatabase db = redis.GetDatabase();

db.StringSet("foo", "Test Data");
Console.WriteLine(db.StringGet("foo")); 
