from gmssl import sm3

def verify_integrity(message, expected_hash):
    # msg = [i for i in message]
    hasher = sm3.sm3_hash(message)
    return hasher == expected_hash

# 示例消息和预期的哈希值
message = [123456]
expected_hash = '74ef45f3a8c47cb48c4428d6824ffaa5fda8941135cce34d9cee205180a6f1fd'

# 检测消息完整性
result = verify_integrity(message,expected_hash)
if result:
    print("消息完整性验证通过，消息未被篡改")
else:
    print("消息完整性验证失败，消息可能已被篡改")

hasher1 = sm3.sm3_hash([123456])
print(hasher1)